# Final-Project-Dashboard-

# Dashboard DiCo - E-Commerce Data Analysis

This project is part of the final submission for the **Data Analysis with Python** course at Dicoding. The project includes data analysis and the creation of an interactive dashboard using **Streamlit** to visualize insights from an e-commerce dataset.

## Overview
The goal of this project is to analyze the provided e-commerce dataset and extract valuable insights. The analysis answers key business questions such as:
1. **What is the most purchased product on the platform?**
2. **How does price affect the number of sales?**
3. **What is the distribution of sales across different product categories?**

The interactive dashboard created with **Streamlit** provides visualizations for these insights.

## Dataset
The dataset used in this project is the **E-Commerce Public Dataset** which contains multiple CSV files. The primary datasets used are:
- `order_items.csv`: Information about the products in each order.
- `products.csv`: Product details such as name and category.
- `order_payments.csv`: Payment details of each order.
  
Additional data like customer information, seller details, and geolocation data were also utilized to enhance the analysis.

## Analysis Steps
1. **Data Gathering**: Loading and merging relevant CSV files.
2. **Data Cleaning**: Handling missing values and ensuring data consistency.
3. **Exploratory Data Analysis (EDA)**: Answering business questions through data visualizations.
4. **Dashboard Creation**: Using **Streamlit** to create an interactive dashboard that visualizes the key findings.


## How to Run
### Running Locally
1. Clone the repository to your local machine.
2. Run the dashboard locally using Streamlit:
   ```bash
   streamlit run dashboard/dashboard.py
   ```

## Requirements
The following libraries are required to run the analysis and dashboard:
- `pandas`
- `numpy`
- `matplotlib`
- `streamlit`

## Acknowledgments
Special thanks to **Dicoding** for providing the dataset and guidance throughout this project.

