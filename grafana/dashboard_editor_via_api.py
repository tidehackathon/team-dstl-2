import json
import requests

def panel_input_sql_output_table(sql_input):
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
        'gridPos': {'h': 8, 'w': 12, 'x': 0, 'y': 0}, 
        'id': 4, 
        'options': {'footer': {'fields': '', 'reducer': ['sum'], 'show': False}, 'showHeader': True}, 
        'pluginVersion': '9.3.6', 
        'targets': [
            {
                'datasource': {'type': 'postgres', 'uid': 'P44368ADAD746BC27'}, 
                'editorMode': 'code', 
                'format': 'table', 
                'rawQuery': True, 
                'rawSql': sql_input, 
                'refId': 'A', 
                'sql': {'columns': [{'parameters': [], 'type': 'function'}], 
                        'groupBy': [{'property': {'type': 'string'}, 'type': 'groupBy'}], 'limit': 50}
            }
            ], 
        'title': 'Panel Title', 
        'type': 'table'
        }
    
    return panel_dict

def add_panel_to_dashboard(sql_input, dashboard_dict):
    dashboard_dict['dashboard']['panels'].append(
        panel_input_sql_output_table(sql_input)
    )

    new_dashboard = dashboard_dict
    print("Number of panels : ", len(new_dashboard['dashboard']['panels']))

    return new_dashboard

def get_dashboard(username, password, ip_addr, port, dashboard_uid):
    grafana_url = 'http://{username}:{password}@{ip_addr}:{port}'.format(
        username = username,
        password = password,
        ip_addr = ip_addr,
        port = port
    )

    dashboard_get_json_endpoint = '/api/dashboards/uid/'

    request_target = grafana_url + dashboard_get_json_endpoint + dashboard_uid
    response = requests.get(request_target)
    print(response)

    response_json = json.loads(response.text)
    print(response_json)

    return response_json

def update_dashboard_on_grafana(username, password, ip_addr, port, dashboard_dict):
    grafana_url = 'http://{username}:{password}@{ip_addr}:{port}'.format(
        username = username,
        password = password,
        ip_addr = ip_addr,
        port = port
    )
    
    headers = {
        'Content-Type': 'application/json',
    }

    dashboard_update_endpoint = '/api/dashboards/db'

    response = requests.post(
        grafana_url + dashboard_update_endpoint,
        headers=headers,
        data=json.dumps(dashboard_dict)
    )

    print(response)


if __name__ == "__main__":
    dashboard_uid = '1MB0c91Vz'

    # Grafana host details
    username = 'admin'
    password = 'qwerty'
    ip_addr = 'grafana' # with docker compose, the ip_addr is just the name of the service
    port = '3000'

    # Get dashboard json and load into dictionary
    dashboard = get_dashboard(username, password, ip_addr, port, dashboard_uid)

    # Add new panel to dashboard
    dashboard = add_panel_to_dashboard(
        'SELECT * FROM capability_tasks',
        dashboard
        )

    # Create new panel in the dashboard
    update_dashboard_on_grafana(username, password, ip_addr, port, dashboard)
    