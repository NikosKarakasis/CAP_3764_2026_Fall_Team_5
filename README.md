# Seoul Bike Sharing Demand — Team 5

### A CAP 3764 Fall 2026 project analyzing and predicting hourly bike rental demand in Seoul.
Team: Hayla Medina, Alexia Lucas, Nikos Karakasis

---

### Project Overview
The project uses the Seoul Bike Sharing Demand dataset, containing 8,760 hourly records and 14 weather, calendar, and rental-demand variables from December 2017 through November 2018.

---
### Repository Structure
- data/ — raw dataset (SeoulBikeData.csv)
- notebooks/01_eda.ipynb — cleaning and exploratory data analysis
- notebooks/02_modeling.ipynb — planned modeling
- my_modules/data_loader.py — loads and cleans the dataset (load_seoul_bike_data)
- my_modules/lower_upper_limits.py — calculates outlier limits with Tukey's fences (quartile_limits)
- bike_dataset_packages_cap3764-seoul-bike.yml — Conda environment with pinned package versions
---
### How to Run
You need Anaconda or Miniconda installed. Then, in the Anaconda Prompt (Windows) or a terminal (Mac/Linux):

1. Download the project and go into its folder:
   git clone https://github.com/NikosKarakasis/CAP_3764_2026_Fall_Team_5.git
   cd CAP_3764_2026_Fall_Team_5
2. Create the environment (only needed the first time):
   conda env create -f bike_dataset_packages_cap3764-seoul-bike.yml
3. Activate the environment:
   conda activate "bike_dataset_packages_(cap3764-seoul-bike)"
4. Open Jupyter Lab:
   jupyter lab
5. In Jupyter Lab, open notebooks/01_eda.ipynb and click Run → Run All Cells.
---
### Data Preparation
The data-loading function (load_seoul_bike_data):
- Reads the Korean-encoded CSV using cp949
- Converts dates to datetime
- Renames columns to snake_case
Initial checks found 0 missing values and 0 duplicate rows, so all 8,760 rows were retained.
---
### Outlier Handling
The quartile_limits function finds the lower and upper limits of a column (Q1 − 1.5×IQR and Q3 + 1.5×IQR).
- Wind speed outliers were removed, leaving 8,599 rows (161 removed).
- Other columns kept their outliers because they are natural or meaningful: rental spikes come from rush hours and seasons, visibility is capped at 2,000 (10m), and rain, snow, and solar radiation are naturally rare or daytime-only.
---
### Key EDA Findings
- Bike rentals are right-skewed.
- Summer has the highest average demand; Winter has the lowest.
- Demand is highest around 6 PM (1,503 rentals/hour).
- Non-functioning days have 0 rentals.
- Temperature has the strongest weather correlation with rentals (r = 0.54).
- Dew point is highly correlated with temperature (r = 0.91).
---
### Next Steps
1. Remove non-functioning hours for modeling.
2. Prepare and encode features.
3. Train a models.
4. Evaluate using R², RMSE, and MAE.
5. Build an interactive Streamlit demand predictor.
---
### Data Source
Seoul Bike Sharing Demand — UCI Machine Learning Repository

---