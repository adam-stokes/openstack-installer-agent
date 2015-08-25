# Copyright (C) 2015 Adam Stokes
# Copyright (C) 2015 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .routes import route
from tornado.web import Application
from tornado import ioloop
import configparser


class Agent:
    def __init__(self, opts):
        self.opts = opts
        self.config = configparser.ConfigParser()
        self.config.read('/etc/openstack/agent.conf')
        self.port = self.config['runtime']['port']
        if self.opts.port:
            self.port = self.opts.port

    def run(self):
        settings = {}
        application = Application(route.get_routes(), **settings)
        application.listen(self.opts.port)
        ioloop.IOLoop.current().start()
