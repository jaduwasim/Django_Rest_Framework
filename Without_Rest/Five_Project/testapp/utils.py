import json

def is_json(json_string):
    try:
        p_dict = json.loads(json_string)
        valid = True
    except ValueError:
        valid = False
    return valid