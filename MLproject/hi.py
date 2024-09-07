import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

   #Set page configuration

st.set_page_config(page_icon="Health Gaurd",layout="wide")

   #path of working directory

working_dir = os.path.dirname(os.path.abspath(__file__))

   #loding of the saved model

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_model = pickle.load(open('heart_model.sav','rb'))
       #page Layout 

st.markdown("""
    <style>
    .main { background-color: #F0F2F6; }
    .stButton>button { background-color: #4CAF50; color: white; }
    .stTabs>div>div { border-bottom: 4px solid #4CAF50; }
    </style>
    """, unsafe_allow_html=True)  

     # Tab Navigation  

tabs = st.tabs(["Diabetes Prediction", "Heart Disease Prediction","Parkinson's Prediction","Breast Cancer Prediction"])         

    #sidebar for navigation



    # Diabetese prediction page


    
      #page title 
with tabs[0]:     
    st.title('Diabetes Predection Using ML')

      #getting the input data from the user
    col1,col2,col3 = st.columns(3)

    with col1:
        Pregnancies = col1.slider('Number of Pregnancies',0, 20, 0)
    
    with col2:
        Glucose = col2.slider('Glucose Level',0, 200, 120)

    with col3:
        BloodPressure = col3.slider('Blood Pressure Value',0, 200, 80)

    with col1:
        SkinThickness = col1.slider('Skin Thickness',0, 100, 20)
    
    with col2:
        Insulin = col2.slider('Insulin Level',0, 900, 30)

    with col3:
        BMI = col3.slider('BMI Values',0.0, 70.0, 25.0)

    with col1:
        DiabetesPedigreeFunction = col1.slider('Diabetes Pedigree Function Value',0.0, 2.5, 0.5)
    
    with col2:
        Age = col2.slider('Age of the Person',0, 100, 25)

       # backend logics
    diab_diagnosis = ''

       #creation of a button

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.success(diab_diagnosis)   


    #Heart disease

# Heart Disease Prediction Page
with tabs[1]:
    st.title('Heart Disease Prediction Using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = col1.slider('Age', 0, 100, 50)

    with col2:
        sex = col2.radio('Sex', ['Male', 'Female'])

    with col3:
        cp = col3.selectbox('Chest Pain types', ['Type 1', 'Type 2', 'Type 3', 'Type 4'])

    with col1:
        trestbps = col1.slider('Resting Blood Pressure', 0, 200, 120)

    with col2:
        chol = col2.slider('Serum Cholestoral in mg/dl', 100, 600, 200)

    with col3:
        fbs = col3.radio('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])

    with col1:
        restecg = col1.radio('Resting Electrocardiographic results', ['Normal', 'Abnormal'])

    with col2:
        thalach = col2.slider('Maximum Heart Rate achieved', 50, 220, 150)

    with col3:
        exang = col3.radio('Exercise Induced Angina', ['Yes', 'No'])

    with col1:
        oldpeak = col1.slider('ST depression induced by exercise', 0.0, 10.0, 1.0)

    with col2:
        slope = col2.selectbox('Slope of the peak exercise ST segment', ['Upsloping', 'Flat', 'Downsloping'])

    with col3:
        ca = col3.slider('Major vessels colored by fluoroscopy', 0, 4, 0)

    with col1:
        thal = col1.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversable Defect'])

    # Convert categorical variables to numeric values
    sex_numeric = 1 if sex == 'Male' else 0
    fbs_numeric = 1 if fbs == 'Yes' else 0
    exang_numeric = 1 if exang == 'Yes' else 0
    restecg_numeric = 1 if restecg == 'Abnormal' else 0
    slope_numeric = {'Upsloping': 1, 'Flat': 2, 'Downsloping': 3}.get(slope, 0)
    thal_numeric = {'Normal': 1, 'Fixed Defect': 2, 'Reversable Defect': 3}.get(thal, 0)
    cp_numeric = {'Type 1': 1, 'Type 2': 2, 'Type 3': 3, 'Type 4': 4}.get(cp, 0)  # Added conversion for cp

    # Backend logics
    Heart_diagnosis = ''

    # Creation of a button
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex_numeric, cp_numeric, trestbps, chol, fbs_numeric, restecg_numeric, thalach, exang_numeric, oldpeak, slope_numeric, ca, thal_numeric]
        Heart_Prediction = heart_model.predict([user_input])
        Heart_diagnosis = 'The person is having Heart disease' if Heart_Prediction[0] == 1 else 'The person does not have any heart disease'
        st.success(Heart_diagnosis)
          
# Parkinson's Prediction Tab
with tabs[2]:
    st.title("Parkinson's Prediction coming soon.....")
    st.write("This feature is under development.") 

# Breast Cancer Prediction Tab (Dummy for UI Consistency)
with tabs[3]:
    st.title("Breast Cancer Prediction coming soon...")
    st.write("This feature is under development.")
      

    


