def vowel_counter(func_to_decorate):
    vowel_count = 0
    
    def wrapper(doc):
        nonlocal vowel_count
        vowels = "aeiou"

        for char in doc:
            if char in vowels:
                vowel_count += 1

        print(f"Vowel count: {vowel_count}") 
        return func_to_decorate
    return wrapper

@vowel_counter
def process_doc(doc):
    print(f"Document: {doc}")

process_doc("What")
# Vowel count: 1
# Document: What

process_doc("a wonderful")
# Vowel count: 5
# Document: a wonderful

process_doc("world")
# Vowel count: 6
# Document: world

###

# ARGS AND KWARGS
def print_arguments(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print_arguments("hello", "world", a=1, b=2)

## 

def args_logger(*args, **kwargs):
    num_of_args = 1
    num_of_kwargs = 1

    if args:
        for item in args:
            print(f"{num_of_args}. {item}")
            num_of_args += 1
    
    if kwargs:
        kw = sorted(kwargs.items)
        for key, value in kw:
            print(f"* {key}: {value}")

##

def configure_plugin_decorator(func):
    def wrapper(*args):
        kwargs = dict(args)
        return func(**kwargs)
    return wrapper

##
def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        converted_args = list(map(convert_md_to_txt, args))

        def change_value(item):
            key, value = item
            return (key, convert_md_to_text(value))
        
        converted_kwargs = dict(map(change_value, kwargs.items()))

        return func(*converted_args, **converted_kwargs)
    return wrapper


def convert_md_to_text(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")

    return "\n".join(lines)