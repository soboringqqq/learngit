favorite_language = {
    'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print(favorite_language['sarah'] + '\n')

for key, language in favorite_language.items(): # loop all key-value
	print("\nKey:" + key)
	print("language:" + language)
print("\n")

for name in favorite_language.keys(): # loop all key
	print(name.title())

for name in favorite_language: # same with keys()
	print(name.title())

for language in favorite_language.values(): # loop all values
	print(language)
print("\n")

for language in set(favorite_language.values()): # unique items in dictionary
	print(language)
