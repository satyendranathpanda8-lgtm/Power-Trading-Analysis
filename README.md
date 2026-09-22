# ⚡ Power Trading Analysis

## 📌 Project Overview

**Power Trading Analysis** is a data analytics project focused on analyzing electricity trading patterns, market prices, trading volumes, and the relationship between electricity market activity and weather conditions.

The project uses **Python, SQL, and Power BI** to clean, analyze, and visualize electricity trading data and generate meaningful business insights.

---

## 🎯 Objectives

* Analyze electricity trading patterns over time.
* Study **Market Clearing Price (MCP)** trends.
* Analyze **Purchase Bid, Sell Bid, and Market Clearing Volume (MCV)**.
* Examine the relationship between weather conditions and electricity market prices.
* Identify monthly and seasonal variations in MCP.
* Compare electricity market activity across different locations/stations.
* Build an interactive Power BI dashboard for data-driven analysis.

---

## 🛠️ Tools & Technologies

| Tool         | Purpose                                |
| ------------ | -------------------------------------- |
| 🐍 Python    | Data cleaning, preprocessing & EDA     |
| 🗄️ MySQL    | Data querying & analysis               |
| 📊 Power BI  | Dashboard & visualization              |
| 📑 Excel/CSV | Data storage and initial data handling |

### Python Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## 🔄 Project Workflow

```text
Raw Data
   ↓
Data Cleaning & Preprocessing
   ↓
Exploratory Data Analysis
   ↓
SQL Analysis
   ↓
Power BI Data Modeling
   ↓
Dashboard Development
   ↓
Insights & Interpretation
```

---

## 📂 Project Structure

```text
Power-Trading-Analysis/
│
├── Python/
│   └── Power_Trading_Analysis.py
│
├── SQL/
│   └── Power_Trading_Analysis.sql
│
├── PowerBI/
│   └── Power_Trading_Analysis.pbix
│
├── Architecture/
│   └── Project_Architecture.png
│
├── Screenshots/
│   └── Dashboard.png
│
└── README.md
```

> The raw dataset is not included in this repository.

---

## 🧹 Data Cleaning

The dataset was prepared using Python before analysis.

Major preprocessing steps included:

* Removed duplicate records.
* Converted date values into the required date format.
* Handled missing numerical values using median imputation.
* Handled missing categorical values using mode.
* Converted relevant columns into appropriate data types.
* Prepared the cleaned dataset for SQL analysis and Power BI visualization.

---

## 📊 Key Variables

Some of the important variables used in the analysis include:

* **Hour**
* **Purchase Bid (MW)**
* **Sell Bid (MW)**
* **MCV (MW)**
* **Final Scheduled Volume (MW)**
* **MCP (₹/MWh)**
* **Temperature**
* **Relative Humidity**
* **Station/Location**
* **Date**

---

## 📈 Power BI Dashboard

The Power BI dashboard focuses on electricity market trends and relationships between trading activity, market prices, and weather conditions.

### Key Analysis

* MCP trend analysis
* 7-day rolling average of MCP
* 30-day rolling average of MCP
* Monthly average MCP
* Purchase vs Sell Bid analysis
* Market Clearing Volume analysis
* Station-wise analysis
* Weather variable analysis
* Correlation analysis between weather variables and MCP

### Dashboard Preview

![Power Trading Dashboard](Screenshots/Dashboard.png)

---

## 📐 Statistical Analysis

Correlation analysis was performed to examine the relationship between selected weather variables and MCP.

For example, some stations showed a negative correlation between wind-related variables and MCP.

**Important:** Correlation indicates an association between variables and does not establish causation.

---

## 💡 Key Insights

The analysis helps identify:

* Changes in electricity market prices over time.
* Variations in trading volume and scheduled electricity.
* Monthly and seasonal MCP patterns.
* Differences in electricity market activity across locations.
* Relationships between weather conditions and electricity market prices.

---

## 🧠 Skills Demonstrated

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Python for Data Analytics
* SQL Data Analysis
* Data Visualization
* Power BI Dashboard Development
* DAX & Time-Series Analysis
* Correlation Analysis
* Business Insight Generation

---

## 🚀 Future Improvements

* Add more weather parameters.
* Perform advanced time-series forecasting.
* Build predictive models for MCP.
* Analyze additional power stations and renewable energy sources.
* Automate data refresh and dashboard updates.

---

## 👤 Author

**Satyendra Nath Panda**

Aspiring Data Analyst | Python | SQL | Power BI

---

⭐ If you find this project useful, feel free to explore the repository and provide feedback.
