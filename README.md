# 🌎 Team 13 — Earth Pulse: Global Seismic Activity Dashboard

## Project Overview

Earth Pulse is an interactive Streamlit dashboard designed for **international earthquake risk analysts** to explore historical earthquake activity and support seismic risk assessment.

The dashboard uses historical earthquake records from 1965 to 2016 to help analysts identify geographic concentrations of earthquakes, examine changes in recorded activity over time, and investigate major seismic events.

Rather than displaying every available variable, the dashboard focuses on a small number of key indicators and visualizations that support meaningful analysis.

The application includes four analytical views:

* **Global Overview** — Summarizes earthquake activity through headline metrics, a global map, and an annual trend chart.
* **Spatiotemporal Explorer** — Allows analysts to explore geographic and temporal earthquake patterns using interactive filters.
* **Regional Analysis** — Compares the distribution of earthquakes across magnitude categories.
* **Event Explorer** — Provides detailed records for investigating individual earthquakes.

The dashboard is intended for historical analysis rather than real-time earthquake monitoring or prediction.

---

# 1. Dataset and Decision-Maker

## 1.1 Dataset

**Dataset Name:** Significant Earthquakes, 1965–2016

**Kaggle Source:**

https://www.kaggle.com/datasets/usgs/earthquake-database

**Original Data Source:** United States Geological Survey (USGS)

**Data Period:** 1965–2016

The original dataset contains **23,412 seismic event records and 21 variables**.

Each row represents one recorded seismic event. The original dataset includes natural earthquakes and other seismic events, such as nuclear explosions.

For this dashboard, I selected only records classified as `Earthquake` because the intended users are interested in natural earthquake activity.

After filtering and cleaning, the dashboard contains **23,232 earthquake records**.

The CSV file is smaller than 25 MB, making it suitable for GitHub storage and Streamlit Cloud deployment.

### Important Variables

| Column    | Description                     |
| --------- | ------------------------------- |
| Date      | Date of the recorded event      |
| Time      | Recorded event time             |
| Latitude  | Geographic latitude             |
| Longitude | Geographic longitude            |
| Depth     | Earthquake depth in kilometers  |
| Magnitude | Recorded earthquake magnitude   |
| Type      | Classification of seismic event |
| Source    | Data source information         |

### Data Preparation

The data preparation process includes:

1. Loading the original CSV dataset using Pandas.
2. Keeping only records where `Type == "Earthquake"`.
3. Converting mixed date formats into a consistent datetime format.
4. Extracting the year for temporal analysis.
5. Converting latitude, longitude, depth, and magnitude into numeric values.
6. Removing records missing essential fields required for visualization.
7. Creating magnitude categories for comparing earthquake severity.

These steps help maintain consistent records and prevent non-earthquake events from affecting the analysis.

## 1.2 Decision-Maker

**Target User: International Earthquake Risk Analyst**

The dashboard is designed for analysts responsible for examining historical earthquake activity and identifying areas that may require further risk assessment.

The intended user reviews historical patterns during regular risk assessment work and investigates relevant historical events when preparing regional assessments.

In a future production system connected to updated earthquake data, analysts could also use the dashboard after significant new events.

---

# 2. Why a Dashboard?

## 2.1 Current Problem

Without an interactive dashboard, analysts may need to examine large CSV files, apply filters manually, and generate separate charts to compare earthquake activity across locations and time periods.

This process takes additional time and makes it harder to move between global patterns and individual event records.

A static report can answer a specific question, but it is less flexible when analysts need to examine different regions, time periods, or magnitude thresholds.

## 2.2 Decision Supported

The main decision supported by this dashboard is **which geographic areas or historical earthquake patterns deserve further investigation**.

For example:

> If an earthquake risk analyst observes repeated high-magnitude earthquakes or a concentration of historical events in a particular region, they will prioritize that region for further investigation and review additional geological and exposure information before updating the risk assessment.

This decision connects the information displayed on the dashboard to a practical analytical action.

Historical earthquake frequency alone does not establish future earthquake probability or expected damage. Therefore, the dashboard is used to identify areas for further investigation rather than to make final risk predictions.

## 2.3 Why a Dashboard Instead of a Report or Alert?

A dashboard is appropriate because analysts repeatedly need to answer similar questions using different filters.

These questions include:

* Where are recorded earthquakes concentrated?
* How does the number of recorded earthquakes vary across years?
* Which earthquakes have the highest magnitudes?
* How do earthquake characteristics differ across selected periods?

A weekly report would provide a fixed summary, while the dashboard allows analysts to change the date and magnitude ranges independently.

An alert would be more appropriate for notifying users about a newly detected major earthquake. However, an alert cannot replace the historical exploration and comparison supported by this dashboard.

For these reasons, the dashboard is intended to support repeated analysis, while a future production system could use separate alerts for urgent events.

---

# 3. Exploratory Data Analysis and Dashboard Design

## 3.1 Exploratory Data Analysis

Before designing the dashboard, I explored the dataset using Pandas and Matplotlib.

The EDA included:

