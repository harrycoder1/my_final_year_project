import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from cleaning import WaterApi

# Initialize WaterApi
api = WaterApi()

# Set title for the Streamlit app
st.title("Auto-Plant Care")
# Description text
st.text("""The “Automated Road plant soil moisture level identification and irrigation using esp8266 and data analytics” a sustainable solution towards care of plants on roads. With the used of esp8266 module along with data analytics provide a solution towards wastage of water while watering of plants on roads by tankers and spilling of mud on roads in that process causing increase in chances of accidents. Using moisture sensors to accurately measure water content of soil and supplying of water when required along with effective tracking of water supplied for irrigation. Providing a effective water usage analytics and automated irrigation saving water and manual labor and efforts while maintaining roadside greenery and supporting vegetation
Keywords: esp8266, automated irrigation, water usage analytics, water saving, moisture sensors
""")

# Get monthly data from the API
monthly_data = api.get_monthly()

# Get weekly and daily data (Assuming you have similar methods in your WaterApi class)
df_week = api.get_weekly()
df_daily = api.get_daily()

# For pie chart Monthly:
total = monthly_data["litreWater"].sum()

# Month names for labels
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']

# Calculate percentage of water utilized
monthly_data["percentage_water_utilize"] = round((monthly_data['litreWater'] / total) * 100, 2)

# Assign month names to the DataFrame
monthly_data["months"] = months

# Create a figure with subplots for monthly and weekly/daily data
fig, axs = plt.subplots(2, 2, figsize=(15, 15))  # 2 rows, 2 columns

# Create Pie Chart
sizes = monthly_data["percentage_water_utilize"]
labels = monthly_data["months"]

axs[0, 0].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
axs[0, 0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
axs[0, 0].set_title("Water Utilization by Month")

# Create Bar Plot
sns.barplot(x='months', y='litreWater', data=monthly_data, color="orange", ax=axs[0, 1])
axs[0, 1].set_title("Months vs Litres of Water Used")
axs[0, 1].set_ylabel("Litres of Water")
axs[0, 1].set_xlabel("Months")

# Create Weekly Line Plot
axs[1, 0].plot(df_week['start_time'], df_week['litreWater'], lw=2, marker=".")
axs[1, 0].set_title("Week Uses vs Litres of Water")
axs[1, 0].set_xlabel("Weeks")
axs[1, 0].set_ylabel("Litres of Water")
axs[1, 0].tick_params(axis='x', rotation=45)
axs[1, 0].legend(["Litres of Water Used"], loc='upper right')

# Create Daily Line Plot
axs[1, 1].plot(df_daily['start_time'], df_daily['litreWater'], lw=2)
axs[1, 1].set_title("Day vs Litres of Water Utilized")
axs[1, 1].set_xlabel("Days")
axs[1, 1].set_ylabel("Litres of Water")
axs[1, 1].tick_params(axis='x', rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the combined figure in Streamlit
st.pyplot(fig)

