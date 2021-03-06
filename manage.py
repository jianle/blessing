# -*- coding: utf-8 -*-

from flask.ext.script import Manager, Server
from app import app
import web

manager = Manager(app)

manager.add_command("run", Server(host='0.0.0.0', port=5000, use_debugger=True))
manager.add_command("runserver", Server(host='0.0.0.0', port=5000, use_debugger=False))

if __name__ == '__main__':
  manager.run()
