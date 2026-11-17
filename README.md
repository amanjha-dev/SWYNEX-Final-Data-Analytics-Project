# SWYNEX Final Data Analytics Project

### Retail Analytics | End-to-End Data Analytics Case Study

This repository contains my final data analytics project completed as part of the internship at **SWYNEX Technologies**.

The project demonstrates an end-to-end data analytics workflow, including data cleaning, exploratory data analysis, interactive dashboard development, business insights, and recommendations.

---

## Project Overview

The objective of this project is to analyze retail transaction data and identify meaningful patterns in:

- Product category performance
- Regional sales contribution
- Yearly and monthly sales trends
- Order status distribution
- Customer satisfaction
- Returned-order records
- Data quality and consistency

The final output is an interactive retail analytics dashboard supported by a documented business case study.

## Dataset Information

| Attribute | Details |
|---|---|
| Domain | Retail Analytics |
| Initial records | 4,310 |
| Final cleaned records | 4,200 |
| Total columns | 21 |
| Dataset format | CSV |

The dataset includes customer information, order details, product categories, pricing, discounts, recorded sales, profit, shipping information, satisfaction scores, and order statuses.

## Project Workflow

### Task 1 – Data Cleaning and Preparation

Performed data cleaning using Python and Pandas.

Key operations:

- Removed 30 blank records.
- Removed 80 duplicate records.
- Standardized categorical values.
- Converted date columns into appropriate datetime formats.
- Examined missing values.
- Validated numerical fields.
- Checked invalid and out-of-range values.

Final cleaned dataset: **4,200 records**.

### Task 2 – Exploratory Data Analysis

Performed EDA using:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

Analyses included:

- Product category performance.
- Regional sales distribution.
- Yearly sales trends.
- Order status distribution.
- Customer satisfaction.
- Returned-order analysis.
- Sales-data consistency.

### Task 3 – Interactive Dashboard

Developed an interactive dashboard using:

- Streamlit
- Plotly
- Pandas

Dashboard features:

- KPI cards.
- Monthly sales and profit trends.
- Category-wise sales.
- Region-wise sales.
- Order-status distribution.
- Customer satisfaction analysis.
- Returned-order analysis.
- Interactive filters.
- Filtered data export.

## Key Business Insights

1. Electronics contributes approximately 58.90% of recorded sales.
2. Furniture contributes approximately 21.46%.
3. South is the highest-contributing region at approximately 27.82%.
4. Recorded sales peaked in 2023 at approximately 64.53 million.
5. Recorded sales declined approximately 21.45% in 2024.
6. Delivered records represent approximately 65.02% of the dataset.
7. Average customer satisfaction is approximately 3.02/5.
8. Approximately 78.02% of comparable records have a greater than 10% discrepancy between recorded sales and the simple quantity-price-discount calculation.

See `insights/Business_Insights_and_Recommendations.md` for detailed findings and recommendations.

## Dashboard Preview

Dashboard screenshots are available in:

`dashboard/screenshots/`

- `dashboard-overview.png`
- `customer-and-data-quality.png`

## Repository Structure

```text
SWYNEX-Final-Data-Analytics-Project/
│
├── README.md
│
├── data/
│   └── cleaned_dataset.csv
│
├── notebooks/
│   ├── 01_data_cleaning.py
│   └── 02_exploratory_data_analysis.py
│
├── dashboard/
│   ├── app.py
│   └── screenshots/
│       ├── dashboard-overview.png
│       └── customer-and-data-quality.png
│
├── reports/
│   └── Final_Analytics_Case_Study.md
│
├── insights/
│   └── Business_Insights_and_Recommendations.md
│
└── requirements.txt
```

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/SWYNEX-Final-Data-Analytics-Project.git
```

Navigate into the project:

```bash
cd SWYNEX-Final-Data-Analytics-Project
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run dashboard/app.py
```

The dashboard will open in your browser.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming and analysis |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Streamlit | Interactive dashboard |
| Plotly | Interactive charts |
| GitHub | Version control and project hosting |

## Data Quality Limitation

The recorded `sales_amount` values do not consistently match:

`quantity × unit_price × (1 − discount_pct)`

The original recorded sales and profit values have been retained in the analysis.

Approximately 78.02% of comparable records show a discrepancy greater than 10%.

This issue should be investigated with the source-system business rules before using the figures for financial reporting.

Returned-order proportions are based on recorded order status and should not automatically be interpreted as final lifecycle return rates.

## Project Outcome

This project demonstrates practical experience in:

- Data cleaning and preparation.
- Exploratory data analysis.
- Business data interpretation.
- Data visualization.
- Interactive dashboard development.
- Identifying data-quality issues.
- Communicating business recommendations.

---

**Project completed as part of the SWYNEX Technologies Internship.**

#SWYNEX #DataAnalytics #Python #EDA #Streamlit #DataVisualization #BusinessIntelligence