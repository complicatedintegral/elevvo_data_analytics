# Elevvo Data Analytics | Internship Projects

Welcome to my **Elevvo Data Analytics** internship repository! This collection showcases hands‑on projects from the Elevvo Two Week Data Analytics Internship track, highlighting real‑world business use cases and data storytelling.

## 🧪 Project Overview

### Sales Performance Dashboard using Excel

1. Downloaded the dataset “Superstore Sales Dataset” from Kaggle, unzipped the folder and extracted the excel file from it
2. Organized the dataset into a table so that it will help with dynamic pivot tables and filtering
3. Made a PivotTable, which opened a new sheet with a pivot table on the left and the PivotTable Fields tab on the right
4. Used PivotTable to find the total revenue sorted by category, monthly sales trends and units sold by category, respective tables can be found in the images folder
5. Used pie chart for visualizing total revenue, bar graph for visualizing monthly sales trends and bar graph for visualizing units sold per category

### Exploratory Data Analysis on Titanic Dataset

1. Downloaded the dataset “Titanic - Machine Learning from Disaster” from Kaggle, and loaded the data using pandas module in python
2. Handling missing values:
- Age column filled with median age.
- Cabin column dropped because too many values are missing
- Embarked column filled with the most common port value
1. Converted columns to categories wherever appropriate
2. Visualized group based insights using bar plots and heat maps

### SQL Sales Analysis - Chinook Database

1. Download `Chinook_MySql.sql` from [Chinook GitHub Repo](https://github.com/lerocha/chinook-database)
2. Imported the dataset into MySQL command line client to perform analysis using join queries and window functions
3. Key queries used were for top selling tracks, revenue by country, monthly sales trends and top three tracks by country (using window function ROW_NUMBER)
