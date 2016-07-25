import flask
from flask import Flask, jsonify, render_template, request
from app import app

PLUGIN_NAME="PUBLISH"



@app.route('/yield')
def proc():
    def inner():
        proc = subprocess.Popen(
            "python ./test.py",             #call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE
        )
        print sys.stderr, "proc end"
        for line in iter(proc.stdout.readline,''):
            time.sleep(0.2)                           # Don't need this just shows the text streaming
            yield line.rstrip() + '<br/>\n'

    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

