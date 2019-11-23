#!/usr/bin/python3

__author__ = 'Jan Kempeneers'

from flask import Flask, stream_with_context, render_template, request, jsonify, Response
import time
import data
from datetime import datetime

app = Flask(__name__)

def stream_template(template_name, **context):
    # http://flask.pocoo.org/docs/patterns/streaming/#streaming-from-templates
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    # uncomment if you don't need immediate reaction
    ##rv.enable_buffering(5)
    return rv

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def index():
    ip_address = data.get_ip()
    return render_template('index.html', ip_address=ip_address)

@app.route('/demos', methods=('GET', 'POST'))
def hello():
    ip_address = data.get_ip()
    def f():
        while True:
            now = datetime.now().strftime("%Y.%m.%d|%H:%M:%S")
            yield str('{}'.format(now))
            time.sleep(1)
    if request.method == 'POST':
        def g():
            counter = int(request.form['counter'])
            for ctr in range(counter):
                time.sleep(1)
                yield str('{}'.format(ctr+1))
        return Response(stream_template('demos.html', ip_address=ip_address, data=stream_with_context(g()), data_cont=stream_with_context(f())))
        
    else:
        return Response(stream_template('demos.html', ip_address=ip_address, data_cont=stream_with_context(f())))
#        return render_template('demos.html', ip_address=ip_address)

@app.route('/variable', methods=('GET', 'POST'))
def variable():
    def g():
        x_axis_steps=10
        x_value=0
        while True:
            sine_datapoint = data.get_sine_datapoint(x_value)
            x_value += x_axis_steps
            yield str('{}'.format(sine_datapoint))
            # yield jsonify(sine_datapoint=sine_datapoint)
            time.sleep(1)
    return Response(stream_template('variable.html', data=(stream_with_context(g()))))

@app.route('/reboot')
def reboot():
    os.system('sudo reboot -h now')

@app.route('/shutdown')
def shutdown():
    os.system('sudo shutdown -h now')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)