# -*- coding: utf-8 -*-

import inspect
import pickle


def save(var, filename=None):
    """ save var to filename using its variable name from outer scope
        e.g. file.save(var) saves var as "var.dat"
    """
    frame = inspect.currentframe()
    outer = inspect.getouterframes(frame)[1]
    fstr = inspect.getframeinfo(outer[0]).code_context[0]
    varname = fstr[fstr.index('(')+1:fstr.index(')')].split(', ')[0]
    if filename is None:
        filename = varname + '.dat'
    with open(filename, 'wb') as f:
        pickle.dump(var, f, pickle.HIGHEST_PROTOCOL)
    print(f'Saved {varname} to {filename}')


def load(filename):
    """ load the pickled data from filename
        e.g. var = file.load("var.dat") loads "var.dat"
    """
    if '.' not in filename:
        filename += '.dat'
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            print(f'Loaded {filename}')
            return data
    except FileNotFoundError:
        print(f'File not found: {filename}')
        return None
