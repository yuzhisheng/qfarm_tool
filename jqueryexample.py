import flask
import subprocess
import time          #You don't need this. Just included it so you can see the output stream.
import sys
from flask import Flask, jsonify, render_template, request

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',content= "hello.html")

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

app.run(debug=True, port=5000, host='0.0.0.0')

