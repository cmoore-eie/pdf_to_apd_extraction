import json
import config


def shape_to_dict(shape):
    if len(config.shape_dict.keys()) > 0:
        return config.shape_dict

    if config.is_regular_product:
        test_product_shape = config.regular_product_lower
    else:
        test_product_shape = config.product_shape_lower

    if test_product_shape in config.shape_files.keys():
        shape_file = config.json_store + config.shape_files[test_product_shape]
        with open(shape_file) as json_file:
            config.shape_dict = json.load(json_file)
            return config.shape_dict
    else:
        print(f'!!! Unable to process Shape for {shape} !!!')
        return {'Attributes': []}


def dropdown_to_dict(dropdown_name):
    shape_file = config.json_store + config.shape_files['dropdown']
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
