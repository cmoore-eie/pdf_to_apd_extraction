import json
import config


def build_rules(rule_file, matcher):
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

    build_rules('rules_other.json', matcher)

    if product_shape.lower() == 'motor':
        build_rules('rules_motor.json', matcher)

    if product_shape.lower() == 'home':
        build_rules('rules_home.json', matcher)
