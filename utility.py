import re

import config
from product_shapes import shape_to_dict, dropdown_to_dict, is_related
from constants import markers


def add_xmind_attributes(attributes):
    """ Add attributes to the mind map

    Using the Json file that contains the information about the product shape the first set of
    attributes that are not attached to a category are processed first, this ensure they appear
    as the first set of attribute.

    The second part of the process adds the categories and processes the attributes
    that are attached to the category.
    """
    product_shape = config.config_dict['Product Information']['product_shape']
    shape_dict = shape_to_dict(product_shape)
    for attribute in shape_dict['Attributes']:
        if not (is_related(shape_dict, attribute['NAME'])):
            if not ('CATEGORY' in attribute):
                add_attribute(attribute, attributes, shape_dict)

    question_category_topic = add_question_categories(shape_dict, attributes)
    for attribute in shape_dict['Attributes']:
        if 'CATEGORY' in attribute:
            if not (is_related(shape_dict, attribute['NAME'])):
                add_attribute(attribute, attributes, shape_dict, question_category_topic)


#
# Added the question categories
#
def add_question_categories(shape_dict, topic):
    question_category_topic = dict()
    if 'Attribute Category' in shape_dict:
        for question_category in shape_dict['Attribute Category']:
            item = topic.addSubTopic()
            item.setTitle(question_category['NAME'])
            item.addMarker(markers[question_category['TYPE']])
            question_category_topic[question_category['NAME']] = item
    return question_category_topic


def add_attribute(attribute, topic, shape_dict, question_category_topic=None):
    if 'CATEGORY' in attribute:
        if question_category_topic is not None:
            copy_topic = question_category_topic[attribute['CATEGORY']]
        else:
            copy_topic = topic
    else:
        copy_topic = topic
    item = copy_topic.addSubTopic()
    item.setTitle(attribute['NAME'])
    item.addMarker(markers[attribute['TYPE']])
    if 'LABEL' in attribute.keys():
        item.addLabel(attribute['LABEL'])
    if attribute['TYPE'] == 'dropdown':
        if 'LIST' in attribute.keys():
            dropdown_name = attribute['LIST']
        else:
            dropdown_name = attribute['NAME']
        dropdown_data = dropdown_to_dict(dropdown_name)

        for dropdown_value in dropdown_data:
            if type(dropdown_value) == dict:
                item_option = item.addSubTopic()
                item_option.setTitle(dropdown_value['NAME'])
                item_option.addMarker(markers['text'])
                if 'LABEL' in dropdown_value.keys():
                    item_option.addLabel(dropdown_value['LABEL'])
                extract_related(shape_dict, attribute['NAME'], dropdown_value['NAME'], item_option)
            else:
                item_option = item.addSubTopic()
                item_option.setTitle(dropdown_value)
                item_option.addMarker(markers['text'])
                extract_related(shape_dict, attribute['NAME'], dropdown_value, item_option)


def add_xmind_coverages(coverages, topic):
    for coverage in coverages:
        new_coverage = topic.addSubTopic()
        new_coverage.setTitle(coverages[coverage])
        new_coverage.addMarker(markers['coverage'])


def extract_related(shape_dict, parent, link, topic):
    if 'Related' not in shape_dict.keys():
        return
    related = shape_dict['Related']
    attributes = shape_dict['Attributes']
    for relationship in related:
        if relationship['PARENT'] == parent and relationship['LINK'] == link:
            for attribute in attributes:
                if attribute['NAME'] == relationship['CHILD']:
                    add_attribute(attribute, topic, shape_dict)


def wise_monkey_says(message):
    to_say = f'Wise Monkey has spoken - "{message}"'
    print(to_say)


def to_title(string):
    regex = re.compile("[a-z]+('[a-z]+)?", re.I)
    return regex.sub(lambda grp: grp.group(0)[0].upper() + grp.group(0)[1:].lower(),
                     string)
