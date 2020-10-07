# Predicting Home Values for Zillow
## About the Project
Zillow first launched in 2006. Since then, our company has accumulated a living database of more than 110 million US homes. Not only do we keep track of homes on the market, but off the market as well. What do we do with this data? One value we create is the [Zestimate®](https://www.zillow.com/zestimate/) - the estimate of a home's market value.  

### Goals
The purpose of this project is determine what influences this value based on previous property data during the two months of high real estate demand - May and June.  

We want to be able to predict :
- Key Drivers of market value for single unit properties
- Distribution of tax rates for each county

### Deliverables:
> - Final model created to predict the values of single unit properties that the tax district assesses
> - A reproducable Github repo containing
>   - Walkthrough of the DS pipeline within a jupyter notebook
>   - Acquire/Prepare modules in .py files
> - In a seperate presentation (adding link when complete), answers for the
>   - States and counties properties are located in
>   - Distribution of tax rates for each county

### Background

How does the current Zestimate® perform? According to [FreeStoneProperties](https://www.freestoneproperties.com/blog/truth-zillow-zestimates/#:~:text=Is%20a%20Zillow%20Zestimate%20High,about%20the%20accuracy%20of%20Zestimates.&text=For%20example%2C%20depending%20on%20the,only%2062%25%20of%20the%20time.),
> "The median error for larger markets is usually around 2% of the sale price of the home. But the problem with Zestimates is 
> that when they are wrong, they can be significantly wrong. For example, depending on the metro area, Zillow might be within 5% 
> of the sale price only 62% of the time."    

### Data Dictionary
The main tables within the Zillow database are predictions_2016 and predictions_2017. These contain the observations of each house: the tax value and several different features of the house. The data definition table is below.

| Feature                   | Definition                                                                                                                                                       | Type        |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| parcelid                  | Assigned by your local tax assessment office, unique for each property                                                                                           | discrete    |
| calculatedfinishedsquarefeet                    | Square feet: length (ft.) x width (ft.)      | continuous  |  
| bedroomcnt                   | Number of bedrooms in a unit      | discrete  |  
| bathroomcnt                   | Number of bathrooms in a unit      | discrete  | 
| taxvaluedollarcnt                   | Property taxes of unit for the year      | continuous  | 
| fips                      | Federal Information Processing Standards (6037, 6059, 6111, or null) uniquely identify geographic areas                                                          | categorical |
| latitude                  | Distance of a place north or south of the earth's equator                                                                                                        | continuous  |
| longitude                 | Distance of a place east or west of the meridian                                                                                                                 | continuous  |
| propertycountylandusecode | Land use zones are the codes that the government uses to classify  parcels of land (chars with numbers)                                                          | discrete    |
| propertyzoningdesc        | Zoning refers to municipal or local laws or regulations that dictate  how real property can and cannot be used in certain geographic areas  (chars with numbers) | discrete    |


The visual below takes a more in-depth look at the original database. We can see how the properties tables for 2016 and 2017 contain a majority of the data. These tables also have a whopping amount of 52 columns. Before prepping the data, we can use this visual to make ideas on which features we may not need, can be combined, etc.  
![zillow-database](https://i.pinimg.com/originals/ef/01/89/ef0189cace1f6e5626e1be0368370062.png)  

The descriptive tables shown below have various ranges of values and corresponding meanings. Though we will not be joining these tables during the aquire stage, it has been added for reference. Theses values in the main predictions tables will need to be scaled so they have the same weight.  
  
![zillow-desciptive-tables-with-values](https://i.pinimg.com/originals/85/c5/32/85c5323063cc33dcac255e045df3bd37.png)  

For better quality images, these visuals can also be found on my pinterest [here](https://www.pinterest.com/thompsonbethany01/estimating-home-values/).
## Initial Thoughts & Hypothesis
### Thoughts
Taking a surface look as the database, it is apparent feature engineering will be neccessary to create manageable exploration and modeling from the 52 columns. This may include...
- Creating simpler features, such as story count being 1, 2, or more
- Combining different features, such as 
- Removing features with high null values
- Removing unnecessary features, such as long. and latt. when we also have region ids
- Scaling the final dataframe for modeling
### Hypothesis
More square footage increases value  
> Null hypothesis: House square footage is independent of the tax value  
> Alternative hypothesis: The larger the square feet, the greater the tax value  

Older and younger houses have higher values (or could this be like a reverse bell curve? Old houses have historic value and new houses have value?)  
> Null hypothesis: The age of the house is independent of the tax value  
> Alternative hypothesis: Newer houses have higher tax values  

Location affects property value  
> Null hypothesis: The location of the house is independent of the tax values  
> Alternative hypothesis: One county has higher tax values than the average  

# Project Steps
## Acquire
- Data was aquired from the Zillow SQL Database.
- Login credentials are required.
- The functions are stored in the Acquire.py file.
- File is a reproducible component for gathering the data.

## Prepare
- Created a prep.py file. 
- Data is split into train, validate, and test. 
- Dataset is ready to be analyzed.
- Data is scaled as necessary.
- Erroneous or invalid data is identified.
- File is a reproducible component that handles missing values, fixes data integrity issues, changes data types, and scales data.

## Explore
- Run at least 1 t-test and 1 correlation test.
- Visualize all combinations of variables in some way(s).
- What independent variables are correlated with the dependent?
- Which independent variables are correlated with other independent variables?

Summarized your takeaways and conclusions.

## Model
- Developed a regression model that performs better than a baseline.
- Extablished a baseline model.
- Documented various algorithms and/or hyperparameters.
- Plotted the residuals, computed the evaluation metrics (SSE, RMSE, and/or MSE), compared to baseline, and plotted y by ^y.
- Created a model.py file as 
- File is a reproducible component that will have the functions to fit, predict and evaluate the final model on the test data set.

## Conclusion
Key Drivers of market value for single unit properties are (listed from highest correlation to lowest):
- Square footage of property
- Bathroom count
- Bedrooms count  

Observations:
- Most units are 3 bedrooms/ 2 bath
- Whether a property has a garage, it greatly affects that total square footage
- Three counties were listed in database:
    - Los Angeles County
    - Orange County
    - Ventura County
- Orange County has the highest average tax value for properties
- Los Angeles County has the most amount of properties

# How to Reproduce
All files are reproducible and available for download and use. 
- Acquire.py
- Prepare.py
- Final_Report.ipynb
- Must use login credentials to access Zillow database

# Contact Us 
Bethany Thompson
- thompson.bethany.01@gmail.com

Dani Bojado
- daniella.bojado@gmail.com 