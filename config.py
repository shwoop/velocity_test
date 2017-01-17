"""
Config for apache Velocity test suite.

config is a list of tuple objects detailing the url endpoint, the template to
render, and the context to render the template with.

Lets give an example:
    (
      "/nathalie",
      "nathalie.html",
      {"nathalie": {"name": "Nathalie", "gender": "female"}}
    ),

Here we are defining a url endpoitn of "nathalie", so when the app is running
we will be able to go to "localhost:5000/nathalie" to see our template.

The template in question is called "nathalie.html", the application will look
in the subfolder "templates" for something with that name.

The final option is the context, this is the dynamic data we will provide to
the script to render.  it is a dictionary of dictionaries.  (python
dictionaries are keys and values seperated by colons, surrounded by curly
braces)

Remember:
 * [...] is a list
 * {...} is a dictionary (key:value)
 * (...) is a tuple (same as list)
all are seperated with commas.
"""

config = [
    (
        "/nathalie",
        "nathalie.html",
        {"nathalie": {"name": "Nathalie", "gender": "female"}}
    ),
    (
        "/super/peoples",
        "super_peoples.html",
        {"peoples": [
            {"name": "Nathalie", "gender": "female"},
            {"name": "Alistair", "gender": "male"},
        ]},
    ),
]
