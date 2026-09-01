# Insurance Premium Pricing & Risk Factor Analysis

**Dataset:** [Medical Cost Personal Datasets](https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv) — 1,338 records of US health insurance beneficiaries. Publicly available, originally published in *Machine Learning with R* (Lantz, Packt Publishing).

## Objective
Identify which risk factors drive insurance charges most strongly, and quantify their dollar impact — the analytical approach underlying premium-setting and risk segmentation in insurance underwriting.

## Visual Insights
![Statistical Dashboard](insurance_analysis_dashboard.jpg)
*Figure 1: Statistical validation and regression coefficients generated via Python (matplotlib/seaborn).*

## Methodology
1. **Hypothesis testing**: Welch's t-test (smoker vs. non-smoker), Pearson correlation (BMI vs. charges), one-way ANOVA (regional differences), and a sub-group correlation check to test for a BMI × smoking interaction effect.
2. **Interpretable pricing model**: Linear regression with an explicit BMI × Smoker interaction term — chosen over a black-box model (e.g. XGBoost) because coefficients need to be directly explainable for a pricing/underwriting audience.
3. **Interactive dashboard**: Built in Tableau Public for exploratory drill-down by region, BMI category, and smoking status.

## Key Findings

| Test | Result | Interpretation |
|---|---|---|
| Smoker vs. non-smoker charges | t=32.75, p<0.001; smokers pay **3.8x more** ($32,050 vs $8,434 avg) | Smoking is the dominant cost driver |
| BMI vs. charges (overall) | r=0.198, p<0.001 | Weak — misleading if read alone |
| BMI vs. charges, **smokers only** | r=0.806, p<0.001 | Very strong once smoking is present |
| BMI vs. charges, **non-smokers only** | r=0.084, p=0.006 | Negligible |
| Regional differences | F=2.97, p=0.031 | Significant but practically small |

**The interaction effect is the central insight**: BMI is not a strong standalone pricing factor — its effect is almost entirely conditional on smoking status. The regression confirms this in dollar terms: each additional BMI point adds ~$20 to charges for a non-smoker, but an **extra $1,471** for a smoker.

**Model performance**: R² = 0.865, MAE ≈ $2,757 — comparable accuracy to a gradient-boosted model, with fully interpretable coefficients.

## Business Recommendation
Underwriting models that price BMI and smoking as independent, additive factors will systematically overprice healthy-weight smokers and underprice obese smokers. A joint smoker × BMI-band pricing tier would more accurately reflect true cost risk.

## Interactive Dashboard
[View Interactive Tableau Dashboard](https://public.tableau.com/app/profile/yongyi.ye/viz/Insurance_Risk_Analysis/Dashboard1?publish=yes) 

## Files
- `analysis_v2.py` — full analysis pipeline (hypothesis tests + regression)
- `Insurance_Risk_Analysis_Report.pdf` — polished write-up with charts and business recommendation
- `insurance_analysis_dashboard.jpg` — statistical results dashboard (Python)
- `insurance_tableau_ready.csv` — cleaned dataset with BMI/age categories for Tableau
- `results_summary_v2.txt` — raw statistical output
- `insurance.csv` — source dataset

## Tools
Python (pandas, scipy, scikit-learn) for analysis · Tableau Public for the interactive dashboard
