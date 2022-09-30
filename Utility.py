from ProductShapes import shape_to_dict, dropdown_to_dict
from Constants import markers


def add_xmind_attributes(attributes, config_dict):
    product_shape = config_dict['Product Information']['product_shape']
    shape_dict = shape_to_dict(product_shape)
    for attribute in shape_dict['Attributes']:
        item = attributes.addSubTopic()
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
            for type in dropdown_data:
                item_option = item.addSubTopic()
                item_option.setTitle(type)
                item_option.addMarker(markers['text'])


def add_xmind_coverages(coverages, topic):
    for coverage in coverages:
        new_coverage = topic.addSubTopic()
        new_coverage.setTitle(coverages[coverage])
        new_coverage.addMarker(markers['coverage'])
