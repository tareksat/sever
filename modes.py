"""
modes = {
    '_id',
    name,
    nodes:[
        {name, ports[{'id', name, 'value'}]
        }]
}
"""
from uuid import uuid4
from Database import Database
import requests
from controller import get_node_by_name

class Modes:
    modes = []

    def __init__(self):
        Database.initialize()
        self.load_modes()

    def load_modes(self):
        self.modes = []
        self.modes = Database.load(collection='modes')

    def get_mode_by_id(self, _id):
        mode = Database.find_by_id(collection='modes', query={'_id': _id})
        return mode

    def create_update_mode(self, _name, _nodes, _id=None):
        if _id is None:
            _id = str(uuid4())
            name = _name
            nodes = _nodes
            mode = {'_id': _id, 'name': name, 'nodes': nodes}
            self.modes.append(mode)
            Database.insert(collection='modes', data=mode)
        else:
            mode = Database.find_by_id(collection='modes', query={'_id': _id})
            mode['name'] = _name
            mode['nodes'] = _nodes
            Database.update(collection='modes', query={'_id': _id}, data=mode)
            self.load_modes()

    def delete_mode(self, _id):
        Database.delete(collection='modes', query={'_id': _id})
        self.load_modes()

    def activate_mode(self, _id):
        mode = Database.find_by_id(collection='modes', query={'_id': _id})
        for n in mode['nodes']:
            selected_node = get_node_by_name(n['name'])
            if selected_node['type'] == 'out':
                val_list = []
                for p in n['ports']:
                    val_list.append({'id': p['id'], 'value': p['value']})
                try:
                    requests.put(url='http://{}.local:3000/set_port_values'.format(n['name']), verify=False, timeout=5,
                                     json={'values': val_list})
                except:
                    print('server error')
            else:
                for p in n['ports']:
                    try:
                        requests.get(url='http://{}.local/SET/id/{}/value/{}'.format(n['name'], p['id'], p['value']),
                                     verify=False, timeout=5)
                    except:
                        print('server error')
