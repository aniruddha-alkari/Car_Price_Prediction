# 🚗 Car Price Prediction using Machine Learning

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical-blue?style=for-the-badge&logo=numpy)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit)

</p>

<p align="center">
A complete End-to-End Machine Learning Regression project that predicts the selling price of a used car based on vehicle specifications.
</p>

---

# 📌 Project Overview

Buying or selling a used car at the right market price is challenging because several factors influence a vehicle's value. This project uses **Machine Learning Regression** to estimate the selling price of used cars based on important vehicle attributes.

The application allows users to enter vehicle details through an interactive **Streamlit web application**, and the trained regression model instantly predicts the estimated market price.

The dataset contains information about used cars listed on **CarDekho.com (India)**, including various features such as fuel type, transmission, ownership, engine capacity, mileage, and more. The project compares multiple regression algorithms and selects the best-performing model based on evaluation metrics.

---

# 🎯 Problem Statement

Accurately estimating the resale price of a used car is difficult because vehicle prices depend on multiple factors such as:

- model
- vehicle_age
- km_driven
- seller_type
- fuel_type
- transmission_type
- mileage
- engine
- max_power
- seats

Traditional price estimation relies heavily on manual judgment, making pricing inconsistent.

This project automates the pricing process using Machine Learning to provide reliable market price predictions.

---

# 🚀 Features

✅ End-to-End Machine Learning Pipeline

✅ Data Cleaning & Preprocessing

✅ Exploratory Data Analysis (EDA)

✅ Feature Engineering

✅ Multiple Regression Algorithms Comparison

✅ Hyperparameter Tuning

✅ Best Model Selection

✅ Model Serialization using Joblib/Pickle

✅ Interactive Streamlit Web Application

✅ Real-time Price Prediction

---

# 🧠 Machine Learning Workflow

```
Dataset
    │
    ▼
Data Cleaning
    │
    ▼
Exploratory Data Analysis
    │
    ▼
Feature Engineering
    │
    ▼
Train-Test Split
    │
    ▼
Train Multiple Regression Models
    │
    ▼
Model Evaluation
    │
    ▼
Best Model Selection
    │
    ▼
Save Trained Model
    │
    ▼
Streamlit Web Application
    │
    ▼
Predict Car Price
```

---

# 📊 Dataset Information

The dataset consists of used cars sold on **CarDekho.com (India)**.

It contains information about different vehicle specifications and their corresponding selling prices.

Typical features include:

- model
- vehicle age
- km driven
- seller type
- fuel type
- transmission type
- mileage
- engine
- max power
- seats

**Target Variable**

```
Selling Price
```

This is a **Regression Problem** where the model predicts continuous numerical values.

---

# 🛠 Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-Learn

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Web Framework

- Streamlit

### Model Serialization

- Pickle

---

# 📂 Project Structure

```
Car_Price_Prediction
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│
├── notebook/
│   ├── EDA.ipynb
│   ├── Model Training.ipynb
│
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── utils.py
│   ├── exception.py
│   └── logger.py
│
├── Screenshot/
│
├── app.py
├── requirements.txt
├── setup.py
├── README.md
└── data.csv
```

*(Project structure may vary slightly depending on your repository.)*

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/aniruddha-alkari/Car_Price_Prediction.git
```

```bash
cd Car_Price_Prediction
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser

```
http://localhost:8501
```

---

# 💻 Application Workflow

1. Open Streamlit application.

2. Enter car details such as:

   - model
   - vehicle_age
   - km_driven
   - seller_type
   - fuel_type
   - transmission_type
   - mileage
   - engine
   - max_power
   - seats

3. Click **Predict Price**

4. The trained Machine Learning model estimates the market value of the car.

---

# 📈 Model Training

Several Regression Algorithms were trained and compared.

Examples include:

- Linear Regression
- Ridge Regression
- Lasso Regression
- K-Neighbors Regressor
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor
- AdaBoost Regressor
- CatBoost Regressor

The best-performing model was selected using evaluation metrics such as:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

# 📷 Application Screenshots

Screenshots are available inside the **Screenshot** folder.

Example:

```
Screenshot/
│
├── Home.png
├── Prediction.png
├── Result.png
```

> Replace the above names with the actual screenshots present in your repository.

---

# 📊 Future Improvements

- Deploy on Streamlit Cloud
- Docker Support
- CI/CD Pipeline
- Model Monitoring
- Explain Predictions using SHAP
- REST API using FastAPI
- Cloud Deployment (AWS / Azure / GCP)

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It motivates me to build more Machine Learning and Generative AI projects.

---

# 👨‍💻 Author

**Aniruddha Alkari**

Machine Learning Engineer | Data Scientist | Generative AI Enthusiast

GitHub:

https://github.com/aniruddha-alkari

---

# 📜 License

This project is intended for educational and learning purposes.

Feel free to use and modify it.

---

## 🌟 If you like this project, don't forget to give it a Star ⭐

```
