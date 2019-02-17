from Database import Database
from client import *
from uuid import uuid4

nodeList = []

######################################  Database section  ##############################################################


def insert(_id, name, node_type):
    if Database.find_by_id(collection='nodes', query={'_id': _id}) is None:
        Database.insert(collection='nodes', data={'_id': _id, 'name': name, 'type': node_type})
    else:
        Database.update(collection='nodes', query={'_id': _id}, data={'_id': _id, 'name': name, 'type': node_type})


def delete(_id):
    Database.delete(collection='nodes', query={'_id': _id})


def load_all():
    nodes = Database.load(collection='nodes')
    return nodes


###########################################   Node list section   ######################################################

def load_nodes():
    #nodeList = []
    nodes = load_all()
    for node in nodes:
        n = get_node_data(node['name'])
        if n is not None:
            nodeList.append({
                'id': node['_id'],
                'name': node['name'],
                'status': 'online',
                'type': node['type'],
                'ports': n['ports']
            })
        else:
            nodeList.append({
                'id': node['_id'],
                'name': node['name'],
                'status': 'offline',
                'type': node['type'],
                'ports': []
            })


def get_node_index_by_id(_id):
    for i in range(0, len(nodeList)):
        if nodeList[i]['id'] == _id:
            return i

    return -1


def insert_node(_id, name, ports, node_type):
    index = get_node_index_by_id(_id)
    if index != -1:                             # node already exists in nodeList
        if nodeList[index]['name'] == name:     # Node name did not change
            nodeList[index]['ports'] = ports    # just update ports
            nodeList[index]['status'] = 'online' ,
            nodeList[index]['type'] = node_type
        else:                                   # node name had been changed
            nodeList[index]['name'] = name      # update nodeList with the new node name
            insert(_id, name, node_type)                   # update Database with the new node name
            nodeList[index]['ports'] = ports
            nodeList[index]['status'] = 'online'
    else:                                       # node does not exists in node list
        nodeList.append({
            'id': _id,
            'name': name,
            'status': 'online',
            'ports': ports,
            'type': node_type
        })
        insert(_id, name, node_type )


def set_node_status(_id, status):
    index = get_node_index_by_id(_id)
    nodeList[index]['status'] = status


def remove_node(_id):
    node_index = get_node_index_by_id(_id)
    del nodeList[node_index]
    delete(_id)


def get_node_names():
    n = []
    for node in nodeList:
        n.append({'id': node['id'], 'name': node['name'], 'status': node['status'], 'type': node['type']})
    return n

def get_node_by_name(name):
    for node in nodeList:
        if node['name'] == name:
            return node


def create_small_node(node_name):
    node = get_node_data(node_name)
    for i in range(0, len(node['ports'])):
        node['ports'][i]['value'] = str(node['ports'][i]['value'])

    insert(_id=node['id'], name=node_name, node_type=node['type'])
    insert_node(_id=node['id'], name=node_name, ports=node['ports'], node_type=node['type'])
    load_nodes
