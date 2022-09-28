import shutil

import xmind
from xmind.core.const import TOPIC_DETACHED
from xmind.core.markerref import MarkerId
from xmind.core.topic import TopicElement

marker_coverage = 'gw_coverage'
marker_product = 'gw_product'
marker_line = 'gw_line'
marker_risk_object = 'gw_risk_object'
marker_clause_category = 'gw_clause_category'
marker_money = 'gw_money'

standard_term_types = {
    'Sum Insured': marker_money,
    'Limit': marker_money,
    'Deductible': marker_money
}


def standard_terms(coverage, config_dict):
    terms_indicator = config_dict['Mind Map']['add_basic_terms'].lower()
    if terms_indicator != 'yes' and terms_indicator != 'true':
        return

    for key in standard_term_types:
        term = coverage.addSubTopic()
        term.setTitle(key)
        term.addMarker(standard_term_types[key])


def build_sheet(sheet1, coverages, config_dict):
    sheet1.setTitle("Product")

    product = sheet1.getRootTopic()
    product.setTitle(config_dict['Product Information']['product_name'])
    product.addLabel(config_dict['Product Information']['product_label'])
    product.addMarker(marker_product)

    line = product.addSubTopic()
    line.setTitle(config_dict['Product Information']['line_name'])
    line.addLabel(config_dict['Product Information']['line_label'])
    line.addMarker(marker_line)

    line_attribute = line.addSubTopic()
    line_attribute.setTitle("Attributes")

    line_coverage = line.addSubTopic()
    line_coverage.setTitle("Coverages")

    line_exclusions = line.addSubTopic()
    line_exclusions.setTitle("Exclusions")

    line_conditions = line.addSubTopic()
    line_conditions.setTitle("Conditions")

    risk_object = line.addSubTopic()
    risk_object.setTitle("Risk Object")
    risk_object.addMarker(marker_risk_object)

    risk_object_attribute = risk_object.addSubTopic()
    risk_object_attribute.setTitle("Attributes")

    risk_object_coverage = risk_object.addSubTopic()
    risk_object_coverage.setTitle("Coverages")
    risk_object_coverage_category = risk_object_coverage.addSubTopic()
    risk_object_coverage_category.setTitle("Standard Coverages")
    risk_object_coverage_category.addMarker(marker_clause_category)

    risk_object_exclusions = risk_object.addSubTopic()
    risk_object_exclusions.setTitle("Exclusions")
    risk_object_exclusions_category = risk_object_exclusions.addSubTopic()
    risk_object_exclusions_category.setTitle("Standard Exclusions")
    risk_object_exclusions_category.addMarker(marker_clause_category)

    risk_object_conditions = risk_object.addSubTopic()
    risk_object_conditions.setTitle("Conditions")
    risk_object_conditions_category = risk_object_conditions.addSubTopic()
    risk_object_conditions_category.setTitle("Standard Exclusions")
    risk_object_conditions_category.addMarker(marker_clause_category)

    for coverage in coverages:
        new_coverage = risk_object_coverage_category.addSubTopic()
        new_coverage.setTitle(coverages[coverage])
        new_coverage.addMarker(marker_coverage)
        standard_terms(new_coverage, config_dict)


def generate_xmind(coverages, config_dict):
    output_file = config_dict['Base Information']['output_document']
    shutil.copyfile('APDBase.xmind', output_file)
    workbook = xmind.load(output_file)
    sheet1 = workbook.getPrimarySheet()
    build_sheet(sheet1, coverages, config_dict)

    # topic = sheet1.getRootTopic().getTopics()
    # remove_node = sheet1.getRootTopic().getChildNodesByTagName('children')
    # sheet1.getRootTopic().removeChild(remove_node)
    # gen_sheet2(workbook, sheet1)
    xmind.save(workbook, path=output_file)
