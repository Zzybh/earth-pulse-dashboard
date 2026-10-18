# 🌎 Team 13 — Earth Pulse: Global Seismic Activity Dashboard

## Project Overview

Earth Pulse is an interactive Streamlit dashboard designed for **international earthquake risk analysts** to explore global seismic activity patterns and support earthquake risk assessment decisions.

The dashboard uses historical earthquake data to provide key performance indicators, geographic visualizations, annual trends, and detailed event exploration.

Rather than displaying every available variable, the dashboard prioritizes information that helps analysts identify significant earthquake patterns, investigate areas of concern, and support risk assessment.

The dashboard includes four analytical views:

* **Global Overview** — View key earthquake indicators, geographic distribution, and annual trends.
* **Spatiotemporal Explorer** — Explore earthquake locations and activity across different time periods.
* **Regional Analysis** — Examine the distribution of earthquakes across magnitude categories.
* **Event Explorer** — Investigate individual earthquake records in detail.

---

## 1. Dataset and Data Source

### Dataset Name

**Significant Earthquakes, 1965–2016**

### Data Source

Kaggle Dataset:

https://www.kaggle.com/datasets/usgs/earthquake-database

Original data source: **United States Geological Survey (USGS)**

### Dataset Description

The dataset contains historical records of significant seismic events worldwide from 1965 to 2016.

Each row represents one recorded seismic event.

Important variables include:

| Column    | Description                       |
| --------- | --------------------------------- |
| Date      | Date of the seismic event         |
| Time      | Time of occurrence                |
| Latitude  | Geographic latitude               |
| Longitude | Geographic longitude              |
| Depth     | Depth of the event in kilometers  |
| Magnitude | Recorded magnitude                |
| Type      | Type of seismic event             |
| Source    | Source of the seismic information |

### Dataset Size and Cleaning

The original dataset contains **23,412 seismic event records** and **21 variables**.

For this dashboard, only natural earthquakes (`Type == "Earthquake"`) are included. Other seismic event types are excluded to keep the analysis focused on natural earthquake activity.

The data cleaning process also removes records with missing essential values required for visualization, including geographic coordinates, depth, magnitude, and date information.

After filtering and cleaning, the dashboard uses **23,232 earthquake records** for analysis.

The CSV file is under 25 MB, making it suitable for GitHub storage and Streamlit Cloud deployment.

### Data Period

**1965–2016**

The dataset is a historical snapshot rather than a live earthquake monitoring feed.

---

## 2. Target Decision-Maker

### Target User

**International Earthquake Risk Analyst**

The dashboard is designed for analysts responsible for examining global seismic activity, identifying areas that may require further investigation, and supporting earthquake risk assessment.

### Usage Frequency

In a production environment, analysts would review the dashboard:

* Weekly to examine seismic activity patterns.
* After significant earthquake events to investigate affected areas and update risk assessments.

### Decision Supported

The main decision supported by the dashboard is:

> If an earthquake risk analyst observes unusual changes in recorded seismic activity or repeated high-magnitude earthquakes in a region, they will investigate that area and determine whether the existing risk assessment needs to be updated.

This connects the information displayed on the dashboard to a specific action.

---

## 3. Why a Dashboard?

### Current Problem

Without a centralized dashboard, analysts may need to manually examine earthquake records, filter large datasets, and create separate charts or reports to understand geographic and temporal patterns.

This process takes additional time and makes it harder to compare information across different periods and earthquake magnitudes.

Important patterns may also be overlooked when information is distributed across separate analyses.

### Why a Dashboard Instead of a Report?

A static report is useful for answering a specific question at a particular time. However, earthquake risk analysts repeatedly need to examine similar questions using different time periods and magnitude thresholds.

An interactive dashboard allows analysts to:

* Monitor key earthquake indicators.
* Compare historical earthquake activity across years.
* Explore geographic concentrations of earthquakes.
* Focus on events above selected magnitude thresholds.
* Investigate individual earthquake records when additional detail is needed.

A weekly report would provide a fixed summary, while the dashboard allows analysts to explore different questions without repeatedly preparing new reports.

For urgent earthquake events, an automated alert would complement the dashboard rather than replace it. The dashboard would provide additional context for investigation.

---

## 4. Exploratory Data Analysis (EDA)

Before designing the dashboard, the dataset was explored using Pandas and Matplotlib.

The exploratory analysis focused on:

* Dataset shape and data types.
* Missing values and data quality.
* Earthquake magnitude distributions.
* Annual earthquake event counts.
* Geographic coordinates and earthquake depth.
* Relationships between earthquake characteristics.

### How EDA Influenced the Dashboard Design

**Magnitude Distribution**

Examining earthquake magnitudes motivated the inclusion of the Major Earthquakes (M ≥ 7) KPI and magnitude-based filtering.

