import json
import os.path
import re
import sys
import config
import constants
from product_shapes import shape_to_dict, dropdown_to_dict, is_related
from constants import markers


def add_xmind_attributes(topic, json_object):
    """ Add attributes to the mind map

    Using the Json file that contains the information about the product shape the first set of
    attributes that are not attached to a category are processed first, this ensures they appear
    as the first set of attribute.

    The second part of the process adds the categories and processes the attributes
    that are attached to the category.

    :parameter topic The topic used for attachment
    :parameter json_object json containing the object structure
    """
    # product_shape = config.config_dict['Product Information']['product_shape']
    # shape_to_dict(product_shape)

    attributes = json_object[constants.json_keys['attributes']]
    for attribute in attributes:
        if not (is_related(json_object, attribute['NAME'])):
            if not (constants.json_keys['category'] in attribute):
                add_attribute(attribute, topic, json_object)

    if constants.json_keys['attribute_category'] in json_object.keys():
        question_category_topic = add_question_categories(topic, json_object)
        for attribute in attributes:
            if constants.json_keys['category'] in attribute.keys():
                if not (is_related(json_object, attribute['NAME'])):
                    add_attribute(attribute, topic, json_object, question_category_topic)


def add_question_categories(topic, json_object):
    """ Adds the question (Attribute) categories to the mind map

    Question Categories are added to the topic that is passed in,
    as there could be multiple added at the same time the new
    topics (Question Categores) are added to a dictionary that
    is used to add the correct attributes to the correct question
    categories

    :parameter topic The topic that will be used to add the question categories to
    :parameter category_key The key to the category section, 'Attribute Category', 'Line Attribute Category'
    """
    question_category_topic = dict()
    if constants.json_keys['attribute_category'] in json_object.keys():
        question_categories = json_object[constants.json_keys['attribute_category']]
        for question_category in question_categories:
            item = topic.addSubTopic()
            item.setTitle(question_category['NAME'])
            item.addMarker(markers[question_category['TYPE']])
            if 'LABEL' in question_category.keys():
                item.addLabel(question_category['LABEL'])
            question_category_topic[question_category['NAME']] = item
    return question_category_topic


def add_coverage_categories(topic, json_object):
    coverage_category_topic = dict()
    if constants.json_keys['coverage_category'] in json_object.keys():
        coverage_categories = json_object[constants.json_keys['coverage_category']]
        for coverage_category in coverage_categories:
            item = topic.addSubTopic()
            item.setTitle(coverage_category['NAME'])
            item.addMarker(markers[coverage_category['TYPE']])
            if 'LABEL' in coverage_category.keys():
                item.addLabel(coverage_category['LABEL'])
            coverage_category_topic[coverage_category['NAME']] = item
    return coverage_category_topic


def add_dropdown(attribute, item, json_object):
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
            extract_related(json_object, attribute['NAME'], dropdown_value['NAME'], item_option)
        else:
            item_option = item.addSubTopic()
            item_option.setTitle(dropdown_value)
            item_option.addMarker(markers['text'])
            extract_related(json_object, attribute['NAME'], dropdown_value, item_option)


def add_attribute(attribute, topic, json_object, question_category_topic=None):
    if constants.json_keys['category'] in attribute.keys():
        if question_category_topic is not None:
            if constants.json_keys['category'] in attribute.keys():
                copy_topic = question_category_topic[attribute[constants.json_keys['category']]]
        else:
            copy_topic = topic
    else:
        copy_topic = topic

    item = copy_topic.addSubTopic()
    item.setTitle(attribute['NAME'])
    item.addMarker(markers[attribute['TYPE']])
    if 'LABEL' in attribute.keys():
        item.addLabel(attribute['LABEL'])
    if constants.json_keys['attributes'] in attribute.keys():
        for attribute_attribute in attribute[constants.json_keys['attributes']]:
            add_attribute(attribute_attribute, item, json_object)

    if attribute['TYPE'] == 'dropdown':
        add_dropdown(attribute, item, json_object)
    return item


def add_xmind_coverages(coverages, json_object, topic):
    """Create the coverages in the mind map

    Coverages should belong to a category, and they are created first, once
    created the coverages are added to the correct category. If there are any terms
    these are added to the coverage by using the add attribute function, terms could
    include risk objects when a coverage schedule is created, these have attributes
    and this is passed to the standard add attribute process.

    :parameter coverages (list) A list of coverage dicts
    :parameter topic (topic) The base topic to attach the coverages to
    :parameter category_key The dictionary key for the coverage categories
    """
    if constants.json_keys['coverage_category'] in json_object.keys():
        coverage_categories = add_coverage_categories(topic, json_object)
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
                    new_term = add_attribute(term, new_coverage, json_object)

                    if 'ATTRIBUTES' in term.keys():
                        for term_attribute in term['ATTRIBUTES']:
                            add_attribute(term_attribute, new_term, json_object)
    else:
        wise_monkey_says_oops(f'Coverages must have a category and none are defined for {json_object["NAME"]}')


def extract_related(json_object, parent, link, topic):
    if constants.json_keys['related'] in json_object.keys():
        related = json_object[constants.json_keys['related']]
        attributes = json_object[constants.json_keys['attributes']]
        for relationship in related:
            if relationship['PARENT'] == parent and relationship['LINK'] == link:
                for attribute in attributes:
                    if attribute['NAME'] == relationship['CHILD']:
                        add_attribute(attribute, topic, json_object)


def wise_monkey_says(message):
    to_say = f'Wise Monkey has spoken - {message}'
    print(to_say)


def wise_monkey_says_oops(message):
    to_say = f'Wise Monkey OOPS - {message}'
    print(to_say)


def to_title(string):
    regex = re.compile("[a-z]+('[a-z]+)?", re.I)
    return regex.sub(lambda grp: grp.group(0)[0].upper() + grp.group(0)[1:].lower(),
                     string)


def load_shape_files():
    file = config.json_store_location + 'json_store.json'
    try:
        with open(file) as json_file:
            list_items = json.load(json_file)['Json Store']
            for item in list_items:
                config.json_store_files.update(item)
    except:
        wise_monkey_says_oops(f"The json file json_store.json can't be processed")
        sys.exit(1)


def load_phrase_files():
    file_key = f'{config.product_shape_lower} phrases'
    file_path = f'{config.json_store_location}{config.json_store_files[file_key]}'
    if os.path.exists(file_path):
        with open(file_path) as json_file:
            list_items = json.load(json_file)['Phrases']
            for item in list_items:
                config.matcher_phrases.append(item['NAME'])


def write_tokens(doc):
    output_tokens = config.config_dict['Process']['output_tokens'].lower()
    if output_tokens == 'yes' or output_tokens == 'true':
        with open(config.config_dict['Process']['token_file'], 'w') as file:
            line = f'text|lemma|pos_|tag|dep_|shape_|is_alpha|is_stop|is_title|is_sent_start|morph|has_dep()|right_edge.text'
            file.write(line)
            for token in doc:
                line = f'{token.text}|{token.lemma_}|{token.pos_}|{token.tag_}|{token.dep_}|' \
                       f'{token.shape_}|{token.is_alpha}|{token.is_stop}|{token.is_title}|' \
                       f'{token.is_sent_start}|{token.morph}|{token.has_dep()}|{token.right_edge.text} \n'
                file.write(line)
