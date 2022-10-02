import re

import config
from product_shapes import shape_to_dict, dropdown_to_dict, is_related
from constants import markers


def add_xmind_attributes(attributes, attribute_key='Attributes', category_key='Attribute Category'):
    """ Add attributes to the mind map

    Using the Json file that contains the information about the product shape the first set of
    attributes that are not attached to a category are processed first, this ensure they appear
    as the first set of attribute.

    The second part of the process adds the categories and processes the attributes
    that are attached to the category.
    """
    product_shape = config.config_dict['Product Information']['product_shape']
    shape_to_dict(product_shape)
    for attribute in config.shape_dict[attribute_key]:
        if not (is_related(config.shape_dict, attribute['NAME'])):
            if not ('CATEGORY' in attribute):
                add_attribute(attribute, attributes, config.shape_dict)

    question_category_topic = add_question_categories(config.shape_dict, attributes, category_key)
    for attribute in config.shape_dict[attribute_key]:
        if 'CATEGORY' in attribute:
            if not (is_related(config.shape_dict, attribute['NAME'])):
                add_attribute(attribute, attributes, config.shape_dict, question_category_topic)


#
# Added the question categories
#
def add_question_categories(shape_dict, topic, category_key):
    question_category_topic = dict()
    if category_key in shape_dict:
        for question_category in shape_dict[category_key]:
            item = topic.addSubTopic()
            item.setTitle(question_category['NAME'])
            item.addMarker(markers[question_category['TYPE']])
            question_category_topic[question_category['NAME']] = item
    return question_category_topic


def add_coverage_categories(shape_dict, topic, category_key):
    coverage_category_topic = dict()
    if category_key in shape_dict:
        for coverage_category in shape_dict[category_key]:
            item = topic.addSubTopic()
            item.setTitle(coverage_category['NAME'])
            item.addMarker(markers[coverage_category['TYPE']])
            if 'LABEL' in coverage_category.keys():
                item.addLabel(coverage_category['LABEL'])
            coverage_category_topic[coverage_category['NAME']] = item
    return coverage_category_topic


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
        if 'OPTIONS' in attribute.keys():
            dropdown_data = attribute['OPTIONS']
        else:
            dropdown_data = dropdown_to_dict(dropdown_name)

        for dropdown_value in dropdown_data:
            if type(dropdown_value) == dict:
                item_option = item.addSubTopic()
                item_option.setTitle(dropdown_value['NAME'])
                if 'TYPE' in dropdown_value.keys():
                    item_option.addMarker(markers[dropdown_value['TYPE']])
                else:
                    item_option.addMarker(markers['text'])
                if 'LABEL' in dropdown_value.keys():
                    item_option.addLabel(dropdown_value['LABEL'])
                extract_related(shape_dict, attribute['NAME'], dropdown_value['NAME'], item_option)
            else:
                item_option = item.addSubTopic()
                item_option.setTitle(dropdown_value)
                item_option.addMarker(markers['text'])
                extract_related(shape_dict, attribute['NAME'], dropdown_value, item_option)
    return item


def add_xmind_coverages(coverages, topic, category_key='Coverage Category'):
    """Create the coverages in the mind map

    Coverages should belong to a category, and they are created first, once
    created the coverages are added to the correct category. If there are any terms
    these are added to the coverage by using the add attribute function, terms could
    include risk objects when a coverage schedule is created, these have attributes
    and this is passed to the standard add attribute process.

    :parameter coverages (list) A list of coverage dicts
    :parameter topic (topic) The base topic to attach the coverages to
    """
    coverage_categories = add_coverage_categories(config.shape_dict, topic, category_key)
    for coverage in coverages:
        if 'CATEGORY' in coverage:
            topic_to_use = coverage_categories[coverage['CATEGORY']]
        else:
            topic_to_use = topic
        new_coverage = topic_to_use.addSubTopic()
        new_coverage.setTitle(coverage['NAME'])
        new_coverage.addMarker(markers['coverage'])
        if 'LABEL' in coverage.keys():
            new_coverage.addLabel(coverage['LABEL'])

        if 'TERMS' in coverage.keys():
            for term in coverage['TERMS']:
                new_term = add_attribute(term, new_coverage, config.shape_dict)

                if 'ATTRIBUTES' in term.keys():
                    for term_attribute in term['ATTRIBUTES']:
                        add_attribute(term_attribute, new_term, config.shape_dict)


def extract_related(shape_dict, parent, link, topic):
    if 'Related' not in shape_dict.keys():
        return
    related = shape_dict['Related']
    attributes = shape_dict['Attributes']
    for relationship in related:
        if relationship['PARENT'] == parent and relationship['LINK'] == link:
            for attribute in attributes:
                if attribute['NAME'] == relationship['CHILD']:
                    add_attribute(attribute, topic, config.shape_dict)


def wise_monkey_says(message):
    to_say = f'Wise Monkey has spoken - "{message}"'
    print(to_say)


def to_title(string):
    regex = re.compile("[a-z]+('[a-z]+)?", re.I)
    return regex.sub(lambda grp: grp.group(0)[0].upper() + grp.group(0)[1:].lower(),
                     string)
