def sum(a):
  def inner_sum(b):
    return a + b
  return inner_sum

print(sum(1)(2))
# prints 3

####

def converted_font_size(font_size):
    def doc_type(doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("invalid doc type")
    return doc_type

####

# currying is often used to change a function's signature to make it conform to a specific shape. For example:
def colorize(converter, doc):
  # ...
  converter(doc)
  # ...

###

def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_length(doc):
            count = 0
            split_doc = doc.split()
            for line in split_doc:
                if sequence in line:
                    count += 1
            return count
        return with_length
    return with_char

###

def create_markdown_image(alt_text):
    alt_text = "![" + alt_text + "]"
    
    def escape_characters(url):
        new_url = url.replace("(", "%28")
        new_url = new_url.replace(")", "%29")
        new_url = "(" + new_url + ")"
        appended_url = alt_text + new_url

        def quote_title(title=None):
            if title:
                title = '"' + title + '"'
                return appended_url[:-1] + " " + title + ")"
            else:
                return appended_url
        return quote_title
    return escape_characters
                
                
            
