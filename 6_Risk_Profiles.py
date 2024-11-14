import streamlit as st

st.title("Risk Profiles")
st.write("You are now on Risk Profiles.")



with st.expander("Click to see High Risk customers"):
    st.dataframe(highrisk_json_df)

with st.expander("Click to see Very High Risk customers"):    
    st.dataframe(veryhighrisk_json_df)