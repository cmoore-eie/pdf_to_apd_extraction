import shutil
from datetime import date
import xmind

import config
import product_shape_regular
from constants import markers
import product_shape_private_motor
import product_shape_home
from product_shapes import shape_to_dict
from utility import add_xmind_attributes, add_xmind_coverages

standard_term_types = {
    'Sum Insured': markers['money'],
    'Limit': markers['money'],
    'Deductible': markers['money']
}


def standard_terms(coverage):
    terms_indicator = config.config_dict['Mind Map']['add_basic_terms'].lower()
    if terms_indicator != 'yes' and terms_indicator != 'true':
        return

    for key in standard_term_types:
        term = coverage.addSubTopic()
        term.setTitle(key)
        term.addMarker(standard_term_types[key])


def apply_product_shape(line, coverages):
    if config.product_shape_lower == 'home':
        product_shape_home.apply_shape(line, coverages)
        return
    if config.product_shape_lower == 'private motor':
        product_shape_private_motor.apply_shape(line, coverages)
        return
    if config.is_regular_product:
        product_shape_regular.apply_shape(line)
        return

    apply_standard_product_shape(line, coverages)


def apply_standard_product_shape(line, coverages):
    risk_object = line.addSubTopic()
    risk_object.setTitle("Risk Object")
    risk_object.addMarker(markers['risk_object'])

    risk_object_notes = risk_object.addSubTopic()
    risk_object_notes.setTitle("Notes")
    risk_object_notes.addMarker(markers['info'])

    risk_object_attribute = risk_object.addSubTopic()
    risk_object_attribute.setTitle("Attributes")

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

    for coverage in coverages:
        new_coverage = risk_object_coverage_category.addSubTopic()
        new_coverage.setTitle(coverages[coverage])
        new_coverage.addMarker(markers['coverage'])
        standard_terms(new_coverage)


def apply_about(line):
    line_about = line.addSubTopic()
    line_about.setTitle("About")
    line_about.addMarker(markers['info'])
    line_about_version = line_about.addSubTopic()
    line_about_version.setTitle('Version')
    info = line_about_version.addSubTopic()
    info.setTitle('1.0')

    line_about_date = line_about.addSubTopic()
    line_about_date.setTitle('Date')
    info = line_about_date.addSubTopic()
    info.setTitle(date.today().isoformat())

    line_about_author = line_about.addSubTopic()
    line_about_author.setTitle('Author')
    info = line_about_author.addSubTopic()
    info.setTitle('Wise Monkey')

    line_about_description = line_about.addSubTopic()
    line_about_description.setTitle('Description')
    if config.is_regular_product:
        description = f'Built from Regular Product = {config.regular_product}'
    else:
        description = f'Auto Generated {config.product_shape} product'
    info = line_about_description.addSubTopic()
    info.setTitle(description)


def build_sheet(sheet1, coverages):
    if config.is_regular_product:
        shape_to_dict(config.regular_product_lower)
    else:
        shape_to_dict(config.product_shape_lower)

    sheet1.setTitle("Product")

    product = sheet1.getRootTopic()
    product.setTitle(config.config_dict['Product Information']['product_name'])
    product.addLabel(config.config_dict['Product Information']['product_label'])
    product.addMarker(markers['product'])

    line = product.addSubTopic()
    line.setTitle(config.config_dict['Product Information']['line_name'])
    line.addLabel(config.config_dict['Product Information']['line_label'])
    line.addMarker(markers['line'])

    apply_about(line)

    line_notes = line.addSubTopic()
    line_notes.setTitle("Notes")
    line_notes.addMarker(markers['info'])

    line_attribute = line.addSubTopic()
    line_attribute.setTitle("Attributes")

    if 'Line Attributes' in config.shape_dict.keys():
        add_xmind_attributes(line_attribute, 'Line Attributes', 'Line Attribute Category')

    line_coverage = line.addSubTopic()
    line_coverage.setTitle("Coverages")

    if 'Line Coverages' in config.shape_dict.keys():
        add_xmind_coverages(config.shape_dict['Line Coverages'], line_coverage, 'Line Coverage Category')

    line_exclusions = line.addSubTopic()
    line_exclusions.setTitle("Exclusions")

    line_conditions = line.addSubTopic()
    line_conditions.setTitle("Conditions")

    apply_product_shape(line, coverages)


def generate_xmind(coverages):
    output_file = config.config_dict['Base Information']['output_document']
    shutil.copyfile('APDBase.xmind', output_file)
    workbook = xmind.load(output_file)
    sheet1 = workbook.getPrimarySheet()
    build_sheet(sheet1, coverages)

    xmind.save(workbook, path=output_file)
