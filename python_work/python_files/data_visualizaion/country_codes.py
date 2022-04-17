from pygal_maps_world.i18n import COUNTRIES  # changed in pygal

def get_country_code(country_name):
	"""Return the pygal 2-digit country code for the given country."""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
			
		# If the country wasn's found, return None.
	return None

# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))
# print(get_country_code('Zimbabwe'))