These elements allow analysts to focus on stronger earthquakes rather than treating every recorded event as equally important.

**Annual Earthquake Activity**

Examining event counts by year motivated the Seismic Events by Year chart.

This visualization helps analysts compare historical activity across different periods and identify years that may deserve further investigation.

**Geographic Distribution**

The availability of latitude and longitude information motivated the global earthquake map.

This allows analysts to identify geographic concentrations of recorded earthquakes and investigate specific locations.

**Earthquake Depth**

Depth was included as a color dimension on the map, providing additional information without requiring another separate chart.

These EDA considerations, together with the intended user's needs, guided the selection of dashboard elements.

---

## 5. Dashboard Design Decisions

The dashboard follows a focused design: important information appears first, while more detailed exploration is available through separate navigation options.

### 5.1 Headline Key Performance Indicators

Three KPIs are displayed at the top of the dashboard using Streamlit's `st.metric`.

| KPI                       | Purpose                                                   | Decision Value                                         |
| ------------------------- | --------------------------------------------------------- | ------------------------------------------------------ |
| Total Events              | Counts earthquakes matching the selected filters          | Provides an overview of recorded earthquake activity   |
| Maximum Magnitude         | Shows the largest recorded magnitude in the selected data | Helps identify the strongest event                     |
| Major Earthquakes (M ≥ 7) | Counts earthquakes with magnitude at least 7              | Helps analysts focus on potentially significant events |

These metrics provide an immediate summary without requiring users to examine detailed charts.

All three KPIs respond to the selected date and magnitude filters.

### 5.2 Supporting Visualizations

**Global Earthquake Risk Map**

The map displays the geographic locations of historical earthquakes.

* Latitude and Longitude represent location.
* Marker size represents magnitude.
* Marker color represents earthquake depth.

**Decision supported:** Analysts can identify geographic concentrations of historical earthquakes and investigate areas with significant recorded activity.

The map provides historical context and does not independently predict future earthquake risk.

**Seismic Events by Year**

This line chart displays the number of recorded earthquakes in each year within the selected filters.

**Decision supported:** Analysts can compare historical earthquake activity across years and identify periods that may require further investigation.

Changes in recorded counts must be interpreted carefully because historical reporting and data completeness may vary.

**Magnitude Category Analysis**

The dashboard groups earthquakes into the following magnitude categories:

* 5.5–6.0
* 6.0–7.0
* 7.0–8.0
* Above 8.0

**Decision supported:** Analysts can compare earthquake counts across magnitude levels and focus on more significant events.

**Event Explorer**

The Event Explorer displays individual earthquake records, including dates, locations, magnitudes, depths, and event types.

**Decision supported:** Analysts can investigate specific earthquakes after identifying patterns in the summary visualizations.

### 5.3 Interactive Filters

The dashboard includes two main filters.

**Date Range**

Allows analysts to focus on selected years and compare earthquake activity across historical periods.

**Magnitude Range**

Allows analysts to restrict the analysis to earthquakes within selected magnitude thresholds.

These filters were chosen because they directly support the intended analytical decisions without adding unnecessary complexity.

### 5.4 Dashboard Layout and Information Hierarchy

The dashboard follows a top-to-bottom information hierarchy.

**Top — Key Information**

The title, dashboard purpose, data period, and three headline KPIs appear first.

This allows analysts to quickly understand the dataset's scope and the most important summary information.

**Middle — Supporting Evidence**

The global earthquake map and annual trend chart provide additional context about where earthquakes occurred and how recorded activity changed over time.

**Detailed Exploration**

Magnitude analysis and individual event records are available through separate navigation options.

This structure keeps the main dashboard focused while allowing analysts to access more detailed information when necessary.

The layout prioritizes quick interpretation over displaying as many charts as possible.

---

## 6. What Was Intentionally Excluded?

### 6.1 Complete Raw Dataset on the Main Page

The dataset contains thousands of earthquake records.

Displaying the complete table on the main page would take up substantial space and make the most important information harder to identify.

Instead, detailed records are available through the Event Explorer.

This keeps the main dashboard focused on summary indicators and supporting visualizations.

### 6.2 Scientific Measurement Uncertainty Variables

The original dataset includes technical variables related to earthquake measurement uncertainty.

Although these variables may be valuable for specialized scientific analysis, they are less directly relevant to the dashboard's primary purpose of exploring historical seismic patterns.

They were therefore excluded from the main visualizations to reduce complexity.

### 6.3 Non-Earthquake Seismic Events

The original dataset includes event types other than natural earthquakes.

These records were excluded so that the dashboard consistently focuses on natural earthquake activity.

This prevents different seismic event types from being combined into the headline earthquake indicators.

---

## 7. Data Limitations and Interpretation

### Historical Data

The dashboard uses historical records from 1965 to 2016.