* Checking the dataset shape and data types.
* Identifying missing values.
* Examining the distribution of earthquake magnitudes.
* Analyzing annual earthquake counts.
* Exploring the relationship between earthquake depth and magnitude.

The analysis helped identify which variables were most relevant to the intended user's decisions.

### Key EDA Observations

**Magnitude Distribution**

The dataset contains earthquakes of different magnitudes, with relatively fewer events at the highest magnitude levels.

This supports including a separate indicator for major earthquakes rather than relying only on total event counts.

**Earthquake Activity Over Time**

Recorded earthquake counts vary across years.

This supports including an annual trend chart so analysts can compare historical periods and investigate changes in recorded activity.

However, changes in recorded counts may also reflect differences in earthquake detection and reporting over time.

**Geographic Location and Depth**

Latitude, longitude, and depth provide complementary information about earthquake locations and characteristics.

This supports using a geographic map where marker size represents magnitude and marker color represents depth.

These findings guided the selection of the dashboard's headline metrics, visualizations, and filters.

## 3.2 Headline Metrics

The dashboard uses exactly three headline KPIs, displayed at the top using Streamlit's `st.metric` and `st.columns`.

### KPI 1: Total Events

Shows the number of natural earthquake records matching the selected filters.

**Reason for inclusion:** It provides a quick summary of the amount of recorded earthquake activity within the selected period and magnitude range.

### KPI 2: Maximum Magnitude

Shows the highest recorded earthquake magnitude within the filtered dataset.

**Reason for inclusion:** It helps analysts quickly identify the strongest recorded event in the selected data.

### KPI 3: Major Earthquakes (M ≥ 7)

Shows the number of recorded earthquakes with magnitude greater than or equal to 7.

**Reason for inclusion:** It separates major earthquakes from the overall event count and helps analysts identify periods with potentially significant seismic events.

These three indicators provide a concise summary without overwhelming the user with unnecessary numbers.

## 3.3 Supporting Visualizations

### Global Earthquake Map

The geographic map uses:

* Latitude and longitude to show earthquake locations.
* Marker size to represent magnitude.
* Marker color to represent earthquake depth.

**Reason for inclusion:** Geographic distribution is central to understanding historical seismic activity. The map helps analysts locate concentrations of recorded earthquakes and identify areas for further investigation.

The map shows historical earthquake locations, not a validated prediction of future earthquake risk.

### Seismic Events by Year

The line chart shows the number of recorded earthquakes in each year.

**Reason for inclusion:** Analysts can examine historical changes in recorded earthquake activity and compare periods.

The chart complements the headline event count by showing how recorded activity varies over time.

### Magnitude Category Analysis

The bar chart groups earthquakes into magnitude categories.

**Reason for inclusion:** It helps analysts compare the frequency of different earthquake magnitude ranges.

This analysis focuses on magnitude distribution rather than geographic regions.

### Event Explorer

The Event Explorer provides a detailed table containing event dates, locations, magnitudes, depths, and event types.

**Reason for inclusion:** Analysts may need to examine individual records after identifying an interesting pattern in the summary charts.

The detailed table is placed in a separate view to avoid overcrowding the main dashboard.

## 3.4 Filters

The dashboard provides two main filters.

**Date Range:** Allows analysts to focus on particular historical periods and compare earthquake activity across years.

**Magnitude Range:** Allows analysts to focus on earthquakes of particular magnitudes, including major events.

Both filters directly support the intended analytical decisions.

Additional filters were not prioritized because they would increase interface complexity without necessarily improving the main workflow.

## 3.5 Dashboard Layout and Information Hierarchy

The dashboard follows a top-to-bottom information hierarchy.

**Top — Headline Information**

The dashboard title, data period, refresh information, and three headline KPIs appear first.

This allows analysts to understand the scope and main statistics of the selected data quickly.

**Middle — Supporting Analysis**

The geographic map and annual trend chart appear below the KPIs.

These visualizations provide more context by showing where earthquakes occurred and how recorded activity changed over time.

**Detailed Views — Further Investigation**

Magnitude analysis and individual event records are available through navigation options.

This keeps the main overview focused while allowing analysts to investigate more detailed questions when necessary.

The layout prioritizes the most important information and reduces unnecessary scrolling through detailed records.

## 3.6 What I Chose Not to Show

### 1. The Complete Raw Dataset on the Main Page

The original dataset contains thousands of records.

Displaying the entire dataset on the main page would make it difficult to identify important patterns quickly.

Instead, detailed records are available through the Event Explorer when needed.

### 2. Scientific Measurement Error Variables

The dataset contains technical variables related to measurement uncertainty and recording methods.

Although these variables may be important for specialized scientific research, they are not essential to the dashboard's primary task of exploring historical earthquake patterns.

Excluding them from the main interface keeps the dashboard easier to interpret.

These variables are not necessarily unimportant; they are simply outside the scope of this particular dashboard.

## 3.7 Data Limitations and Potential Misinterpretations

### Historical Data

The dataset covers 1965–2016 and does not update automatically.

The dashboard should not be interpreted as a real-time earthquake monitoring system.

### Significant Earthquake Coverage

