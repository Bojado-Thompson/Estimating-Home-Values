# Taking a look at the properties_2017 table as a whole
# 2,985,217 values
SELECT *
FROM properties_2017;

# 19,149 values
# Query for MVP, only includes square feet, bedroom, and bathroom as X features 
# Narrows down to "Hot" months of May and July
SELECT prop.id, calculatedfinishedsquarefeet, bedroomcnt, bathroomcnt, taxvaluedollarcnt
FROM properties_2017 as prop
JOIN propertylandusetype as land ON prop.propertylandusetypeid = land.propertylandusetypeid
JOIN predictions_2017 as pred ON pred.id = prop.id 
	AND (pred.transactiondate LIKE '2017-06-%'
	OR pred.transactiondate LIKE '2017-07-%')
WHERE prop.propertylandusetypeid IN (260, 261, 263, 264, 266, 279);

# 2,699,253 values
# Query for MVP, only includes square feet, bedroom, and bathroom as X features
SELECT id, calculatedfinishedsquarefeet, bedroomcnt, bathroomcnt, taxvaluedollarcnt
FROM properties_2017 as prop
JOIN propertylandusetype as land ON prop.propertylandusetypeid = land.propertylandusetypeid
JOIN 
WHERE prop.propertylandusetypeid IN (260, 261, 263, 264, 266, 279);

# Checking null values in features used in MVP query
# 45,097 null in squarefeet
SELECT COUNT(*)
FROM properties_2017
WHERE calculatedfinishedsquarefeet is null;

# 2,945 null in bedroom counts
SELECT COUNT(*)
FROM properties_2017
WHERE bedroomcnt is null;

# 2,957 in bathroom
SELECT COUNT(*)
FROM properties_2017
WHERE bathroomcnt is null;

# Determining which ID's to include in query, only need single unit properties
# Joining propertylandusetype table for single use properties
SELECT land.propertylandusetypeid, propertylandusedesc as property_description, COUNT(land.propertylandusetypeid) as house_count
FROM properties_2017 as prop
JOIN propertylandusetype as land ON prop.propertylandusetypeid = land.propertylandusetypeid
GROUP BY land.propertylandusetypeid;

SELECT prop.id as property_id, prop.fips as county_id, prop.latitude, prop.longitude, prop.taxamount, prop.taxvaluedollarcnt 
FROM properties_2017 as prop
JOIN predictions_2017 as pred ON pred.id = prop.id 
	AND (pred.transactiondate LIKE '2017-06-%'
	OR pred.transactiondate LIKE '2017-07-%')
WHERE prop.propertylandusetypeid IN (260, 261, 263, 264, 266, 279);
