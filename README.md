# Auto-Plant Care 🌱

This project is an innovative solution for automating the irrigation process and monitoring water utilization for roadside divider plants. It combines IoT, data analysis, and visualization to make the watering process more efficient, cost-effective, and environmentally friendly.

## Project Overview

Current manual methods of watering roadside plants involve water tankers, leading to inefficiencies such as:

- Overuse of water.
- Risk of accidents due to mud spills on roads.
- High labor costs and uncalculated water usage.

The **Auto-Plant Care** system addresses these issues by:

- Using **moisture sensors** to monitor soil conditions.
- Automating water supply based on the soil's water content.
- Tracking and visualizing water usage with a user-friendly interface.

## Features

1. **Data Visualization**:
   - Monthly, weekly, and daily water usage analysis.
   - Pie charts, bar plots, and line graphs to track water utilization trends.
2. **IoT Integration**:
   - Utilizes moisture sensors for real-time soil monitoring.
3. **Streamlit Dashboard**:
   - Interactive web app displaying water usage data and insights.
4. **Cost Efficiency**:
   - Reduces manual labor and fuel usage while optimizing water consumption.

## Technologies Used

- **Streamlit**: For creating the interactive dashboard.
- **Plotly**: For visualizing water usage data.
- **Python**: Backend logic and API integration.
- **IoT Sensors**: For real-time soil moisture detection.
- **API Integration**: To fetch water usage data.

## How to Run the Project

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd auto-plant-care
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Open the app in your browser at `http://localhost:8501`.

## Data Flow

1. **Input**:
   - Data fetched from IoT sensors through an API.
2. **Processing**:
   - Analyzed and structured using the `WaterApi` Python class.
3. **Output**:
   - Visualized as pie charts, bar plots, and line graphs.

## API Integration

This project integrates with an API to fetch water usage data. The API provides:

- Monthly water usage (`get_monthly`).
- Weekly water usage (`get_weekly`).
- Daily water usage (`get_daily`).

## Visualizations

- **Pie Chart**: Percentage of water utilization by month.
- **Bar Chart**: Monthly water usage.
- **Line Graphs**: Weekly and daily water usage trends.

## Future Enhancements

- Add predictive analytics for water usage.
- Introduce real-time alerts for low moisture levels.
- Expand to support additional IoT devices and APIs.

## Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push:
   ```bash
   git push origin feature-name
   ```
4. Submit a pull request.









