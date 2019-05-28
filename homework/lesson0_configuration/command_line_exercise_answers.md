# Command Line Exercise Homework

FOR THE QUESTIONS 3-6,
PLEASE INCLUDE BOTH THE ANSWER AND THE COMMAND LINE COMMAND YOU USED TO GET THE ANSWER

#### 1. cd in to the configuration_files directory: (raw_data/configuration_files)

#### 2. How many aws_config_files directories are there (e.g. aws_config_files_1)?
There are 5 aws_config_files

#### 3. In which directory is config42.ini?
aws_config_files_4

- option 1 - search for the full file name
find . -name 'config42.ini'
- option 2 - search for the a subset of the file name
find . -name '*42*'

#### 4. Use a find, a pipe, and wc to count how many config files exist in aws_config_files_3.
19
- find aws_config_files_3 -name '*ini' | wc -l

#### 5. What is the output region specified in config33.ini
us-west-2

- find which dir contains the config file
	- find . -name '*33*'
- cd into that dir
	-	cd aws_config_files_5
- view the config file (you can also use head, tail, or less)
	- cat config33.ini

#### 6. Use grep to search which file contains the term 'exercise_answer' and provide the answer/
file: aws_config_files_4/config42.ini
answer: 42

- find the file that contains exercise_answer
	- grep -rl 'exercise_answer' .
-  view the file to find the answer
	 - cat aws_config_files_4/config42.ini

#### 7. BONUS use $() to copy all of the .ini files into a new directory called all_ini
- create a new directory
	- mkdir all_ini
- copy all the .ini files into all_ini
	- cp $(find . -name '*.ini') all_ini
