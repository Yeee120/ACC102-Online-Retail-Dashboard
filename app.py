
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Page settings
st.set_page_config(page_title="Online Retail Dashboard", layout="wide")

# Title
st.title("Online Retail Sales Dashboard")
st.write("This dashboard provides an interactive overview of revenue trends, product performance, and country-level sales patterns.")

# Load data
df = pd.read_excel("Online Retail.xlsx")

# Create revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Data cleaning
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
df = df.dropna(subset=["Description"])

# Create month column
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)

# Sidebar filter
country_list = sorted(df["Country"].unique())
selected_country = st.sidebar.selectbox("Filter by Country", ["All"] + country_list)

if selected_country != "All":
    filtered_df = df[df["Country"] == selected_country]
else:
    filtered_df = df.copy()

# KPI calculations
total_revenue = filtered_df["Revenue"].sum()
total_orders = filtered_df["InvoiceNo"].nunique()
total_customers = filtered_df["CustomerID"].nunique()
average_order_value = total_revenue / total_orders if total_orders > 0 else 0

# KPI display
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"{total_revenue:,.2f}")
col2.metric("Total Orders", total_orders)
col3.metric("Total Customers", total_customers)
col4.metric("Average Order Value", f"{average_order_value:,.2f}")

# Monthly revenue trend
st.subheader("Monthly Revenue Trend")
monthly_revenue = filtered_df.groupby("YearMonth")["Revenue"].sum().reset_index()

fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(monthly_revenue["YearMonth"], monthly_revenue["Revenue"], marker="o")
ax1.set_title("Monthly Revenue Trend")
ax1.set_xlabel("Year-Month")
ax1.set_ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig1)

# Top products by revenue
st.subheader("Top 10 Products by Revenue")
top_products = (
    filtered_df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig2, ax2 = plt.subplots(figsize=(10, 6))
top_products.sort_values().plot(kind="barh", ax=ax2)
ax2.set_title("Top 10 Products by Revenue")
ax2.set_xlabel("Revenue")
ax2.set_ylabel("Product")
plt.tight_layout()
st.pyplot(fig2)

# Top countries by revenue
st.subheader("Top 10 Countries by Revenue")
top_countries = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig3, ax3 = plt.subplots(figsize=(10, 6))
top_countries.sort_values().plot(kind="barh", ax=ax3)
ax3.set_title("Top 10 Countries by Revenue")
ax3.set_xlabel("Revenue")
ax3.set_ylabel("Country")
plt.tight_layout()
st.pyplot(fig3)