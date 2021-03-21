#!/bin/bash

# Write a bash script to:
# Create twenty-five empty (0 KB) files (Hint: Use the touch command).
# The file names should be <yourName><number>, <yourName><number+1>, <yourName><number+2> and so on.
# Design the script so that each time you execute it, it creates the next batch of 25 files
# with increasing numbers starting with the last or max number that already exists.
# Do not hard code these numbers. You need to generate them using automation. Test the script.
# Display a long list of the directory and its contents to validate that the script created the expected files.
# Save the script and make a note of its location (absolute path) for future reference.

#search for file name, if exists, move on with function, if not, use original
#User name input:
echo "Please input first and last name, separated by _ :"
read name
#identifying the first variable by counting the number of files in the directory 
#that begin the username and include a number in the name
filenum=$(ls | grep "$name[0-9]*.txt" | wc -l)
#Where should the next batch of files created start numbering?
str=$(($filenum+1))
#Where should the next batch of files end numbering?
end=$(($str+24))
#If files already exist, then filenum will be > 0, so execute the sequence from str to end
if [[ $filenum -gt 0 ]]; then
    for i in $(seq $str $end); do
    touch $name$i".txt"
    done
else #if files don't already exist, simply create the file.
    for i in {1..25}; do
        touch $name$i".txt"
    done
fi
