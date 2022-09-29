#
# When coverage words are to be removed it will check against this list and not add the name to the lable of the
# topic
#
coverage_words = ['cover', 'coverage']

#
# Product Shapes dictate what additional attributes are needed to be added by default
#
product_shapes = dict()
product_shapes['other'] = []
product_shapes['home'] = [{'NAME': 'Structure Type', 'TYPE': 'dropdown'},
                          {'NAME': 'Number Bedrooms', 'TYPE' : 'dropdown'},
                          {'NAME': 'Number Rooms', 'TYPE' : 'dropdown'},
                          {'NAME': 'Basement', 'TYPE': 'boolean'},
                          {'NAME': 'Swimming Pool', 'TYPE': 'boolean'},
                          {'NAME': 'When Built', 'TYPE': 'number'},
                          {'NAME': 'Wall Construction', 'TYPE': 'dropdown'},
                          {'NAME': 'Roof Construction', 'TYPE': 'dropdown'},
                          {'NAME': 'Who Occupies the Property', 'TYPE': 'dropdown', 'LIST': 'Occupancy'},
                          {'NAME': 'How long is the Property normally occupied', 'TYPE': 'dropdown', 'LIST': 'Occupied'},
                          {'NAME': 'What type of locks are the majority of external doors fitted with', 'TYPE': 'text'},
                          {'NAME': 'Are all accessible windows, fanlights and skylights fitted with key operated locks?', 'TYPE': 'boolean'},
                          {'NAME': 'Do you have CCTV at the property to be insured', 'TYPE': 'dropdown', 'LIST': 'Yes No'},
                          {'NAME': 'Does the CCTV system have remote internet monitoring?', 'TYPE': 'boolean'},
                          {'NAME': 'Which areas are covered', 'TYPE': 'text'},
                          {'NAME': 'Is there an intruder alarm in full and effective operation?', 'TYPE': 'dropdown', 'LIST': 'Yes No'},
                          {'NAME': 'Is it maintained under contract by a registered installer?', 'TYPE': 'boolean'},
                          {'NAME': 'Is there a police response or professional key holder response provided by the system?', 'TYPE': 'boolean'},
                          {'NAME': '"Have any of the buildings at the home, including the outbuildings:Suffered any structural damage, structural repair or underpinning?"', 'TYPE': 'boolean'},
                          {'NAME': '"Have any of the buildings at the home, including the outbuildings:Any signs of internal or external cracks?', 'TYPE': 'boolean'},
                          {'NAME': '"Have any of the buildings at the home, including the outbuildings: Been monitored for subsidence or movement?', 'TYPE': 'boolean'}]

product_shapes['private motor'] = [{'NAME': 'Address', 'TYPE': 'location'},
                                   {'NAME': 'Vehicle Type', 'TYPE': 'dropdown'},
                                   {'NAME': 'Registration Plate', 'TYPE': 'text'},
                                   {'NAME': 'VIN Number', 'TYPE': 'text'},
                                   {'NAME': 'Make', 'TYPE': 'text'},
                                   {'NAME': 'Model', 'TYPE': 'text'},
                                   {'NAME': 'Engine Type', 'TYPE': 'text'},
                                   {'NAME': 'Power - KW', 'TYPE': 'number'},
                                   {'NAME': 'Vehicle Weight', 'TYPE': 'number'},
                                   {'NAME': 'Year of First Registration', 'TYPE': 'date_time'},
                                   {'NAME': 'Usage', 'TYPE': 'dropdown', 'LIST': 'Vehicle Usage'},
                                   {'NAME': 'Engine Capacity CC', 'TYPE': 'number'},
                                   {'NAME': 'Value of Vehicle', 'TYPE': 'money'},
                                   {'NAME': 'Torque ', 'TYPE': 'money'},
                                   {'NAME': 'Modification', 'TYPE': 'boolean'},
                                   {'NAME': 'Annual Km', 'TYPE': 'number'},
                                   {'NAME': 'Liability Bonus Malus', 'TYPE': 'text'},
                                   {'NAME': 'Kasko Bonus Malus', 'TYPE': 'text'},
                                   {'NAME': 'Damage Deductible', 'TYPE': 'money'},
                                   {'NAME': 'Is the vehicle leased', 'TYPE': 'boolean'},
                                   {'NAME': 'Is car alarmed ?', 'TYPE': 'boolean'}]
