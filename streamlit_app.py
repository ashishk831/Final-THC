import streamlit as st
import pandas as pd
import joblib
import numpy as np



st.sidebar.header("Model Prediction or Report")

selected_report = st.sidebar.selectbox("Select from below", ["Data Integrity","Feature Drift", "Label Drift","Model Prediction"])

if selected_report=="Model Prediction":
        st.header("Sales Optimization Model")
        def predict(ad_id, age, gender, interest, Impressions, Clicks, Spent, Total_Conversion, CTR, CPC):
        #def predict(ad_id, age, gender, interest,  Spent, Total_Conversion, CTR, CPC):
            if gender == 'Male':
                gender = 0
            else:
                gender = 1
            ad_id = int(ad_id)
            age = int(age)
            gender = int(gender)
            interest = int(interest)
            Impressions = int(Impressions)
            Clicks = int(Clicks)
            Spent = float(Spent)
            Total_Conversion = int(Total_Conversion)
            CTR = float(CTR)
            CPC = float(CPC)

    #     # Create a dictionary with input values
    #         input_data = {
    #             'ad_id': [ad_id],
    #             'age': [age],
    #             'gender': [gender],
    #             'interest': [interest],
    #             'Impressions': [Impressions],
    #             'Clicks': [Clicks],
    #             'Spent': [Spent],
    #             'Total_Conversion': [Total_Conversion],
    #             'CTR': [CTR],
    #             'CPC': [CPC]
    #         }
    # # Create a DataFrame from the input data
    #         input_df = pd.DataFrame(input_data)
            input=np.array([[ad_id, age, gender, interest, Impressions, Clicks, Spent, Total_Conversion, CTR, CPC]]).astype(np.float64)
    
            model = joblib.load('model/model.pkl')
    # Make prediction
            prediction = model.predict(input)
            prediction= np.round(prediction)
    # Return the predicted value for Approved_Conversion
            # return round(prediction[0])
            return prediction
        
        ad_id = st.number_input('Enter the advertisement ID',min_value = 0)
        age = st.number_input('Enter the target age stoup',min_value = 0)
        gender = st.radio("Gender",('Male','Female'))
        interest = st.selectbox('Interest', [2, 7, 10, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 
                        26, 27, 28, 29, 30, 31, 32, 36, 63, 64, 65, 66, 100, 101, 102, 
                        103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114])
        Impressions = st.number_input('Enter the number of impressions',min_value = 0)
        Clicks = st.number_input('Enter the number of clicks',min_value = 0)
        Spent = st.number_input('Enter the amount spent on the ad',min_value = 0)
        Total_Conversion = st.number_input('Enter the total conversion count',min_value = 0)
        CTR = st.number_input('Enter the Click-Through Rate',min_value = 0)
        CPC = st.number_input('Enter the Cost Per Click',min_value = 0)

        if st.button("Predicted Approved Conversion"): 
             output = predict(ad_id, age, gender, interest, Impressions, Clicks, Spent, Total_Conversion, CTR, CPC)
             st.success("Approved Conversion Rate  :{}".format(output))
        # Create stadio interface with improved styling
else:
    st.header("Sales Model Monitoring Report")
    report_file_name = "report/"+ selected_report.replace(" ", "") + ".html"
    HtmlFile = open(report_file_name, 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    st.components.v1.html(source_code, width=1200, height=1500, scrolling=True)

