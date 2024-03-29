# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-TODAY OpenERP S.A. <http://www.openerp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

RELEASE_LEVELS = [ALPHA, BETA, RELEASE_CANDIDATE, FINAL] = ['alpha', 'beta', 'candidate', 'final']
RELEASE_LEVELS_DISPLAY = {ALPHA: ALPHA,
                          BETA: BETA,
                          RELEASE_CANDIDATE: 'rc',
                          FINAL: ''}

# version_info format: (MAJOR, MINOR, MICRO, RELEASE_LEVEL, SERIAL)
# inspired by Python's own sys.version_info, in order to be
# properly comparable using normal operarors, for example:
#  (6,1,0,'beta',0) < (6,1,0,'candidate',1) < (6,1,0,'candidate',2)
#  (6,1,0,'candidate',2) < (6,1,0,'final',0) < (6,1,2,'final',0)
version_info = (7, 0, 0, FINAL, 0)
version = '.'.join(map(str, version_info[:2])) + RELEASE_LEVELS_DISPLAY[version_info[3]] + str(version_info[4] or '')
serie = major_version = '.'.join(map(str, version_info[:2]))

description = 'OpenERP Server'
long_desc = '''OpenERP is a complete ERP and CRM. The main features are accounting (analytic
and financial), stock management, sales and purchases management, tasks
automation, marketing campaigns, help desk, POS, etc. Technical features include
a distributed server, flexible workflows, an object database, a dynamic GUI,
customizable reports, and XML-RPC interfaces.
'''
classifiers = """Development Status :: 5 - Production/Stable
License :: OSI Approved :: GNU Affero General Public License v3
Programming Language :: Python
"""
url = 'http://www.openerp.com'
author = 'OpenERP S.A.'
author_email = 'info@openerp.com'
license = 'AGPL-3'

nt_service_name = "openerp-server-" + serie

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
version = "7.0-20130830-231101"
# server bzr version: 5060 launchpad_translations_on_behalf_of_openerp-20130830052438-jvtrussyel6pvhct on lp:~openerp/openobject-server/7.0
# addons bzr version: 9401 dle@openerp.com-20130830125155-1vedifnupu2xvth7 on lp:~openerp/openobject-addons/7.0
# web bzr version: 4022 launchpad_translations_on_behalf_of_openerp-20130830052505-e346k0xxesqii63n on lp:~openerp/openerp-web/7.0
