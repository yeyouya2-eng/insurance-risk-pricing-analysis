# Tableau Dashboard — Build Guide

This project's statistical analysis was done in Python, but the dashboard should
be built in **Tableau Public** (free, no license needed) since that's the tool
listed on your resume. This takes about 15–20 minutes.

## Setup
1. Download Tableau Public: https://public.tableau.com/en-us/s/download
2. Open Tableau Public → **Connect to Data** → **Text File** → select `insurance_tableau_ready.csv`
3. Go to a new **Worksheet**

## Sheet 1: "Smoker vs Non-Smoker Charges"
- Drag **Smoker** to Columns
- Drag **Charges** to Rows
- Change mark type to **Box Plot** (Marks card dropdown)
- Right-click the Charges axis → this shows the distribution gap directly
- Add **Charges** to Label, set aggregation to **Average**, format as currency

## Sheet 2: "BMI vs Charges Interaction"
- Drag **BMI** to Columns, **Charges** to Rows
- Change mark type to **Circle**
- Drag **Smoker** to **Color** — this is the key chart: two visibly different
  slopes for smokers vs non-smokers
- Right-click on the chart → **Trend Lines** → **Show Trend Lines** (do this
  per color/smoker group) — this visually proves the interaction effect

## Sheet 3: "Charges by Region"
- Drag **Region** to Columns, **Charges** (Average) to Rows
- Mark type: **Bar**
- Sort descending by clicking the sort icon on the Charges axis

## Sheet 4: "BMI Category x Smoker Heatmap"
- Drag **BMI Category** to Rows, **Smoker** to Columns
- Drag **Charges** (Average) to Color and to Label
- Mark type: **Square** — this produces a heatmap showing the Obese+Smoker
  cell is by far the most expensive segment

## Dashboard
1. Click **New Dashboard** (bottom tab bar)
2. Set size to **Automatic** or a fixed 1200x900
3. Drag all 4 sheets onto the canvas, arrange in a 2x2 grid
4. Add a title text box: "Insurance Premium Risk Factor Analysis"
5. Add a filter action: right-click **Region** → **Use as Filter**, so clicking
   a region filters the other three charts

## Publish
1. **File → Save to Tableau Public As...**
2. Sign in / create a free Tableau Public account
3. Once published, copy the shareable link
4. Paste that link into `README.md` in place of `[INSERT TABLEAU PUBLIC LINK]`
   and into your resume bullet point

This gives you a real, clickable, interactive artifact that anyone (including
an interviewer) can open and explore — not just a static image.
