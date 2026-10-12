import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(
    page_title="Earth Pulse",
    layout="wide"
)
@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/database.csv"
    )

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    df["Year"] = (
        df["Date"]
        .dt.year
    )

    return df


df = load_data()
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
year_range = st.slider(
    "Select Year Range",
    int(df.Year.min()),
    int(df.Year.max()),
    (
        int(df.Year.min()),
        int(df.Year.max())
    )
)
mag_range = st.slider(
    "Select Magnitude Range",
    float(df.Magnitude.min()),
    float(df.Magnitude.max()),
    (
        5.5,
        float(df.Magnitude.max())
    )
)
filtered = df[
    (df.Year >= year_range[0]) &
    (df.Year <= year_range[1]) &
    (df.Magnitude >= mag_range[0]) &
    (df.Magnitude <= mag_range[1])
]
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
            filtered.Magnitude.max(),
            1
        )
    )


with col3:
    major = len(
        filtered[
            filtered.Magnitude >= 7
        ]
    )

    st.metric(
        "Major Earthquakes (≥7)",
        major
    )
st.subheader(
    "Global Earthquake Distribution"
)


fig_map = px.scatter_geo(
    filtered,
    lat="Latitude",
    lon="Longitude",
    size="Magnitude",
    color="Depth",
    hover_name="Location",
    projection="natural earth"
)


st.plotly_chart(
    fig_map,
    use_container_width=True
)
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
    y="Count"
)


st.plotly_chart(
    fig_line,
    use_container_width=True
)
st.caption(
    """
    Note:
    This dashboard uses historical earthquake data.
    It does not represent real-time earthquake monitoring.
    """
)