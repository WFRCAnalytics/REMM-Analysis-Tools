sim.step("dev_tracking")



# get all buildings

	# identify all parcels that have buildings on them
	
	# identify parcels that don't have buildings on them

# get parcels
	
	# get list of all parcels

	# add column (land_developed)
		- if parcel has no buildings developed land is 0
		- if parcel has a building on it, developed land is total parcel acreage


	# add column(new building type)
	
	# add column
	
	
# get new buildings
 - identify which parcels have a new building and what type they are


- do types later
- dont know if allbuildings get updated (if redevelopment occurs) or if it contains full history of buildings
- older buildings get overwritten, need to access building from previous year, try to access cache first


base table (beginning year):
-------------------------------------
parcel_id', 'parcel_id_REMM', 'county_id', 'zone_id','parcel_acres',  'land_value', 'land_cost', 'max_far', 'max_dua', 'residential_units', 'job_spaces', 'building_sqft', 'residential_sqft',  'building_count' , 'hasBuildings', 'wasDeveloped', 'wasRedeveloped'

every year table (e.g.2015):
--------------------------------------
parcel_id', 'parcel_id_REMM', 'county_id', 'zone_id','parcel_acres',  'land_value', 'land_cost', 'max_far', 'max_dua', 'residential_units', 'job_spaces', 'building_sqft', 'residential_sqft',  'building_count', 'hasBuildings', 'wasDeveloped', 'wasRedeveloped', 'new_res_units', 'new_job_spaces', 'acreage_dev', 'acreage_redev', 'new value'

'res_units_added' = postsim res units - presim res units
'job_spacesres_units_added' = postsim job spaces - presim job spaces
'acreage_dev'  = parcel acreage, if 'wasDeveloped' == True
'acreage_redev'  =  parcel acreage, if 'wasRedeveloped' == True
'value_added_dev' = (land value + postsim improvement value) - (land value), if 'wasDeveloped' == True
'value_added_redev'= (land value + postsim improvement value) - (land value + presim improvement value), if 'wasRedeveloped' == True