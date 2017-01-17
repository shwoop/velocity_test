velocity_test
===

This is a simple framework to test out the apache velocity template engine
without requiring any further programming knowledge.

Please place any templates into the "templates" directory.
Please refer to the "config.py" file for instructions on how to register the
template to a url and provide some context to feed the template.

The framework uses airspeed to render velocity templates in python so the
lightweight flask framework could be used.

[apache velocity](http://velocity.apache.org/)
[flask](http://flask.pocoo.org/)
[airspeed](https://github.com/purcell/airspeed)
