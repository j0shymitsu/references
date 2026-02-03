# Reading Files in Python

## Summary

In Python, you can read the contents of a file using the open() function within a with block. This ensures proper 
handling of file resources. When you open a file with open(), you can read its contents using methods like read(), which 
returns the entire content as a string.

## Docs

[Python with Statement](https://docs.python.org/3/reference/compound_stmts.html#with)\
[Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

## Examples

### Reading a file and printing its contents:
```python
with open('contents.txt') as file:
    content = file.read()
    print(content)
```
