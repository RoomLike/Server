#!/usr/bin/python
from bottle import SimpleTemplate

tpl = SimpleTemplate('Hello {{name}}!')
#tpl.render(name='World')
