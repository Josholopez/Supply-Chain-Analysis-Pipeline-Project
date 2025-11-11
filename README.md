# Analysis of Supply Chain Data with Python and visualisations with Power BI and Tableau.

The data was extracted from Kaggle: https://www.kaggle.com/datasets/harshsingh2209/supply-chain-analysis
using the Kaggle library in Python to download and unzip the dataset with the Kaggle API
and the OpenAI library to read the downloaded dataset in CSV format, and analyse its content using a prompt that describes the content, and create the 'metadata' that it was originally missing from the dataset in Kaggle.

**1. High-level Description:**
This dataset captures detailed information about a variety of beauty and personal care products (haircare, skincare, cosmetics), spanning sales, logistics, manufacturing, quality inspection, and transportation. Each row represents a unique product (SKU), with data on its sales performance, supply chain metrics, customer demographics, QA outcomes, and related costs.

---

**2. Key Columns and Their Meaning:**

- **Product type**: Category of product (e.g., skincare, haircare, cosmetics).
- **SKU**: Stock Keeping Unit, a unique product identifier.
- **Price**: Selling price per unit.
- **Availability**: Units available for sale.
- **Number of products sold**: Count of units sold.
- **Revenue generated**: Total sales revenue per SKU.
- **Customer demographics**: Targeted/recorded customer type (e.g., gender identity).
- **Stock levels**: Current stock quantity.
- **Lead times**: Time (days) from order to delivery.
- **Order quantities**: Units ordered in latest batch.
- **Shipping times**: Time (days) to ship to customer.
- **Shipping carriers/costs**: Logistical provider and related shipping expense.
- **Supplier name/location**: Supplier identity and region.
- **Production volumes/costs**: Manufacturing batch size and costs.
- **Inspection results/defect rates**: Quality check outcome and observed defect rate.
- **Transportation modes/routes/costs**: How products are shipped, via which path, with shipping cost.
- (There are a few redundant columns, e.g., "Lead times" and "Lead time," both present.)

---

**3. Data Quality Issues:**

- **Missing values**: Sample does not show explicit blanks, but checks on full dataset needed to confirm completeness (e.g., any 'Unknown' or blank entries).
- **Duplicates**: Based on sample, each SKU appears once, but full dataset should be checked for duplicate SKUs.
- **Outliers/Inconsistencies**:
    - Some entries (e.g., "Defect rates" of 0.02 vs. 4.85) suggest wide variability; need to assess if these are realistic.
    - "Revenue generated" and "Number of products sold" do not always seem consistent with "Price" (likely due to discounts or data entry errors).
    - "Customer demographics" includes 'Unknown'; this may need addressing for demographic analyses.
    - "Lead times" vs. separate "Lead time" columns could imply duplication or ambiguity.
    - "Product type," "Supplier name," and "Location" are categorical but may have inconsistent labeling across full data.
- **Redundant/Confusing Columns**: E.g., "Lead time" vs. "Lead times", clarify definitions.
