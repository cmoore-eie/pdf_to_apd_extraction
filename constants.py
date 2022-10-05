version_number = '0.4'

json_keys = dict()
json_keys['attributes'] = 'ATTRIBUTES'
json_keys['related'] = 'RELATED'
json_keys['attribute_category'] = 'ATTRIBUTE_CATEGORY'
json_keys['coverage_category'] = 'COVERAGE_CATEGORY'
json_keys['coverages'] = 'COVERAGES'
json_keys['risk_objects'] = 'RISK_OBJECTS'
json_keys['category'] = 'CATEGORY'
json_keys['line'] = "LINE"

#
# When coverage words are to be removed it will check against this list and not add the name to the label of the
# topic
#
coverage_words = ['cover', 'coverage']

#
# Markers are the icons added to the topics
#
markers = dict()
markers['attribute_category'] = 'gw_question'
markers['boolean'] = 'gw_boolean'
markers['clause_category'] = 'gw_clause_category'
markers['coverage'] = 'gw_coverage'
markers['date_time'] = 'gw_date_time'
markers['dropdown'] = 'gw_drop_down'
markers['exposure'] = 'gw_exposure'
markers['info'] = 'symbol-info'
markers['line'] = 'gw_line'
markers['location'] = 'gw_location'
markers['money'] = 'gw_money'
markers['number'] = 'gw_integer'
markers['product'] = 'gw_product'
markers['risk_object'] = 'gw_risk_object'
markers['text'] = 'gw_text'

#
# Common Conversions
#
common_conversions = dict()
common_conversions['Loss Rent'] = 'Loss of Rent'
common_conversions['Selling Home'] = 'Selling Your Home'
common_conversions['Increased Cost Working'] = 'Increased Cost of Working'
common_conversions['Trace Access'] = 'Trace and Access'
common_conversions['Theft Outbuildings'] = 'Theft from Outbuildings'
common_conversions['Contents University'] = 'Contents at University'
common_conversions['Contents Temporarily Away Home'] = 'Contents Temporarily Away from Home'
common_conversions['Theft Unattended Motor Vehicle'] = 'Theft from Unattended Motor Vehicle'
common_conversions['Loss Theft Keys'] = 'Loss or Theft of Keys'
common_conversions['Water Oil Escaping'] = 'Water or Oil Escaping'
common_conversions['Storm Flood'] = 'Storm or Flood'
common_conversions['Theft Attempted Theft'] = 'Theft or Attempted Theft'
