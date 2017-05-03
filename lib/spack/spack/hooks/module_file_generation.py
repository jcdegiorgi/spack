##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
import spack.modules
import spack.modules.common
import llnl.util.tty as tty

try:
    enabled = spack.modules.common.configuration['enable']
except KeyError:
    tty.debug('NO MODULE WRITTEN: list of enabled module files is empty')
    enabled = []


def _for_each_enabled(pkg, method_name):
    """Calls a method for each enabled module"""
    for name in enabled:
        generator = spack.modules.module_types[name](pkg.spec)
        getattr(generator, method_name)()


post_install = lambda pkg: _for_each_enabled(pkg, 'write')
post_uninstall = lambda pkg: _for_each_enabled(pkg, 'remove')
