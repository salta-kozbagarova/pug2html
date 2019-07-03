import tags
import re
import sys


pug_data = []
html_lines = []
html_line = None
tag = None
splitted_line = None
indent_tags = {}
first_ind_len = None


# Gets the number of indents before a tag
def get_indent_length(str):
    ind_len = len(str) - len(str.lstrip())
    return ind_len


# Removes all stored tags with an indent higher
# than `start_point` from `indent_tags` dict
def clear_indent_tags(start_point):
    keys = indent_tags.keys()    
    keys = list(filter(lambda x: x >= start_point, keys))
    for key in keys:
        indent_tags.pop(key, None)


def close_deeper_tags(start_point):
    _html_line = ''
    keys = indent_tags.keys()    
    keys = list(filter(lambda x: x > start_point, keys))
    keys.sort(reverse = True)
    for key in keys:
        tag = indent_tags.get(key).get('tag')
        tag_type = indent_tags.get(key).get('type')
        if tag_type == 'paired':
            _html_line += '</{}>\n'.format(tag)
        elif tag_type == 'unpaired':
            _html_line += '\n'
    return _html_line


def close_tags(start_point):
    _html_line = ''
    _html_line = close_deeper_tags(start_point)
    
    if start_point in indent_tags:
        prev_tag = indent_tags.get(start_point).get('tag')
        tag_type = indent_tags.get(start_point).get('type')
        if tag_type == 'paired':
            _html_line += '</{}>\n'.format(prev_tag)
        elif tag_type == 'unpaired':
            _html_line += '\n'

    clear_indent_tags(start_point)
    return _html_line


def get_tag_with_attrs(line):
    attrs = re.findall(r"(\w+)(\(.[^\)]*\))(.*)", line)
    if len(attrs) > 0:
        attrs = attrs[0]
        if len(attrs) == 3:
            tag = attrs[0]
            splitted_line = attrs[2]
            attrs = attrs[1][1:-1]
            attrs = re.findall(r"([\w-]+='.[^']*')", attrs)
            if len(attrs) == 0:
                return (None, '', '')
            else:
                attrs = ' ' + ' '.join(attrs)
                return (tag, attrs, splitted_line)
        else:
            return (None, '', '')
    else:
        return (None, '', '')


if __name__ == "__main__":

    args = sys.argv[1:]

    if len(args) < 2:
        raise Exception('Argument error: 2 arguments excepted')
    
    input_file = args[0]
    output_file = args[1]

    with open(input_file, 'r') as file:
        pug_data = file.readlines()


    if len(pug_data) > 0:
        first_line = pug_data[0]
        first_ind_len = get_indent_length(first_line)


    for line in pug_data:
        if len(line.strip()) == 0:
            html_lines.append('\n')
            continue
        html_line = ''
        ind_len = get_indent_length(line)
        html_line = close_tags(ind_len)
        line = line.strip()
        
        tag, attrs, splitted_line = get_tag_with_attrs(line)

        if not tag:
            splitted_line = line.split(' ')
            if len(splitted_line) <= 0:
                continue
            else:
                tag = splitted_line.pop(0)
                splitted_line = ' '.join(splitted_line)

        if line == 'doctype html':
        	html_line = '<!DOCTYPE html>\n'
        	html_lines.append(html_line)
        	continue

        if tag in tags.paired_tags:
            indent_tags[ind_len] = {'tag': tag, 'type': 'paired'}
            html_line += '<{}{}>'.format(tag, attrs)
            html_line += splitted_line + '\n'
        elif tag in tags.unpaired_tags:
            indent_tags[ind_len] = {'tag': tag, 'type': 'unpaired'}
            html_line += '<{}{}/>'.format(tag, attrs)
            html_line += splitted_line + '\n'
        elif tag == '|':
            indent_tags.pop(ind_len, None)
            html_line += '\n' + splitted_line
        elif tag[0] in ['#', '.']:
            attrs = re.findall(r"(#\w*\d*|\.\w*\d*)", tag)
            attr_id = ''
            attrs_classes = []
            for attr in attrs:
                if attr.startswith('#'):
                    attr_id = attr[1:]
                else:
                    attrs_classes.append(attr[1:])
            attr_line = ' id="{}"'.format(attr_id) if attr_id else ''
            attr_line += ' class="{}"'.format(' '.join(attrs_classes)) if len(attrs_classes) > 0 else ''
            indent_tags[ind_len] = {'tag': 'div', 'type': 'paired'}
            html_line += '<{}{}>'.format('div', attr_line)
            html_line += splitted_line + '\n'
        else:
            html_line += tag + ' ' + splitted_line + '\n'
        html_lines.append(html_line)

    if first_ind_len != None:
        html_line = close_tags(first_ind_len)
        html_lines.append(html_line)


    with open(output_file, 'w') as file:
        file.write(''.join(html_lines))
        print('Successfully converted!')