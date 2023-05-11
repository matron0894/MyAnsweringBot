import pandas as pd

def create_series(foods, calories):
    # write your code here ....
    return pd.Series(calories, index=foods, name="Calorie content")