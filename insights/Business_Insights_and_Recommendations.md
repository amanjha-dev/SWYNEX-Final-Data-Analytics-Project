# Business Insights and Recommendations

## 1. Product Category Performance

**Observation:**

- Electronics contributes approximately 58.90% of recorded sales.
- Furniture contributes approximately 21.46%.
- Together, these categories contribute approximately 80.36%.

**Business Interpretation:**

Recorded sales are concentrated in a small number of product categories. Electronics is the dominant category.

**Recommendations:**

- Investigate the products driving Electronics sales.
- Monitor inventory availability for high-contributing products.
- Evaluate whether Furniture has opportunities for further growth.
- Avoid excessive dependence on a single category.

## 2. Regional Performance

**Observation:**

- South contributes approximately 27.82% of recorded sales.
- Central contributes approximately 15.39%.

**Business Interpretation:**

The South region has the largest recorded sales contribution, while Central has the smallest.

**Recommendations:**

- Examine the product mix and customer behaviour in South.
- Identify successful sales strategies that could be replicated.
- Investigate possible operational or marketing challenges in Central.
- Analyze region-level demand before allocating inventory.

## 3. Yearly Sales Trend

**Observation:**

- Recorded sales peaked in 2023 at approximately 64.53 million.
- Recorded sales declined by approximately 21.45% in 2024.

**Business Interpretation:**

The decline indicates a potential performance issue that requires further investigation.

**Recommendations:**

- Compare yearly order volumes.
- Investigate pricing and discount strategies.
- Examine product-category performance across years.
- Review inventory availability and marketing campaigns.
- Identify whether the decline is concentrated in particular regions or categories.

## 4. Order Status Analysis

**Observation:**

- Delivered: 65.02%
- Returned: 14.57%
- Cancelled: 8.24%

**Business Interpretation:**

A meaningful share of order records is classified as returned or cancelled.

**Recommendations:**

- Investigate cancellation reasons.
- Analyze return reasons by product category.
- Review fulfilment and delivery processes.
- Monitor pending and shipped orders to identify operational delays.

Note: These percentages represent the dataset's recorded order statuses, not necessarily final lifecycle outcomes.

## 5. Customer Satisfaction

**Observation:**

- Average satisfaction: approximately 3.02/5.
- Missing satisfaction values: 346.
- Missing-value percentage: approximately 8.24%.

**Business Interpretation:**

The average satisfaction score suggests room for improvement, although missing feedback limits the completeness of the analysis.

**Recommendations:**

- Improve post-purchase feedback collection.
- Investigate low-rated products and categories.
- Compare satisfaction across regions.
- Examine whether returned orders are associated with lower satisfaction.

## 6. Returned Orders by Category

**Observation:**

- Electronics has the highest status-based returned-record proportion at approximately 15.79%.
- Books has the lowest at approximately 13.52%.

**Business Interpretation:**

Electronics deserves closer investigation because of its relatively higher returned-record proportion.

**Recommendations:**

- Investigate product quality and specifications.
- Review product descriptions and customer expectations.
- Examine packaging and shipping damage.
- Analyze return reasons at SKU level.

## 7. Sales Data Consistency

**Observation:**

The expected simple sales calculation is:

`quantity × unit_price × (1 − discount_pct)`

Approximately 78.02% of comparable records differ from the recorded sales amount by more than 10%.

**Business Interpretation:**

The recorded sales field may follow additional business rules or contain inconsistencies. This affects confidence in financial analysis.

**Recommendations:**

- Verify the sales calculation with the source system.
- Check tax, shipping, refund, and discount treatment.
- Investigate outliers and unusual transactions.
- Establish a documented calculation standard.
- Validate the data before using it for financial reporting.

## 8. Overall Business Priorities

| Priority | Recommended action |
|---|---|
| High | Investigate sales calculation discrepancies |
| High | Understand the 2024 recorded-sales decline |
| High | Analyze Electronics returns |
| Medium | Improve customer feedback collection |
| Medium | Investigate Central region performance |
| Medium | Improve order fulfilment monitoring |

## Final Conclusion

The analysis identifies important patterns in category contribution, regional performance, order outcomes, and customer satisfaction.

However, the sales-data inconsistency is a critical limitation. The business should validate its source-system calculations before treating recorded sales and profit as audited financial figures.

The dashboard and analysis provide a starting point for deeper operational and commercial investigation.