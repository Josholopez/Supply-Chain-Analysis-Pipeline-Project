# 📊 Supply Chain Data Analysis Pipeline Project (Kaggle, Python, OpenAI and Power BI)

This project demonstrates a complete data analysis workflow, integrating multiple tools and technologies to extract, process, enrich, and visualize data for business insights.
**Kaggle Dataset:** https://www.kaggle.com/datasets/harshsingh2209/supply-chain-analysis

<p align="center">
<img width="900" height="370" alt="e70652d6-42ac-4f60-a24d-b648711cf502" src="https://github.com/user-attachments/assets/918555bc-9f97-45b5-913b-c364f5121815" />


---

## 🔧 Project Workflow Overview

1. **Data Extraction from Kaggle**
   - Utilizes the Kaggle API to programmatically download datasets.
   - Ensures reproducibility and automation in data acquisition.

2. **Data Processing with Pandas**
   - Reads and explores the dataset using Python and Pandas.
   - Performs data cleaning, handling missing values, and formatting.

3. **Metadata Enrichment via OpenAI API**
   - Connects to the OpenAI API to analyze and interpret missing or unclear metadata.
   - Adds contextual understanding and improves data quality.

4. **Export to Excel Format**
   - Cleansed and enriched data is exported to `.xlsx` format.
   - Prepares the dataset for seamless integration with Power BI.

5. **Power BI Integration**
   - Imports the Excel file into Power BI.
   - Normalizes the data model, adjusts data types, and resolves inconsistencies.

6. **KPI Development and Dashboard Visualization**
   - Creates calculated measures and KPIs to track performance.
   - Designs an interactive dashboard to visualize insights and trends.

---

## 🎯 Key Skills Demonstrated

- API integration (Kaggle & OpenAI)
- Data wrangling and cleaning with Pandas
- Data enrichment using AI
- Excel export for BI tools
- Power BI modeling and visualization
- KPI creation and storytelling with data
  
**Dashboard Preview**
<p align="center">
<img width="707" height="396" alt="dashboard_preview" src="https://github.com/user-attachments/assets/7fb61ec7-3f9a-49c2-a66b-c93e3233d166" />

---

**Data Insights**<br>
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

---

**3. Data Quality Issues:**

- **Missing values**: Dataset does not show any 'Unknown' or blank entries.
- **Duplicates**: each SKU appears once, no duplicated SKUs found.
- **Outliers/Inconsistencies**:
    - "Revenue generated" and "Number of products sold" do not always seem consistent with "Price" (likely due to discounts or data entry errors).
    - "Customer demographics" includes 'Unknown'; this may need addressing for demographic analyses.
    - "Lead times" vs. separate "Lead time" columns could imply duplication or ambiguity.
    - "Product type," "Supplier name," and "Location" are categorical but may have inconsistent labeling across full data.
- **Redundant/Confusing Columns**: E.g., "Lead time" vs. "Lead times", clarify definitions.
