"""
Insurance Premium Pricing & Risk Factor Analysis (Analyst-focused version)
Replaces XGBoost with simple linear regression for interpretability,
keeps hypothesis testing as the analytical core.
"""
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("insurance.csv")

# Hypothesis tests (same as before, this is the analytical core)
smoker_charges = df[df.smoker == "yes"]["charges"]
nonsmoker_charges = df[df.smoker == "no"]["charges"]
t_stat, p_val = stats.ttest_ind(smoker_charges, nonsmoker_charges, equal_var=False)

corr_bmi, p_bmi = stats.pearsonr(df["bmi"], df["charges"])

regions = [df[df.region == r]["charges"] for r in df.region.unique()]
f_stat, p_anova = stats.f_oneway(*regions)

smokers_df = df[df.smoker == "yes"]
nonsmokers_df = df[df.smoker == "no"]
corr_smoker, p_s = stats.pearsonr(smokers_df["bmi"], smokers_df["charges"])
corr_nonsmoker, p_ns = stats.pearsonr(nonsmokers_df["bmi"], nonsmokers_df["charges"])

# Simple linear regression (analyst-appropriate, interpretable coefficients)
df_model = df.copy()
df_model["sex"] = df_model["sex"].map({"male": 1, "female": 0})
df_model["smoker_flag"] = df_model["smoker"].map({"yes": 1, "no": 0})
df_model["bmi_x_smoker"] = df_model["bmi"] * df_model["smoker_flag"]  # interaction term
df_model = pd.get_dummies(df_model, columns=["region"], drop_first=True)

feature_cols = ["age", "sex", "bmi", "children", "smoker_flag", "bmi_x_smoker"] + \
               [c for c in df_model.columns if c.startswith("region_")]
X = df_model[feature_cols]
y = df_model["charges"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
lr = LinearRegression()
lr.fit(X_train, y_train)
preds = lr.predict(X_test)

mae = mean_absolute_error(y_test, preds)
r2 = r2_score(y_test, preds)

coefs = pd.Series(lr.coef_, index=feature_cols).sort_values(key=abs, ascending=False)

print("LINEAR REGRESSION RESULTS")
print(f"MAE: ${mae:,.2f}  |  R^2: {r2:.4f}")
print("\nCoefficients (impact per unit, holding others constant):")
print(coefs)
print(f"\nInteraction term (bmi_x_smoker) coefficient: {coefs['bmi_x_smoker']:.2f}")
print("-> This confirms: each BMI point adds this much MORE to charges specifically for smokers")

with open("results_summary_v2.txt", "w") as f:
    f.write("INSURANCE PRICING ANALYSIS - ANALYST-FOCUSED VERSION\n")
    f.write("="*55 + "\n\n")
    f.write("HYPOTHESIS TESTS\n")
    f.write(f"Smoker vs non-smoker: t={t_stat:.3f}, p={p_val:.2e}\n")
    f.write(f"  Smoker avg: ${smoker_charges.mean():,.2f} | Non-smoker avg: ${nonsmoker_charges.mean():,.2f}\n")
    f.write(f"BMI-charges correlation (overall): r={corr_bmi:.3f}, p={p_bmi:.2e}\n")
    f.write(f"Regional ANOVA: F={f_stat:.3f}, p={p_anova:.4f}\n")
    f.write(f"BMI-charges, smokers only: r={corr_smoker:.3f}\n")
    f.write(f"BMI-charges, non-smokers only: r={corr_nonsmoker:.3f}\n\n")
    f.write("LINEAR REGRESSION (interpretable pricing model)\n")
    f.write(f"MAE: ${mae:,.2f} | R^2: {r2:.4f}\n\n")
    f.write("Coefficients:\n")
    f.write(coefs.to_string())

print("\nSaved results_summary_v2.txt")
