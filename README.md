# 🌎 Earth Pulse — Global Seismic Activity Dashboard

## Project Overview

Earth Pulse is an interactive Streamlit dashboard designed for international earthquake risk analysts to monitor global seismic activity patterns.

The dashboard transforms historical earthquake records into meaningful insights through key metrics, geographic visualization, and time-series analysis. Instead of displaying every available data point, this project focuses on the information that supports earthquake risk assessment and monitoring decisions.

---

# 1. Dataset

## Dataset Name

**Significant Earthquakes, 1965-2016**

## Source

Kaggle Dataset:

https://www.kaggle.com/datasets/usgs/earthquake-database?resource=download

Original data source:

United States Geological Survey (USGS)

---

## Dataset Description

This dataset contains significant earthquake records collected around the world from 1965 to 2016.

Each row represents one earthquake event.

The dataset includes information such as:

| Column | Description |
|--------|-------------|
| Date | Date when the earthquake occurred |
| Time | Time of earthquake occurrence |
| Latitude | Geographic latitude |
| Longitude | Geographic longitude |
| Depth | Earthquake depth in kilometers |
| Magnitude | Earthquake magnitude |
| Type | Type of seismic event |
| Location | Earthquake location description |

---

## Dataset Size

The dataset contains:

**23,412 earthquake records**

and

**21 variables**

The CSV file size is under 25 MB, making it suitable for GitHub storage and Streamlit Cloud deployment.

---

## Data Period

**1965 - 2016**

---

# 2. Decision Maker

## Target User

**International Earthquake Risk Analyst**

The dashboard is designed for earthquake risk analysts who monitor global seismic activity and evaluate potential risk areas.

---

## Usage Frequency

Analysts review this dashboard:

- Weekly for general monitoring
- Immediately after major earthquake events

---

# 3. Why This Dashboard?

## Current Problem

Without this dashboard, analysts need to manually explore large earthquake datasets and create separate reports to identify geographic patterns, magnitude changes, and high-risk regions.

This process requires additional time and makes it harder to quickly identify important seismic events.

---

## Decision Supported

Our dashboard supports the following decision:

> If earthquake analysts observe increasing seismic activity or repeated high-magnitude earthquakes in a region, they will investigate that area and update their risk assessment.

---

## Why a Dashboard Instead of a Report?

A report provides information at a single point in time.

A dashboard is more appropriate because earthquake analysts repeatedly need to:

- Explore different time periods
- Compare earthquake magnitude levels
- Identify geographic patterns

Interactive visualization allows users to quickly understand earthquake activity without repeatedly creating manual reports.

---

# 4. Dashboard Design Decisions

## Key Metrics

We selected three headline metrics that users can understand within seconds.

---

## 1. Total Earthquakes

### Purpose

Shows the total number of earthquake events based on the selected filters.

### Why It Matters

Provides a quick overview of seismic activity volume.

---

## 2. Maximum Magnitude

### Purpose

Displays the strongest earthquake magnitude within the selected dataset.

### Why It Matters

Extreme magnitude events are more likely to require additional investigation.

---

## 3. Major Earthquakes (Magnitude ≥ 7)

### Purpose

Counts earthquakes with magnitude greater than or equal to 7.

### Why It Matters

Large earthquakes are more likely to create significant impacts and require attention.

---

# Supporting Visualizations

## 1. Global Earthquake Distribution Map

The map displays earthquake locations around the world.

Visualization features:

- Latitude and Longitude → Geographic location
- Magnitude → Point size
- Depth → Color scale

### Decision Supported

Helps analysts identify regions with frequent or severe earthquake activity.

---

## 2. Earthquake Activity Trend Over Time

This chart shows how earthquake activity changes from 1965 to 2016.

### Decision Supported

Allows analysts to observe historical patterns and compare activity across different years.

---

# Filters

The dashboard includes only filters that support decision-making.

## Year Range

Allows users to analyze earthquake activity during different time periods.

## Magnitude Range

Allows users to focus on stronger earthquakes and reduce unnecessary information.

---

# 5. What We Chose Not to Show

## 1. Individual Earthquake Records Table

### Reason

The dataset contains thousands of earthquake events.

Displaying all individual records would make the dashboard harder to interpret and would not support high-level risk decisions.

---

## 2. Scientific Measurement Error Variables

### Reason

Some variables describe measurement uncertainty and technical scientific details.

Although these fields may be useful for researchers, they do not directly support earthquake risk monitoring decisions.

---

# 6. Data Limitations

## Historical Dataset

This dataset represents a historical snapshot from 1965 to 2016.

It does not provide real-time earthquake monitoring.

A production version would require continuously updated earthquake data sources.

---

## Significant Earthquake Focus

The dataset focuses on significant earthquake events and does not represent every small earthquake.

Therefore, users should not interpret this dashboard as a complete record of all seismic activity.

---

## Missing Values

Some scientific measurement fields contain missing values.

These fields are not used in the main dashboard analysis, so missing values do not affect the primary insights.

---

# 7. Data Refresh Strategy

## Production Refresh Frequency

The production version of this dashboard should refresh:

**Daily**

---

## Reason

Earthquake information changes continuously, but risk analysts usually make decisions based on daily or weekly patterns.

Real-time updates would increase system complexity and cost without significantly improving most decisions.

---

## Review Frequency

Analysts should review the dashboard:

- Weekly for monitoring
- Immediately after major earthquake events

---

## Action Trigger

The following situation should trigger further investigation:

> If an earthquake above magnitude 7.0 occurs in a populated region, analysts should investigate the event and update risk assessments.

---

## Cost of Stale Data

Outdated information may:

- Delay risk evaluation
- Slow emergency planning
- Prevent timely response to significant seismic activity

---

# 8. Technology Stack

## Tools Used

- Python
- Pandas
- Matplotlib
- Plotly
- Streamlit

## Deployment

Streamlit Cloud

---

# 9. Team Members

- Zhao Ziyu
- Chen Yuxiu
- Zhu Hanglin
- Wang Qirun

---

# 10. Project Structure
