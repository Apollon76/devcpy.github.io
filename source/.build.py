import sys
import os
import re


tags = {'header': 'header.html',
        'newsbar': 'newsbar.html',
        'footer': 'footer.html', }

def get_content(filename: str):
    with open(filename) as f:
        text = f.read()
    return text

def get_tag_content(matched):
    global tags

    if matched.group(1) in tags:
        return get_content(tags[matched.group(1)])
    else:
        return ''

def build(filename: str):
    text = get_content(filename)
    new_text = re.sub(r'<!-- (\w+) ?-->', get_tag_content, text)
    with open('../' + filename, 'w') as f:
        f.write(new_text)

def main():
    for filename in os.listdir('.'):
        if os.path.splitext(filename)[1] == '.html':
            build(filename)

main()
