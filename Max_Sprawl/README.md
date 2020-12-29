# REMM Max Sprawl Scenario

## Adjusted Redevelopment Friction:

The redevelopment friction file (redev_friction.csv) contains a list of parcels and a friction factor that is applied to the cost of redeveloping that parcel. 

I obtained all of the parcel ids from the base year data file and added them to file. Each parcel id in the file, existing and new, was given a friction factor of 100,000 to strongly discourage redevelopment on that parcel.

## Adjusted Policy Layer:

The scenario input or policy layer (zoning_parcels_p.csv) contains information about parcels within defined developments such as urban centers and staging areas. 

Agricultural parcels within this planning scenario were previously set to become available post 2035. The development year on these parcels were lowered to 2025 to encourage sooner development. Additionally, agricultural polygons from the Water-Related Land Use dataset were used to spatially select additional parcels from the REMM parcel dataset and add them to the policy layer (also becoming available in 2025). Parcels that intersected with the Utah Lake TAZ boundary were removed.

All agricultural parcels that had a null value for the Maximum Dwelling Units per Acre (MAX_DUA) attribute were given an assumed value of 3.5.

Parcels in the policy layer that were located within the “urban centers” were identified and removed to encourage more sprawl. These parcels were identified using WFRC’s Regionally Significant Centers and Land Use dataset.

## Deliverables:

To account for randomness, the model was run five times and the results were averaged using the pandas library in python. The outputs files are both spatial and nonspatial and include:

- SE tables in csv format (TDM-ready) for 2015, 2020, 2030, 2040, 2050
- a geodatabase containing:
	- The SE output in feature dataset form (filter by year using definition query)
	- SE Output 2050 (Max Sprawl) minus SE Output 2050 (Normal Run)
	- SE Output 2050 (Max Sprawl) minus SE Output 2015 (Base year)
