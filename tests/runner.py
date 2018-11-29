# tests/runner.py
import unittest

# import your test modules

import login_scripts
import admin_scripts
import API_Scripts
import misc_scripts

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTest(loader.loadTestsFromModule(misc_scripts))
suite.addTest(loader.loadTestsFromModule(login_scripts))
suite.addTest(loader.loadTestsFromModule(admin_scripts))
suite.addTest(loader.loadTestsFromModule(API_Scripts))


# initialize a runner, pass it your suite and run it
executor = unittest.TextTestRunner(verbosity=3)
result = executor.run(suite)