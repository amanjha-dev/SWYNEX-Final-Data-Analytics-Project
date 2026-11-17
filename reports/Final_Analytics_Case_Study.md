# Retail Data Analytics – End-to-End Case Study

**Internship:** SWYNEX Technologies  
**Project:** Final Data Analytics Project  
**Domain:** Retail Analytics  
**Tools:** Python, Pandas, NumPy, Matplotlib, Streamlit, Plotly, GitHub

---

## 1. Executive Summary

This project presents an end-to-end retail data analytics workflow, beginning with raw data preparation and ending with an interactive business intelligence dashboard.

The objective was to analyze retail transactions, identify patterns in sales performance, understand customer and order behaviour, investigate regional and product-category contributions, and communicate the findings through visualizations.

The project was completed in three major stages:

1. Data Cleaning and Preparation
2. Exploratory Data Analysis (EDA)
3. Interactive Dashboard Development

The final result is a consolidated analytics case study containing the cleaned dataset, analytical findings, dashboard visualizations, and business recommendations.

## 2. Problem Statement

Retail businesses generate large amounts of transactional data. However, raw datasets frequently contain missing values, duplicate records, inconsistent formats, and data-quality issues.

Without proper preparation and analysis, businesses may struggle to identify:

- Which product categories contribute most to recorded sales?
- Which geographical regions perform better?
- How does recorded sales performance change over time?
- What proportion of orders are delivered, returned, or cancelled?
- How satisfied are customers?
- What data-quality problems could affect business decisions?

The objective of this project was to transform retail transaction data into meaningful business insights and develop an interactive dashboard to support data exploration and decision-making.

## 3. Dataset Information

The project uses an Indian retail transaction dataset.

| Attribute | Description |
|---|---|
| Initial records | 4,310 |
| Final cleaned records | 4,200 |
| Columns | 21 |
| Data type | Structured tabular data |
| Domain | Retail and e-commerce |

### Important dataset columns

- `order_id`: Unique order identifier
- `order_date`: Date of the order
- `customer_id`: Customer identifier
- `customer_name`: Customer name
- `age`: Customer age
- `gender`: Customer gender category
- `region`: Geographical region
- `city`: Customer city
- `product_category`: Product category
- `product_name`: Product name
- `quantity`: Purchased quantity
- `unit_price`: Unit price
- `discount_pct`: Discount percentage
- `sales_amount`: Recorded sales amount
- `profit`: Recorded profit
- `shipping_cost`: Shipping cost
- `payment_method`: Payment method
- `customer_satisfaction`: Customer satisfaction score
- `return_flag`: Return indicator
- `order_status`: Order status
- `days_to_ship`: Shipping duration

## 4. Task 1 – Data Cleaning and Preparation

The first stage focused on improving the quality and consistency of the dataset.

### 4.1 Initial Dataset

The original dataset contained 4,310 records.

### 4.2 Cleaning Operations

The following operations were performed:

**1. Removal of blank records**

- Identified 30 blank records.
- Removed these records from the dataset.

**2. Duplicate removal**

- Identified 80 duplicate records.
- Removed duplicate entries to avoid repeated observations.

**3. Standardization of categorical values**

- Standardized inconsistent gender labels.
- Ensured consistent categorical representations.

**4. Date formatting**

- Converted date values into appropriate datetime format.
- Prepared the date column for time-based analysis.

**5. Missing-value handling**

- Examined missing values in numerical and categorical columns.
- Used median-based handling for selected numerical fields where appropriate.
- Preserved missing customer satisfaction values rather than fabricating ratings.

**6. Numerical validation**

- Validated age, quantity, discount percentage, and shipping-time values.
- Examined invalid and out-of-range values.
- Handled invalid shipping-cost values as missing.

### 4.3 Final Dataset

After cleaning:

- Initial records: 4,310
- Blank records removed: 30
- Duplicate records removed: 80
- Final records: 4,200

The cleaned dataset was used for the subsequent analysis and dashboard development.

## 5. Task 2 – Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the structure of the dataset, discover trends, and identify relationships between business variables.

### 5.1 Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly

### 5.2 Analysis Performed

The following analyses were conducted:

- Product-category sales analysis
- Regional sales analysis
- Yearly and monthly sales trends
- Order-status distribution
- Customer satisfaction analysis
- Returned-order analysis
- Sales-data consistency analysis

