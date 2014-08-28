#!/usr/bin/python
def main():
	words_file = open('alice.txt','r')
	dictionary_file = open('dictionary.txt','r')
	dictionary_of_words = {}
	words_string = dictionary_file.read()
	exclude = set(string.punctuation)
	s = ''.join(ch for ch in s if ch not in exclude)
	# for word in dictionary_file:
	# 	dictionary_of_words[word.strip()]=True
	# list_of_words = []
	# wrong_words = []
	# for line in words_file:
	# 	for word in line.split():
	# 		list_of_words.append(word.strip())
	# for word in list_of_words:
	# 	if word not in dictionary_of_words:
	# 		wrong_words.append(word)
	# print wrong_words

if __name__ == '__main__':
  main()