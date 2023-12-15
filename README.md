# SALE-CONVERTION-OPTIMISATIONS-MLOPs

## Introduction
Write intro


## Problem Statement
Describe problem


## Deployment

Let's jump into the Python packages you need. Within the Python environment of your choice, run:

```bash
git clone https://github.com/apache/airflow
cd sale-projects/sale-prediction
pip install -r requirements.txt
```

Kedro

* ``Scalability:`` Airflow can be scaled to handle a large number of tasks and workflows.

* ``Reliability:`` Airflow is designed to be reliable and fault-tolerant.

* ``Flexibility:`` Airflow can be used to automate a wide variety of workflows, from simple to complex.

* ``Extensibility:`` Airflow can be easily extended to meet the needs of specific organizations.

```bash
#Installing kedro

```


note


```note```



## Solution
Solution


## Training dataset
dataset description

* ``ad_id``:- An unique ID for each ad.

* ``xyz_campaign_id`` - An ID associated with each ad campaign of XYZ company.

* ``fb_campaign_id`` - An ID associated with how Facebook tracks each campaign.

* ``age`` - Age of the person to whom the ad is shown.

* ``gender`` - Gender of the person to whim the add is shown

* ``interest`` - A code specifying the category to which the person’s interest belongs (interests are as mentioned in the person’s Facebook public profile).

* ``Impressions`` - The number of times the ad was shown.

* ``Clicks`` - Number of clicks on for that ad.

* ``Spent`` - Amount paid by company xyz to Facebook, to show that ad.

* ``Total conversion`` - Total number of people who enquired about the product after seeing the ad.

* ``Approved conversion`` - Total number of people who bought the product after seeing the ad. <--- Target Class 


## Training Pipeline
Our standard training pipeline consists of several steps:

* ``data_preprocessing``:- data_preprocessing

* ``data_split``:- This operator will split the dataset into two part. On first part the model will be trained and on second set model will be tested.

* ``model_training``:- This operator is used to train model on dataset.

* ``model_evaluation``:- This operator is used to evaluate the model performance.

Below is the pipeline workflow which we will implement in this project.

## Model Selection Pipeline
In model training pipeline we have used ensemble learning with DecisionTreeClassifier, RandomForestClassifier, AdaBoostClassifier and GradientBoostingClassifier. Once model training is completed then model evaluatoin will be executed. Then we will created model selection pipeline which compare the model and select the best model.

* ``model_selection_operator``:- In model training operator we used multiple ML algorithm to train model. In this operator we will compare the different model and choose the best model. 

## Model Prediction Pipeline
As we have half million test record on which model is neither training or tested. We will use this data set to check how good is our model.  

* ``model_prediction_operator``:- This operator is used to predict the model on new unseen dataset.

## Model Monitoring and Log Analysis

Airflow also offer the feature to monitor our model in real-time. When the DAGs are executed there are different status through which it passes.Below is status code show.  
![image](https://github.com/ashishk831/FRAUD-PREDICTION-MLOPs/assets/81232686/c6f942af-ad8b-45c3-be13-52300a737b24)

In Airflow we can also monitor the logs, DAGS generate log when the pipeline is executed. Below is the image.
![image](https://github.com/ashishk831/FRAUD-PREDICTION-MLOPs/assets/81232686/122eaa72-a56b-43f1-b4a0-cf55487ba226)

## Demo Streamlit App ![image](https://github.com/ashishk831/FRAUD-PREDICTION-MLOPs/assets/81232686/85fbe63c-37e7-4757-af9b-7d15127ef02a) 


There is a live demo of this project using Streamlit which you can find here. It takes some input features for the product and predicts the customer satisfaction rate using the latest trained models. If you want to run this Streamlit app in your local system, you can run the following command to access the app locally.

``streamlit run streamlit_app.py``

The cloud version of app can also be accessed using below url.

```
https://fraud-prediction-mlops-d8rcgc2prmv9xapx5ahhhn.streamlit.app/
```

Below is the sample model result.
