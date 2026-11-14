# Seoul Bike Sharing Demand — Team 5
A CAP 3764 Fall 2026 project analyzing and forecasting hourly bike rental demand in Seoul.

**Team:** Hayla Medina, Alexia Lucas, Nikos Karakasis

## Project Overview
The project uses the Seoul Bike Sharing Demand dataset, which contains 8,760 hourly records and 14 weather, calendar, and rental-demand variables from December 2017 through November 2018. We explore the drivers of demand and then build time-series models that forecast the number of bikes rented each hour.

## Repository Structure
```
├── data/
│   └── SeoulBikeData.csv              # raw dataset
├── my_modules/
│   ├── data_collection_module.py      # data loading/renaming + IQR outlier limits
│   └── feature_engineering.py         # time-series feature builder (lags, rolling means, calendar)
├── notebooks/
│   ├── 01_eda.ipynb                   # cleaning and exploratory data analysis
│   ├── 02_modeling.ipynb              # initial modeling notebook
│   └── 02_time_series_modeling.ipynb  # time-series forecasting + SHAP interpretation
├── environment.yml                    # Conda environment
└── README.md
```

## Setup
```bash
conda env create -f environment.yml
conda activate cap3764-team5
jupyter lab
```
The environment includes the modeling libraries used in the notebooks: `scikit-learn` 1.9.1, `xgboost` 3.4.1, and `shap` 0.54.1. If you created the environment before these were added, run `conda env update -f environment.yml --prune`.

## Data Preparation
`load_seoul_bike_data`:
- Reads the Korean-encoded CSV using `cp949`
- Converts dates to datetime
- Renames columns to snake_case

Initial checks found 0 missing values and 0 duplicate rows, so all 8,760 rows were kept.

For modeling:
- `date` and `hour` are combined into a single hourly `datetime` index.
- Wind speed outliers are **clipped** to Tukey's fences (Q1 − 1.5·IQR, Q3 + 1.5·IQR) using `quartile_limits`, rather than dropped, so the hourly series has no gaps.

## Key EDA Findings
- Bike rentals are right-skewed.
- Summer has the highest average demand; Winter has the lowest.
- Demand is highest around 6 PM (1,503 rentals/hour).
- Non-functioning days have 0 rentals.
- Temperature has the strongest weather correlation with rentals (r = 0.54).
- Dew point is highly correlated with temperature (r = 0.91).

## Time-Series Modeling
**Features** (`make_features`):
- Calendar: `hour`, `dayofweek`, `month`
- Lags: demand 1 h, 2 h, 24 h, and 168 h earlier
- Rolling means: past 24 h and 168 h (computed from past values only to avoid leakage)
- Weather/status covariates: temperature, humidity, wind, visibility, dew point, solar radiation, rainfall, snowfall, season, holiday, functioning day (categoricals one-hot encoded)

**Validation:** chronological split. The last 7 days (Nov 24–30, 2018; 168 hours) are the test set and the remaining 8,424 hours are for training. XGBoost hyperparameters were tuned with `TimeSeriesSplit` (3 folds) + `GridSearchCV`. Best: `learning_rate=0.03`, `max_depth=6`, `n_estimators=400`.

**Results on the test week:**

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Linear Regression | 130.9 | 198.5 | 0.707 |
| Random Forest | 53.5 | 76.0 | 0.957 |
| **XGBoost (tuned)** | **49.2** | **67.6** | **0.966** |

**SHAP interpretation (XGBoost):**
- `lag_1` (previous hour's demand) is by far the most important feature, followed by `lag_2`, `solar_radiation`, `hour`, `lag_168`, and `lag_24`.
- `hour` captures the commuting rush (7–8 AM and 5–6 PM boost the forecast; 9–10 AM pulls it down after the morning peak).
- Warm temperatures raise demand and cold temperatures lower it, with the effect leveling off in extreme heat. Rainfall and high humidity reduce demand.

## Limitations
- The test set is a single week in late autumn. Other seasons may behave differently.
- Lag features use the previous hour's demand, so the models forecast one hour ahead.

## Next Steps
1. Evaluate with rolling-origin backtesting across all seasons.
2. Explore multi-step (e.g., 24-hour-ahead) forecasting.
3. Build an interactive Streamlit demand predictor using the tuned XGBoost model.

## Data Source
[Seoul Bike Sharing Demand — UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand)
