def num_words(string):
	list_of_words = string.split()
	wordcount = len(list_of_words)
	return wordcount

def count_characters(characters):
	character_dictionary = {}
	for character in characters:
		character = character.lower()
		if character in character_dictionary:
			character_dictionary[character] += 1
		else:
			character_dictionary[character] = 1
	return character_dictionary

def convert_dict_to_list(char_dict):
	chars_list = [] 
	for char, count in char_dict.items():
		char_info = {"char": char, "count": count}
		chars_list.append(char_info)

	def sort_on(dict_item):
		return dict_item["count"]

	chars_list.sort(reverse=True, key=sort_on)

	return chars_list


