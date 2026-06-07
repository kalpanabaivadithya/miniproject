import streamlit as st
from interview import get_response
from auth import login

st.set_page_config(
    page_title="AI Interview Preparation Assistant",
    page_icon="🤖"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ------------------------
# LOGIN PAGE
# ------------------------

if not st.session_state.logged_in:

    st.title("AI Interview Preparation Assistant")

    st.write(
        "Prepare for Technical and HR Interviews"
    )

    login()

    st.markdown("---")

    st.subheader("Continue with Google")

    CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID"

    google_login_url = (
        f"https://accounts.google.com/o/oauth2/v2/auth"
        f"?client_id={CLIENT_ID}"
        f"&redirect_uri=http://localhost:8501"
        f"&response_type=code"
        f"&scope=openid%20email%20profile"
    )

    st.link_button(
        "Continue with Google",
        google_login_url
    )

# ------------------------
# DASHBOARD
# ------------------------

else:

    st.title("Interview Dashboard")

    st.success(
        f"Welcome {st.session_state.user}"
    )

    question = st.text_area(
        "Ask Interview Question"
    )

    if st.button("Generate Answer"):

        with st.spinner("Generating..."):

            answer = get_response(question)

            st.markdown("### Answer")

            st.write(answer)

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()