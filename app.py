import streamlit as st
import pandas as pd
import numpy as np


def calc_nest_egg(savings,years,rate):
    '''
    Calculate nest egg after a period time when saving a certain value over 
    time.
    '''
    numerator = (1 + rate/1200) ** (12*years) - 1
    denominator = rate/1200
    # Monthly savings → Nest egg
    return savings*numerator/denominator

def calc_nest_egg_over_time(monthly_saving ,r , total_years):
    '''
    Calculate a list of the size of the nest egg over time
    '''
    return [calc_nest_egg(monthly_saving, y, r) for y in range(0,total_years)]

monthly_savings = st.slider('Monthly Saving', 200, 6000, 1000, 200)
rate = st.slider('Rate', 1., 12., 7., 0.5)
total_years = st.slider('Years', 5, 40, 8) + 1

df = pd.DataFrame(
    data = {
        f'${savings} per month': 
            calc_nest_egg_over_time(savings,rate,total_years)
            for savings in range(1000,5_600,800)
    }
)

st.line_chart(df)