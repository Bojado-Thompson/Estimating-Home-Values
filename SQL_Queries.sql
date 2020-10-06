# Taking a look at the properties_2017 table as a whole
# 2,985,217 values
SELECT *
FROM properties_2017;

# 2,699,253 values
# Query for MVP, only includes square feet, bedroom, and bathroom as X features
SELECT id, calculatedfinishedsquarefeet, bedroomcnt, bathroomcnt, taxvaluedollarcnt
FROM properties_2017 as prop
JOIN propertylandusetype as land ON prop.propertylandusetypeid = land.propertylandusetypeid
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