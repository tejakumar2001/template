import streamlit as st

def registration():
    st.title("Registration")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if password == confirm_password:
            st.success("Registration successful! You can now login.")
            
        else:
            st.error("Passwords do not match. Please try again.")

def login():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        
        if username == "admin" and password == "password":
            st.success("Logged in successfully!")
            st.write("Redirecting to the home page...")
            home()
        else:
            st.error("Invalid username or password. Please try again.")

def home():
    st.title("Home")

    st.write("Welcome to the home page!")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Login", "Registration"))

    if page == "Login":
        login()
    elif page == "Registration":
        registration()

if __name__ == "__main__":
    main()

