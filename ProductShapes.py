import json

shape_files = {'private motor': 'product_shape_private_motor.json',
               'home': 'product_shape_home.json'}


def shape_to_dict(shape):
    if shape.lower() in shape_files.keys():
        shape_file = shape_files[shape.lower()]
        with open(shape_file) as json_file:
            data = json.load(json_file)
            return data
    else:
        print(f'!!! Unable to process Shape for {shape} !!!')
        return {'Attributes': []}
