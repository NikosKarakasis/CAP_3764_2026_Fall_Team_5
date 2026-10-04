# Seoul Bike Sharing Demand — Team 5
A CAP 3764 Fall 2026 project analyzing and predicting hourly bike rental demand in Seoul.
Team: Hayla Medina, Alexia Lucas, Nikos Karakasis

Project Overview
The project uses the Seoul Bike Sharing Demand dataset, containing 8,760 hourly records and 14 weather, calendar, and rental-demand variables from December 2017 through November 2018.

Repository Structure
- data - raw dataset
- 01_eda.ipynb — cleaning and exploratory data analysis
- 02_modeling.ipynb — planned modeling
- data_collection_module.py — reusable data loading and cleaning functions
- environment.yml — Conda environment

Setup
conda env create -f environment.yml
conda activate cap3764-team5
jupyter lab

Data Preparation
The data-loading function:
- Reads the Korean-encoded CSV using cp949
- Converts dates to datetime
- Renames columns to snake_case
Initial checks found 0 missing values and 0 duplicate rows, so all 8,760 rows were retained.

Key EDA Findings
- Bike rentals are right-skewed.
- Summer has the highest average demand; Winter has the lowest.
- Demand is highest around 6 PM (1,503 rentals/hour).
- Non-functioning days have 0 rentals.
- Temperature has the strongest weather correlation with rentals (r = 0.54).
- Dew point is highly correlated with temperature (r = 0.91).
  
Next Steps
1. Remove non-functioning hours for modeling.
2. Prepare and encode features.
3. Train a Linear Regression model.
4. Evaluate using R², RMSE, and MAE.
5. Build an interactive Streamlit demand predictor.

Data Source
Seoul Bike Sharing Demand — UCI Machine Learning Repository
