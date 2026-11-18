# AI Context — Monthly Car Sales Forecasting with Backtesting

## Project identity
- **Project:** Monthly Car Sales Forecasting
- **Learning track:** PA Day 10 — Track J (Real-world problems)
- **Subtopic:** Sales forecasting
- **Repository:** https://github.com/atanuduttagupta/ai-daily-practice/tree/main/AI/car-sales-forecasting
- **Interactive app:** https://ai-daily-practice-car-sales-forecasting.streamlit.app/

## Project objective
Forecast the next 12 months of monthly car sales and assess whether the forecasting models are reliable by evaluating them on historical periods through backtesting (time-series cross-validation).

The project emphasizes an important principle: a forecasting model should be compared with a simple baseline, and it must only use information that would have been available at the forecast origin.

## Dataset
- Monthly car sales in Quebec.
- Period: January 1960 to December 1968.
- Number of observations: 108 monthly data points.
- Source: public CSV hosted in the `jbrownlee/Datasets` GitHub repository.
- The CSV is downloaded automatically on first execution and cached locally as `monthly-car-sales.csv`.
- Internet access is required for the first download.

## Technology
- Python
- StatsForecast (Nixtla)
- pandas
- NumPy
- Matplotlib
- Streamlit for the interactive app

## Forecasting models
1. **Seasonal Naive:** baseline forecast that repeats the value from the same season in the previous cycle. With a 12-month season, next June is predicted using the latest June.
2. **AutoARIMA:** automatically searches for suitable ARIMA settings and models relationships involving past observations and past forecast errors.
3. **AutoETS:** exponential smoothing model that can represent level, trend, and seasonality.
4. **AutoTheta:** Theta forecasting method, included as a comparatively simple forecasting approach.

The seasonal period is 12 months in the default project configuration.

## Backtesting approach
Backtesting simulates historical forecasting situations:
1. Select a historical forecast origin.
2. Train using only observations available before that origin.
3. Forecast the next 12 months.
4. Compare those forecasts with the actual observations.
5. Repeat at other historical origins.

The reference implementation uses:
- Forecast horizon: `h = 12`
- Number of windows: `n_windows = 3`
- Step size: `step_size = 12`

Time-series observations must not be randomly shuffled. Training on observations from after the forecast origin would create data leakage.

## Evaluation metrics
- **MAE (Mean Absolute Error):** average absolute forecast error, measured in sales units.
- **RMSE (Root Mean Squared Error):** square root of the average squared error; larger misses receive greater penalty.
- **MAPE (Mean Absolute Percentage Error):** average absolute percentage error. It can be unstable when actual values are zero or close to zero.

Lower values are preferred for these error metrics, while metric choice should reflect the practical cost of forecast errors.

## Reference results in the project README
One documented run reports:

| Model | MAE | RMSE | MAPE |
|---|---:|---:|---:|
| SeasonalNaive (baseline) | 1,462 | 1,811 | 8.4% |
| AutoARIMA | 1,639 | 1,986 | 10.2% |
| AutoETS | 1,890 | 2,444 | 11.6% |
| AutoTheta | 2,456 | 2,992 | 14.5% |

In that run, the Seasonal Naive baseline achieved the lowest error across the reported metrics. This illustrates why a baseline is important: a more complex model is not automatically more accurate.

These numbers describe one series and three backtest windows. They are not universal model rankings, and results may vary with the data, selected windows, and library versions.

## Main implementation workflow
1. Load the CSV and create the StatsForecast data format:
   - `unique_id`: series identifier
   - `ds`: monthly date
   - `y`: sales value
2. Configure the four forecasting models with a seasonal length of 12.
3. Run `StatsForecast.cross_validation()` using a 12-month horizon, three windows, and a 12-month step.
4. Calculate MAE, RMSE, and MAPE for each model.
5. Fit the models on all available observations and forecast the next 12 months.
6. Plot historical sales and each model's forecast in `forecast.png`.

## Interactive Streamlit app
The app provides:
- Historical sales chart and data table.
- Controls for forecast horizon, seasonal period, backtest step size, and number of windows.
- Model selection for Seasonal Naive, AutoARIMA, AutoETS, and AutoTheta.
- Backtest scorecard with MAE, RMSE, and MAPE.
- Model error comparison chart.
- Inspection of individual backtest predictions.
- Final forecast table and chart.
- CSV download of the forecast.
- Learning tabs explaining backtesting, models, metrics, and further experiments.

## Suggested experiments
1. Increase `n_windows` from 3 to 5 and see whether model rankings change.
2. Add 80% and 95% prediction intervals.
3. Add models such as AutoCES, Holt-Winters, and Naive.
4. Replace the sample dataset with another monthly sales series using `Month` and `Sales` columns.
5. Compare with LightGBM using lag features through the `mlforecast` ecosystem.

## Limitations and interpretation
- The dataset contains only 108 observations and one historical time series.
- The baseline winning in one backtest does not mean it will always win.
- Only three backtest windows are used in the reference run.
- The dataset is historical (1960–1968); the exercise demonstrates forecasting methodology rather than providing a current commercial car-market forecast.
- Prediction intervals and additional external signals (such as promotions, holidays, or prices) are not included in the reference implementation.

## Run locally
Install dependencies from `requirements.txt`, then run:

```bash
python main.py
```

For the interactive app, Streamlit must also be installed and included in `requirements.txt` for cloud deployment:

```bash
python -m streamlit run app.py
```

The deployed interactive app is available at:
https://ai-daily-practice-car-sales-forecasting.streamlit.app/
