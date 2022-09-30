import json

shape_files = {'private motor': 'product_shape_private_motor.json',
               'home': 'product_shape_home.json',
               'dropdown': 'product_shape_dropdown.json'}


def shape_to_dict(shape):
    if shape.lower() in shape_files.keys():
        shape_file = shape_files[shape.lower()]
        with open(shape_file) as json_file:
            data = json.load(json_file)
            return data
    else:
        print(f'!!! Unable to process Shape for {shape} !!!')
        return {'Attributes': []}


def dropdown_to_dict(dropdown_name):
    shape_file = shape_files['dropdown']
    with open(shape_file) as json_file:
        data = json.load(json_file)
        if dropdown_name in data.keys():
            return data[dropdown_name]
        else:
            return []


#
# if the child is part of a defined relationship it will be created when the dropdown values of the parent are
# processed, otherwise it needs to be ignored. This function returns False if the child is not related otherwise
# it will return True
#
def is_related(shape_dict, child):
    if 'Related' not in shape_dict.keys():
        return False
    related = shape_dict['Related']
    for relationship in related:
        if relationship['CHILD'] == child:
            return True
    return False
