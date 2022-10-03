import config
from constants import markers
from product_shapes import shape_to_dict
from utility import add_xmind_attributes, add_xmind_coverages


def apply_shape(line, coverages):
    product_shape = config.config_dict['Product Information']['product_shape']
    shape_to_dict(product_shape)
    for attribute in config.shape_dict['Risk Object']:
        risk_object = line.addSubTopic()
        risk_object.setTitle(attribute['NAME'])
        risk_object.addMarker(markers[attribute['TYPE']])
        if 'LABEL' in attribute.keys():
            risk_object.addLabel(attribute['LABEL'])

        risk_object_notes = risk_object.addSubTopic()
        risk_object_notes.setTitle("Notes")
        risk_object_notes.addMarker(markers['info'])

        risk_object_attribute = risk_object.addSubTopic()
        risk_object_attribute.setTitle("Attributes")

        add_xmind_attributes(risk_object_attribute)

        risk_object_coverage = risk_object.addSubTopic()
        risk_object_coverage.setTitle("Coverages")
        risk_object_coverage_category = risk_object_coverage.addSubTopic()
        risk_object_coverage_category.setTitle("Primary Coverages")
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

        add_xmind_coverages(coverages, risk_object_coverage_category)
