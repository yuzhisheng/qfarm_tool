from flask import render_template
from app import app

from os.path import dirname, basename, isfile
import glob
import sys
modules = glob.glob(dirname(__file__)+"/*.py")
plugin_modules = [basename(f)[:-3] for f in modules if isfile(f) and basename(f).startswith("plugin") ]
print sys.stderr, plugin_modules


import pkgutil

# this is the package we are inspecting -- for example 'email' from stdlib
# import email



@app.route('/')
def index():
    for importer, modname, ispkg in pkgutil.iter_modules("plugins"):
        print sys.stderr, "Found submodule %s (is a package: %s)" % (modname, ispkg)
    return render_template('index.html')

@app.route('/getPage')
def getPage():
    index = request.args.get('index', 0, type=int)
    return jsonify(result=render_template('hello.html') + str(index))