### 5.3 Major Findings

**Product Category**

Electronics contributed approximately 58.90% of recorded sales, while Furniture contributed approximately 21.46%.

Together, these two categories accounted for approximately 80.36% of recorded sales.

**Regional Performance**

The South region contributed approximately 27.82% of recorded sales, making it the highest-contributing region.

The Central region contributed approximately 15.39%, making it the lowest-contributing region.

**Yearly Sales Trend**

Recorded sales peaked in 2023 at approximately 64.53 million.

Recorded sales declined by approximately 21.45% in 2024 compared with 2023.

**Order Status**

- Delivered: 65.02%
- Returned: 14.57%
- Cancelled: 8.24%
- Other statuses: Remaining records

**Customer Satisfaction**

The average recorded customer satisfaction score was approximately 3.02 out of 5.

There were 346 missing satisfaction values, representing approximately 8.24% of the cleaned dataset.

**Returned Orders**

Electronics had the highest status-based returned-record proportion at approximately 15.79%.

Books had the lowest at approximately 13.52%.

These proportions are based on the available order-status records and should not automatically be interpreted as final lifecycle return rates.

## 6. Task 3 – Interactive Dashboard Development

The third stage focused on transforming analytical findings into an interactive dashboard.

### Technologies Used

- Python
- Streamlit
- Pandas
- Plotly

### Dashboard Features

**KPI Cards**

- Recorded Sales
- Recorded Profit
- Total Orders
- Average Customer Satisfaction

**Interactive Filters**

- Order date range
- Region
- Product category
- Order status

**Visualizations**

- Monthly recorded sales and profit trends
- Recorded sales by product category
- Recorded sales by region
- Order-status distribution
- Customer satisfaction by category
- Returned-order records by category

**Additional Features**

- Filtered dataset preview
- CSV export functionality
- Data-quality warning

### Dashboard Screenshots

The dashboard screenshots are available in:

`dashboard/screenshots/`

- `dashboard-overview.png`
- `customer-and-data-quality.png`

## 7. Business Insights

The analysis produced several useful observations:

1. Recorded sales are concentrated in Electronics and Furniture.
2. The South region contributes the largest share of recorded sales.
3. Recorded sales declined in 2024 after reaching their peak in 2023.
4. Returned and cancelled order records represent a significant proportion of the dataset.
5. Customer satisfaction averages approximately 3.02 out of 5.
6. Electronics has the highest status-based returned-record proportion.
7. Recorded sales values contain inconsistencies that require further investigation.

Detailed recommendations are documented in `insights/Business_Insights_and_Recommendations.md`.

## 8. Data Quality Limitations

One important issue identified during the analysis was an inconsistency between the recorded `sales_amount` and the value calculated using:

`quantity × unit_price × (1 − discount_pct)`

Approximately 78.02% of comparable records showed a discrepancy greater than 10%.

The original recorded sales and profit values were retained instead of silently replacing them with calculated values.

This is important because the source dataset may follow additional business rules involving taxes, shipping, discounts, refunds, or other adjustments.

Therefore, recorded sales-based conclusions should be considered directional until the source-system calculation is verified.

Other limitations include:

- Missing customer satisfaction values.
- Order-status data representing a snapshot rather than necessarily a complete order lifecycle.
- No independent validation of the source-system profit calculation.

## 9. Business Recommendations

Based on the analysis:

- Investigate the recorded-sales decline in 2024.
- Analyze Electronics returns at product and reason-code level.
- Identify the factors contributing to stronger performance in the South region.
- Improve customer feedback collection.
- Investigate the sales calculation discrepancies.
- Monitor order fulfilment, cancellations, and returns separately.

## 10. Conclusion

This project demonstrates the complete data analytics lifecycle, from data cleaning and exploratory analysis to interactive dashboard development.

The work helped develop practical experience in handling structured datasets, identifying data-quality problems, analyzing business performance, creating visualizations, and communicating findings.

The final dashboard provides an accessible way to explore retail performance, while the case study documents the analytical methodology, findings, limitations, and recommendations.

**Project Status: Completed – SWYNEX Technologies Internship, Tasks 1–3 consolidated into the final Task 4 case study.**