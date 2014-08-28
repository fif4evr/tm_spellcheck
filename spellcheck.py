#!/usr/bin/python
import sys
def spellcheck(filename):
	words_file = open(filename,'r')
	dictionary_file = open('dictionary.txt','r')
	dictionary_of_words = {}
	for word in dictionary_file:
		dictionary_of_words[word.strip()]=True
	list_of_words = []
	wrong_words = []
	for line in words_file:
		for word in line.split():
			list_of_words.append(word.strip())
	for word in list_of_words:
		if word not in dictionary_of_words:
			wrong_words.append(word)
	print wrong_words

def main():
  if len(sys.argv) != 2:
    print 'Please specify the file to spellcheck'
    sys.exit(1)
  else:
  	which_file = sys.argv[1]
  	spellcheck(which_file)

if __name__ == '__main__':
  main()