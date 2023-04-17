import pandas as pd
import numpy as np

def load_passengers():
    # Load the Titanic dataset
    df = pd.read_csv('data/titanic.csv')

    # Select only the female passengers
    female_passengers = df[df['Sex'] == 'female']

    return female_passengers
