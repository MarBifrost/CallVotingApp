encodings = ['utf-8', 'utf-16', 'latin-1', 'gbk', 'gb2312']

for encoding in encodings:
    try:
        with open('calls/models.py', 'r', encoding=encoding) as f:
            content = f.read()
        print(f"Successfully read with encoding: {encoding}")
        # If it worked, you can save the content in the correct encoding
        with open('calls/models.py', 'w', encoding='utf-8') as f:
            f.write(content)
        break  # Exit if successful
    except UnicodeDecodeError:
        print(f"Failed to read with encoding: {encoding}")