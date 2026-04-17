# Online Retail Sales Dashboard

## Project Overview
This project develops a small interactive data analysis tool based on the Online Retail dataset. The main purpose of the project is to help a store owner or manager understand sales performance through an interactive dashboard.

The dashboard focuses on:
- revenue trends over time
- top-performing products
- country-level sales patterns

## Analytical Problem
The main analytical problem is:

How can an online retail store owner use historical transaction data to identify sales trends, top-selling products, and country-level sales patterns for better decision-making?

## Target User
The target user is a small online store owner or store manager who wants to monitor business performance and gain practical sales insights.

## Dataset
The dataset used in this project is the **Online Retail** dataset from the UCI Machine Learning Repository. It contains transaction-level records from a UK-based online retail business.

Main variables include:
- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

**Original source:** UCI Machine Learning Repository, Online Retail dataset  
**Access date:** 16 April 2026

The dataset file used in this project is included in the repository as `Online Retail.xlsx`.

## Repository Contents
This repository includes:
- `ACC102_Online_Retail_Dashboard.ipynb` – Jupyter Notebook showing the analytical workflow
- `app.py` – Streamlit dashboard application
- `Online Retail.xlsx` – dataset file
- `requirements.txt` – required Python libraries
- `README.md` – project overview and running instructions

## Main Python Methods Used
This project uses Python for:
- data loading
- data cleaning
- revenue calculation
- date transformation
- grouping and aggregation
- visualisation
- dashboard development with Streamlit

## Dashboard Features
The dashboard includes:
- KPI summary (Total Revenue, Total Orders, Total Customers, Average Order Value)
- Monthly revenue trend
- Top 10 products by revenue
- Top 10 countries by revenue
- Country filter in the sidebar

## How to Run the Project Locally
1. Clone or download this repository.
2. Make sure all files remain in the same folder.
3. Install the required libraries using:

```bash
pip install -r requirements.txt
```
4. Run the Streamlit app using:

```bash
streamlit run app.py
```
5. Open the local Streamlit link shown in the terminal.

## Notes for the Marker
- The app is designed to run locally after cloning the repository.
- The dataset file `Online Retail.xlsx` is included in the repository.
- The code uses relative paths rather than hard-coded local file paths.

## Limitations
- The dataset contains many missing values in `CustomerID`, which limits customer-level analysis.
- Some entries such as `DOTCOM POSTAGE` and `Manual` may not represent standard products.
- The dataset ends on 9 December 2011, so the final month is incomplete.

## Author
Zhixi Ye
2471322
