# Student Performance Predictor

End-to-end machine learning project that predicts a student's **math score** from demographic and academic context.

This repository is structured as a production-style portfolio project with:
- reproducible data ingestion and preprocessing,
- model training pipeline,
- persisted model artifacts,
- Flask web app for real-time inference,
- clear project organization and documentation.

## Problem Statement

Given student profile information (gender, race/ethnicity, parental education, lunch type, test preparation status, reading score, and writing score), predict the target variable:

- `math_score`

## Project Structure

```
StudentPerformance_Predictor/
|-- app.py
|-- application.py
|-- requirements.txt
|-- setup.py
|-- README.md
|-- artifacts/
|   |-- model.pkl
|   |-- preprocessor.pkl
|   |-- train.csv
|   |-- test.csv
|   `-- data.csv
|-- notebook/
|   |-- 1 . EDA STUDENT PERFORMANCE .ipynb
|   |-- 2. MODEL TRAINING.ipynb
|   `-- data/
|       `-- stud.csv
|-- src/
|   |-- components/
|   |   |-- data_ingestion.py
|   |   |-- data_transformation.py
|   |   `-- model_trainer.py
|   |-- pipeline/
|   |   |-- train_pipeline.py
|   |   `-- predict_pipeline.py
|   |-- exception.py
|   |-- logger.py
|   `-- utils.py
`-- templates/
		|-- index.html
		`-- home.html
```

## ML Pipeline Overview

1. Data Ingestion
- Loads source dataset from `notebook/data/stud.csv`.
- Splits into train/test data and stores CSV snapshots under `artifacts/`.

2. Data Transformation
- Numerical pipeline:
	- median imputation
	- standard scaling
- Categorical pipeline:
	- most-frequent imputation
	- one-hot encoding
	- sparse scaling
- Persists fitted preprocessor to `artifacts/preprocessor.pkl`.

3. Model Training
- Trains and compares multiple regressors (scikit-learn based).
- Selects best model by test $R^2$ score.
- Persists selected model to `artifacts/model.pkl`.

4. Inference
- Flask app collects user inputs from UI.
- Applies saved preprocessor + model.
- Returns predicted `math_score`.

## Tech Stack

- Python 3.9+
- Flask
- NumPy, Pandas
- scikit-learn
- Matplotlib, Seaborn (EDA)
- Dill (serialization)

## Local Setup

1. Clone repository
```bash
git clone <your-repo-url>
cd StudentPerformance_Predictor
```

2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. (Optional) Install as package
```bash
pip install -e .
```

## Run Training Pipeline

```bash
python -m src.pipeline.train_pipeline
```

Expected output:
- train/test CSV files under `artifacts/`
- `artifacts/preprocessor.pkl`
- `artifacts/model.pkl`

## Run Web App

```bash
python app.py
```

Then open:
- `http://127.0.0.1:5000/`

## Notebooks

- `notebook/1 . EDA STUDENT PERFORMANCE .ipynb`: exploration and understanding data patterns.
- `notebook/2. MODEL TRAINING.ipynb`: model experimentation workflow.

## Portfolio Highlights

- End-to-end MLOps-style pipeline separation (`components` and `pipeline` modules)
- Clean exception handling and logging utilities
- Model serving through a web UI
- Reproducible local workflow without cloud platform lock-in

## Future Improvements

- Add automated tests for pipeline modules
- Add model tracking and experiment registry
- Add API endpoint versioning and request schema validation
- Containerize with Docker for environment consistency

## License

This project is available for educational and portfolio use.
