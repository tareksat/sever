from flask import Flask, request, jsonify
from flask_cors import CORS
from controller import *
from client import get_node_data
from modes import Modes
from inputs import Inputs
import os

inputs = Inputs()
modes = Modes()
Database.initialize()
load_nodes()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['POST'])
def update_node():
    data = request.get_json()
    insert_node(_id=data['id'], name=data['name'], node_type=data['type'], ports=data['ports'])
    return "OK"


@app.route('/get_node_names', methods=['GET'])
def get_node_headers():
    nodes = get_node_names()
    return jsonify({'nodes': nodes})


@app.route('/remove_node', methods=['POST'])
def delete_node():
    data = request.get_json()
    remove_node(data['id'])
    return 'OK'


@app.route('/get_node_ports', methods=['POST'])
def get_node_ports():
    data = request.get_json()
    index = get_node_index_by_id(data['id'])
    ports = nodeList[index]['ports']
    status = nodeList[index]['status']
    name = nodeList[index]['name']
    type = nodeList[index]['type']
    if status == 'online':
        return jsonify({'name': name, 'type': type, 'status': status, 'ports': ports})
    return jsonify({'name': name, 'type': type,'status': status, 'ports': ports})


@app.route('/get_node_ports_firstTime', methods=['POST'])
def get_node_ports_first_time():
    data = request.get_json()
    index = get_node_index_by_id(data['id'])
    x = get_node_data(nodeList[index]['name'])
    if x is not None:
        insert_node(_id=data['id'], name=nodeList[index]['name'], ports=x['ports'])
        return jsonify({'status': 'online', 'ports': x['ports']})
    else:
        set_node_status(data['id'], 'offline')
        return jsonify({'status': 'offline', 'ports': []})


@app.route('/set_port_value', methods=['POST'])
def set_port_status():
    data = request.get_json()
    x = set_port_value(data['node_name'], data['node_type'], data['port_id'], data['port_status'])
    if x:
        return 'Succeeded'
    return 'Failed'

# for small modules
@app.route('/add_small_node', methods=['POST'])
def update_node_module():
    data = request.get_json()
    small_node = {'name': data['name']}
    create_small_node(data['name'])
    return"ok"

@app.route('/create_mode', methods=['POST'])
def create_mode():
    data = request.get_json()
    modes.create_update_mode(_name=data['name'], _nodes=data['nodes'])
    return "OK"

@app.route('/get_mode', methods=['POST'])
def get_mode():
    data = request.get_json()
    mode = modes.get_mode_by_id(_id=data['id'])
    return jsonify({'mode': mode})


@app.route('/update_mode', methods=['POST'])
def update_mode():
    data = request.get_json()
    modes.create_update_mode(_id= data['id'], _name=data['name'], _nodes=data['nodes'])
    return "OK"


@app.route('/delete_mode', methods=['POST'])
def delete_mode():
    data = request.get_json()
    modes.delete_mode(_id=data['id'])
    return "OK"


@app.route('/load_modes', methods=['GET'])
def load_all_modes():
    return jsonify({'modes': modes.modes})


@app.route('/activate_mode', methods=['POST'])
def activate_mode():
    data = request.get_json()
    modes.activate_mode(_id=data['id'])
    return "OK"


@app.route('/load_inputs', methods=['GET'])
def load_all_inputs():
    return jsonify({'inputs': inputs.inputs})


@app.route('/create_input', methods=['POST'])
def create_input():
    data = request.get_json()
    if data['id'] == '':
        inputs.create_update_input(name=data['name'], val='0', active_mode_id=data['active_mode_id'],
                                   active_mode=data['active_mode'], inactive_mode_id=data['inactive_mode_id'],
                                   inactive_mode=data['inactive_mode'])
    else:
        inputs.create_update_input(name=data['name'], val='0', active_mode_id=data['active_mode_id'],
                                   active_mode=data['active_mode'], inactive_mode_id=data['inactive_mode_id'],
                                   inactive_mode=data['inactive_mode'], _id=data['id'])

    return "OK"


@app.route('/update_input', methods=['POST'])
def update_input():
    data = request.get_json()
    inputs.create_update_input(name=data['name'], val='0', active_mode_id=data['active_mode_id'],
                               active_mode=data['active_mode'], inactive_mode_id=data['inactive_mode_id'],
                               inactive_mode=data['inactive_mode'], _id=data['id'])
    return "OK"


@app.route('/delete_input', methods=['POST'])
def delete_input():
    data = request.get_json()
    inputs.delete_input(data['id'])
    return "OK"


@app.route('/handle_input', methods=['POST'])
def handle_input():
    data = request.get_json()
    i = inputs.get_input_by_name(data['name'])
    if data['value'] == '1':  # active input
        modes.activate_mode(i['active_mode_id'])
    else:
        modes.activate_mode(i['inactive_mode_id'])
    return "OK"

@app.route('/system_update')
def handle_input():
    os.system("git pull")
    return "OK"


app.run(host='0.0.0.0', port=3000)
