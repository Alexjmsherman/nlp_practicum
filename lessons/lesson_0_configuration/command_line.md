

## Command Line:
      Reference: https://www.git-tower.com/blog/posts/command-line-cheat-sheet

**View directory and files**

- print working directory

      pwd

 - list files and directories

       ls
      
**Navigate directories**
 - change directory

       cd [path]

       cd Desktop


**Create Files and Directories**
 - create a directory

       mkdir
       
       mkdir test

 - create a file
              
       touch

       touch new.txt

**Copy/Move files**
 - copy a file

       cp

       cp  new.txt new1.txt


- move or rename a file

      mv
        
      mv new1.txt new2.txt
**Observe files**
- view the first rows of a file

      head
- view the last rows of a file

      tail 
- view the entire file all at once

      cat
- view the files by scrolling through it

      less

**Find Files**
 - find a file

       find

       find . -name 'pattern'
  
  - find  a file using a regex pattern (* = match any character multiple times) to match all csv files
          
        find . -name '*csv'
  
  - find  a file using a regex pattern (? = match any single character) to match all csv or tsv files

        find . -name '*.?sv'

**Grep Files**
 - find a pattern in a file

       grep

       grep 'pattern' filename

- recursively look for the pattern across files

      grep -r 'pattern'


**Write output to file **
    
  - export       
   
        >

        find . -name '*.csv' > output.txt

**Command Substitution**
 - use the result of a command as a variable

       $()

       cp $(find . -name '*.csv') .

**Pipes**
 
- combine (chain) commands
           
      |
      
      find . -name '*csv' | sort > output.txt

**Remove Files/Directories**
 - remove a file or directory

       rm

       rm new.txt
       rm -r test

**Permissions**
       
- chmod and permission number explanations: 


      chmod 
      
      https://www.linux.org/threads/file-permissions-chmod.4124/
      https://help.ubuntu.com/community/FilePermissions

-----------------------------------------
## TEXT EDITOR: VIM

**Open text editor**
      
    vim

Insert mode (to add new text)
          
    i

Exit vim

    press Esc
    press Shift and colon

    exiting vim analysis: https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/

To quit without saving, type:

    q!
To quit and save (write), type:

    wq

-----------------------------------------
## GITHUB

**Clone GitHub Account**
      
   Set up Git username and email

    git config --global user.name ‘John Doe’
    
    git config --global user.email ‘johndoe@example.com’
    
    git config --global core.editor ’C:\Program Files\Sublime Text 3\subl.exe’

   copy the files of a git repo locally
    
    git clone [url]
    
    git clone https://github.com/Alexjmsherman/nlp_practicum_cohort1
