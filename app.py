import streamlit as st
from frankfurter import Frankfurter
from currency import Currency

def main():
    st.set_page_config(page_title="Currency Converter", layout="wide")
    st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>FX Converter</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Welcome to your currency converter app using Web API</p>", unsafe_allow_html=True)

    frankfurter = Frankfurter()
    currency_options = frankfurter.get_available_currency()

    user_amount = st.number_input("Enter the amount to be converted", key="category_input")
    from_currency = st.selectbox("From Currency", currency_options )
    to_currency = st.selectbox("To Currency", currency_options, index=1 )
    
    if st.button("Get Latest Rate"):
        tab1, tab2 = st.tabs(["Latest Rate", "Rate Trends"])

        with tab1:
            currency = Currency(from_currency, to_currency, user_amount)
            st.header("Latest Conversion Rate")
            st.markdown(currency.return_format_result())

        with tab2:
            st.header("Trend over last 3 years")
            st.pyplot(frankfurter.get_last_years_trend(from_currency, to_currency))
        
    
    user_date = st.date_input( "Select a date",value="today", format="YYYY/MM/DD" )
    
    if st.button("Conversion Rate"):

        currency = Currency(from_currency, to_currency, user_amount, user_date)
        st.header("Conversion Rate")
        st.markdown(currency.return_format_result())

if __name__ == "__main__":
    main()