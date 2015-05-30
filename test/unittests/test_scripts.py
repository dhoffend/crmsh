# Copyright (C) 2014 Kristoffer Gronlund <kgronlund@suse.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#


from os import path
from nose.tools import eq_
from crmsh import scripts

scripts._script_dirs = lambda: [path.join(path.dirname(__file__), 'scripts')]


def test_list():
    eq_(set(['v2', 'legacy', 'xml']), set(scripts.list_scripts()))


def test_load_legacy():
    script = scripts.load_script('legacy')
    assert script is not None
    eq_('legacy', script.name)


def test_load_xml():
    script = scripts.load_script('xml')
    assert script is not None
    eq_('xml', script.name)


def test_load_v2():
    script = scripts.load_script('v2')
    assert script is not None
    eq_('v2', script.name)
    eq_('Apache Webserver', script.shortdesc)
    eq_({}, script)
