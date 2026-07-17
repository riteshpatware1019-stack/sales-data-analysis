import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Sales Data Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Sales Data Analytics Dashboard")
st.write("Analyze sales performance, profit, and customer insights.")

df = pd.read_csv("Data/cleaned_sales_data.csv")


# Side bar
st.sidebar.header("Filters")

#Category Filter
category = st.sidebar.selectbox(
    "Category",
    ["All"] + list(df["Category"].unique())
)

#City Filters
city = st.sidebar.selectbox(
    "City",
    ["All"] + list(df["City"].unique())
)


filtered = df.copy()

if category != "All":
    filtered = filtered[filtered["Category"] == category]

if city != "All":
    filtered = filtered[filtered["City"] == city]



# KPI Cards
total_sales = filtered["Sales"].sum()
total_profit = filtered["Profit"].sum()
total_orders = filtered.shape[0]
avg_sales = filtered["Sales"].mean()

col1, col2, col3 ,col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Orders",total_orders)
col4.metric("Average Sales", f"${avg_sales:,.2f}")


# Sales by Category
fig,  ax = plt.subplots(figsize=(6,5))
filtered.groupby("Category")["Sales"].sum().plot(
    kind="bar",
    ax=ax
)
plt.title("Sales by Category")
st.pyplot(fig)


# Monthly Sales
fig, ax = plt.subplots()
filtered.groupby("Month")["Sales"].sum().plot(
    kind="line",
    marker="o",
    ax=ax
)
plt.title("Monthly Sales")
st.pyplot(fig)


# Sales by City
fig, ax = plt.subplots()
filtered.groupby("City")["Sales"].sum().plot(
    kind="barh",
    ax=ax
)
plt.title("Sales by city")
st.pyplot(fig)


# Profit Distribution
fig, ax = plt.subplots()
ax.hist(filtered["Profit"], bins=20)
plt.title("Profit Distribution")
st.pyplot(fig)


# Sales vs Profit
fig, ax = plt.subplots()
ax.scatter(
    filtered["Sales"],
    filtered["Profit"]
)
plt.xlabel("Sales")
plt.ylabel("Profit")
st.pyplot(fig)


# Data Table
st.subheader("Sales Data")
st.dataframe(filtered)


# Download Button 
csv = filtered.to_csv(index=False)

st.download_button(
    "Download CSV",
    csv,
    "filtered_sales.csv",
    "text/csv"
)




