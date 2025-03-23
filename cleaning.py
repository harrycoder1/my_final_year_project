import pandas as pd
import requests as api

class WaterApi:
    def __init__(self) -> None:
        URL = "http://nodewater.whf.bz/json.php?apikey=LIFQpwnVeyZ84Yvxk9OPDAaXV9PsbIGc&view=true"
        res = api.get(URL)
        
        # Ensure API request was successful
        if res.status_code != 200:
            raise Exception(f"Failed to fetch data, status code: {res.status_code}")

        __data = res.json()
        
        # Check if the response contains 'Data'
        if 'Data' not in __data:
            raise Exception("Invalid response: 'Data' key missing in API response")

        # Load data into a DataFrame
        self.data_set = pd.DataFrame(__data['Data'])

        # Ensure the required columns exist
        required_columns = {'duration', 'litreWater', 'start_time'}
        if not required_columns.issubset(self.data_set.columns):
            raise Exception(f"Missing columns in data: {required_columns - set(self.data_set.columns)}")

        # Convert columns safely
        self.data_set['duration'] = pd.to_numeric(self.data_set['duration'], errors='coerce').fillna(0).astype(int)
        self.data_set['litreWater'] = pd.to_numeric(self.data_set['litreWater'], errors='coerce').fillna(0.0).astype(float)

        # Drop rows where start_time is missing
        self.data_set.dropna(subset=['start_time'], inplace=True)

        # Convert 'start_time' to datetime safely
        self.data_set['start_time'] = pd.to_datetime(self.data_set['start_time'], format="%d-%m-%Y %H:%M", errors='coerce')

        # Drop invalid datetime rows
        self.data_set.dropna(subset=['start_time'], inplace=True)

        # Make a copy of the cleaned DataFrame
        self.data_new = self.data_set.copy()

        # Set 'start_time' as the index
        self.data_new.set_index('start_time', inplace=True)

    def __get_data_by_filter(self, date_flag, value):
        return self.data_new.resample(date_flag)[value]

    def get_monthly(self):
        monthly_duration = self.__get_data_by_filter('M', 'duration')
        monthly_litre_water = self.__get_data_by_filter('M', 'litreWater')

        m_d = monthly_duration.sum().reset_index()
        m_l = monthly_litre_water.sum().reset_index()

        return pd.merge(m_d, m_l, on='start_time', how="inner")

    def get_weekly(self):
        weekly_duration = self.__get_data_by_filter('W', 'duration')
        weekly_water_litre = self.__get_data_by_filter('W', 'litreWater')

        w_d = weekly_duration.sum().reset_index()
        w_l = weekly_water_litre.sum().reset_index()

        return pd.merge(w_d, w_l, on="start_time", how="inner")

    def get_daily(self):
        daily_duration = self.__get_data_by_filter('D', 'duration')
        daily_litre_water = self.__get_data_by_filter('D', 'litreWater')

        d_d = daily_duration.sum().reset_index()
        d_l = daily_litre_water.sum().reset_index()

        return pd.merge(d_d, d_l, on="start_time", how="inner")
