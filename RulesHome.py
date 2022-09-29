
home_rules = dict()
home_rules['alternative_accommodation'] = [{'LEMMA': 'alternative'}, {'LEMMA': 'accommodation'}]
home_rules['home_coverage'] = [
    [{'LOWER': 'home'}, {'LOWER': 'and'}, {'LOWER': 'detached'}, {'IS_PUNCT': True, 'OP': '?'}, {'LOWER': 'coverages'}],
    [{'LOWER': 'home'}, {'LOWER': 'and'}, {'LOWER': 'detached'}, {'LOWER': 'coverages'}]
]
home_rules['fine_arts'] = [{'LOWER': 'fine'}, {'LOWER': 'arts'}]
home_rules['personal_property_care_facility'] = [{'LEMMA': 'personal'}, {'LEMMA': 'property'}, {}, {}, {'LEMMA': 'care'}, {'LEMMA': 'facility'}]
home_rules['flood_coverage'] = [{'LEMMA': 'flood'}, {'LEMMA': 'coverage'}]
home_rules['earthquake_coverage'] = [{'LEMMA': 'earthquake'}, {'LEMMA': 'coverage'}]
home_rules['roof_leak_coverage'] = [{'LEMMA': 'roof'}, {'LEMMA': 'leak'}, {'LEMMA': 'coverage'}]
home_rules['watercraft_coverage'] = [{'LEMMA': 'Watercraft'}, {'LEMMA': 'coverage'}]
home_rules['vacancy_coverage'] = [{'LEMMA': 'Vacancy'}, {'LEMMA': 'coverage'}]
home_rules['glass_coverage'] = [{'LEMMA': 'Glass'}, {'LEMMA': 'coverage'}]
home_rules['storage_coverage'] = [{'LEMMA': 'storage'}, {'LEMMA': 'coverage'}]
home_rules['under_construction_coverage'] = [{'LEMMA': 'under'}, {'LEMMA': 'construction'}, {'LEMMA': 'coverage'}]
home_rules['rented_home_coverage'] = [{'LEMMA': 'rent'}, {'LEMMA': 'home'}, {'LEMMA': 'coverage'}]
home_rules['short_term_renter_coverage'] = [
    [{'LEMMA': 'short'}, {'IS_PUNCT': True, 'OP': '?'}, {'LEMMA': 'term'}, {'LEMMA': 'renter'}, {'LEMMA': 'coverage'}],
    [{'LEMMA': 'short'}, {'LEMMA': 'term'}, {'LEMMA': 'renter'}, {'LEMMA': 'coverage'}]
]
home_rules['rental_income_coverage'] = [
    [{'LEMMA': 'rental'}, {'LEMMA': 'income'}, {'LEMMA': 'coverage'}],
    [{'LEMMA': 'loss'}, {'LEMMA': 'of'}, {'LEMMA': 'rent'}]
]
home_rules['seasonal_home_coverage'] = [{'LEMMA': 'seasonal'}, {'LEMMA': 'home'}, {'LEMMA': 'coverage'}]
home_rules['seasonal_home_theft_coverage'] = [{'LEMMA': 'seasonal'}, {'LEMMA': 'home'}, {'LEMMA': 'theft'}, {'LEMMA': 'coverage'}]
home_rules['employee_compensation_coverage'] = [{'LEMMA': 'employee'}, {'LEMMA': 'compensation'}, {'LEMMA': 'coverage'}]
home_rules['identity_theft_coverage'] = [{'LEMMA': 'identity'}, {'LEMMA': 'theft'}, {'LEMMA': 'coverage'}]
home_rules['trace_access_coverage'] = [
    [{'LEMMA': 'trace'}, {}, {'LEMMA': 'access'}, {'LEMMA': 'cover'}],
    [{'LEMMA': 'trace'}, {}, {'LEMMA': 'access'}, {'LEMMA': 'leak'}]
]
home_rules['underground_service'] = [
    [{'LEMMA': 'underground'}, {}, {'LEMMA': 'service'}],
    [{'LEMMA': 'underground'}, {'LEMMA': 'service'}]
]
home_rules['home_alterations_coverage'] = [
    [{'LEMMA': 'alteration'}, {}, {}, {'LEMMA': 'home'}]
]
home_rules['home_sale_coverage'] = [
    [{'LEMMA': 'sale'}, {}, {}, {'LEMMA': 'home'}],
    [{'LEMMA': 'sell'}, {}, {'LEMMA': 'home'}]
    ]
