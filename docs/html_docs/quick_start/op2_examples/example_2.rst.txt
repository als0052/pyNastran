.. _op2-example-2-displacement-static:

################################
Example 2: Displacement (static)
################################
This example will demonstate:

 - calculating total deflection of the nodes for a static case for an OP2
 - calculate von mises stress and max shear


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

we're analyzing a static problem, so itime=0

we're also assuming subcase 1

.. code-block:: python

    >>> itime = 0
    >>> isubcase = 1

get the displacement object

.. code-block:: python

    >>> disp = model.displacements[isubcase]

displacement is an array

.. code-block:: python

    # data = [tx, ty, tz, rx, ry, rz]
    # for some itime
    # all the nodes -> :
    # get [tx, ty, tz] -> :3
    >>> txyz = disp.data[itime, :, :3]

calculate the total deflection of the vector

.. code-block:: python

    >>> from numpy.linalg import norm
    >>> total_xyz = norm(txyz, axis=1)

since norm's axis parameter can be tricky, we'll double check the length

.. code-block:: python

    >>> nnodes = disp.data.shape[1]
    >>> assert len(total_xyz) == nnodes

we could also have found nnodes by using the attribute.

It has an underscore because the object is also used for elements.  The underscore name is the SORT1 name, but your data may be in SORT2 format.

.. code-block:: python

    >>> nnodes2 = disp._nnodes
    >>> assert nnodes == nnodes2
    >>> assert nnodes == 72

Additionally, we know we have 72 nodes from the shape:

.. code-block:: python

    op2.displacements[1]
      type=RealDisplacementArray nnodes=72
      data: [t1, t2, t3, r1, r2, r3] shape=[1, 72, 6] dtype=float32
      gridTypes
      lsdvmns = [1]

now we'll loop over the nodes and print the total deflection

.. code-block:: python

    >>> msg = 'nid, gridtype, tx, ty, tz, txyz'
    >>> print(msg)
    >>> for (nid, grid_type), txyz, total_xyzi in zip(disp.node_gridtype, txyz, total_xyz):
    >>>     msg = '%s, %s, %s, %s, %s, %s' % (nid, grid_type, txyz[0], txyz[1], txyz[2], total_xyzi)
    >>>     print(msg)

    nid, gridtype, tx, ty, tz, txyz
    1, 1, 0.00764469, 4.01389e-05, 0.000111137, 0.00764561
    2, 1, 0.00762899, 5.29171e-05, 0.000142154, 0.0076305
    3, 1, 0.00944763, 6.38675e-05, 7.66179e-05, 0.00944816
    4, 1, 0.00427092, 2.62277e-05, 7.27848e-05, 0.00427162
    5, 1, 0.00152884, 1.71054e-05, -3.47525e-06, 0.00152894
    ...
