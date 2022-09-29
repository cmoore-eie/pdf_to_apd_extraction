from Constants import markers, dropdown, product_shapes


def apply_shape(line, coverages, config_dict):
    risk_object = line.addSubTopic()
    risk_object.setTitle("Structure")
    risk_object.addMarker(markers['risk_object'])

    risk_object_notes = risk_object.addSubTopic()
    risk_object_notes.setTitle("Notes")
    risk_object_notes.addMarker(markers['info'])

    risk_object_attribute = risk_object.addSubTopic()
    risk_object_attribute.setTitle("Attributes")
    add_attributes(risk_object_attribute)

    risk_object_coverage = risk_object.addSubTopic()
    risk_object_coverage.setTitle("Coverages")
    risk_object_coverage_category = risk_object_coverage.addSubTopic()
    risk_object_coverage_category.setTitle("Standard Coverages")
    risk_object_coverage_category.addMarker(markers['clause_category'])

    risk_object_coverage_building_category = risk_object_coverage.addSubTopic()
    risk_object_coverage_building_category.setTitle("Building Coverages")
    risk_object_coverage_building_category.addMarker(markers['clause_category'])

    risk_object_coverage_contents_category = risk_object_coverage.addSubTopic()
    risk_object_coverage_contents_category.setTitle("Contents Coverages")
    risk_object_coverage_contents_category.addMarker(markers['clause_category'])

    risk_object_exclusions = risk_object.addSubTopic()
    risk_object_exclusions.setTitle("Exclusions")
    risk_object_exclusions_category = risk_object_exclusions.addSubTopic()
    risk_object_exclusions_category.setTitle("Standard Exclusions")
    risk_object_exclusions_category.addMarker(markers['clause_category'])

    risk_object_conditions = risk_object.addSubTopic()
    risk_object_conditions.setTitle("Conditions")
    risk_object_conditions_category = risk_object_conditions.addSubTopic()
    risk_object_conditions_category.setTitle("Standard Conditions")
    risk_object_conditions_category.addMarker(markers['clause_category'])

    for coverage in coverages:
        new_coverage = risk_object_coverage_category.addSubTopic()
        new_coverage.setTitle(coverages[coverage])
        new_coverage.addMarker(markers['coverage'])


def add_attributes(attributes):
    for attribute in product_shapes['home']:
        item = attributes.addSubTopic()
        item.setTitle(attribute['NAME'])
        item.addMarker(markers[attribute['TYPE']])
        if attribute['TYPE'] == 'dropdown':
            if 'LIST' in attribute.keys():
                dropdown_name = attribute['LIST']
            else:
                dropdown_name = attribute['NAME']
            for type in dropdown[dropdown_name]:
                item_option = item.addSubTopic()
                item_option.setTitle(type)
                item_option.addMarker(markers['text'])
