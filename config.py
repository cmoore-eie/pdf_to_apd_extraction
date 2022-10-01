""" Contains Global variables

Information that should be treated as global in nature are added here.
Importing the module will bring the variables into scope of other
modules.
"""
config_dict = dict()
shape_dict = dict()
product_shape = ''
product_shape_lower = ''
go_product = ''
go_product_lower = ''
shape_files = {'private motor': 'product_shape_private_motor.json',
               'home': 'product_shape_home.json',
               'dropdown': 'product_shape_dropdown.json',
               'gw_uk_homeowners': 'product_shape_gw_uk_homeowners.json'}
