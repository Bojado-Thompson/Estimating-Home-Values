# Predicting Home Values for Zillow
## About the Project
### Goals
Zillow first launched in 2006. Since then, our company has accumulated a living database of more than 110 million US homes. Not only do we keep track of homes on the market, but off the market as well. What do we do with this data? One value we create is the [Zestimate®](https://www.zillow.com/zestimate/) - the estimate of a home's market value.  

The purpose of this project is determine what influences this value based on previous property data during the two months of high real estate demand - May and June.

Deliverables for this project include:
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
| parcelid                  | assigned by your local tax assessment office, unique for each property                                                                                           | discrete    |
| *sqft                     | squarefeet, length ft. x width ft.                                                                                                                               | continuous  |
| buildingclass             | description of wall structure, materials, etc. (1-5 or null)                                                                                                     | categorical |
| buildingqualitytypeid     | no description (1-12 or null)                                                                                                                                    | categorical |
| decktypeid                | no description (66 or null)                                                                                                                                      | categorical |
| finishedsqft*             | no description (1 - 290345)                                                                                                                                      | continuous  |
| fips                      | Federal Information Processing Standards (6037, 6059, 6111, or null) uniquely identify geographic areas                                                          | categorical |
| heatingorsystem           | description of air conditioning, such as energy source (1-25)                                                                                                    | categorical |
| latitude                  | distance of a place north or south of the earth's equator                                                                                                        | continuous  |
| longitude                 | distance of a place east or west of the meridian                                                                                                                 | continuous  |
| pooltypeid*               | no description (1 or null)                                                                                                                                       | categorical |
| propertycountylandusecode | Land use zones are the codes that the government uses to classify  parcels of land (chars with numbers)                                                          | discrete    |
| propertyzoningdesc        | zoning refers to municipal or local laws or regulations that dictate  how real property can and cannot be used in certain geographic areas  (chars with numbers) | discrete    |
| rawcensustractandblock    | census tracts are relatively small subdivisions of a county block group is a cluster of blocks within a tract                                                    | discrete    |
|                           |                                                                                                                                                                  |             |

The visual below takes a more in-depth look at the original database. We can see how the properties tables for 2016 and 2017 contain a majority of the data. These tables also have a whopping amount of 52 columns. Before prepping the data, we can use this visual to make ideas on which features we may not need, can be combined, etc.  
![zillow-database](https://i.pinimg.com/originals/ef/01/89/ef0189cace1f6e5626e1be0368370062.png)  

The descriptive tables shown below have various ranges of values and corresponding meanings. Though we will not be joining these tables during the aquire stage, it has been added for reference. Theses values in the main predictions tables will need to be scaled so they have the same weight.  
  
![zillow-desciptive-tables-with-values](https://i.pinimg.com/originals/85/c5/32/85c5323063cc33dcac255e045df3bd37.png)  

For better quality images, these visuals can also be found on my pinterest [here](https://www.pinterest.com/thompsonbethany01/estimating-home-values/).
## Initial Thoughts & Hypothesis
### Thoughts
Taking a surface look as the database, it is apparent feature engineering will be neccessary to create manageable exploration and modeling from the 52 columns. This may include...
- creating simpler features, such as story count being 1, 2, or more
- combining different features, such as 
- removing features with high null values
- removing unnecessary features, such as long. and latt. when we also have region ids
- scaling the final dataframe for modeling
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
## Prepare
## Explore
## Model
## Conclusion
# How to Reproduce