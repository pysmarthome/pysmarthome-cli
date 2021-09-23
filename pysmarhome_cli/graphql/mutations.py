import json
dev_mutation = lambda id, action, *args: f'''
    mutation {{
        device_action(id: "{id}", action: "{action}", args: {json.dumps(args)}) {{
            id
            power
        }}
    }}
'''

activate_scene_mutation = lambda id: f'''
    mutation {{
        activate_scene(id: "{id}") {{
            id
        }}
    }}
'''
