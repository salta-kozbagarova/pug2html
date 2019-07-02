paired_tags = [
    'html',
    'body',
    'p',
    'a',
    'span',
    'ul',
    'li',
    'table',
    'tbody',
    'thead',
    'tr',
    'td',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'section',
    'head',
    'style',
    'script',
    'title',
    'div',
    'form',
    'select',
    'option',
    'textarea'
]

unpaired_tags = [
    'img',
    'meta',
    'link',
    'br',
    'hr',
    'input'
]

tags = {
    'html': {
        'paired': True
    },
    'body': {
        'paired': True
    },
    'p': {
        'paired': True
    },
    'a': {
        'paired': True
    },
    'span': {
        'paired': True
    },
    'ul': {
        'paired': True,
        'has_children': True
    },
    'li': {
        'paired': True,
        'parent': 'ul'
    },
    'table': {
        'paired': True,
        'has_children': True
    },
    'tbody': {
        'paired': True,
        'parent': 'table',
        'has_children': True
    },
    'thead': {
        'paired': True,
        'parent': 'table',
        'has_children': True
    },
    'tr': {
        'paired': True,
        'parent': 'thead',
        'has_children': True
    },
    'td': {
        'paired': True,
        'parent': 'thead'
    },
    'h1': {
        'paired': True
    },
    'h2': {
        'paired': True
    },
    'h3': {
        'paired': True
    },
    'h4': {
        'paired': True
    },
    'h5': {
        'paired': True
    },
    'section': {
        'paired': True
    },
    'head': {
        'paired': True
    },
    'style': {
        'paired': True
    },
    'script': {
        'paired': True
    },
    'title': {
        'paired': True
    },
    'div': {
        'paired': True
    },
    'form': {
        'paired': True
    },
    'select': {
        'paired': True
    },
    'option': {
        'paired': True
    },
    'textarea': {
        'paired': True
    },
    'img': {
        'unpaired': True
    },
    'meta': {
        'unpaired': True
    },
    'link': {
        'unpaired': True
    },
    'br': {
        'unpaired': True
    },
    'hr': {
        'unpaired': True
    },
    'input': {
        'unpaired': True
    }
}