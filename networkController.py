from uuid import uuid4

def get_node_data(node_name):
    if node_name != 'Tarek':
        return{
           "id": str(uuid4()),
            "name": node_name ,
            "ports": [
                {
                    "enabled": "Enabled",
                    "id": "a553da5a-431a-4e1e-858d-2058d2aef2f4",
                    "name": "R-1",
                    "status": {
                        "B": 0,
                        "G": 0,
                        "R": 0,
                        "value": 1
                    },
                    "type": "OUT"
                },
                {
                    "enabled": "Enabled",
                    "id": "4fa0c6df-90dd-4f85-a4da-a902f570becb",
                    "name": "R-2",
                    "status": {
                        "B": 0,
                        "G": 0,
                        "R": 0,
                        "value": 0
                    },
                    "type": "OUT"
                },
                {
                    "enabled": "Enabled",
                    "id": "34d5377f-fc5f-4ecc-9fff-b4a3eaa84af9",
                    "name": "R-3",
                    "status": {
                        "B": 0,
                        "G": 0,
                        "R": 0,
                        "value": 1
                    },
                    "type": "OUT"
                },
                {
                    "enabled": "Enabled",
                    "id": "ef60570f-0fa8-4171-8783-ced46b8b690a",
                    "name": "R-4",
                    "status": {
                        "B": 0,
                        "G": 0,
                        "R": 0,
                        "value": 0
                    },
                    "type": "OUT"
                },
                {
                    "enabled": "Enabled",
                    "id": "81a20e94-07f0-4a9c-ba02-1b6374b297f1",
                    "name": "R-5",
                    "status": {
                        "B": 0,
                        "G": 0,
                        "R": 0,
                        "value": 1
                    },
                    "type": "OUT"
                },
                {
                    "enabled": "Enabled",
                    "id": "b6ac9450-0a95-4ec2-be77-e99e42a2bacf",
                    "name": "R-6",
                    "status": {
                        "B": 0,
                        "G": 0,
                        "R": 0,
                        "value": 0
                    },
                    "type": "OUT"
                },
                {
                    "enabled": "Enabled",
                    "id": "dbf8bc3e-bed3-4944-bf8b-4f3b659bce29",
                    "name": "S-1",
                    "status": {
                        "B": 0,
                        "G": 0,
                        "R": 0,
                        "value": 1
                    },
                    "type": "IN"
                },
                {
                    "enabled": "Enabled",
                    "id": "83ffa3f7-f875-4566-ba62-130ea98e8da6",
                    "name": "S-2",
                    "status": {
                        "B": 0,
                        "G": 0,
                        "R": 0,
                        "value": 1
                    },
                    "type": "IN"
                },
                {
                    "enabled": "Enabled",
                    "id": "91367a24-8bc1-48a3-a330-94e7087aad86",
                    "name": "S-3",
                    "status": {
                        "B": 0,
                        "G": 0,
                        "R": 0,
                        "value": 1
                    },
                    "type": "IN"
                },
                {
                    "enabled": "Enabled",
                    "id": "534f9395-daae-4473-97d8-f5476ddd0689",
                    "name": "S-4",
                    "status": {
                        "B": 0,
                        "G": 0,
                        "R": 0,
                        "value": 1
                    },
                    "type": "IN"
                },
                {
                    "enabled": "Enabled",
                    "id": "e813bcda-79ea-4d88-8f20-52ceb3e19686",
                    "name": "RGB",
                    "status": {
                        "B": 61,
                        "G": 61,
                        "R": 244,
                        "value": 0
                    },
                    "type": "RGB"
                },
                {
                    "enabled": "Enabled",
                    "id": "574eb619-d537-4a17-a7fe-c3b60021c939",
                    "name": "Dimmer",
                    "status": {
                        "B": 0,
                        "G": 0,
                        "R": 0,
                        "value": 111
                    },
                    "type": "dimmer"
                }
            ]

        }
    else:
        return None