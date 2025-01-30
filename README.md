# **Web application for predicting chronic kidney disease**
# Overview :
A web application that determines whether a person has chronic kidney disease or not through a set of features through which we enter data into the model and then predict the result. 
+ The most important of these features are: (BMI , Family History Kidney Disease , Systolic BP , Fasting Blood Sugar , HbA1c , Serum Creatinine , BUN Levels , GFR , Protein in Urine , Edema , Muscle Cramps , Itching).
 
# Project advantages :
* User interface: A simple interface for easy input of health data.
* AdaBoost model: The AdaBoost model, known for its high accuracy in predictions, is used.
* Instant prediction: Provides instant prediction results based on user inputs.

# Technologies Used :
* Frontend: HTML, CSS, JavaScript.
* Backend: Python, Flask.
* Machine learning Models : logistic regression, KNN, SVM, Random forest, Decision tree, XGBoost, AdaBoost and AdaBoost was chosen as the best model in terms of precision, recall, and, ROC-AUC for predicting CKD outcomes in the web application.

 # Project steps : 
 ### 1. Data Import:
+ Download the Chronic Kindney Disease dataset from Kaggle.

### 2. Data Analysis:
* Explore data and analyze different features.
* Creating visualizations to highlight the relationships between different features and the outcome. 

### 3. Data processing and cleaning: 
* Data cleaning by removing the unimportant feature that does not have a significant impact on the result.
* Reduce high cardinality by using binning.
* Data encoding using label encoding.

### 4. Model Building:
* Try different algorithms like: Logistic regression, KNN, SVM, Random forest, Decision tree, XGBoost, AdaBoost.
*  Each model is evaluated based on precision, recall, and roc-auc, and the best model in terms of precision, recall, and roc-auc is selected for use in predicting the outcome in the web application based on user input.
  
### 5. Model improvement:
* Improving the model using techniques such as cross-validation and feature engineering.
* Compare the different models and choose the one that provides the best result.

### 6. Model Deployment:
* Save the Best Model: Save the trained model to a file (using joblib or pickle).
* Create a Flask Web Application: Develop a web application using Flask to serve the model.
* Build User Interface: Create an interface using HTML and CSS for users to input their health data.
* Integrate Model with Web App: By uploading the saved model in the Flask application and using it to generate predictions based on user inputs.
* Running the model: By testing it with data input to make a prediction of the result.
 
 # Project Objective:
* Develop a web application using the AdaBoost model to predict chronic kidney disease based on a set of input data with high prediction accuracy to predict whether a person has kidney disease or not.

# Results of the model chosen to display prediction results (AdaBoost):
## Train Data
* #### Accuracy Score: 0.96
* #### ROC AUC Score: 0.96
* #### Confusion Matrix:
 
 Actual \ Predicted | 0 | 1 |
| ------------- | ------------- |------------- |
| 0  | (TN) 1146  |  (FP) 70 |
| 1  | (FN) 19 |  (TP) 1197 |

* #### Performance Metrics for Model Classification:
 
|Class  | Precision | Recall | F1-score | Support | 
| ------------- | ------------- |------------- |------------- |------------- |
| 0  | 0.98 | 0.94 | 0.96 | 1216 |
| 1  |  0.94| 0.98 | 0.96 | 1216 |

## Test Data:
* #### Accuracy Score: 0.94
* #### ROC AUC Score: 0.6842532467532467
* #### Confusion Matrix: 

 Actual \ Predicted | 0 | 1 |
| ------------- | ------------- |------------- |
| 0  | (TN) 9 |  (FP) 15 |
| 1  | (FN) 2 |  (TP) 306 |


* #### Performance Metrics for Model Classification:
 
|Class  | Precision | Recall | F1-score | Support | 
| ------------- | ------------- |------------- |------------- |------------- |
| 0  | 0.82 | 0.38 | 0.51 | 24 |
| 1  |  0.95| 0.99 | 0.97 | 308 |

## Dataset Link /
### The dataset for this project can be found [here](https://www.kaggle.com/datasets/rabieelkharoua/chronic-kidney-disease-dataset-analysis)

 # Web application images and prediction results:  
 ### 1. Home page : 
 The home page contains a simple definition of the web application and a button to go to the medical data registration page. 
![img14](https://github.com/user-attachments/assets/658986bc-2c41-483e-87ea-f2e9f7f169f1)
________________________________________________________________________________________
### 2. Medical data entry form page : 
It contains a set of important features through which data is entered to display the prediction result.
![img15](https://github.com/user-attachments/assets/b8f23b57-fa8e-4899-a8b8-9f7db993dcc0)
________________________________________________________________________________________
### 3. Medical data entry form page with data entry of the person to be diagnosed 
![img16](https://github.com/user-attachments/assets/b23c84c1-fea3-475b-9a3e-4b106e834ec4)
________________________________________________________________________________________
### 4. Display the prediction result: 
Display the prediction result based on the entered data with an alert message to conduct further medical examination. It also contains 2 buttons, one to go to the home page and another to return to the data entry form.
![img17](https://github.com/user-attachments/assets/3714170c-653c-4d52-8fa0-7e0b93b04ff8)
