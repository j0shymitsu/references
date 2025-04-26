# BASH CHEAT SHEET

---


## Variables 
```bash

name="Josh"
echo "Hello, $name"

```

## Input
```bash

read -p "Enter your name: " name

```

## Arithmetic
``` bash

echo $((5 + 3))    # 8
let "x = 10 * 2"   # 20

```

## Conditionals
``` bash
if [ "$name" == "Josh" ]; then
    echo "Welcome!"
elif [ "$name" == "Root" ]; then
    echo "Admin access"
else
    echo "Access denied"
fi    # end if
```

## Loops
```bash 
for i in {1..5}; do
    echo "Iteration $i"
done

count=1
while[ $count -le 5 ]; do
    echo "Count is $count"
    ((count++))
done
```

## Arrays
```bash
fruits=("apple" "banana" "cherry")
echo ${fruits[1]}    # banana
```

# Functions
```bash
greet(){
    echo "Hello, $1!"
}
greet "Josh"
```

## File Tests
```bash
[ -f file.txt ]    # true if file exists
[ -d folder ]      # true if directory exists
[ -z "$var" ]      # true if variable is empty
```

## String Tests
```bash 
[ "$a" == "$b" ]    # equal
[ "$a" != "$b"]     # not equal
```

## File Ops
```bash
touch file.txt          # create a file
mkdir folder            # make directory
rm file.txt             # remove file
mv old.txt new.txt      # rename or move
cp file.txt backup.txt  # copy file
```

## Useful Commands
```bash
ls -la              # list all files in detail
pwd                 # print working directory
cd /path/to/dir     # change directory
cat file.txt        # view file contents
head file.txt       # first 10 lines
tail file.txt       # last 10 lines
grep "text" file    # search text
```

## Exit Codes
```bash
echo $?     # last commands exit status
```

## Shebang (first line in scripts)
```bash
!/bin/bash
```

## Misc
```bash
top    # tskmgr, essentially 
```

## grep
```bash
grep 'string' filename                  # Search for string in a file
grep 'string' file1 file2               # Search in multiple files
grep -r 'string' /path/to/directory     # Recursive search in directories

# Common Options; follow 'grep'
-i      # Ignore case
-w      # Match whole words only
-v      # Invert match (exclude lines with the pattern)
-n      # Show line numbers of matches
-c      # Count number of matching lines
-l      # List filenames with matches
-o      # Show only matching parts of lines
```

## lsd
```bash
lsd -la
lsd -lh
lsd -lS
lsd -ltr

lsd -d */
lsd --tree
```