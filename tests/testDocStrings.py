import unittest
import doctest

def load_tests(loader, tests, ignore):
    # Module to exclude for doctest
    base_loaded = dir() + ['base_loaded']
    
    # import modules with docstring tests here
    #from foo import bar
    
    # Do set difference to find
    for_testing = set(dir()) - set(base_loaded)

    for module in for_testing:
        tests.addTests(doctest.DocTestSuite(locals()[module]))
    return tests
