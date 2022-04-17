from pygal_maps_world.i18n import COUNTRIES # changed in pygal

for country_code in sorted(COUNTRIES.keys()):
	print(country_code, COUNTRIES[country_code])
