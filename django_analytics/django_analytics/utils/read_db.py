import pandas as pd
from .models import Cars

def csv_to_db():
    df = pd.read_csv("data/cars_dataset.csv")
    
    records = df.to_records()
    
    for record in records:
        pass

