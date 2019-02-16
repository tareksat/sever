import requests
from controller import *


def get_node_data(name):
    try:
        n = get_node_by_name(name)
        if n['type'] == 'out':
            r = requests.get(url='http://{}.local:3000/get_all_enabled_ports'.format(name), verify=False, timeout=5)
            return r.json()
        else:
            r = requests.get(url='http://{}.local/get_all_enabled_ports'.format(name), verify=False)
            return r.json()
    except:
        try:
            r = requests.get(url='http://{}.local/get_all_enabled_ports'.format(name), verify=False, timeout=5)
            return r.json()
        except:
            print('Server not found')


def set_port_value(node_name, node_type, port_id, port_status):
    try:
        if node_type == 'out':
            r = requests.put(url='http://{}.local:3000/set_port_value'.format(node_name), verify=False, timeout=5,
                             json={'id': port_id, 'value': port_status})
        else:
            r = requests.get(url='http://{}.local/SET/id/{}/value/{}'.format(node_name, port_id, port_status),
                             verify=False, timeout=5)
        return True
    except:
        return False


def set_port_name(node_name, port_id, port_name):
    try:
        r = requests.put(url='http://{}.local:3000/update_port_name'.format(node_name), verify=False, timeout=5,
                         json={'id': port_id, 'name': port_name})
        return True
    except:
        return False
