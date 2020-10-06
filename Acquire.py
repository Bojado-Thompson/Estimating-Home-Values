# Data is aquired from the company SQL Database, login credentials are required  

#################################### Function Imports ##############################################

# OS allows us to check if the data is already stored on our computer
import os
# Pandas reads the data into the variable
import pandas as pd
# Holds login credentials for SQL Database in a seperate file not added to GitHub
# env should only be stored locally on your computer
# Add to your .gitignore file to ensure credentials not compromised by uploading online
from env import host, username, password

#################################### SQL Connection Function ##############################################

# Function uses Login credentials to create a connection to the company SQL database
# NOTE: BE SURE NOT TO ADD YOUR CREDENTIALS TO GITHUB WHEN RECREATING THE PROJECT
def get_db_url(db_name):

    '''
    Connect to the SQL database with credentials stored in env file.
    Function parameter is the name of the database to connect to.
    Returns url.
    '''
    
    # Creates the url and the function returns this url
    url = f'mysql+pymysql://{username}:{password}@{host}/{db_name}'
    return (url)

#################################### Acquire Zillow Home Data ##############################################

# Function connects to the SQL database to store the data in a variable which can be used throughout the project
# Saves the data as a .csv file, returns as a pandas data frame
def get_home_data():

    '''
    Connect to SQL Database with url function called within this function.
    Checks if database is already saved to computer in csv file.
    If no file found, saves to a csv file and assigns database to df variable.
    If file found, just assigns database to df variable.
    Returns df variable holding the  Home Value database.
    Includes all 52 Columns.
    '''
    
    # data_name allows the function to work no matter what a user might have saved their file name as
    # First, we check if the data is already stored in the computer
    # First conditional runs if the data is not already stored in the computer
    if os.path.isfile('zillow_home.csv') == False:

        # Querry selects the whole predicstion_2017 table from the database
        sql_querry = '''
                        SELECT *
                        FROM properties_2017
                        ;
                    '''

        # Connecting to the data base and using the query above to select the data
        # the pandas read_sql function reads the query into a DataFrame
        df = pd.read_sql(sql_querry, get_db_url('zillow'))

        # If any duplicates found, this removes them
        # df.columns.duplicated() returns a boolean array, True for a duplicate or False if it is unique up to that point
        # Use ~ to flip the booleans and return the df as any columns that are not duplicated
        # df.loc accesses a group of rows and columns by label(s) or a boolean array
        df = df.loc[:,~df.columns.duplicated()]

        # The pandas to_csv function writes the data frame to a csv file
        # This allows data to be stored locally for quicker exploration and manipulation
        df.to_csv('zillow_home.csv')

    # This conditional runs if the data has already been saved as a csv (if the function has already been run on your computer)
    else:
        # Reads the csv saved from above, and assigns to the df variable
        df = pd.read_csv('zillow_home.csv', index_col=0)

    return df


#################################### Acquire Zillow MVP Home Data ##############################################

# Function connects to the SQL database to store the data in a variable which can be used throughout the project
# Saves the data as a .csv file, returns as a pandas data frame
def get_mvp_home_data():

    '''
    Connect to SQL Database with url function called within this function.
    Checks if database is already saved to computer in csv file.
    If no file found, saves to a csv file and assigns database to df variable.
    If file found, just assigns database to df variable.
    Returns df variable holding the  Home Value database for the MVP.
    ID, bedroom/bathroom count, and taxvaluedollarcnt
    '''
    
    # data_name allows the function to work no matter what a user might have saved their file name as
    # First, we check if the data is already stored in the computer
    # First conditional runs if the data is not already stored in the computer
    if os.path.isfile('zillow_home_mvp.csv') == False:

        # Querry selects the whole dataframe, joining each table on their foreign keys
        # We will have double columns on the foreign keys because they are joined together
        sql_querry = '''
                        SELECT id, calculatedfinishedsquarefeet, bedroomcnt, bathroomcnt, taxvaluedollarcnt
                        FROM properties_2017 as prop
                        JOIN propertylandusetype as land ON prop.propertylandusetypeid = land.propertylandusetypeid
                        WHERE prop.propertylandusetypeid IN (260, 261, 263, 264, 266, 279);
                    '''

        # Connecting to the data base and using the query above to select the data
        # the pandas read_sql function reads the query into a DataFrame
        df = pd.read_sql(sql_querry, get_db_url('zillow'))

        # Removes duplicates if any
        # df.columns.duplicated() returns a boolean array, True for a duplicate or False if it is unique up to that point
        # Use ~ to flip the booleans and return the df as any columns that are not duplicated
        # df.loc accesses a group of rows and columns by label(s) or a boolean array
        df = df.loc[:,~df.columns.duplicated()]

        # The pandas to_csv function writes the data frame to a csv file
        # This allows data to be stored locally for quicker exploration and manipulation
        df.to_csv('zillow_home_mvp.csv')

    # This conditional runs if the data has already been saved as a csv (if the function has already been run on your computer)
    else:
        # Reads the csv saved from above, and assigns to the df variable
        df = pd.read_csv('zillow_home_mvp.csv', index_col=0)

    return df




########################################### Get Location Home Data ####################################################
def get_home_location():

    '''
    Connect to SQL Database with url function called within this function.
    Checks if database is already saved to computer in csv file.
    If no file found, saves to a csv file and assigns database to df variable.
    If file found, just assigns database to df variable.
    Returns df variable holding the  Home Value database.
    '''
    
    # data_name allows the function to work no matter what a user might have saved their file name as
    # First, we check if the data is already stored in the computer
    # First conditional runs if the data is not already stored in the computer
    if os.path.isfile('zillow_location.csv') == False:

        # Querry selects the whole dataframe, joing each table on their foriegn keys
        # We will have double columns on the foriegn keys because they are joined together
        sql_querry = '''
                        SELECT id as property_id, fips as county_id, latitude, longitude, taxamount, taxvaluedollarcnt 
                        FROM properties_2017
                        WHERE fips is not null 
                        AND latitude is not null 
                        AND longitude is not null 
                        AND taxamount is not null 
                        AND taxvaluedollarcnt is not null;
                    '''

        # Connecting to the data base and using the querry above to select the data
        # the pandas read_sql function reads the query into a DataFrame
        df = pd.read_sql(sql_querry, get_db_url('zillow'))

        # Removes duplicates if any
        # df.columns.duplicated() returns a boolean array, True for a duplicate or False if it is unique up to that point
        # Use ~ to flip the booleans and return the df as any columns that are not duplicated
        # df.loc accesses a group of rows and columns by label(s) or a boolean array
        df = df.loc[:,~df.columns.duplicated()]

        # The pandas to_csv function writes the data frame to a csv file
        # This allows data to be stored locally for quicker exploration and manipulation
        df.to_csv('zillow_location.csv')

    # This conditional runs if the data has already been saved as a csv (if the function has already been run on your computer)
    else:
        # Reads the csv saved from above, and assigns to the df variable
        df = pd.read_csv('zillow_location.csv', index_col=0)

    return df