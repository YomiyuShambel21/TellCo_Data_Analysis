import streamlit as st
from multiapp import MultiApp

# Import the converted notebooks as modules
from apps import User_Overview_Analysis
from apps import user_engagement_analysis
from apps import user_experience_analysis
from apps import user_satisfaction_analysis

# Create a multi-page app
app = MultiApp()

# Title of the dashboard
st.title("TELLCO DATA INSIGHTS")

# Add all your applications here
app.add_app("User Overview Analysis", User_Overview_Analysis.app)
app.add_app("User Engagement Analysis", user_engagement_analysis.app)
app.add_app("User Experience Analysis", user_experience_analysis.app)
app.add_app("User Satisfaction Analysis", user_satisfaction_analysis.app)

# Run the app
app.run()