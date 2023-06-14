import json

def is_json(json_data):
    try:
        p_dict = json.loads(json_data)
        valid = True
    except ValueError:
        valid = False
    return valid