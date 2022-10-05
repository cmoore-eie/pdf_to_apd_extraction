import json
import os
import sys
import config
import constants
import utility


def shape_to_dict(shape):
    if len(config.shape_dict.keys()) > 0:
        return config.shape_dict

    if config.is_regular_product:
        test_product_shape = config.regular_product_lower
    else:
        test_product_shape = config.product_shape_lower

    if test_product_shape in config.json_store_files.keys():
        file_path = config.json_store_location + config.json_store_files[test_product_shape]
        if os.path.exists(file_path):
            with open(file_path) as json_file:
                config.shape_dict = json.load(json_file)
                return config.shape_dict
        else:
            utility.wise_monkey_says_oops(f'Missing shape file from the json store located at {config.json_store_location}')
            utility.wise_monkey_says_oops(f'Please add the file {config.json_store_files[config.product_shape_lower]}')
            sys.exit(1)
    else:
        utility.wise_monkey_says_oops(f'There is no definition for Shape {shape}')
        utility.wise_monkey_says_oops(f'Proceeding with no product shape')
        return {'Attributes': []}


def dropdown_to_dict(dropdown_name):
    shape_file = config.json_store_location + config.json_store_files['dropdown']
    with open(shape_file) as json_file:
        data = json.load(json_file)
        if dropdown_name in data.keys():
            return data[dropdown_name]
        else:
            return []


def is_related(json_object, child):
    """Identifies if the attribute is a child in the relationship

    if the child is part of a defined relationship it will be created when the dropdown values of the parent are
    processed, otherwise it needs to be ignored.

    :parameter shape_dict the product shape dictionary
    :parameter child the attribute to search for
    :return bool False if the child is not related otherwise it will return True
    """
    if constants.json_keys['related'] not in json_object.keys():
        return False
    related = json_object[constants.json_keys['related']]
    for relationship in related:
        if relationship['CHILD'] == child:
            return True
    return False
