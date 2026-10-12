import streamlit as st
import pandas as pd
import plotly.express as px


# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="Earth Pulse",
    layout="wide"
)


# -------------------------
# Load Data
# -------------------------

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/database.csv"
    )

    # Convert date
    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    df["Year"] = df["Date"].dt.year


    # Ensure numeric columns
    numeric_columns = [
        "Latitude",
        "Longitude",
        "Depth",
        "Magnitude"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )


    # Remove invalid rows
    df = df.dropna(
        subset=[
            "Latitude",
            "Longitude",
            "Depth",
            "Magnitude",
            "Year"
        ]
    )

    return df



df = load_data()


# -------------------------
# Title
# -------------------------

st.title(
    "🌎 Earth Pulse — Global Seismic Activity Monitor"
)


st.caption(
    "Dashboard for international earthquake risk analysts "
    "to monitor global seismic patterns."
)


st.info(
    """
    Data Period: 1965-2016  
    Source: Kaggle Significant Earthquakes Dataset (USGS)  
    Production Refresh: Daily
    """
)



# -------------------------
# Filters
# -------------------------

st.sidebar.header(
    "Filters"
)


year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (
        int(df["Year"].min()),
        int(df["Year"].max())
    )
)


mag_range = st.sidebar.slider(
    "Select Magnitude Range",
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


# -------------------------
# Check Empty Data
# -------------------------

if filtered.empty:

    st.warning(
        "No earthquake records match your selected filters."
    )

    st.stop()



# -------------------------
# KPI Metrics
# -------------------------

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Total Earthquakes",
        len(filtered)
    )


with col2:

    st.metric(
        "Maximum Magnitude",
        round(
            filtered["Magnitude"].max(),
            1
        )
    )


with col3:

    major_events = len(
        filtered[
            filtered["Magnitude"] >= 7
        ]
    )

    st.metric(
        "Major Earthquakes (≥7)",
        major_events
    )



# -------------------------
# Map
# -------------------------

st.subheader(
    "Global Earthquake Risk Map"
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



# -------------------------
# Trend Chart
# -------------------------

st.subheader(
    "Earthquake Activity Trend"
)


trend = (
    filtered
    .groupby("Year")
    .size()
    .reset_index(
        name="Count"
    )
)


fig_line = px.line(
    trend,
    x="Year",
    y="Count",
    markers=True
)


st.plotly_chart(
    fig_line,
    use_container_width=True
)



# -------------------------
# Footer
# -------------------------

st.caption(
    """
    Note:
    This dashboard uses historical earthquake data.
    It does not represent real-time earthquake monitoring.
    """
)
