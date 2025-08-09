import pickle
import streamlit as st
from streamlit_option_menu import option_menu


loan_model = pickle.load(open('loan_model.sav', 'rb'))

mail_model = pickle.load(open('mail_model.sav', 'rb'))

'''
_model = pickle.load(open('_model.sav', 'rb'))

_model = pickle.load(open('_model.sav', 'rb'))
'''

with st.sidebar:

    selected = option_menu('Multiple Prediction Systems',

                          ['Loan Prediction',
                           'Mail Prediction'],
                          icons=['cash-coin', 'envelope-at'],
                          default_index=0)

if (selected == 'Loan Prediction'):

    # page title
    st.title('Loan Prediction using ML')
,Loan_Amount_Term,Credit_History,Property_Area


    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Gender = st.text_input('Gender')

    with col2:
        Married = st.text_input('Married')

    with col3:
        Dependents = st.text_input('Dependents')

    with col1:
        Education = st.text_input('Education')

    with col2:
        Self_Employed = st.text_input('Self_Employed')

    with col3:
        ApplicantIncome = st.text_input('ApplicantIncome')

    with col1:
        CoapplicantIncome = st.text_input('CoapplicantIncome')

    with col2:
        LoanAmount = st.text_input('LoanAmount')

    with col3:
        Loan_Amount_Term = st.text_input('Loan_Amount_Term')

    with col1:
        Credit_History = st.text_input('Credit_History')

    with col2:
        Property_Area = st.text_input('Property_Area')

    loan_result = ''

    # creating a button for Prediction

    if st.button('Loan Status Test Result'):
        loan_prediction = loan_model.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])

        if (loan_prediction[0] == 1):
          loan_result = 'Loan application is approved!'
        else:
          loan_result = 'Loan application is rejected!'

    st.success(loan_result)



if (selected == 'Mail Prediction'):

    # page title
    st.title('Mail Prediction using ML')


    # getting the input data from the user

    Message = st.text_input('Type your message for the mail:')

    mail_result = ''

    # creating a button for Prediction

    if st.button('Mail Test Result'):
        mail_prediction = mail_model.predict([[Message]])

        if (mail_prediction[0] == 1):
          mail_result = 'This is a spam mail!'
        else:
          mail_result = 'This is a ham mail!'

    st.success(mail_result)


'''
if (selected == '     Prediction'):

    # page title
    st.title('    Prediction using ML')


    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('    ')

    with col2:
        Glucose = st.text_input('     ')

    with col3:
        BloodPressure = st.text_input('      ')

    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('     Test Result'):
        diab_prediction = diabetes_model.predict([[     ,    ,    ]])

        if (_prediction[0] == 1):
          diab_diagnosis = '  '
        else:
            _diagnosis = ' '

    st.success(  _diagnosis)


if (selected == '     Prediction'):

    # page title
    st.title('    Prediction using ML')


    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('    ')

    with col2:
        Glucose = st.text_input('     ')

    with col3:
        BloodPressure = st.text_input('      ')

    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('     Test Result'):
        diab_prediction = diabetes_model.predict([[     ,    ,    ]])

        if (_prediction[0] == 1):
          diab_diagnosis = '  '
        else:
            _diagnosis = ' '

    st.success(  _diagnosis)
'''
