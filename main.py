import sys

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

from stats import num_words
from stats import count_characters
from stats import convert_dict_to_list

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	book_text = get_book_text(sys.argv[1])
	numberofwords = num_words(book_text)
	character_instances = count_characters(book_text)
	sorted_list = convert_dict_to_list(character_instances)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}")
	print("----------- Word Count ----------")
	print(f"Found {numberofwords} total words")
	print("--------- Character Count -------")
	
	for item in sorted_list:
		char = item["char"]
		if char.isalpha():
			print(f"{char}: {item['count']}")
	
	print("============= END ===============")

main()
