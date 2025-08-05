def file_type_getter(file_extension_tuples):

    extension_list = {}

    for file, spec in file_extension_tuples:
        for file_type in spec:
            extension_list[file_type] = file
    
    get_file_type = lambda file_type: extension_list.get(file_type, "Unknown")
    
    return get_file_type

file_extension_tuples = [
    ("document", [".doc", ".docx", ".pdf", ".txt"]),
    ("image", [".jpg", ".jpeg", ".png", ".gif", ".bmp"]),
    ("audio", [".mp3", ".wav", ".flac"]),
    ("video", [".mp4", ".avi", ".mov", ".mkv"]),
    ("archive", [".zip", ".rar", ".7z", ".tar.gz"]),
    ("code", [".py", ".js", ".java", ".c", ".cpp"]),
    ("spreadsheet", [".xls", ".xlsx", ".csv"]),
    ("presentation", [".ppt", ".pptx"]),
]

get_file_type = file_type_getter(file_extension_tuples)

print(get_file_type(".docx"))
print(get_file_type(".png"))
print(get_file_type(".mp3"))
print(get_file_type(".unknown"))