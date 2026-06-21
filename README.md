# 🎓 Student Performance Predictor

<p align="center">
	<a href="#"><img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white" alt="Python"></a>
	<a href="#"><img src="https://img.shields.io/badge/Flask-Web%20App-000000?logo=flask&logoColor=white" alt="Flask"></a>
	<a href="#"><img src="https://img.shields.io/badge/scikit--learn-ML%20Pipeline-F7931E?logo=scikitlearn&logoColor=white" alt="scikit-learn"></a>
	<a href="#"><img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white" alt="Pandas"></a>
	<a href="#"><img src="https://img.shields.io/badge/Status-Production%20Polished-0A7B83" alt="Status"></a>
</p>

<p align="center">
	✨ End-to-end ML portfolio project to predict a student's <b>math score</b> from profile and academic indicators.
</p>

---

## 🚀 Project Overview

This repository demonstrates a complete machine learning workflow, from raw data ingestion to real-time web inference.

### ✅ What this project includes

- ⚙️ Modular ML pipeline (ingestion → transformation → training)
- 🧠 Multi-model regression benchmarking with best-model selection
- 💾 Serialized artifacts for reproducible inference
- 🌐 Flask app for interactive score prediction
- 🧹 Clean, production-grade project structure and docs

---

## 🎯 Problem Statement

Given student attributes such as:

- gender
- race/ethnicity
- parental level of education
- lunch type
- test preparation course
- reading score
- writing score

predict the target variable:

👉 `math_score`

---

## 🧱 Project Architecture

```text
StudentPerformance_Predictor/
├── app.py
├── application.py
├── requirements.txt
├── setup.py
├── README.md
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   ├── test.csv
│   └── data.csv
├── notebook/
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── data/
│       └── stud.csv
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
└── templates/
		├── index.html
		└── home.html
```

---

## 🔬 ML Pipeline (End-to-End)

### 1) 📥 Data Ingestion

- Reads dataset from `notebook/data/stud.csv`
- Splits into train/test sets
- Stores snapshots in `artifacts/`

### 2) 🧼 Data Transformation

- Numerical pipeline: median imputation + standard scaling
- Categorical pipeline: most-frequent imputation + one-hot encoding + scaling
- Saves preprocessor as `artifacts/preprocessor.pkl`

### 3) 🤖 Model Training

- Trains and evaluates multiple regression models
- Compares performance using $R^2$
- Persists best model as `artifacts/model.pkl`

### 4) 🌍 Inference Serving

- User submits form inputs via Flask UI
- App loads preprocessor + model artifacts
- Returns predicted math score instantly

---

## 🧰 Tech Stack

- 🐍 Python 3.9+
- 🌐 Flask
- 🧮 NumPy, Pandas
- 📊 scikit-learn
- 📈 Matplotlib, Seaborn
- 💾 Dill (artifact serialization)

---

## ⚡ Quick Start

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd StudentPerformance_Predictor
```

### 2. Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. (Optional) Install package in editable mode

```bash
pip install -e .
```

---

## 🏋️ Run Training Pipeline

```bash
python -m src.pipeline.train_pipeline
```

Expected outputs:

- `artifacts/train.csv`
- `artifacts/test.csv`
- `artifacts/preprocessor.pkl`
- `artifacts/model.pkl`

---

## 🌐 Run the Web App

```bash
python app.py
```

Open in browser:

- `http://127.0.0.1:5000/`

---

## 📓 Notebooks

- `notebook/1 . EDA STUDENT PERFORMANCE .ipynb` → exploratory data analysis
- `notebook/2. MODEL TRAINING.ipynb` → model experimentation workflow

---

## 💼 Portfolio Highlights

- ✅ Strong modular separation of ML components
- ✅ Portable and reproducible local pipeline
- ✅ Clean exception handling and logging layers
- ✅ Polished web interface for non-technical users
- ✅ Professional repository organization

---

## 🔭 Future Scope

- Add automated unit/integration tests
- Add experiment tracking (MLflow or similar)
- Add model versioning and API schema validation
- Add Dockerization + CI checks

---

## 📜 License

This project is available for educational, learning, and portfolio purposes.
