#  NVIDIA (NVDA) Stock Price Prediction Analysis

##  Project Overview
This project demonstrates the transition from a basic statistical approach to an **Adaptive Machine Learning system** for predicting NVIDIA's stock prices. By using **Support Vector Regression (SVR)** and a "Live Learning" approach, we successfully reduced the prediction error by nearly 70%.

---

##  Methodology Step-by-Step

### 1. Data Infrastructure
* **Source**: Real-time market data retrieved from a **MongoDB** database.
* **Preprocessing**: We implemented `StandardScaler` to normalize our features. This ensures that high-magnitude data like **Volume** doesn't overwhelm price data during the model's distance-based calculations.

### 2. Feature Engineering (The Multi-Dimensional Vector)
Instead of looking at dates alone, we built a 4-dimensional **Feature Vector** for every day:
* `Price_Yesterday`: The immediate anchor for today's prediction.
* `Price_Avg_5d`: Captures short-term momentum and trends.
* `Vol_Yesterday`: Market strength indicator.
* `Price_Range`: A measure of daily volatility (High minus Low).

### 3. Model Evolution
* **Phase 1: Linear Regression**: Served as a baseline but failed to capture the non-linear "swings" of NVDA stock.
* **Phase 2: SVR with RBF Kernel**: Switched to Support Vector Regression. Using the **RBF Kernel**, the model gained the flexibility to "bend" its prediction line around complex data points.
* **Phase 3: Adaptive "Live" Learning**: The final breakthrough. Instead of a static model, we implemented a loop that **retrains the model every morning** using all available historical data up to that second.

---

##  Results & Performance

We used **Mean Absolute Error (MAE)** to measure the average dollar difference between our prediction and the actual closing price.

| Model Version | MAE (Error in USD) |
| :--- | :--- |
| Initial Static Model | $11.22 |
| **Final Adaptive SVR** | **$3.57** |



---

##  Key Takeaways for Data Science
* **Retraining is Critical**: In volatile markets like Tech stocks, a model trained a month ago is already obsolete. Daily updates are mandatory.
* **Context Matters**: Adding Volume and Price Range to the feature vector allowed the SVR to "understand" market sentiment, not just price history.
* **Mathematical Optimization**: Setting $C=500$ and $\gamma=0.01$ allowed the model to find the optimal balance between fitting past data and predicting the future.