#!/usr/bin/env python
# Filename: ConEmu_msg_writer.py

"""
This module contains functions that read the .html formatted ouput from the 
ConEmu editor during a sphinx compilation session. These functions look for 
specific kinds of html tags and extract those lines to lists. 

Those lists contain error messages, warning messages, or blank lines (I 
think?). These different message lists are then written to separate output 
files to make reading through error and warning messages easier. 

The full .html file form ConEmu is huge for PyNastran. So far I can't find a 
way to make Sphinx only log the errors and warnings to the console either. 

Created by als0052
Created on 05-06-2021
Updated on 05-06-2021
"""

from pathlib import Path
import re


def read_file(fn):
	"""Read the contents of the HTML file
	
		:param fn: The html file to read
		:type fn: Pathlike, str
	"""
	with open(fn, 'r', encoding='utf-8') as fin:
		html_content = fin.read()
	return html_content


def get_errors(html_file):
	"""Find all the error lines in the html file
	
		:param html_file: The html code or file to search
		:type html_file: str
	"""
	error_regex = re.compile(r'(?<=<br> )(<span style="color: #DC322F; .*)')
	return error_regex.findall(html_file)


def get_warnings(html_file):
	"""Find all the warning lines in the html file
	
		:param html_file: The html code or file to search
		:type html_file: str
	"""
	warning_regex = re.compile(r'(?<=<br> )(<span style="color: #CB4B16; .*)')
	return warning_regex.findall(html_fie)


def get_blank_lines(html_file):
	"""Find all the blank lines in the html file
	
		:param html_file: The html code or file to search
		:type html_file: str
	"""
	blank_lines_regex = re.compile(
		r'(?<=<br> )(<span style="color: #EEE8D5; .*)')
	return blank_lines_regex.findall(html_file)


def write_to_files(fn, msg_dict):
	"""Write the messages to separate files
		
		:param fn: The basic file to write to. Note that nothing will be 
			written to this exact file, but slighlty differently named 
			versions of this file.
		:type fn: Pathlike, str
		:param msg_dict: The dictionary containing the lists of error 
			messages, warning messages, and blank line messages. Must have 
			the following keys: ``errors``, ``warnings``, ``blank_lines``
		:type msg_dict: dict
	"""
	fn = Path(fn)
	basic_name = fn.name
	fnouts = {
		'errors': fn.parent.with_name(f'{basic_name}_errors.txt'),
		'warnings': fn.parent.with_name(f'{basic_name}_warning.txt'),
		'blank_lines': fn.parent.with_name(f'{basic_name}_blanks.txt')}
	
	for key, msg_list in msg_dict.items():
		# key is the type of message list
		# msg_list is the list of messages
		fnout = fnouts[key]  # Output filename
		with open(fnout, 'w', encoding='utf-8') as fout:
			for msg in msg_list:
				print(msg, file=fout)
	print(f'Finished writing output files.')
	return None


if __name__ == "__main__":
	raise NotImplementedError(f'TODO: Finish this script')
