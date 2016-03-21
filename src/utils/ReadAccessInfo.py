import json

'''
'''

access_file = 'data/access_keys.json'

def get_access_info(index=5):
    with open(access_file) as f:
        data = f.read()
        data = json.loads(data)

        access_obj_list = []
        for item in data:
            access_obj = {}
            for entry in data[item]:
                access_obj_list.append(entry)
        
        return access_obj_list[index]

