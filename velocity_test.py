#!/usr/bin/python
import os
from flask import Flask
from airspeed import Template
from config import config

app = Flask(__name__)


@app.route("/")
def index():
    return """
<html>
  <body>
    <h1>
      Velocity templating engine test framework.
    </h1>
    <p>
      Please refer to the config.py file for registering new endpoints.
    </p>
  </body>
</html>"""


def create_view(t, c):
    def callable():
        return Template(t).merge(c)
    return callable


if __name__ == "__main__":
    for conf in config:
        try:
            url, template, context = conf
        except:
            print "Bad formatted config entry: %s" % conf
            continue
        if type(context) is not dict:
            print "Skipping %s entry as final context is not a dict" % url
            continue
        template = "templates/%s" % template
        if not os.path.isfile(template):
            print "Cannot find template (%s)" % template
            continue
        with open(template) as f:
            template = f.read()
        app.add_url_rule(
            url,
            url.replace("/", "_"),
            create_view(template, context)
        )
    app.run()