It does not provide real-time earthquake monitoring, and its results should not be interpreted as current seismic conditions.

### Significant Earthquake Coverage

The dataset focuses on significant seismic events and does not include every earthquake worldwide.

Therefore, the Total Events KPI represents the number of records within the selected dataset and filters, not the complete number of earthquakes that occurred globally.

### Missing Values and Data Cleaning

Records missing essential geographic, magnitude, depth, or date information were excluded from the dashboard analysis.

As a result, the dashboard represents the cleaned subset of available records.

### Historical Reporting Differences

Earthquake detection and reporting practices may have changed over time.

Therefore, an increase in recorded earthquake counts does not necessarily mean that the true global earthquake rate increased.

### Risk Interpretation

Earthquake magnitude and location provide useful information, but they are not sufficient to determine overall risk.

Population exposure, infrastructure vulnerability, local geological conditions, and other factors also affect earthquake impacts.

The dashboard should therefore be used as an exploratory tool to support further risk assessment rather than as a complete risk prediction system.

---

## 8. Data Refresh Strategy

### 8.1 Production Refresh Frequency

**Intended production refresh frequency: Daily**

The current dashboard uses a fixed historical Kaggle dataset and does not automatically receive new earthquake records.

In a production environment, the dashboard would connect to an updated earthquake data source.

Daily refreshes would provide a practical balance between data freshness, analytical needs, and system maintenance.

### 8.2 Why Daily Refresh?

Earthquake events occur continuously, but the dashboard's primary purpose is to support repeated risk analysis rather than immediate emergency warning.

For routine analytical reviews, daily updates would generally provide sufficient information.

Real-time data processing would require additional infrastructure and maintenance.

Urgent earthquake notifications should be handled through a separate alert system rather than relying only on scheduled dashboard refreshes.

### 8.3 Review Frequency

The intended review schedule is:

* **Weekly:** Analysts review broader earthquake activity patterns and areas of concern.
* **Event-driven:** Analysts investigate significant earthquakes when notified through an appropriate external alert system.

The data refresh frequency and review frequency are different because new information may arrive more frequently than routine analytical decisions are made.

### 8.4 Action Trigger

The main action trigger is:

> If an earthquake with magnitude 7.0 or greater occurs near a populated area, the analyst should investigate the event and assess whether regional risk estimates need to be updated.

This threshold is intended to prioritize investigation, not to predict earthquake damage.

A production implementation would require current event information and population exposure data to evaluate this trigger.

### 8.5 Cost of Stale Data

Outdated data could lead to:

* Delayed identification of significant earthquake events.
* Slower updates to regional risk assessments.
* Decisions based on incomplete recent activity.
* Delays in communicating relevant information to stakeholders.

Daily refreshes would reduce these problems for routine analysis, while urgent events would still require a separate alert mechanism.

### 8.6 Data Transparency

The dashboard displays its historical data period and intended production refresh frequency.

It also includes a note explaining that the current application is intended for historical analysis and does not represent real-time monitoring.

This helps prevent users from confusing the historical dataset with live earthquake information.

---

## 9. Technology Stack

The dashboard was developed using:

* **Python** — Application development and data processing.
* **Pandas** — Data cleaning, filtering, and aggregation.
* **Matplotlib** — Exploratory data analysis.
* **Plotly** — Interactive geographic and statistical visualizations.
* **Streamlit** — Dashboard interface and interactive controls.
* **GitHub** — Source code hosting and version control.
* **Streamlit Community Cloud** — Application deployment.

---

## 10. Team Members

This project builds on the dataset and dashboard concept developed by Team 13.

Team members:

* Zhao Ziyu
* Chen Yuxiu
* Zhu Hanglin
* Wang Qirun

For Assignment 4 Part 1, the application and GitHub repository are submitted individually, with the README documenting the student's own design decisions and justifications.

---

## 11. Project Structure

```text
earth-pulse-dashboard/
├── app.py
├── EDA.ipynb
├── README.md
├── requirements.txt
└── data/
    └── database.csv
```

**File Descriptions**

* `app.py` — Main Streamlit dashboard application.
* `EDA.ipynb` — Exploratory data analysis notebook.
* `README.md` — Project documentation and design justifications.
* `requirements.txt` — Python package dependencies.
* `data/database.csv` — Historical earthquake dataset.

---

## 12. Conclusion

Earth Pulse demonstrates how historical earthquake records can be transformed into a focused, interactive dashboard for risk analysis.

The project prioritizes a clearly defined decision-maker, meaningful KPIs, supporting visualizations, and a practical data refresh strategy.

By separating high-level information from detailed exploration, the dashboard helps analysts investigate historical seismic activity without unnecessary visual complexity.

The current application supports historical analysis, while a future production version could incorporate regularly updated earthquake data and separate event alerts to support more timely risk assessment.
