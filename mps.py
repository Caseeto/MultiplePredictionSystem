import pickle
import streamlit as st
from streamlit_option_menu import option_menu


loan_model = pickle.load(open('loan_model.sav', 'rb'))

mail_model = pickle.load(open('mail_model.sav', 'rb'))

with st.sidebar:

    selected = option_menu('Multiple Prediction Systems',

                          ['Loan Prediction',
                           'Mail Prediction'],
                          icons=['cash-coin', 'envelope-at'],
                          default_index=0)

if (selected == 'Loan Prediction'):

    # page title
    st.title('Loan Prediction using ML')


    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Gender = st.text_input('Gender(Female:0, Male:1)')

    with col2:
        Married = st.text_input('Married(No:0, Yes:1)')

    with col3:
        Dependents = st.text_input('Number of dependents')

    with col1:
        Education = st.text_input('Graduate(No:0, Yes:1)')

    with col2:
        Self_Employed = st.text_input('Self Employed(No:0, Yes:1)')

    with col3:
        ApplicantIncome = st.text_input('Applicant Income(Amount)')

    with col1:
        CoapplicantIncome = st.text_input('Coapplicant Income(Amount)')

    with col2:
        LoanAmount = st.text_input('Loan(Amount)')

    with col3:
        Loan_Amount_Term = st.text_input('Loan Amount Term(Days)')

    with col1:
        Credit_History = st.text_input('Credit History(No:0, Yes:1)')

    with col2:
        Property_Area = st.text_input('Property Area(Rural:0, Semi-Urban:1, Urban:2')

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
        mail_prediction = mail_model.predict([Message])

        if (mail_prediction[0] == 1):
          mail_result = 'This is a spam mail!'
        else:
          mail_result = 'This is a ham mail!'

    st.success(mail_result)



