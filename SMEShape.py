from Constants import markers, dropdown


def apply_shape(line, coverages, config_dict):
    risk_object = line.addSubTopic()
    risk_object.setTitle("Risk Object")
    risk_object.addMarker(markers['risk_object'])

    risk_object_notes = risk_object.addSubTopic()
    risk_object_notes.setTitle("Notes")
    risk_object_notes.addMarker(markers['info'])

    risk_object_attribute = risk_object.addSubTopic()
    risk_object_attribute.setTitle("Attributes")
    add_attributes(risk_object_attribute, 'Risk Types')

    risk_object_coverage = risk_object.addSubTopic()
    risk_object_coverage.setTitle("Coverages")
    risk_object_coverage_category = risk_object_coverage.addSubTopic()
    risk_object_coverage_category.setTitle("Standard Coverages")
    risk_object_coverage_category.addMarker(markers['clause_category'])

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


def add_attributes(attributes, attribute):
    item = attributes.addSubTopic()
    item.setTitle(attribute)
    if attribute in dropdown.keys():
      item.addMarker(markers['dropdown'])
      for type in dropdown[attribute]:
        item_option = item.addSubTopic()
        item_option.setTitle(type)
        item_option.addMarker(markers['text'])
    else:
        item.addMarker(markers['text'])
