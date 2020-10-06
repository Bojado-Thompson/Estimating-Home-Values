# Import libraries
import pandas as pd
from Acquire import get_mvp_home_data

# Function to prepare the data
def prep_zillow_df(df):
    # Dropped null values
    df = df.dropna()
    # Rename column names
    df = df.rename(columns = {'calculatedfinishedsquarefeet':'sqft'})
    df = df.rename(columns = {'bedroomcnt':'bedroom_count'})
    df = df.rename(columns = {'bathroomcnt':'bathroom_count'})
    df = df.rename(columns = {'taxvaluedollarcnt':'tax_value'}) 
    return df


# Function to split the data into train, validate, and test
def train_test_validate(df):   
# split into train, validate, and test sets
    train_and_validate, test = train_test_split(df, test_size = .10, random_state=123)
    train, validate = train_test_split(train_and_validate, test_size = .20, random_state=123)

    return train, validate, test