home_rules['home_emergency_cover'] = [
    [{'LEMMA': 'Home'}, {}, {}, {'LEMMA': 'Emergency'}, {'LEMMA': 'Assistance'}],
    [{'LOWER': 'home'}, {'LEMMA': 'Emergency'}, {'LEMMA': 'Assistance'}],
    [{'LOWER': 'home'}, {'LOWER': 'emergency'}, {'LOWER': 'cover'}]
    ]
home_rules['home_contents_cover'] = [{'LEMMA': 'Home'}, {}, {}, {'LEMMA': 'Home'}]
home_rules['accidental_damage_cover'] = [
    [{'LOWER': 'buildings'}, {}, {'LOWER': 'accidental'}, {}, {'LOWER': 'damage'}],
    [{'LOWER': 'accidental'}, {'LOWER': 'damage'}, {}, {'LOWER': 'buildings'}],
    [{'LOWER': 'accidental'}, {'LOWER': 'damage'}, {}, {'LOWER': 'cover'}],
    [{'LOWER': 'accidental'}, {'LOWER': 'breakage'}]
]
home_rules['replacement_locks_cover'] = [
    [{'LOWER': 'replacement'}, {}, {'LOWER': 'locks'}],
    [{'LOWER': 'replacement'}, {'LOWER': 'locks'}]
    ]
home_rules['emergency_access'] = [
    [{'LOWER': 'emergency'}, {}, {'LOWER': 'access'}],
    [{'LOWER': 'emergency'}, {'LOWER': 'access'}]
    ]
home_rules['personal_belongings'] = [{'LEMMA': 'personal'}, {'LEMMA': 'belonging'}]
home_rules['garden_cover'] = [{'LOWER': 'garden'}, {'LOWER': 'cover'}]
home_rules['pedal_cycle_cover'] = [
    [{'LEMMA': 'pedal'}, {'LEMMA': 'cycle'}, {'LOWER': 'cover'}],
    [{'LOWER': 'bicycle'}, {'LOWER': 'cover'}]
    ]
home_rules['legal_expenses'] = [{'LOWER': 'legal'}, {'LOWER': 'expenses'}]
home_rules['legal_cover'] = [{'LOWER': 'legal'}, {'LOWER': 'cover'}]
home_rules['removed_fixtures'] = [{'LOWER': 'removed'}, {'LOWER': 'fixtures'}, {'LOWER': 'and'}, {'LOWER': 'fittings'}]
home_rules['lock_replacement'] = [{'LOWER': 'lock'}, {'LOWER': 'replacement'}]
home_rules['debris_removal'] = [{'LOWER': 'debris'}, {'LOWER': 'removal'}]
home_rules['damage_underground_pipes'] = [{'LOWER': 'damage'}, {}, {'LOWER': 'underground'}, {'LOWER': 'pipes'}]
home_rules['increased_water_charges'] = [{'LOWER': 'increased'}, {'LOWER': 'water'}, {'LOWER': 'charges'}]
home_rules['building'] = [{'LOWER': 'building', 'IS_TITLE': True, 'POS': 'NOUN'}]
home_rules['property'] = [{'LOWER': 'property', 'IS_TITLE': True, 'POS': 'NOUN'}]
home_rules['terrorism'] = [{'LOWER': 'terrorism', 'IS_TITLE': True, 'POS': 'PROPN'}]
home_rules['engineering'] = [{'LOWER': 'engineering', 'IS_TITLE': True, 'POS': 'PROPN'}]
home_rules['money_malicious_attack'] = [{'LOWER': 'money'}, {'LOWER': 'and', 'OP': '?'}, {'LOWER': 'malicious'}, {'LOWER': 'attack'}]

# Personal property in a care facility
# Damage to underground pipes


