from flask import Markup
# Markup转义HTML标签
x = Markup('<strong>hello %s</strong>') % '<p>langzi</p>'
print(x)
print(Markup(x).striptags)
print(Markup.escape(x))
