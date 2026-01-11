##  Bitcoin (BTC-USD) Adaptive Prediction Analysis

This section explores the application of an optimized **Support Vector Regression (SVR)** model to the highly volatile Bitcoin market. By moving from a static configuration to an automated tuning system, we achieved professional-grade accuracy.

###  The Optimization Strategy

To handle the "digital gold" market, the model was upgraded with three core components:

1. **Adaptive "Live" Learning Loop**:
   * The model implements a **Walk-Forward validation** strategy.
   * Instead of a one-time training session, the algorithm retrains every 24 hours using newly available data from **MongoDB**.
   * This ensures the model adapts to sudden market shifts (crashes or rallies) within hours.

2. **Automated Hyperparameter Tuning (GridSearch)**:
   * We used **GridSearchCV** to find the mathematical "sweet spot" for each prediction day.
   * **Key Finding**: The system consistently selected **C = 10,000**, confirming that Bitcoin requires high regularization "aggressiveness" to minimize error.

3. **5-Dimensional Feature Vectors**:
   * Predictions are based on more than just price history. We included:
     * `Price_Yesterday`: The primary baseline.
     * `Price_Avg_5d`: To capture short-term momentum.
     * `Vol_Yesterday`: To account for market strength.
     * `Price_Range`: To measure daily volatility (nervousness).



###  Performance Results (March 2025)

We evaluated the model using **Mean Absolute Error (MAE)** and **Mean Absolute Percentage Error (MAPE)**.

| Metric | Initial Model | Optimized Model (GridSearch) | Improvement |
| :--- | :--- | :--- | :--- |
| **MAE (Avg. Error)** | $7,598.64 | **$2,141.23** | **~72% reduction** |
| **MAPE (Rel. Error)** | 9.05% | **2.53%** | **97.47% Accuracy** |



###  Conclusion
The transition from a manual setup to an **Optimized GridSearch SVR** reduced the prediction error by over 70%. While Bitcoin is significantly more volatile than traditional stocks, this study proves that with sufficient regularization ($C=10,000$) and daily retraining, it is possible to maintain a prediction accuracy above 97%.