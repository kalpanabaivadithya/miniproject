import streamlit as st

users = {
    "student@gmail.com": "123456",
    "admin@gmail.com": "admin123"
}

def login():

    st.subheader("Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Sign In"):

        if email in users and users[email] == password:
            st.session_state["logged_in"] = True
            st.session_state["user"] = email
            st.success("Login Successful")
            st.rerun()

        else:
            st.error("Invalid Credentials")