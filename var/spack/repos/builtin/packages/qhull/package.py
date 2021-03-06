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
from spack import *

class Qhull(Package):
    """Qhull computes the convex hull, Delaunay triangulation, Voronoi
       diagram, halfspace intersection about a point, furt hest-site
       Delaunay triangulation, and furthest-site Voronoi diagram. The
       source code runs in 2-d, 3-d, 4-d, and higher dimensions. Qhull
       implements the Quickhull algorithm for computing the convex
       hull. It handles roundoff errors from floating point
       arithmetic. It computes volumes, surface areas, and
       approximations to the convex hull."""

    homepage = "http://www.qhull.org"

    version('master', git='https://github.com/qhull/qhull')
    version('7.2.0', 'e6270733a826a6a7c32b796e005ec3dc',
            url="http://www.qhull.org/download/qhull-2015-src-7.2.0.tgz")

    version('1.0', 'd0f978c0d8dfb2e919caefa56ea2953c',
            url="http://www.qhull.org/download/qhull-2012.1-src.tgz")

    # https://github.com/qhull/qhull/pull/5
    patch('qhull-iterator.patch', when='@1.0')
    patch('pkgconfig.patch', when='@7.2.0')
    patch('intel_compiler.patch', when='%intel@:16')
    
    depends_on('cmake')

#    def setup_dependent_environment(self, spack_env, run_env, extension_spec):
#        spack_env.prepend('PKG_CONFIG_PATH', self.prefix.lib)
   
    def install(self, spec, prefix):
        with working_dir('spack-build', create=True):
            cmake('..', *std_cmake_args)
            make()
            make("install")
