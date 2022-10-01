import json

from spacy import matcher

import config
from rules_motor import motor_rules

custom_rules = dict()
custom_rules['building_base_coverage'] = [{'LEMMA': 'Building'}, {'IS_PUNCT': True, 'OP': '?'}, {'LEMMA': 'Base'}, {'LEMMA': 'cover'}]
custom_rules['building_extended_coverage'] = [{'LEMMA': 'Building'}, {'IS_PUNCT': True, 'OP': '?'}, {'LEMMA': 'Extended'}, {'LEMMA': 'Coverage'}]
custom_rules['building_roof_extension_coverage'] = [{'LEMMA': 'Building'}, {'IS_PUNCT': True, 'OP': '?'}, {'LEMMA': 'Roof'}, {'LEMMA': 'extension'}]
custom_rules['business_Interruption'] = [{'LEMMA': 'Business'}, {'LEMMA': 'Interruption'}]
custom_rules['business_travel'] = [{'LEMMA': 'Business'}, {'LEMMA': 'Travel'}]
custom_rules['commercial_legal_expenses'] = [{'LEMMA': 'commercial'}, {'LEMMA': 'Legal'}, {'LEMMA': 'expense'}]
custom_rules['contractor_all_risks'] = [{'LEMMA': 'contractor'}, {'IS_PUNCT': True, 'OP': '?'}, {'LEMMA': 'all'}, {'LEMMA': 'risk'}]
custom_rules['employer_liability'] = [{'LEMMA': 'Employers'}, {'IS_PUNCT': True, 'OP': '?'}, {'LEMMA': 'Liability'}]
custom_rules['environmental_liability'] = [{'LEMMA': 'Environmental'}, {'LEMMA': 'Liability'}]
custom_rules['extended_coverage'] = [
        [{'LEMMA': 'Extended'}, {'LEMMA': 'Coverage'}],
        [{'LEMMA': 'Coverage'}, {'LEMMA': 'Extensions'}]
    ]
custom_rules['goods_in_transit'] = [{'LEMMA': 'good'}, {'LEMMA': 'in'}, {'LEMMA': 'Transit'}]
custom_rules['group_personal_accident'] = [{'LEMMA': 'Group'}, {'LEMMA': 'Personal'}, {'LEMMA': 'Accident'}]
custom_rules['home_assistance'] = [{'IS_PUNCT': True, 'OP': '?'}, {'LOWER': 'home'}, {'IS_PUNCT': True, 'OP': '?'}, {'LOWER': 'assistance'}]
custom_rules['household_basic_coverage'] = [{'LEMMA': 'Household'}, {'IS_PUNCT': True, 'OP': '?'}, {'LEMMA': 'Basic'}, {'LEMMA': 'Coverage'}]
custom_rules['household_blanket_coverage'] = [{'LEMMA': 'Household'}, {'IS_PUNCT': True, 'OP': '?'}, {'LEMMA': 'Blanket'}, {'LEMMA': 'Coverage'}]
custom_rules['household_extended_coverage'] = [{'LEMMA': 'Household'}, {'IS_PUNCT': True, 'OP': '?'}, {'LEMMA': 'Extended'}, {'LEMMA': 'Coverage'}]
custom_rules['private_civil_liability'] = [{'LEMMA': 'private'}, {'LEMMA': 'civil'}, {'LEMMA': 'Liability'}]
custom_rules['public_liability'] = [
    [{'LOWER': 'public'}, {'LOWER': 'liability'}],
    [{'LOWER': 'liability'}, {}, {}, {'LOWER': 'public'}]
    ]
# custom_rules['property_rule'] = [{'LEMMA': 'property'}]

def build_rules(rule_file, matcher):
    rule_dict = dict()
    with open(rule_file) as json_file:
        data = json.load(json_file)
        for rule_name in data.keys():
            pattern_json = data[rule_name]
            pattern = []
            for pattern_list in pattern_json:
                item_body = []
                for pattern_item in pattern_list:
                    item_body_part = dict()
                    for key in pattern_item.keys():
                        if key == 'IS_PUNCT':
                            item_body_part[key] = True
                        elif key == 'IS_TITLE':
                            item_body_part[key] = True
                        else:
                            item_body_part[key] = pattern_item[key]
                    item_body.append(item_body_part)
                pattern.append(item_body)
            matcher.add(rule_name.upper(), pattern, on_match=None)

def build_matcher_rules(matcher):
    product_shape = config.config_dict['Product Information']['product_shape']
    for key in custom_rules:
        pattern = custom_rules[key]
        if type(pattern[0]) is list:
            matcher.add(key.upper(), pattern, on_match=None)
        else:
            matcher.add(key.upper(), [pattern], on_match=None)

    if product_shape.lower() == 'motor':
        for key in motor_rules:
            pattern = motor_rules[key]
            if type(pattern[0]) is list:
                matcher.add(key.upper(), pattern, on_match=None)
            else:
                matcher.add(key.upper(), [pattern], on_match=None)

    if product_shape.lower() == 'home':
        build_rules('rules_home.json', matcher)
