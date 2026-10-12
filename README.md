# 🌎 Team 13 — Earth Pulse: Global Seismic Activity Dashboard

## Project Overview

Earth Pulse is an interactive Streamlit dashboard designed for international earthquake risk analysts to monitor global seismic activity patterns and support earthquake risk assessment decisions.

The dashboard transforms historical earthquake records into meaningful insights through key metrics, geographic visualization, time-series analysis, regional comparison, and event exploration.

Instead of displaying every available data point, this project focuses on the information that helps analysts identify important seismic patterns and make informed decisions.

The dashboard provides four analytical perspectives:

- **Global Overview** — High-level monitoring of worldwide seismic activity
- **Spatiotemporal Explorer** — Exploration of earthquake activity across different time periods
- **Regional Analysis** — Comparison of earthquake characteristics by magnitude categories
- **Event Explorer** — Detailed investigation of individual earthquake records

---

# 1. Dataset

## Dataset Name

**Significant Earthquakes, 1965-2016**

---

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
| Source | Data source information |

---

## Dataset Size

The original dataset contains:

**23,412 earthquake records**

and

**21 variables**

After removing records with missing geographic or measurement values required for visualization, the dashboard uses:

**23,409 valid earthquake records**

for analysis.

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

- Weekly for general seismic monitoring
- Immediately after major earthquake events

---

# 3. Why This Dashboard?

## Current Problem

Without this dashboard, analysts need to manually explore large earthquake datasets and create separate reports to identify geographic patterns, magnitude changes, and high-risk regions.

This process requires additional time and makes it difficult to quickly identify important seismic events.

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
- Investigate specific earthquake events

Interactive visualization allows users to quickly understand earthquake activity without repeatedly creating manual reports.

---

# 4. Dashboard Design Decisions

## Key Performance Indicators (KPIs)

We selected four headline metrics that users can understand within seconds.

---

## 1. Total Events

### Purpose

Shows the total number of earthquake events based on the selected filters.

### Why It Matters

Provides a quick overview of seismic activity volume and helps analysts understand the scale of current observations.

---

## 2. Maximum Magnitude

### Purpose

Displays the strongest earthquake magnitude within the selected dataset.

### Why It Matters

Extreme magnitude events are more likely to require additional investigation and risk assessment.

---

## 3. Average Depth

### Purpose

Shows the average earthquake depth of selected events.

### Why It Matters

Depth provides additional context about earthquake characteristics and helps analysts understand differences between seismic events.

---

## 4. Major Earthquakes (Magnitude ≥7)

### Purpose

Counts earthquakes with magnitude greater than or equal to 7.

### Why It Matters

Large earthquakes are more likely to create significant impacts and require attention.

---

# Supporting Visualizations

## 1. Global Earthquake Risk Map

The map displays earthquake locations around the world.

Visualization features:

- Latitude and Longitude → Geographic location
- Magnitude → Point size
- Depth → Color scale

### Decision Supported

Helps analysts identify regions with frequent or severe earthquake activity.

---

## 2. Seismic Events by Year

This time-series chart shows how earthquake activity changes from 1965 to 2016.

### Decision Supported

Allows analysts to observe historical activity patterns and compare earthquake frequency across different years.

---

## 3. Regional Analysis

This view groups earthquakes by magnitude categories:

- 5.5-6.0
- 6.0-7.0
- 7.0-8.0
- 8.0+

### Decision Supported

Helps analysts compare earthquake severity distribution.

---

## 4. Event Explorer

This view provides detailed earthquake records for users who need additional investigation.

### Decision Supported

Allows analysts to examine specific earthquake events after identifying important patterns.

---

# Filters

The dashboard includes only filters that support decision-making.

---

## Date Range

Allows users to analyze earthquake activity during different time periods.

---

## Magnitude Range

Allows users to focus on earthquakes with specific severity levels and reduce unnecessary information.

---

# 5. What We Chose Not to Show

## 1. Complete Raw Dataset Table

### Reason

The dataset contains thousands of earthquake events.

Displaying all records at once would make the dashboard harder to interpret and would not support high-level risk decisions.

Only the Event Explorer view provides detailed records when users need deeper investigation.

---

## 2. Scientific Measurement Error Variables

### Reason

Some variables describe technical measurement uncertainty.

Although these fields may be useful for scientific research, they do not directly support earthquake risk monitoring decisions.

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

## Missing Values and Data Cleaning

Some scientific measurement fields contain missing values.

Records missing essential geographic or measurement information were removed before visualization.

The dashboard therefore represents cleaned earthquake records rather than the complete raw dataset.

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

```
earth-pulse-dashboard/

├── app.py
├── EDA.ipynb
├── README.md
├── requirements.txt
│
└── data/
    └── database.csv
```
