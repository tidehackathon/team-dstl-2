import json
import os
import pprint

path_to_dashboard_json = os.path.join(
    "dashboards", 
    "Dashboard_for_Interoperability-1676974127650.json"
    )

f = open(path_to_dashboard_json)
         
dashboard_dict = json.load(f)

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(dashboard_dict["panels"][1])

# Test adding a new panel
new_panel_dict = {'test': 'test'}

f.close()