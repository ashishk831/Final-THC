# SALE-CONVERTION-OPTIMISATIONS-MLOPs

## Introduction
Advertising product to right set of customer is a bigger challenge for the company. There are many ways to target customer through online channels such as youtube, facebook, google. These company provide them platform to show their ads. But as a company who want to increase their revenue by selling product showing ads will not help much. There needs to be a method through which we can ensure that we are reaching right customer and converting them as a customer to generate revenue.

## Problem Statement
In this project we will build a model which will predict whether the customer will buy product or not after seeing the ads. This will be help company in utilizing there resource more and getting right set of customer. We can also monitor our model to see if there is any change in data or model prediction. 

## Deployment

Let's jump into the Python packages you need. Within the Python environment of your choice, run:

```bash
git clone https://github.com/apache/airflow
cd sale-projects/sale-prediction
pip install -r requirements.txt
```

Kedro
Kerdo is a open-source tool for machine learning engineers. 
* ``Handles Complexity:`` It provide a stucture to test data which can be pushed to production after successful testing.

* ``Standardisation:`` It provides standard template for project. Making it earrlier to understand for others.

* ``Production-Ready:`` Code can be easily pushed to production with exploratory code that you can transition to reproducible, maintainable, and modular experiments.

```bash
#Installing kedro

pip install kedro

#Installing kedro-viz

pip install kedro-viz

#create project
kedro new

#create pipeline
kedro pipeline create <pipeline-name>

#Run kedro
kedro run

#Visualizing pipeline
kedro viz
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

![image](https://github.com/ashishk831/Final-THC/assets/81232686/9fda8085-5ce2-408f-a75b-d0c8771edf5c)


In Airflow we can also monitor the logs, DAGS generate log when the pipeline is executed. Below is the image.
![image](https://github.com/ashishk831/Final-THC/assets/81232686/15a2555b-4761-4fa2-92a4-06f78eed9db6)


## Demo Streamlit App 



There is a live demo of this project using Streamlit which you can find here. It takes some input features for the product and predicts the customer satisfaction rate using the latest trained models. If you want to run this Streamlit app in your local system, you can run the following command to access the app locally.

``streamlit run streamlit_app.py``

The cloud version of app can also be accessed using below url.

```
https://fraud-prediction-mlops-d8rcgc2prmv9xapx5ahhhn.streamlit.app/
```

Below is the sample model result.
