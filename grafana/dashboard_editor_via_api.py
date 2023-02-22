import json
import requests
import pprint

def panel_input_sql_output_table():
    panel_dict = {
        'datasource': {'type': 'postgres', 'uid': 'P44368ADAD746BC27'}, 
        'fieldConfig': {
            'defaults': {'color': {'mode': 'thresholds'}, 
                    'custom': {'align': 'auto', 'displayMode': 'auto', 'inspect': False}, 
                    'mappings': [], 
                    'thresholds': {'mode': 'absolute', 'steps': [{'color': 'green', 'value': None}, {'color': 'red', 'value': 80}]}
                }, 
            'overrides': []
        }, 
        'gridPos': {'h': 8, 'w': 12, 'x': 12, 'y': 0}, 
        'id': 4, 
        'options': {'footer': {'fields': '', 'reducer': ['sum'], 'show': False}, 'showHeader': True}, 
        'pluginVersion': '9.3.6', 
        'targets': [
            {
                'datasource': {'type': 'postgres', 'uid': 'P44368ADAD746BC27'}, 
                'editorMode': 'code', 
                'format': 'table', 
                'rawQuery': True, 
                'rawSql': 'SELECT * FROM operational_domains ', 
                'refId': 'A', 
                'sql': {'columns': [{'parameters': [], 'type': 'function'}], 
                        'groupBy': [{'property': {'type': 'string'}, 'type': 'groupBy'}], 'limit': 50}
            }
            ], 
        'title': 'Panel Title', 
        'type': 'table'
        }
    
    return panel_dict

dashboard_uid = '1MB0c91Vz'
grafana_url = 'http://admin:qwerty@localhost:3000'.rstrip()

dashboard_update_endpoint = '/api/dashboards/db'
dashboard_get_json = '/api/dashboards/uid/'

# Get dashboard json and load into dictionary.

headers = {
    'Content-Type': 'application/json',
}

print(grafana_url + dashboard_get_json + dashboard_uid)
response = requests.get(
    grafana_url + dashboard_get_json + dashboard_uid
    )

print(response)

response_json = json.loads(response.text)

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(response_json)

print(response_json)

panel1 = response_json['dashboard']['panels'][1]

print(panel1)

panel_template = panel1