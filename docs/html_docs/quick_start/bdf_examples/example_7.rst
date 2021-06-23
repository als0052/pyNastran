.. _bdf-example-7-get-elements-by-material-id:

######################################
Example 7: Get Elements by Material ID
######################################
This example will demonstate:

 - getting a list of elements that have a certain material

our model

.. code-block:: python

    >>> import pyNastran
    >>> pkg_path = pyNastran.__path__[0]
    >>> test_path = os.path.join(pkg_path, '..', 'models', 'sol_101_elements')
    >>> bdf_filename = os.path.join(test_path, 'static_solid_shell_bar.bdf')

instantiate the model

.. code-block:: python

    >>> from pyNastran.bdf.bdf import BDF
    >>> model = BDF()
    >>> model.read_bdf(bdf_filename, xref=True)
    >>> f = open('junk.out', 'w')

assume you want the eids for material 10

.. code-block:: python

    >>> pid_to_eids_map = model.get_property_id_to_element_ids_map()
    >>> mid_to_pids_map = model.get_material_id_to_property_ids_map()
    >>> pids1 = mid_to_pids_map[1]
    >>> print('pids1 = %s' % pids1)
    pids1 = [1, 2, 3, 4, 5]
    >>> eids = []
    >>> for pid in pids1:
    >>>     eids += pid_to_eids_map[pid]

convert to elements instead of element IDs

.. code-block:: python

    >>> elements = []
    >>> for eid in eids:
    >>>     element = model.Element(eid)
    >>>     elements.append(element)
    >>>     print(str(element).rstrip())
    
    CBAR          13       1      15      19      0.      1.      0.
    $ Direct Text Input for Bulk Data
    $ Pset: "shell" will be imported as: "pshell.1"
    CHEXA          1       2       2       3       4       1       8       5
                   6       7
    CPENTA         2       2       6       8       5      10      11       9
    CPENTA         3       2       6       7       8      10      12      11
    CTETRA         4       2      10      11       9      13
    CTETRA         5       2      10      12      11      13
    CROD          14       3      16      20
    CROD          15       3      17      21
    CQUAD4         6       4       4       1      14      15
    CQUAD4         7       4       3       2      17      16
    CTRIA3         8       4       4       3      16
    CTRIA3         9       4      16      15       4
    CTRIA3        10       4       1       2      17
    CTRIA3        11       4      17      14       1
    $
    CBEAM         12       5      14      18      0.      1.      0.     GGG
