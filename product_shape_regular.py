import config
import constants
from constants import markers
from product_shapes import shape_to_dict
from utility import add_xmind_attributes, add_xmind_coverages


def apply_shape(line, coverages = None):
    shape_to_dict(config.regular_product_lower)
    for json_risk_object in config.shape_dict[constants.json_keys['risk_objects']]:
        risk_object = line.addSubTopic()
        risk_object.setTitle(json_risk_object['NAME'])
        risk_object.addMarker(markers[json_risk_object['TYPE']])
        if 'LABEL' in json_risk_object.keys():
            risk_object.addLabel(json_risk_object['LABEL'])

        risk_object_notes = risk_object.addSubTopic()
        risk_object_notes.setTitle("Notes")
        risk_object_notes.addMarker(markers['info'])

        risk_object_attribute = risk_object.addSubTopic()
        risk_object_attribute.setTitle("Attributes")

        if constants.json_keys['attributes'] in json_risk_object.keys():
            add_xmind_attributes(risk_object_attribute, json_risk_object)

        risk_object_coverage = risk_object.addSubTopic()
        risk_object_coverage.setTitle("Coverages")

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

        if constants.json_keys['coverages'] in json_risk_object.keys():
            coverages = json_risk_object[constants.json_keys['coverages']]
            add_xmind_coverages(coverages, json_risk_object, risk_object_coverage)
