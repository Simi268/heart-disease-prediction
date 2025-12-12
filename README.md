❤ Heart Disease Prediction using Machine Learning

This project predicts the likelihood of heart disease based on patient health parameters using machine learning algorithms. The goal is to build an accurate, reliable model by comparing multiple classifiers and finally selecting the best-performing one.


---

📌 Project Overview

Heart disease remains one of the leading causes of death worldwide. Early prediction can help save lives by enabling timely diagnosis and treatment.

In this project, we:

Performed Exploratory Data Analysis (EDA)

Preprocessed the dataset (handling missing values, encoding, scaling)

Built a machine learning pipeline

Compared two models:

Logistic Regression

Random Forest Classifier


Selected the best model based on performance metrics

Developed a simple prediction application



---

🧠 Algorithms Used

🔹 Logistic Regression

A linear model used for binary classification. Works well when features are linearly related.

🔹 Random Forest Classifier

An ensemble method that builds multiple decision trees and takes the majority vote.
It performed better in this project, so it was selected as the final model.


---

📊 Dataset Features

Common attributes in heart disease datasets include:

Age

Sex

Chest pain type

Blood pressure

Cholesterol

Fasting blood sugar

Resting ECG

Maximum heart rate

Exercise-induced angina

ST depression

Number of major vessels

Thalassemia




---

🔍 Exploratory Data Analysis (EDA)

In the EDA phase, we analyzed:

Correlation between variables

Distribution of key features

Outlier detection

Patterns related to heart disease presence


Heatmaps and visualizations helped in understanding relationships between features and the target.


---

🏗 Model Building & Pipeline

A preprocessing + modeling pipeline was created that handled:

OneHotEncoding of categorical variables

Scaling numerical inputs

Splitting into train/test sets

Fitting both models

Comparing accuracy, precision, recall, and F1-score


A model comparison table was generated, where Random Forest performed better than Logistic Regression.


---

🧪 Evaluation Metrics

Metrics used:

Accuracy

Precision

Recall

F1-Score

Confusion Matrix


Random Forest showed higher overall performance, especially in recall, which is critical in medical prediction.


---

🏆 Final Model Selected

✔ Random Forest Classifier

Reason:

Highest accuracy

Best recall (helps minimize false negatives)

Handles non-linear relationships well

Robust to noise



---

💻 Application

A small application (application.py) was created to:

Take user inputs

Process them through the trained model

Provide prediction:

1 = Heart disease likely

0 = No heart disease



This app can be used for demonstration or extended into a web interface.




🚀 Future Improvements

Deploy the model using Flask/Streamlit

Add more models (XGBoost, SVM, Neural Networks)

Improve UI for user interaction

Hyperparameter tuning using GridSearchCV/RandomizedSearchCV
