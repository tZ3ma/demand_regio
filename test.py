# interpreter = C:\Users\ammon.hic\Code\Virtualenvironments\demand_regio\Scripts\python.exe
print("hello world")
from disaggregator import config

cfg = config.get_config(ruamel_yaml=False)
info = cfg['database_host']

print(info)

from disaggregator import data, plot

df_spatial = data.database_description('spatial', force_update=True)
example_df = df_spatial.head()

print(example_df)

dict_nuts3_name = config.dict_region_code(keys='natcode_nuts3', values='name')
dict_nuts3_name

print(dict_nuts3_name)