product_shapes['commercial building'] = []
product_shapes['sme'] = ['Risk Types']

home_cover = [['fine', 'arts'], ['alternative', 'accommodation'], ['flood', 'coverage'],
              ['earthquake', 'coverage']]

#
# dropdown contains the values dropdown options, the attribute from product shapes
#
dropdown = dict()
dropdown['Yes No'] = ['Yes', 'No']
dropdown['Risk Type'] = ['Public Liability', 'Cyber', 'D and O', 'Garage', 'Garden Structure'],
dropdown['Structure Type'] = ['Detached House', 'Semi detached House', 'Detached Bungalow', 'Semi detached Bungalow',
                              'Flat/Maisonette above Ground Floor', 'Flat/Maisonette Ground Floor',
                              'Mid Terraced House', 'Outbuildings', 'Park Home', 'End of Terrace House']
dropdown['Number Bedrooms'] = ['Up to 2', 'Three', 'Four', 'Five', 'Six', 'More than 6']
dropdown['Number Rooms'] = ['Up to 2', 'Three', 'Four', 'Five', 'Six', 'More than 6']
dropdown['Wall Construction'] = ['Brick', 'Brick and stone', 'Timber Frame/Brick', 'Cob Construction', 'Concrete',
                                 'Corrugated Iron', 'Flint', 'Glass', 'Metal', 'Plastic',
                                 'Prefabricated Building - Combustible Materials',
                                 'Prefabricated Building - Non Combustible Materials', 'Stone', 'Timber',
                                 'Timber Frame', 'Timber/Plaster', 'Wattle And Daub Construction',
                                 'Woodwork Construction', 'Timber Frame/Stone', 'Timber Frame/Timber',
                                 'Timber Frame/Lathe And Plaster', 'Steel Frame/Brick',
                                 'Steel Frame/Render Or Pebbledash', 'Wytchett or Wichert', 'Steel Frame',
                                 'Structurally Insulated Panels (SIPs)', 'Aluminium', 'Mundic Block', 'Straw Bale',
                                 'Lathe And Plaster', 'Clunch', 'Bungaroosh', 'Other']
dropdown['Roof Construction'] = ['Asphalt', 'Other', 'Asbestos', 'Concrete', 'Corrugated Iron', 'Felt On Timber',
                                 'Fibreglass', 'Glass', 'Metal', 'Plastic', 'Shingle', 'Slate', 'Stramit',
                                 'Thatch - Fibre', 'Thatch - Reed', 'Tile', 'Timber', 'Turnerised',
                                 'Woodwork Construction', 'Ethylene Propylene Diene Monomer EPDM', 'Aluminium',
                                 'Copper', 'Lead', 'Shingle – Pine/Spruce/Cedar', 'Shingle – AsphaltZinc',
                                 'ECO / Green Roofs', 'Polycarbonate']
dropdown['Occupancy'] = ['Unoccupied', 'You, your family and lodgers immediate relative', 'You and your family',
                         'Non immediate relative/employee']
dropdown['Occupied'] = ['Usually occupied during the day', 'Usually occupied at night',
                        'Usually occupied day and night', 'Holiday/Weekend use only' 'Left Empty']
dropdown['Vehicle Type'] = ['Passenger Car', 'Truck or Lorry', 'Camping Van', 'Special Vehicles', 'Motorcycle',
                            'Snowmobile', 'Moped', 'Light trailer', 'Camping trailer', 'Heavy trailer',
                            'Electric vehicles']
dropdown['Vehicle Usage'] = ['Private', 'Commercial', 'Shared', 'Taxi']

#
# Markers are the icons added to the topics
#
markers = dict()
markers['boolean'] = 'gw_boolean'
markers['clause_category'] = 'gw_clause_category'
markers['coverage'] = 'gw_coverage'
markers['date_time'] = 'gw_date_time'
markers['dropdown'] = 'gw_drop_down'
markers['info'] = 'symbol-info'
markers['line'] = 'gw_line'
markers['location'] = 'gw_location'
markers['money'] = 'gw_money'
markers['number'] = 'gw_integer'
markers['product'] = 'gw_product'
markers['risk_object'] = 'gw_risk_object'
markers['text'] = 'gw_text'

