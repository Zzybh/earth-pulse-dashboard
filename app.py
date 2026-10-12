import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Team 13 - Earth Pulse",
    layout="wide"
)


@st.cache_data
def load_data():
    df = pd.read_csv("data/database.csv")

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Year"] = df["Date"].dt.year

    for col in ["Latitude", "Longitude", "Depth", "Magnitude"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(
        subset=[
            "Latitude",
            "Longitude",
            "Depth",
            "Magnitude",
            "Year"
        ]
    )

    df["Magnitude Category"] = pd.cut(
        df["Magnitude"],
        bins=[5.5, 6, 7, 8, 10],
        labels=[
            "5.5-6.0",
            "6.0-7.0",
            "7.0-8.0",
            "8.0+"
        ],
        include_lowest=True
    )

    return df


df = load_data()


# Header
st.title("🌎 Team 13 — Earth Pulse")
st.subheader("Global Seismic Intelligence")

st.caption(
    "Interactive dashboard for international earthquake risk analysts "
    "to monitor global seismic activity and support risk assessment."
)

st.info(
    """
    Historical Data: 1965-2016  
    Source: Kaggle Significant Earthquakes Dataset (USGS)  
    Production Refresh Frequency: Daily
    """
)


# Navigation style sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Explore",
    [
        "Global Overview",
        "Spatiotemporal Explorer",
        "Regional Analysis",
        "Event Explorer"
    ]
)


# Controls
st.sidebar.divider()
st.sidebar.header("Global Control Center")

year_range = st.sidebar.slider(
    "Date Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (
        int(df["Year"].min()),
        int(df["Year"].max())
    )
)

mag_range = st.sidebar.slider(
    "Magnitude Range",
    float(df["Magnitude"].min()),
    float(df["Magnitude"].max()),
    (
        5.5,
        float(df["Magnitude"].max())
    )
)


filtered = df[
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1]) &
    (df["Magnitude"] >= mag_range[0]) &
    (df["Magnitude"] <= mag_range[1])
]


if filtered.empty:
    st.warning("No earthquake records match your filters.")
    st.stop()


# KPI cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Events",
        f"{len(filtered):,}"
    )

with col2:
    st.metric(
        "Maximum Magnitude",
        f"M {filtered['Magnitude'].max():.1f}"
    )

with col3:
    major = len(filtered[filtered["Magnitude"] >= 7])
    st.metric(
        "Major Earthquakes · M≥7",
        f"{major:,}"
    )


# Map
if page in [
    "Global Overview",
    "Spatiotemporal Explorer",
    "Event Explorer"
]:

    st.subheader("Global Earthquake Risk Map")

    st.caption(
        "Marker size represents magnitude; color represents earthquake depth."
    )

    fig_map = px.scatter_geo(
        filtered,
        lat="Latitude",
        lon="Longitude",
        size="Magnitude",
        color="Depth",
        hover_data=[
            "Date",
            "Magnitude",
            "Depth",
            "Type"
        ],
        projection="natural earth"
    )

    st.plotly_chart(
        fig_map,
        use_container_width=True
    )


# Trend chart
if page in [
    "Global Overview",
    "Spatiotemporal Explorer"
]:

    st.subheader("Seismic Events by Year")

    yearly = (
        filtered
        .groupby("Year")
        .size()
        .reset_index(name="Events")
    )

    fig_line = px.line(
        yearly,
        x="Year",
        y="Events",
        markers=True
    )

    st.plotly_chart(
        fig_line,
        use_container_width=True
    )


# Regional analysis
if page == "Regional Analysis":

    st.subheader("Magnitude Category Analysis")

    category = (
        filtered["Magnitude Category"]
        .value_counts()
        .reset_index()
    )

    category.columns = [
        "Magnitude Category",
        "Count"
    ]

    fig_bar = px.bar(
        category,
        x="Magnitude Category",
        y="Count"
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )


# Event explorer
if page == "Event Explorer":

    st.subheader("Selected Earthquake Events")

    st.dataframe(
        filtered[
            [
                "Date",
                "Latitude",
                "Longitude",
                "Magnitude",
                "Depth",
                "Type"
            ]
        ].sort_values(
            "Magnitude",
            ascending=False
        ),
        use_container_width=True
    )


st.caption(
    """
    Note: This dashboard uses historical earthquake data from 1965-2016.
    It is designed for analysis and does not represent real-time monitoring.
    """
)
