# -*- coding:utf-8 -*- 
from flask import render_template, request, jsonify
from app import app
import importlib, os, sys
import plugins

reload(sys)
sys.setdefaultencoding('utf8')

ALL_PLUGINS=[]

for plugin_name in plugins.__all__:
	plugin = importlib.import_module('app.plugins.' + plugin_name)
	ALL_PLUGINS.append(plugin)

for plugin in ALL_PLUGINS:
	print sys.stderr, plugin.PLUGIN_TITLE


@app.route('/')
def index():
    return render_template('index.html', plugin_titles = [plugin.PLUGIN_TITLE for plugin in ALL_PLUGINS])

@app.route('/getPage')
def getPage():
    index = request.args.get('index', 0, type=int)
    return jsonify(result=render_template('hello.html') + str(index))