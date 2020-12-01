# -*- coding: utf-8 -*-

def like(text, pattern, x='*'):
    """ simple pattern matching with * """
    if pattern.startswith(x) and pattern.endswith(x):
        return pattern.strip(x) in text
    elif pattern.startswith(x):
        return text.endswith(pattern.strip(x))
    elif pattern.endswith(x):
        return text.startswith(pattern.strip(x))
    elif x in pattern:
        start, end = pattern.split(x)
        return text.startswith(start) and text.endswith(end)
    else:
        return text == pattern


if __name__ == '__main__':
    text = 'thankspleasesorry'
    assert like(text, text)
    assert like(text, '*thanks*')
    assert like(text, '*please*')
    assert like(text, '*sorry*')
    assert like(text, 'thanks*')
    assert like(text, '*sorry')
    assert not like(text, '*thanks')
    assert not like(text, '*please')
    assert not like(text, 'please')
    assert not like(text, 'please*')
    assert not like(text, 'sorry*')
