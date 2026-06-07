import streamlit as st
from interview import get_response
from auth import login

st.set_page_config(
    page_title="AI Interview Preparation Assistant",
    page_icon="🤖"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = ""

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

    st.info(
        "Google Login requires complete OAuth configuration."
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
        "Ask Technical or HR Interview Question"
    )

    if st.button("Generate Answer"):

        if question.strip():

            with st.spinner("Generating Answer..."):

                answer = get_response(question)

                st.markdown("### Answer")

                st.write(answer)

        else:
            st.warning("Please enter a question.")

    if st.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.user = ""

        st.rerun()