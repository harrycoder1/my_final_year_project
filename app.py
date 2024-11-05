import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from cleaning import WaterApi

# Initialize WaterApi
api = WaterApi()

# Set title for the Streamlit app
st.title("Auto-Plant Care")

# Get monthly, weekly, and daily data from the API
monthly_data = api.get_monthly()
df_week = api.get_weekly()
df_daily = api.get_daily()

# For pie chart Monthly:
total = monthly_data["litreWater"].sum()

# Month names for labels
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November']

# Calculate percentage of water utilized
monthly_data["percentage_water_utilize"] = round((monthly_data['litreWater'] / total) * 100, 2)

# Assign month names to the DataFrame
monthly_data["months"] = months

# Create a pie chart
pie_fig = go.Figure(data=[go.Pie(labels=monthly_data["months"],
                                   values=monthly_data["percentage_water_utilize"],
                                   hole=0.3)])  # Add a hole for a donut chart
pie_fig.update_layout(title_text='Water Utilization by Month', title_font_size=24)

# Create a bar plot for monthly water usage
bar_fig = px.bar(monthly_data, x='months', y='litreWater',
                  title='Months vs Litres of Water Used',
                  labels={'litreWater': 'Litres of Water', 'months': 'Months'},
                  color='litreWater', color_continuous_scale=px.colors.sequential.Viridis)
bar_fig.update_layout(title_font_size=24)

# Create a line plot for weekly water usage
line_weekly_fig = go.Figure()
line_weekly_fig.add_trace(go.Scatter(x=df_week['start_time'], y=df_week['litreWater'],
                                      mode='lines+markers', name='Litres of Water',
                                      line=dict(width=2), marker=dict(size=6)))
line_weekly_fig.update_layout(title='Weekly Water Usage',
                               xaxis_title='Weeks',
                               yaxis_title='Litres of Water',
                               title_font_size=24)
line_weekly_fig.update_xaxes(tickformat="%Y-%m-%d")  # Format x-axis for better readability

# Create a line plot for daily water usage
line_daily_fig = go.Figure()
line_daily_fig.add_trace(go.Scatter(x=df_daily['start_time'], y=df_daily['litreWater'],
                                     mode='lines+markers', name='Litres of Water',
                                     line=dict(width=2), marker=dict(size=6)))
line_daily_fig.update_layout(title='Daily Water Usage',
                              xaxis_title='Days',
                              yaxis_title='Litres of Water',
                              title_font_size=24)
line_daily_fig.update_xaxes(tickformat="%Y-%m-%d")  # Format x-axis for better readability

# Display the figures in Streamlit
st.plotly_chart(pie_fig)
st.plotly_chart(bar_fig)
st.plotly_chart(line_weekly_fig)
st.plotly_chart(line_daily_fig)

# Description text
st.text("This is a description.")
