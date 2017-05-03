from spack import *

import os

class Intelmpi(Package):
    """
    Intel (R) MPI Library 5.1 focuses on making applications perform better on Intel (R) architecture based
    clusters implementing the high performance Message Passing Interface Version 3.0 specification on multiple fabrics.
    It enables you to quickly deliver maximum end user performance even if you change or upgrade to new interconnects,
    without requiring changes to the software or operating environment.
    """
    homepage = 'https://software.intel.com/en-us/intel-mpi-library'
    url = 'fakeurl'
    licensed = True
    only_binary = True

    version('5.1.1')

    provides('mpi')

    def install(self, spec, prefix):
        if '%intel' not in spec:
            raise InstallError('IntelMPI : must use intel compiler')

    def setup_dependent_package(self, module, dep_spec):
        # FIXME : This is done in the wrong way
        # FIXME : It should be dep_spec not self.spec
        self.spec.mpicc = join_path(self.prefix, 'bin64', 'mpiicc')
        self.spec.mpicxx = join_path(self.prefix, 'bin64', 'mpiicpc')
        self.spec.mpifc = join_path(self.prefix, 'bin64', 'mpiifort')
        self.spec.mpif77 = join_path(self.prefix, 'bin64', 'mpiifort')
        self.spec.mpicxx_shared_libs = [
            join_path(self.prefix.lib64, 'libmpicxx.so'),
            join_path(self.prefix.lib64, 'libmpi.so')
        ]

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        """
        For dependencies, make mpicc's use spack wrapper.
        """
        spack_env.set('MPICH_CC' , 'icc')
        spack_env.set('MPICH_CXX', 'icpc')
        spack_env.set('MPICH_F77', 'ifort')
        spack_env.set('MPICH_F90', 'ifort')

        spack_env.set('I_MPI_ROOT',  '/ssoft/spack/external/intel/2016/impi/5.1.3.210')
        spack_env.set('I_MPI_PMI_LIBRARY',  '/usr/lib64/libpmi.so')
        spack_env.set('IPATH_NO_CPUAFFINITY',  '1')

        spack_env.prepend_path('PATH', '/ssoft/spack/external/intel/2016/impi/5.1.3.210/bin64')
        spack_env.set('MPICC', 'mpiicc')
        spack_env.set('MPICXX', 'mpiicpc')
        spack_env.set('MPIFC', 'mpiifort')
        spack_env.set('MPIF90', 'mpiifort')
        spack_env.set('MPIF77', 'mpiifort')
