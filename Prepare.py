# Import libraries
import pandas as pd
from Acquire import get_mvp_home_data
from scipy import stats

# Function to prepare the data
def prep_zillow_df(df):
    # Drop id column 
    df = df.drop('id',axis=1)
    # Drop null values
    df = df.dropna()
    # Rename column names
    df = df.rename(columns = {'calculatedfinishedsquarefeet':'sqft'})
    df = df.rename(columns = {'bedroomcnt':'bedroom_count'})
    df = df.rename(columns = {'bathroomcnt':'bathroom_count'})
    df = df.rename(columns = {'taxvaluedollarcnt':'tax_value'}) 
    return df


# Function to split the data into train, validate, and test
def train_test_validate(df): 
    # Import to use split function, can only split two at a time
    from sklearn.model_selection import train_test_split 

    # split into train, validate, and test sets
    train_and_validate, test = train_test_split(df, test_size = .10, random_state=123)
    train, validate = train_test_split(train_and_validate, test_size = .20, random_state=123)

    # These two print functions allow us to ensure the date is properly split
    # Will print the shape of each variable when running the function
    print("train shape: ", train.shape, ", validate shape: ", validate.shape, ", test shape: ", test.shape)

    # Will print the shape of eachvariable as a percentage of the total data set
    # Varialbe to hold the sum of all rows (total observations in the data)
    total = df.count()[0]
    print("\ntrain percent: ", round(((train.shape[0])/total),2) * 100, 
            ", validate percent: ", round(((validate.shape[0])/total),2) * 100, 
            ", test percent: ", round(((test.shape[0])/total),2) * 100)
    return train, validate, test 

# Removing outliers
# outliers will be any value that is more than 3 standdard deviations from the average
threshold = 3
# print(np.where(z > 3))
Q1 = train.quantile(0.25)
Q3 = train.quantile(0.75)
IQR = Q3 - Q1
train_o = train[(z < 3).all(axis=1)]


# Scaling
# 1. Create the Scaling Object
scaler = sklearn.preprocessing.StandardScaler()

# 2. Fit to the train data only
scaler.fit(train.drop('tax_value', axis=1))

# 3. use the object on the whole df
# this returns an array, so we convert to df in the same line
train_scaled = pd.DataFrame(scaler.transform(train.drop('tax_value', axis=1)))
validate_scaled = pd.DataFrame(scaler.transform(validate.drop('tax_value', axis=1)))
test_scaled = pd.DataFrame(scaler.transform(test.drop('tax_value', axis=1)))

# the result of changing an array to a df resets the index and columns
# for each train, validate, and test, we change the index and columns back to original values

# Train
train_scaled.index = train.index
train_scaled.columns = ['bath_count_scaled','bed_count_scaled','square_feet_scaled']
train = pd.concat((train, train_scaled), axis=1)

# Validate
validate_scaled.index = validate.index
validate_scaled.columns = ['bath_count_scaled','bed_count_scaled','square_feet_scaled']
validate = pd.concat((validate, validate_scaled), axis=1)

# Test
test_scaled.index = test.index
test_scaled.columns = ['bath_count_scaled','bed_count_scaled','square_feet_scaled']
test = pd.concat((test, test_scaled), axis=1)
