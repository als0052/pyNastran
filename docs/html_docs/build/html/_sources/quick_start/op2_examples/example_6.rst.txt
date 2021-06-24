.. _op2-example-6-composite-plate-stress-static:

##########################################
Example 6: Composite Plate Stress (static)
##########################################
This example will demonstate:

 - print the fiber distance and the max principal stress for a static case for an OP2

our model

.. code-block:: python

    >>> import pyNastran
    >>> pkg_path = pyNastran.__path__[0]
    >>> test_path = os.path.join(pkg_path, '..', 'models', 'sol_101_elements')
    >>> op2_filename = os.path.join(test_path, 'static_solid_shell_bar.op2')

instantiate the model

.. code-block:: python

    >>> from pyNastran.op2.op2 import OP2
    >>> model = OP2()
    >>> model.read_op2(op2_filename)
    >>> print(model.get_op2_stats())
    op2.ctria3_composite_stress[1]
      type=RealCompositePlateStressArray nelements=4 ntotal=18
      data: [1, ntotal, 9] where 9=[o11, o22, t12, t1z, t2z, angle, major, minor, max_shear]
      data.shape = (1, 18, 9)
      element types: CTRIA3
      lsdvmns = [1]
    >>> isubcase = 1
    >>> itime = 0 # this is a static case
    >>> stress = model.ctria3_composite_stress[isubcase]

In the previous example, we had an option for a variable number of nodes for the CQUAD4s (1/5), but only nnodes=1 for the CTRIA3s.

In this example, we have 4 layers on one element and 5 on another, but they're all at the centroid.

.. code-block:: python

 #[o11, o22, t12, t1z, t2z, angle, major, minor, ovm]
    >>> eids = stress.element_layer[:, 0]
    >>> layers = stress.element_layer[:, 1]
    >>> maxp = stress.data[itime, :, 6]
    >>> if stress.is_fiber_distance():
    >>>     fiber_dist = stress.data[itime, :, 0]
    >>> else:
    >>>     raise RuntimeError('found fiber curvature; expected fiber distance')
    >>> maxp = stress.data[itime, :, 5]
    >>> for (eid, layer, maxpi) in zip(eids, layers, maxp):
    >>>     print(eid, 'CEN/4', layer, maxpi)

    7  CEN/4 1  89.3406
    7  CEN/4 2  89.3745
    7  CEN/4 3  89.4313
    7  CEN/4 4  89.5115
    8  CEN/4 1 -85.6691
    8  CEN/4 2 -85.6121
    8  CEN/4 3 -85.5193
    8  CEN/4 4 -85.3937
    8  CEN/4 5 -85.2394
    9  CEN/4 1  86.3663
    9  CEN/4 2  86.6389
    9  CEN/4 3  87.0977
    9  CEN/4 4  87.7489
    10 CEN/4 1 -87.6962
    10 CEN/4 2 -87.4949
    10 CEN/4 3 -87.1543
    10 CEN/4 4 -86.6662
    10 CEN/4 5 -86.0192
