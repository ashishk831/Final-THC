import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import deepchecks
from deepchecks.tabular.checks import LabelDrift, FeatureDrift
from deepchecks.tabular.suites import data_integrity

class DataPreprocessor:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def preprocess_data(self):
        self.data.gender = self.data.gender.apply(lambda x: 1 if x == "M" else 0)
        self.data['CTR'] = ((self.data['Clicks'] / self.data['Impressions']) * 100)
        self.data['CPC'] = self.data['Spent'] / self.data['Clicks']
        self.data['CPC'] = self.data['CPC'].replace(np.nan, 0)
        encoder = LabelEncoder()
        encoder.fit(self.data["age"])
        self.data["age"] = encoder.transform(self.data["age"])
        return self.data

class DatasetCreator:
    def __init__(self, df, label_col, cat_features=[]):
        self.dataset = deepchecks.tabular.Dataset(df=df, label=df[label_col], cat_features=cat_features)

class DataIntegrityChecker:
    def __init__(self):
        self.integ_suite = data_integrity()

    def run_check(self, dataset):
        integ_result = self.integ_suite.run(dataset)
        integ_result.save_as_html('report/DataIntegrity.html')

class LabelDriftChecker:
    def __init__(self):
        self.label_check = LabelDrift()

    def run_check(self, train_dataset, test_dataset):
        label_result = self.label_check.run(train_dataset, test_dataset)
        label_result.save_as_html('report/LabelDrift.html')

class FeatureDriftChecker:
    def __init__(self):
        self.feature_checks = FeatureDrift()

    def run_check(self, train_dataset, test_dataset):
        feature_results = self.feature_checks.run(train_dataset=train_dataset, test_dataset=test_dataset)
        feature_results.save_as_html('report/FeatureDrift.html')

# Load and preprocess data
preprocessor = DataPreprocessor('/home/unibash/G3/B/SALE_CNV_OPT/data/KAG_conversion_data.csv')
preprocessed_data = preprocessor.preprocess_data()

# Split data into train and test sets
X = preprocessed_data[['ad_id', 'age', 'gender', 'interest', 'Spent', 'Total_Conversion', 'CTR', 'CPC']]
y = preprocessed_data["Approved_Conversion"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Create datasets
train_dataset = deepchecks.tabular.Dataset(df=X_train,label=y_train,cat_features=[])
test_dataset = deepchecks.tabular.Dataset(df=X_test,label=y_test,cat_features=[])

# Run data integrity check
data_integrity_checker = DataIntegrityChecker()
data_integrity_checker.run_check(train_dataset)

# Run label drift check
label_drift_checker = LabelDriftChecker()
label_drift_checker.run_check(train_dataset, test_dataset)

# Run feature drift check
feature_drift_checker = FeatureDriftChecker()
feature_drift_checker.run_check(train_dataset, test_dataset)