The dataset focuses on significant recorded seismic events and does not include every earthquake worldwide.

As a result, the event counts do not represent the total number of earthquakes that occurred globally.

### Changes in Detection and Reporting

Earthquake detection technology and reporting practices have changed over time.

Therefore, differences in annual recorded earthquake counts should not automatically be interpreted as changes in underlying earthquake occurrence rates.

### Historical Activity Versus Future Risk

A region with many recorded earthquakes is not necessarily the region with the highest expected future damage.

A complete risk assessment also requires information about geological hazards, population exposure, infrastructure, and vulnerability.

### Data Cleaning

The original dataset includes non-earthquake seismic events and some missing measurement fields.

The dashboard excludes non-earthquake event types and records without essential visualization fields.

The final cleaned dataset contains 23,232 natural earthquake records.

---

# 4. Data Refresh Strategy

## 4.1 Intended Production Refresh Frequency

**Daily**

The current dashboard uses a fixed Kaggle dataset from 1965–2016 and does not automatically receive new earthquake records.

For a real production version connected to a continuously updated seismic data source, I would recommend refreshing the underlying dataset daily.

Daily updates would support routine historical pattern analysis without requiring the additional infrastructure of continuous real-time processing.

For urgent earthquake notifications, a separate alerting system would be more appropriate.

## 4.2 Dashboard Review Frequency

**Weekly for routine analysis**

Analysts would review the dashboard weekly to examine recorded activity and identify areas that may require further investigation.

In a future production system, analysts could also review updated information after a significant earthquake.

The review frequency does not need to match the refresh frequency. Data can refresh daily while analysts conduct their routine reviews weekly.

## 4.3 Metric to Track and Action Trigger

**Metric:** Number of major earthquakes (M ≥ 7), together with their geographic locations.

**Action Trigger:** In a future production system, a newly recorded earthquake with magnitude 7.0 or higher near a populated region should trigger a review of the event and relevant exposure information.

The analyst would investigate the affected area and determine whether an updated risk assessment is necessary.

This threshold is an operational screening rule, not a prediction of damage. Smaller earthquakes can also cause serious damage depending on their location, depth, and local conditions.

The current historical dashboard does not provide automatic alerts.

## 4.4 Cost of Stale Data

In a production environment, outdated earthquake information could delay the identification of important new events and lead analysts to base their assessments on incomplete records.

A one-day delay could reduce the usefulness of the dashboard for reviewing a recent significant event.

A week-long delay could also affect routine comparisons and scheduled risk reviews.

However, for long-term historical analysis, minute-by-minute updates would provide limited additional value.

This is why daily data refreshes, weekly routine reviews, and separate urgent alerts would be a reasonable operational design.

## 4.5 Data Period and Refresh Disclosure

The dashboard displays the following information:

**Historical Data:** 1965–2016

**Source:** Kaggle Significant Earthquakes Dataset (USGS)

**Intended Production Refresh Frequency:** Daily

A note also explains that the current application uses historical data and does not represent real-time monitoring.

This distinction helps prevent users from assuming that the displayed information is current.

---

# 5. Application Development and Deployment

## Technology Stack

* Python — Application programming language
* Pandas — Data cleaning and transformation
* Matplotlib — Exploratory data analysis
* Plotly — Interactive charts and geographic visualization
* Streamlit — Dashboard interface
* GitHub — Version control and project hosting
* Streamlit Community Cloud — Application deployment

## Application Features

The application includes:

* Three headline metrics.
* Interactive date and magnitude filters.
* A global earthquake map.
* An annual earthquake activity chart.
* A magnitude category comparison.
* A detailed earthquake event explorer.
* Historical data and refresh frequency disclosures.

## Project Structure

```text
earth-pulse-dashboard/
├── app.py
├── database.csv
├── EDA.ipynb
├── README.md
└── requirements.txt
```

## Deployment

The application is deployed using Streamlit Community Cloud and hosted in a GitHub repository.

**Live Streamlit App:** [https://earth-pulse-dashboard-8wpbadhnttsplpu4haj4n9.streamlit.app]

**GitHub Repository:** [https://github.com/Zzybh/earth-pulse-dashboard]

The repository and deployed application are maintained under my own accounts for individual assignment submission.

---

# 6. Team Information

**Team 13 — Earth Pulse**

* Zhao Ziyu
* Chen Yuxiu
* Zhu Hanglin
* Wang Qirun

The dataset and project concept were developed as part of the group exercise. The final application deployment and the design justifications in this README are prepared for my individual Assignment 4 submission.

---

# 7. Conclusion

Earth Pulse demonstrates how historical earthquake records can be transformed into an interactive analytical dashboard.

The main design goal is to help earthquake risk analysts identify historical patterns, compare earthquake characteristics, and select areas for further investigation.

By prioritizing three headline indicators, a small number of supporting visualizations, and decision-relevant filters, the dashboard provides a focused interface rather than an unnecessarily complex collection of charts.

The project also distinguishes between historical analysis and operational earthquake monitoring, recognizing that accurate risk assessment requires more information than historical event counts alone.
