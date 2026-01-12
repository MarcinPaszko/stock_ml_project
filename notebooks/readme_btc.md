## ## Bitcoin (BTC-USD) Adaptive Prediction Framework

This project demonstrates a multi-stage approach to financial time-series forecasting. It evaluates the effectiveness of **Support Vector Regression (SVR)** across different time horizons, from a short-term "Proof of Concept" to a long-term "Production-Grade" model covering multiple market cycles.

---

### ## Stage I: Short-Term Proof of Concept (March 2025)
**Source File:** `2_BTC_Simulation_March2025_Prediction.ipynb`

* **Objective**: Validate the SVR model's baseline performance using a limited 1-year dataset (2025).
* **Methodology**: Implementation of **GridSearchCV** to automate hyperparameter tuning.
* **Key Results**: 
    * Significant reduction in error by optimizing regularization (**C=10,000**).
    * Achieved **97.47% accuracy** (2.53% MAPE) during the March 2025 test window.
* **Conclusion**: Confirmed that the model can handle Bitcoin's volatility when properly tuned, serving as a gateway to larger-scale analysis.



---

### ## Stage II: Full-History Scalability (12-Year Dataset)
**Current File:** `3_BTC_All_history_prices.ipynb`

* **Objective**: Build a robust model capable of navigating extreme market shifts (bull and bear markets) from 2014 to 2026.
* **Dataset**: Over **4,000 historical records** fetched via `yfinance` and stored in **MongoDB**.
* **Advanced Feature Engineering**: 
    * Incorporated long-term trend indicators: **MA5**, **MA20** (20-day Moving Average).
    * Added **Daily Volatility** (High-Low range) to capture market "nervousness".
* **Performance**: 
    * **98.02% Accuracy** (1.98% MAPE).
    * The model maintained high precision despite the massive price delta between 2014 ($300) and 2026 ($90k+).



---

### ## Data Engineering & MLOps Pipeline
The project utilizes a modern **Medallion Architecture** to ensure data integrity and model reproducibility.

1.  **Ingestion (Bronze)**: Raw data from NBP API and Yahoo Finance stored in **MongoDB**.
2.  **Silver Layer**: Processing and cleaning using **PySpark** and **Pandas**.
3.  **Gold Layer (Inference)**: Optimized SVR model generating daily forecasts.
4.  **Monitoring**: A dedicated `predictions` collection in MongoDB tracks model performance and calculates real-world error (drift) automatically.



---

### ## Final Performance Comparison

| Dataset Scope | Time Horizon | MAPE (Error %) | Accuracy |
| :--- | :--- | :--- | :--- |
| **Short-term (2025)** | 30 Days | 2.53% | 97.47% |
| **Full History (2014-2026)** | **4000+ Days** | **1.98%** | **98.02%** |

**Summary**: Transitioning to full history allowed the model to learn from 12 years of market psychology, resulting in a more stable and accurate prediction system.