# add input
# update input
# delete input
"""
input {
 'id': String,
 'name : String,
 'value;: String,
 'active_mode_id': String,
 'active_mode': String,
 'inactive_mode_id': String,
 'inactive_mode': String
}
"""
from uuid import uuid4
from Database import Database

class Inputs:
    inputs = []

    def __init__(self):
        Database.initialize()
        self.load_all_input()

    def create_update_input(self, name, val, active_mode_id, active_mode, inactive_mode_id, inactive_mode, _id=None):
        if _id is None:
            # create input
            i = {
                '_id': str(uuid4()),
                'name': name,
                'value': val,
                'active_mode_id': active_mode_id,
                'active_mode': active_mode,
                'inactive_mode_id': inactive_mode_id,
                'inactive_mode': inactive_mode
            }
            Database.insert(collection='inputs', data=i)
            self.inputs.append(i)

        else:
            # update an existing input
            Database.update(collection='inputs', query={'_id': _id}, data={
                '_id': _id,
                'name': name,
                'value': val,
                'active_mode_id': active_mode_id,
                'active_mode': active_mode,
                'inactive_mode_id': inactive_mode_id,
                'inactive_mode': inactive_mode
            })
            self.load_all_input()

    def delete_input(self, _id):
        Database.delete(collection='inputs', query={'_id': _id})
        self.load_all_input()

    def load_all_input(self):
        self.inputs = []
        self.inputs = Database.load(collection='inputs')

    def get_input_by_name(self, name):
        for p in self.inputs:
            if p['name'] == name:
                return p

