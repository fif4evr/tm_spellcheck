#!/usr/bin/python
import sys
import pdb

class Word():
	def __init__(self, value, line, index):
		self.value = value
		self.line = line
		self.index = index

	def __repr__(self):
		return 'val: '+ self.value + ', location: ('  + str(self.line) + ', ' + str(self.index) + ')'
	#define a Word class with a location and value


# Get Input Words
	# Output list of Words
def get_input_words(filename):
	words_file = open(filename,'r')
	list_of_words = []
	for line_index, line in enumerate(words_file):
		for word_index, word in enumerate(line.split()):
			# add words and location to list
			list_of_words.append(Word(word.strip(), line_index, word_index))
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
		if word.value not in dictionary_of_words:
			wrong_words.append(word)
	return wrong_words

#Give user a chance to correct
	#output list of Words
def user_fix_words(input_words, wrong_words):
	print 'you messed up the following %d words: %s' % (len(wrong_words), wrong_words)

	corrected_words = []
	for wrong_word in wrong_words:
		wrong_word.value = "BANG"
		corrected_words.append(wrong_word)
	return corrected_words
#make corrected text
	#list of text with corrected words out

def fix_corrected_words(input_words, corrected_words):
	x = 0
	output_words = []
	for input_word in input_words:
		if (input_word.line == corrected_words[x].line) and (input_word.index == corrected_words[x].index):
			input_word.value = corrected_words[x].value
			if x < len(corrected_words) - 1:
				x += 1
		output_words.append(input_word)
	return output_words


#output corrected text
	#doc out
def output_corrected_text(output_words):
	print "This is the output text: "
	print output_words

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
		wrong_words = spellcheck(sanitized_words, dictionary_of_words) #spellcheck the cleaned up words, should be returning messed up words
		corrected_words = user_fix_words(input_words, wrong_words) #fix the wrong words
		output_words = fix_corrected_words(input_words, corrected_words) #builds up a list of Words to output, making corrects as necessary
		output_corrected_text(output_words) #operation complete text, could save file

if __name__ == '__main__':
	main()	