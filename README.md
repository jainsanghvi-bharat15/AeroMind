# AeroMind: Airport Operations Intelligence Platform
## Overview
AeroMind is a platform that helps airports. It looks at flight data finds problems and gives insights to airport managers. The project includes understanding business needs preparing data creating a data warehouse analyzing data and building dashboards.

AeroMind is not a simple flight delay dashboard. It is a solution that shows how airport data can be turned into useful information for airport operators and airline managers.

---
# Project Objectives
* Look at airport performance using 2024 flight data.
* Find reasons for delays, cancellations and diversions.
* Create a data warehouse.
* Analyze data using SQL.
* Build features for aviation.
* Create machine learning models.
* Make dashboards for airport decision-makers.
* Show how AI can help build analytics
---

# Project Workflow
```
Business Understanding
     ↓
Data Understanding
     ↓
Data Cleaning
     ↓
Data Warehouse
     ↓
SQL Analytics
     ↓
Feature Engineering
     ↓
Exploratory Data Analysis
     ↓
Machine Learning
     ↓
Executive Dashboard
```

---
# Repository Structure
## 01_Project_Planning
* Project plan
* Business problem
* Success metrics
* Architecture diagram

## 02_Data_Understanding
* Data dictionary
* Data exploration
* Initial business insights
* Exploratory data analysis report

## 03_Data_Preparation
* Data cleaning using python
* Cleanded Dataset but unable to upload here because of large size.

## 04_Data_Warehouse
* Data warehouse design
* ER diagram
* Dimension tables
* Fact table
* SQL scripts

Dimension Tables:
* Dim_Airline
* Dim_Airport
* Dim_Date
* Dim_Time
* Dim_Delay_Type

Fact Table:
* Fact_Flight_Operations but unable to upload here because of large size.

## 05_SQL_Analytics
* KPIs
* Airport performance
* Airline performance
* Congestion analysis

## 06_Feature_Engineering
* Airport flight volume
* Route analysis
* Hour
* Delayed flight indicator
* Total delay causes
* Extreme delay flag

## 07_Machine_Learning
* Data preprocessing
* Feature selection
* Model training
* Model evaluation
* Prediction visualization

## 08_Dashboard
* Executive Dashboard
* AeroMind Command Center

The dashboard shows:
* Executive KPIs
* Airport performance
* Airline performance
* Congestion monitoring
* Delay analysis
* Root cause insights
The HTML interface was refined using Claude AI.

---
# Technologies Used
* Python
* Pandas
* NumPy
* Matplotlib
* MySQL
* HTML, CSS, JavaScript using OpenAI
* Scikit-learn
* Claude AI
---
# Project Highlights
* Data warehouse
* SQL analytics
* Feature engineering
* Exploratory data analysis
* Machine learning
* Dashboard: AI-assisted dashboard
---
# Author
**Bharat Jain Sanghvi**
B.Tech Student | Data Analytics | Business Intelligence | Machine Learning

## License
This project is, for educational purposes.

# How to Run the Project
## 1. Clone the Repository
```bash
git clone [https://github.com/jainsanghvi-bharat15/AeroMind.git](https://github.com/jainsanghvi-bharat15/AeroMind)
cd AeroMind-Airport-Operations-Intelligence-Platform
```
## 2. Install Required Libraries
install:
```bash
pip install pandas numpy matplotlib scikit-learn mysql-connector-python openpyxl
```
---
## 3. Download the Dataset
Download the **Flight Delay Dataset 2024** from Kaggle and place it in the project folder.
Update the dataset path in the Python scripts if required.
---
## 4. Run the Python Pipeline
Execute the scripts in the following sequence:
### Step 1 – Data Cleaning
```text
Data_Cleaning.py
```
Output:
* Cleaned Flight Dataset
---
### Step 2 – Create Data Warehouse
```text
Fact_Flight_Operation.py
```
Output:
* Fact_Flight_Operations.csv
* Dim_Airline.csv
* Dim_Airport.csv
* Dim_Date.csv
* Dim_Time.csv
* Dim_Delay_Type.csv
---
### Step 3 – Import into MySQL
* Create the `aeromind` database.
* Execute the table creation SQL script.
* Import all Dimension Tables.
* Import the Fact Table.
---
### Step 4 – Execute SQL Analytics
Run the SQL scripts in the following order:
1. KPI.sql
2. Airport_Analysis.sql
3. Airline_Analysis.sql
4. Congestion.sql
5. Root_Cause.sql
---
### Step 5 – Feature Engineering
```text
Feature_Engineer.py
```
Output:
* Engineered_Features.csv
---
### Step 6 – Exploratory Data Analysis
Run:
```text
EDA.py
```
and
```text
Analytics_Statistics.py
```
Outputs:
* EDA Report
* Root Cause Report
* Statistical Analysis
---
### Step 7 – Machine Learning
Run:
```text
ML_Model.py then app.py
```
Outputs:
* Trained Machine Learning Model
* Model Evaluation Metrics
* Prediction Results
* index.html (Model Output)
---
### Step 8 – Dashboard
Open either of the following files in your browser:
```text
AeroMind_Command_Center.html
```
or
```text
AeroMind_Command_Center_v2.html
```
