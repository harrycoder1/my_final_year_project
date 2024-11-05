# import numpy as np
import pandas as pd
import requests as api

class WaterApi:
    def __init__(self) -> None:
        URL = "http://nodewater.whf.bz/json.php?apikey=LIFQpwnVeyZ84Yvxk9OPDAaXV9PsbIGc&view=true"
        res = api.get(URL)
        __data = res.json()

        # Load data into a DataFrame
        self.data_set = pd.DataFrame(__data['Data'])
        self.data_set['duration'] = self.data_set['duration'].astype(int)
        self.data_set['litreWater'] = self.data_set['litreWater'].astype(float)

        # Drop missing values if the last row is completely null
        self.data_set = self.data_set.dropna() if self.data_set.iloc[-1].isnull().sum() == 0 else self.data_set[:-1].dropna()

        # Convert 'start_time' to datetime with the correct format
        self.data_set['start_time'] = pd.to_datetime(self.data_set['start_time'], format="%d-%m-%Y %H:%M")

        # Make a copy of the DataFrame
        self.data_new = self.data_set.copy()

        # Set 'start_time' as the index
        self.data_new.set_index('start_time', inplace=True)

    def __get_data_by_filter(self, date_flag, value):
        return self.data_new.resample(date_flag)[value]

    def get_monthly(self):
        monthly_duration = self.__get_data_by_filter('M', 'duration')
        monthly_litre_water = self.__get_data_by_filter('M', 'litreWater')
        print("Total Duration of motor run")

        m_d = monthly_duration.sum().reset_index('start_time')
        m_l = monthly_litre_water.sum().reset_index('start_time')

        return pd.merge(m_d, m_l, on='start_time', how="inner")

    def get_weekly(self):
        weekly_duration = self.__get_data_by_filter('W', 'duration')
        weekly_water_litre = self.__get_data_by_filter('W', 'litreWater')

        w_d = weekly_duration.sum().reset_index('start_time')
        w_l = weekly_water_litre.sum().reset_index('start_time')

        return pd.merge(w_d, w_l, on="start_time", how="inner")

    def get_daily(self):
        daily_duration = self.__get_data_by_filter('D', 'duration')
        daily_litre_water = self.__get_data_by_filter('D', 'litreWater')

        d_d = daily_duration.sum().reset_index('start_time')
        d_l = daily_litre_water.sum().reset_index('start_time')

        return pd.merge(d_d, d_l, on="start_time", how="inner")
       



