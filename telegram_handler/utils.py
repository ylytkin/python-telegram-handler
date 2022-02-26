import re
from typing import List

__all__ = [
    'close_open_tags',
    'excape_html',
]

TAG_REGEXP = re.compile('<(/?)([^/]+?)>')


def get_open_tags(text: str) -> List[str]:
    tags = []
    
    for match in TAG_REGEXP.finditer(text):
        suffix, tag = match.groups()
        
        if suffix == '':
            tags.append(tag)
        else:
            if len(tags) == 0 or tags[-1] != tag:
                raise ValueError(f'invalid string structure: {text}')
        
            tags.pop()
            
    return tags


def close_open_tags(text: str) -> str:
    for tag in get_open_tags(text):
        text += f'</{tag}>'
        
    return text


def escape_html(text):
    """
    Escapes all html characters in text

    :param str text:
    :rtype: str
    """
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
