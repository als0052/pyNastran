.. _op2-example-1-readwrite:

#####################
Example 1: Read Write
#####################
This example will demonstate:

 - reading the OP2
 - getting some basic information
 - writing the F06

our model

.. code-block:: python

    >>> import pyNastran
    >>> pkg_path = pyNastran.__path__[0]
    >>> test_path = os.path.join(pkg_path, '..', 'models', 'solid_bending')
    >>> op2_filename = os.path.join(test_path, 'solid_bending.op2')
    >>> f06_filename = os.path.join(test_path, 'solid_bending_out.f06')

instantiate the model

.. code-block:: python

    >>> from pyNastran.op2.op2 import OP2
    >>> model = OP2()
    >>> model.read_op2(op2_filename)
    >>> print(model.get_op2_stats())
    op2.displacements[1]
      type=RealDisplacementArray nnodes=72
      data: [t1, t2, t3, r1, r2, r3] shape=[1, 72, 6] dtype=float32
      gridTypes
      lsdvmns = [1]

    op2.spc_forces[1]
      type=RealSPCForcesArray nnodes=72
      data: [t1, t2, t3, r1, r2, r3] shape=[1, 72, 6] dtype=float32
      gridTypes
      lsdvmns = [1]

    op2.ctetra_stress[1]
      type=RealSolidStressArray nelements=186 nnodes=930
      nodes_per_element=5 (including centroid)
      eType, cid
      data: [1, nnodes, 10] where 10=[oxx, oyy, ozz, txy, tyz, txz, o1, o2, o3, von_mises]
      data.shape = (1, 930, 10)
      element types: CTETRA
      lsdvmns = [1]
    >>> model.write_f06(f06_filename)
    F06:
     RealDisplacementArray SUBCASE=1
     RealSPCForcesArray    SUBCASE=1
     RealSolidStressArray  SUBCASE=1 - CTETRA
    >>> print(tail(f06_filename, 21))
    0       186           0GRID CS  4 GP
    0                CENTER  X   9.658666E+02  XY  -2.978357E+01   A   2.559537E+04  LX-0.02 0.20 0.98  -1.094517E+04    2.288671E+04
                             Y   7.329372E+03  YZ   5.895411E+02   B  -7.168877E+01  LY-1.00-0.03-0.01
                             Z   2.454026E+04  ZX  -5.050599E+03   C   7.311813E+03  LZ 0.03-0.98 0.20
    0                     8  X   9.658666E+02  XY  -2.978357E+01   A   2.559537E+04  LX-0.02 0.20 0.98  -1.094517E+04    2.288671E+04
                             Y   7.329372E+03  YZ   5.895411E+02   B  -7.168877E+01  LY-1.00-0.03-0.01
                             Z   2.454026E+04  ZX  -5.050599E+03   C   7.311813E+03  LZ 0.03-0.98 0.20
    0                    62  X   9.658666E+02  XY  -2.978357E+01   A   2.559537E+04  LX-0.02 0.20 0.98  -1.094517E+04    2.288671E+04
                             Y   7.329372E+03  YZ   5.895411E+02   B  -7.168877E+01  LY-1.00-0.03-0.01
                             Z   2.454026E+04  ZX  -5.050599E+03   C   7.311813E+03  LZ 0.03-0.98 0.20
    0                     4  X   9.658666E+02  XY  -2.978357E+01   A   2.559537E+04  LX-0.02 0.20 0.98  -1.094517E+04    2.288671E+04
                             Y   7.329372E+03  YZ   5.895411E+02   B  -7.168877E+01  LY-1.00-0.03-0.01
                             Z   2.454026E+04  ZX  -5.050599E+03   C   7.311813E+03  LZ 0.03-0.98 0.20
    0                    58  X   9.658666E+02  XY  -2.978357E+01   A   2.559537E+04  LX-0.02 0.20 0.98  -1.094517E+04    2.288671E+04
                             Y   7.329372E+03  YZ   5.895411E+02   B  -7.168877E+01  LY-1.00-0.03-0.01
                             Z   2.454026E+04  ZX  -5.050599E+03   C   7.311813E+03  LZ 0.03-0.98 0.20
    1    MSC.NASTRAN JOB CREATED ON 28-JAN-12 AT 12:52:32                       JANUARY  28, 2012  pyNastran v0.7.1       PAGE     3

    1                                        * * * END OF JOB * * *
