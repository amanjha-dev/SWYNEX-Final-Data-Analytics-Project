import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(
    page_title="Retail Performance | SWYNEX",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

DATA_PATH = Path(__file__).parent / "data" / "cleaned_dataset.csv"

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH)
    data["order_date"] = pd.to_datetime(data["order_date"], errors="coerce")
    for col in ["sales_amount", "profit", "quantity", "customer_satisfaction",
                "discount_pct", "days_to_ship", "shipping_cost"]:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")
    data["year"] = data["order_date"].dt.year
    data["month"] = data["order_date"].dt.month
    data["year_month"] = data["order_date"].dt.to_period("M").astype(str)
    return data

df = load_data()

# Styling
st.markdown("""
<style>
    .stApp { background: #f5f7fb; }
    [data-testid="stSidebar"] { background: #101b34; }
    [data-testid="stSidebar"] * { color: #f3f6ff !important; }
    .main-title { font-size: 2rem; font-weight: 800; color: #14213d; margin-bottom: 0; }
    .sub-title { color: #64748b; margin-top: .2rem; margin-bottom: 1.2rem; }
    div[data-testid="stMetric"] {
        background: white; border: 1px solid #e5eaf2; padding: 16px 18px;
        border-radius: 13px; box-shadow: 0 2px 8px rgba(16, 24, 40, .04);
    }
    div[data-testid="stMetricLabel"] { color: #64748b; }
    div[data-testid="stMetricValue"] { color: #14213d; font-weight: 750; }
    .section-label { color: #14213d; font-size: 1.08rem; font-weight: 750; margin: 10px 0 4px 0; }
    .note { background: #fff8e8; border-left: 4px solid #e6a23c; padding: 12px 15px;
            border-radius: 7px; color: #684b16; font-size: .91rem; }
    .foot { color: #718096; font-size: .8rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Retail Performance Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">SWYNEX Internship · Interactive business intelligence report · 2020–2024</div>', unsafe_allow_html=True)

# Sidebar filters
st.sidebar.markdown("## Dashboard Filters")
min_date = df["order_date"].min().date()
max_date = df["order_date"].max().date()
date_range = st.sidebar.date_input("Order date range", value=(min_date, max_date),
                                   min_value=min_date, max_value=max_date)
regions = sorted(df["region"].dropna().unique().tolist())
categories = sorted(df["product_category"].dropna().unique().tolist())
statuses = sorted(df["order_status"].dropna().unique().tolist())
selected_regions = st.sidebar.multiselect("Region", regions, default=regions)
selected_categories = st.sidebar.multiselect("Product category", categories, default=categories)
selected_statuses = st.sidebar.multiselect("Order status", statuses, default=statuses)

filtered = df.copy()
if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    filtered = filtered[filtered["order_date"].dt.date.between(date_range[0], date_range[1])]
elif isinstance(date_range, (tuple, list)) and len(date_range) == 1:
    filtered = filtered[filtered["order_date"].dt.date == date_range[0]]
filtered = filtered[
    filtered["region"].isin(selected_regions)
    & filtered["product_category"].isin(selected_categories)
    & filtered["order_status"].isin(selected_statuses)
]

if filtered.empty:
    st.warning("No records match the selected filters. Change the filters in the sidebar.")
    st.stop()

# KPI row
total_sales = filtered["sales_amount"].sum()
total_profit = filtered["profit"].sum()
orders = filtered["order_id"].nunique()
avg_sales = filtered["sales_amount"].mean()
avg_satisfaction = filtered["customer_satisfaction"].mean()
return_pct = (filtered["order_status"].eq("Returned").sum() / len(filtered) * 100)

def inr_crore(value):
    return f"₹{value / 10_000_000:,.2f} Cr"

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Recorded Sales", inr_crore(total_sales))
k2.metric("Recorded Profit", inr_crore(total_profit))
k3.metric("Orders", f"{orders:,}")
k4.metric("Average Sales / Record", f"₹{avg_sales:,.0f}")
k5.metric("Avg. Satisfaction", f"{avg_satisfaction:.2f} / 5" if pd.notna(avg_satisfaction) else "N/A")

st.markdown("<div class='section-label'>Sales & Profit Overview</div>", unsafe_allow_html=True)
left, right = st.columns([1.55, 1])
with left:
    monthly = (filtered.dropna(subset=["order_date"])
               .groupby("year_month", as_index=False)
               .agg(sales=("sales_amount", "sum"), profit=("profit", "sum")))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=monthly["year_month"], y=monthly["sales"], mode="lines+markers",
                             name="Recorded sales", line=dict(color="#356ae6", width=3)))
    fig.add_trace(go.Scatter(x=monthly["year_month"], y=monthly["profit"], mode="lines+markers",
                             name="Recorded profit", line=dict(color="#13a38b", width=2)))
    fig.update_layout(title="Monthly Sales & Profit Trend", height=360, margin=dict(l=10,r=10,t=55,b=10),
                      paper_bgcolor="white", plot_bgcolor="white", legend=dict(orientation="h", y=1.12),
                      xaxis_title="", yaxis_title="Amount (₹)", hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)
with right:
    category = (filtered.groupby("product_category", as_index=False)
                .agg(sales=("sales_amount", "sum"))
                .sort_values("sales"))
    fig = px.bar(category, x="sales", y="product_category", orientation="h",
                 title="Recorded Sales by Category", text_auto=".2s",
                 color="sales", color_continuous_scale=["#b9ccff", "#2856c5"])
    fig.update_layout(height=360, margin=dict(l=10,r=10,t=55,b=10), coloraxis_showscale=False,
                      paper_bgcolor="white", plot_bgcolor="white", xaxis_title="Sales (₹)",
                      yaxis_title="", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<div class='section-label'>Regional & Order Performance</div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    regional = filtered.groupby("region", as_index=False).agg(sales=("sales_amount","sum"), profit=("profit","sum"))
    fig = px.bar(regional.sort_values("sales"), x="sales", y="region", orientation="h",
                 title="Sales by Region", text_auto=".2s", color_discrete_sequence=["#4169d8"])
    fig.update_layout(height=320, margin=dict(l=5,r=5,t=55,b=5), paper_bgcolor="white", plot_bgcolor="white",
                      xaxis_title="Sales (₹)", yaxis_title="")
    st.plotly_chart(fig, use_container_width=True)
with c2:
    status = filtered["order_status"].value_counts().rename_axis("status").reset_index(name="records")
    fig = px.pie(status, names="status", values="records", hole=.58,
                 title="Order Status Distribution", color_discrete_sequence=px.colors.qualitative.Safe)
    fig.update_layout(height=320, margin=dict(l=5,r=5,t=55,b=5), paper_bgcolor="white",
                      legend=dict(orientation="h", y=-.12))
    st.plotly_chart(fig, use_container_width=True)
with c3:
    satisfaction = (filtered.groupby("product_category", as_index=False)
                    .agg(avg_rating=("customer_satisfaction","mean")))
    fig = px.bar(satisfaction.sort_values("avg_rating"), x="avg_rating", y="product_category",
                 orientation="h", title="Average Satisfaction by Category",
                 text_auto=".2f", color_discrete_sequence=["#13a38b"])
    fig.update_layout(height=320, margin=dict(l=5,r=5,t=55,b=5), paper_bgcolor="white",
                      plot_bgcolor="white", xaxis_title="Average rating (1–5)", yaxis_title="",
                      xaxis=dict(range=[0,5]))
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<div class='section-label'>Returns & Data Quality</div>", unsafe_allow_html=True)
r1, r2 = st.columns([1, 1])
with r1:
    returns = (filtered.assign(is_returned=filtered["order_status"].eq("Returned"))
               .groupby("product_category", as_index=False)
               .agg(total_records=("order_id","count"), returned_records=("is_returned","sum")))
    returns["return_pct"] = returns["returned_records"] / returns["total_records"] * 100
    fig = px.bar(returns.sort_values("return_pct"), x="return_pct", y="product_category",
                 orientation="h", title="Returned Records by Category (%)", text_auto=".2f",
                 color_discrete_sequence=["#e39b42"])
    fig.update_layout(height=330, margin=dict(l=5,r=5,t=55,b=5), paper_bgcolor="white",
                      plot_bgcolor="white", xaxis_title="Returned records (%)", yaxis_title="")
    st.plotly_chart(fig, use_container_width=True)
with r2:
    # Calculate discrepancy only where the inputs are present and the calculated amount is non-zero.
    calc = filtered["quantity"] * filtered["unit_price"] * (1 - filtered["discount_pct"])
    valid = calc.notna() & calc.ne(0) & filtered["sales_amount"].notna()
    mismatch_pct = ((filtered.loc[valid, "sales_amount"] - calc[valid]).abs() / calc[valid].abs() * 100)
    mismatch_count = int((mismatch_pct > 10).sum())
    mismatch_share = (mismatch_count / int(valid.sum()) * 100) if valid.sum() else 0
    st.markdown("#### Sales validation check")
    st.metric("Records differing by >10%", f"{mismatch_count:,} / {int(valid.sum()):,}")
    st.metric("Share of valid records", f"{mismatch_share:.2f}%")
    st.markdown(
        "<div class='note'><b>Interpretation:</b> Sales and profit KPIs use the original recorded fields. "
        "A large discrepancy exists between recorded sales and quantity × unit price × (1 − discount). "
        "Treat financial conclusions as provisional until the source data is validated. "
        "Returned-record percentages are status-based, not verified lifecycle return rates.</div>",
        unsafe_allow_html=True
    )

with st.expander("View filtered data summary"):
    summary = (filtered.groupby(["region","product_category"], as_index=False)
               .agg(records=("order_id","count"), sales=("sales_amount","sum"), profit=("profit","sum")))
    st.dataframe(summary, use_container_width=True, hide_index=True)
    st.download_button("Download filtered data (CSV)", filtered.to_csv(index=False).encode("utf-8"),
                       file_name="swynex_filtered_retail_data.csv", mime="text/csv")

st.markdown("---")
st.markdown("<div class='foot'>SWYNEX Internship · Retail dataset · Dashboard built with Streamlit, Pandas and Plotly. "
            "All figures respond to the sidebar filters. Recorded financial fields are subject to the data-quality limitation shown above.</div>",
            unsafe_allow_html=True)
