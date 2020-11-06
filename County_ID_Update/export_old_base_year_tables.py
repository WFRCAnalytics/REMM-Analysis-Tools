"""  
This code works on the modeling computers since they have an old version of pandas
"""

import pandas as pd

store =pd.HDFStore(r"C:\REMM\data\remm_data_2015_base_year_02082019.h5")

store['buildings'].to_csv(r'E:\REMM_Input_Dump\buildings.csv')
store['buildings_for_estimation'].to_csv(r'E:\REMM_Input_Dump\buildings_for_estimation.csv')
store['buildings_for_estimation_grouped'].to_csv(r'E:\REMM_Input_Dump\buildings_for_estimation_grouped.csv')
store['employment_controls'].to_csv(r'E:\REMM_Input_Dump\employment_controls.csv')
store['households'].to_csv(r'E:\REMM_Input_Dump\households.csv')
store['household_controls'].to_csv(r'E:\REMM_Input_Dump\household_controls.csv')
store['household_for_estimation'].to_csv(r'E:\REMM_Input_Dump\household_for_estimation.csv')
store['households_for_estimation'].to_csv(r'E:\REMM_Input_Dump\households_for_estimation.csv')
store['households_for_estimation1'].to_csv(r'E:\REMM_Input_Dump\households_for_estimation1.csv')
store['jobs'].to_csv(r'E:\REMM_Input_Dump\jobs.csv')
store['parcels'].to_csv(r'E:\REMM_Input_Dump\parcels.csv')
store['travel_data'].to_csv(r'E:\REMM_Input_Dump\travel_data.csv')
store['valid_parcels'].to_csv(r'E:\REMM_Input_Dump\valid_parcels.csv')
store['zoning'].to_csv(r'E:\REMM_Input_Dump\zoning.csv')
store['zoning_base_line'].to_csv(r'E:\REMM_Input_Dump\zoning_base_line.csv')
store['zoning_baseline'].to_csv(r'E:\REMM_Input_Dump\zoning_baseline.csv')
store['zoning_for_parcels'].to_csv(r'E:\REMM_Input_Dump\zoning_for_parcels.csv')

print("done!")
