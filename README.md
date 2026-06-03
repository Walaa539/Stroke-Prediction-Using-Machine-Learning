# Walaa Salah Stroke Prediction Project

## Project Description
This project predicts stroke risk using demographic, medical, and lifestyle information.
The model was trained on a stroke prediction dataset containing variables such as age,
hypertension, heart disease, glucose level, BMI, smoking status, work type, and residence type.

## Project Question
Can machine learning predict whether a patient is at risk of stroke based on clinical and lifestyle features?

## Dataset Overview
The dataset includes:
- Gender
- Age
- Hypertension
- Heart disease
- Ever married
- Work type
- Residence type
- Average glucose level
- BMI
- Smoking status
- Stroke target variable

The target column is:
- stroke: 1 means stroke
- stroke: 0 means no stroke

## Data Cleaning
The dataset was not fully clean. The cleaning phase included:
- Removing the ID column because it does not help prediction
- Handling missing BMI values
- Handling unknown smoking status values
- Checking duplicated rows
- Creating engineered features

## Feature Engineering
New features were created:
- Age group
- BMI category
- Glucose risk category

## Exploratory Data Analysis
The project explored several variables using different visualizations:
- Target distribution plot
- Age distribution plot
- Glucose level boxplot
- Age vs stroke boxplot
- Hypertension vs stroke countplot
- Heart disease vs stroke countplot
- Smoking status vs stroke countplot
- Correlation heatmap

## Models Used
Six machine learning algorithms were compared:
1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Support Vector Machine
5. K-Nearest Neighbors
6. Gradient Boosting

## Evaluation Metrics
The models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- ROC AUC
- Classification report
- Confusion matrix
- ROC curve

## Final Model
The final model was selected based mainly on recall and ROC AUC because the dataset is highly imbalanced.
In healthcare screening, detecting stroke-risk patients is more important than relying only on accuracy.

## Model Interpretation
The model achieved good recall for detecting stroke-risk cases. However, because the dataset is highly
imbalanced, precision was low. This means the model can detect many actual stroke cases, but it may also
classify some non-stroke patients as high-risk.

Therefore, this model is useful as a screening support tool, but it should not replace medical diagnosis.

## Deployment
The final model was deployed using Streamlit.

## How to Run the App
Install the required packages:

```bash
pip install -r requirements.txt
