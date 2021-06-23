.. _op2-example-5-iso-plate-stress-static:

##########################################
Example 5: Isotropic Plate Stress (static)
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

    op2.cquad4_stress[1]
      type=RealPlateStressArray nelements=2 nnodes_per_element=5 nlayers=2 ntotal=20
      data: [1, ntotal, 8] where 8=[fiber_distance, oxx, oyy, txy, angle, omax, omin, von_mises]
      data.shape=(1L, 20L, 8L)
      element types: CQUAD4
      lsdvmns = [1]
    >>> isubcase = 1
    >>> itime = 0 # this is a static case
    >>> stress = model.cquad4_stress[isubcase]
    >>> assert stress.nnodes == 5, 'this is a bilinear quad'

write the data

.. code-block:: python

    #[fiber_dist, oxx, oyy, txy, angle, majorP, minorP, ovm]
    >>> eids = stress.element_node[:, 0]
    >>> nids = stress.element_node[:, 1]
    >>> if stress.is_fiber_distance():
    >>>     fiber_dist = stress.data[itime, :, 0]
    >>> else:
    >>>     raise RuntimeError('found fiber curvature; expected fiber distance')
    >>> maxp = stress.data[itime, :, 5]
    >>> for (eid, nid, fdi, maxpi) in zip(eids, nids, fiber_dist, maxp):
    >>>     print(eid, 'CEN/4' if nid == 0 else nid, fdi, maxpi)

    6 CEN/4 -0.125 8022.26
    6 CEN/4  0.125 12015.9
    6 4     -0.125 7580.84
    6 4      0.125 11872.9
    6 1     -0.125 8463.42
    6 1      0.125 12158.9
    6 14    -0.125 8463.69
    6 14     0.125 12158.9
    6 15    -0.125 7581.17
    6 15     0.125 11872.9
    7 CEN/4 -0.125 10016.3
    7 CEN/4  0.125 10019.5
    7 3     -0.125 10307.1
    7 3      0.125 10311.0
    7 2     -0.125 9725.54
    7 2      0.125 9727.9
    7 17    -0.125 9725.54
    7 17     0.125 9728.06
    7 16    -0.125 10307.1
    7 16     0.125 10311.1

Note we have 2 layers (upper and lower surface) for any PSHELL-based elements
