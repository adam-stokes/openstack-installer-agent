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

from tornado.web import RequestHandler
from uoiagent.routes import route


@route('/install/single')
class SingleInstallHandler(RequestHandler):
    def post(self):
        # run single install steps
        pass


@route('/install/multi')
class MultiInstallHandler(RequestHandler):
    def post(self):
        # run single install steps
        pass


@route('/install/landscape')
class LandscapeInstallHandler(RequestHandler):
    def post(self):
        # run single install steps
        pass
