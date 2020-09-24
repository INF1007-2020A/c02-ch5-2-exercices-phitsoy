#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	num_letters=0
	for chr in text:
		num_letters += int(chr.isalnum())
	# 	if text.isalnum:
	# 		num_letters+=1
	return num_letters
	#return len([None for chr in text if chr.isalnum()])

def get_word_length_histogram(text):
	histogram = [0]
	for word in text.split():
		length = get_num_letters(word)
		if length >= len(histogram):
			histogram += [0] * (length - len(histogram) + 1)
		histogram[length] += int (length != 0)

	return histogram

def format_histogram(histogram):
	ROW_CHAR = "*"

	#alignment=len(str(len(histogram)-1))
	# result=""
	# for i, elem in enumerate(histogram):
	# 	if i == 0:
	# 		continue
	# 	result+= f"{i : >{alignment}} {ROW_CHAR*elem}" + "\n"
	# return result
	#return "\n".join([f"{i : >{alignment}} {ROW_CHAR * elem}" for i, elem in enumerate(histogram) if i != 0])
	return "\n".join([f"{i : >{len(str(len(histogram)-1))}} {ROW_CHAR * elem}" for i, elem in enumerate(histogram) if i != 0])

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	height=max(histogram)
	result=""
	# for i in range(height-1, -1, -1):
	# 	for elem in histogram:
	# 		if elem >= i + 1:
	# 			result += BLOCK_CHAR
	# 		else: result += " "
	# 	result += "\n"
	# result += LINE_CHAR * len(histogram)
	# return result

	for i in range(height-1, -1, -1):
		result += "".join([BLOCK_CHAR if elem >= i + 1 else " " for elem in histogram[1:]]) + "\n"
	result += LINE_CHAR * len(histogram)
	return result


if __name__ == "__main__":
	print(get_num_letters("Hello."))
	print(get_word_length_histogram("Hello, you! dog-catcher"))
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
