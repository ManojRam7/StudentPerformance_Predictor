## Project Overview

**StudentPerformance_Predictor** is an end-to-end machine learning project that predicts student exam performance based on demographic and educational input features. The project uses Python, Jupyter notebooks, and several machine learning libraries to preprocess data, train models, and provide predictions via a web interface.

## Main Components

### 1. Dataset
- The dataset (`stud.csv`) contains features such as gender, race/ethnicity, parental level of education, lunch type, test preparation course, and scores in math, reading, and writing.
- Example columns: `gender`, `race_ethnicity`, `parental_level_of_education`, `lunch`, `test_preparation_course`, `math_score`, `reading_score`, `writing_score`.

### 2. Data Pipeline
- **Data Ingestion:** Code reads the CSV data, splits it into train/test sets, and stores them for further processing (see `src/components/data_ingestion.py`).
- **Data Transformation:** Preprocessing and transformation steps are implied but not fully detailed in the snippet.

### 3. Model Training and Evaluation
- Multiple regression models are considered, including KNeighbors, Decision Tree, Random Forest, AdaBoost, SVR, Linear Regression, Ridge, Lasso, CatBoost, and XGBoost.
- Model evaluation uses metrics like R^2 score and mean squared error.
- Hyperparameter tuning via `RandomizedSearchCV` is included for some models.
- Model performance is tracked and results are stored for comparison.

### 4. Utilities and Logging
- Utility functions for saving/loading models, evaluating models, and logging are implemented (`src/utils.py`, `src/logger.py`).
- Custom exception handling improves error traceability (`src/exception.py`).

### 5. Web Interface
- A Flask-based web app allows users to input student features via a form (`templates/home.html`) and receive performance predictions.
- Inputs include gender, ethnicity, parental education, lunch type, test preparation status, and scores.
- Home and index templates provide a user-friendly interface.

### 6. Deployment
- The project includes configuration for AWS Elastic Beanstalk deployment (`.ebextensions/python.config`), indicating a plan for cloud hosting.

### 7. Notebooks & Results
- Jupyter notebooks are used for exploration, training, and model evaluation (e.g., `notebook/2. MODEL TRAINING.ipynb`).
- Model training notebooks show importing, visualizations, and step-by-step predictive modeling.
- CatBoost training logs and error progression are tracked (`catboost_info/learn_error.tsv`).

---

## How it Works

1. **Data is ingested** from CSV, split into training and testing sets.
2. **Preprocessing and feature engineering** (some details inferred, not all steps shown).
3. **Multiple machine learning models** are trained and evaluated to select the best performer.
4. **A Flask web app** provides predictions based on user input.
5. **Logging, error handling, and deployment scripts** ensure robustness and cloud readiness.

---

## Technologies Used

- Python (Pandas, NumPy, scikit-learn, CatBoost, XGBoost, Flask)
- Jupyter Notebook
- HTML (for templates)
- AWS Elastic Beanstalk (deployment)
- Logging and exception management for maintainability
