#!/usr/bin/env python
import sys
import unittest

from flask_assets import ManageAssets
from flask_script import Manager, Shell

from expressvpn_web import app

manager = Manager(app)

logger = app.logger


@manager.command
def test():
    tests = unittest.TestLoader().discover('tests', pattern='*.py')
    results = unittest.TextTestRunner(verbosity=1).run(tests)
    if not results.wasSuccessful():
        sys.exit(1)


manager.add_command("shell", Shell(use_ipython=True, use_bpython=False))
# work-around bug in flask-assets
app.jinja_env.assets_environment.environment = app.jinja_env.assets_environment
manager.add_command("assets", ManageAssets(app.jinja_env.assets_environment))
manager.run()
