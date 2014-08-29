#!/usr/bin/python
import sys
import pdb
# Get Input Words
	# Output list of Words
def get_input_words(filename):
	words_file = open(filename,'r')
	list_of_words = []
	for line in words_file:
		for word in line.split():
			list_of_words.append(word.strip())
	return list_of_words

#Create Dictionary
	#output dict of Words

def dict_create():
	dictionary_file = open('dictionary.txt','r')
	dictionary_of_words = {}
	for word in dictionary_file:
		dictionary_of_words[word.strip()]=True
	return dictionary_of_words


#Sanitize Input
	#modify list of Words
def sanitize_input(list_to_sanitize):
	sanitized_list = list_to_sanitize
	return sanitized_list

#Create list of misspelled Words
	#output list of misspelled Words
def spellcheck(words_to_check, dictionary_of_words):
	wrong_words = []
	for word in words_to_check:
		if word not in dictionary_of_words:
			wrong_words.append(word)
	return wrong_words

#Give user a chance to correct
	#output list of Words
def user_fix_words(wrong_words):
	print 'you messed up the following %d words' % (len(wrong_words))
	print wrong_words

#output corrected text
	#doc out
def output_corrected_text():
	print 'the text has now been corrected!'

#runner
def main():
    if len(sys.argv) != 2:
        print 'Please specify the file to spellcheck'
        sys.exit(1)
    else:
		which_file = sys.argv[1]
		dictionary_of_words = dict_create() #make the dictionary
		input_words = get_input_words(which_file) #make the words list from the filename passed via commandline
		sanitized_words = sanitize_input(input_words) #clean it up
		misspelled_words = spellcheck(sanitized_words, dictionary_of_words) #spellcheck the cleaned up words, should be returning messed up words
		user_fix_words(misspelled_words) #fix the wrong words
		output_corrected_text() #operation complete text, could save file

if __name__ == '__main__':
	main()	