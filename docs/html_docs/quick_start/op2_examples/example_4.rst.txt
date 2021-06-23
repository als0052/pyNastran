.. _op2-example-4-solid-stress-static:

################################
Example 4: Solid Stress (static)
################################
This example will demonstate:

 - calculate von mises stress and max shear for solid elements for a static case for an OP2

.. math:: \sqrt{T_x^2 + T_y^2 + T_z^2}

our model

.. code-block:: python

    >>> import pyNastran
    >>> pkg_path = pyNastran.__path__[0]
    >>> test_path = os.path.join(pkg_path, '..', 'models', 'solid_bending')
    >>> op2_filename = os.path.join(test_path, 'solid_bending.op2')
    >>> out_filename = os.path.join(test_path, 'solid_bending.out')

instantiate the model

.. code-block:: python

    >>> from pyNastran.op2.op2 import OP2
    >>> model = OP2()
    >>> model.read_op2(op2_filename)
    >>> print(model.get_op2_stats())

    op2.ctetra_stress[1]
      type=RealSolidStressArray nelements=186 nnodes=930
      nodes_per_element=5 (including centroid)
      eType, cid
      data: [1, nnodes, 10] where 10=[oxx, oyy, ozz, txy, tyz, txz, o1, o2, o3, von_mises]
      data.shape = (1, 930, 10)
      element types: CTETRA
      lsdvmns = [1]

we're analyzing a static problem, so itime=0

we're also assuming subcase 1

.. code-block:: python

    >>> itime = 0
    >>> isubcase = 1

get the stress object (there is also cpenta_stress and chexa_stress as well as ctetra_strain/cpenta_strain/chexa_strain)

.. code-block:: python

    >>> stress = model.ctetra_stress[isubcase]

The stress/strain data can often be von_mises/max_shear (same for fiber_distance/curvature), so check!

.. code-block:: python

     #data = [oxx, oyy, ozz, txy, tyz, txz, o1, o2, o3, von_mises]
    >>> o1 = stress.data[itime, :, 6]
    >>> o3 = stress.data[itime, :, 8]
    >>> if stress.is_von_mises():
    >>>     max_shear = (o1 - o3) / 2.
    >>>     von_mises = stress.data[itime, :, 9]
    >>> else:
    >>>     from numpy import sqrt
    >>>     o2 = data[itime, :, 8]
    >>>     von_mises = sqrt(0.5*((o1-o2)**2 + (o2-o3)**2, (o3-o1)**2))
    >>>     max_shear = stress.data[itime, :, 9]
    >>> for (eid, node), vm, ms in zip(stress.element_node, von_mises, max_shear):
    >>>     print(eid, 'CEN/4' if node == 0 else node, vm, ms)

    1 CEN/4 15900.2 2957.35
    1 8     15900.2 2957.35
    1 13    15900.2 2957.35
    1 67    15900.2 2957.35
    1 33    15900.2 2957.35
    2 CEN/4 16272.3 6326.18
    2 8     16272.3 6326.18
    2 7     16272.3 6326.18
    2 62    16272.3 6326.18
    2 59    16272.3 6326.18

Note that because element_node is an integer array, the centroid is 0.  We renamed it to CEN/4 when we wrote it



.. .. todo:: There are two example 4's?
.. 
.. .. --------------------------------
.. .. Example 4: Solid Stress (static)
.. .. --------------------------------
.. This example will demonstate:
.. 
..  - calculating total deflection of the nodes for a dynamic case for an OP2
.. 
.. 
.. .. math:: \sqrt\left(T_x^2 + T_y^2 + T_z^2\right)
.. 
.. our model
.. 
.. .. code-block:: python
.. 
..     >>> import pyNastran
..     >>> pkg_path = pyNastran.__path__[0]
..     >>> test_path = os.path.join(pkg_path, '..', 'models', 'plate_py')
..     >>> op2_filename = os.path.join(test_path, 'plate_py.op2')
.. 
.. ut_filename = os.path.join(test_path, 'solid_bending.out')
.. 
.. instantiate the model
.. 
.. .. code-block:: python
.. 
..     >>> from pyNastran.op2.op2 import OP2
..     >>> model = OP2()
..     >>> model.read_op2(op2_filename)
..     >>> print(model.get_op2_stats())
.. 
..     op2.eigenvectors[1]
..       type=RealEigenvectorArray ntimes=10 nnodes=231
..       data: [t1, t2, t3, r1, r2, r3] shape=[10, 231, 6] dtype=float32
..       gridTypes
..       modes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
..     eigrs = [-0.00037413835525512695, -0.00022113323211669922, -0.0001882314682006836, -0.00010025501251220703, 0.0001621246337890625, 0.00
..     07478296756744385, 1583362560.0, 2217974016.0, 10409966592.0, 11627085824.0]
..     mode_cycles = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
..     >>> isubcase = 1
..     >>> eigenvector = model.eigenvectors[isubcase]
.. 
.. "time/mode/frequency are stored by id, so to get mode 5:
.. 
.. .. code-block:: python
.. 
..     >>> modes = eigenvector._times  # it may not be "time" so we don't use the name "time"
..     >>> from numpy import where
..     >>> imode5 = where(modes == 5)[0]
..     >>> txyz = eigenvector.data[imode5, :, :3]
.. 
.. calculate the total deflection of the vector
.. 
.. .. code-block:: python
.. 
..     >>> from numpy.linalg import norm
..     >>> total_xyz = norm(txyz, axis=1)
.. 
.. get the eigenvalue
.. 
.. .. code-block:: python
.. 
..     >>> print('eigr5 = %s' % eigenvector.eigrs[imode5])
..     eigr5 = 0.000162124633789
.. 