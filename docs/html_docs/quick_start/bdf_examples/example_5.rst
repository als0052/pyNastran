.. _bdf-example-5-get-elements-by-node-id:

##################################
Example 5: Get Elements by Node ID
##################################
This example will demonstate:

 - getting the list of elements that share a certain node

our model

.. code-block:: python

    >>> import pyNastran
    >>> pkg_path = pyNastran.__path__[0]
    >>> test_path = os.path.join(pkg_path, '..', 'models', 'solid_bending')
    >>> bdf_filename = os.path.join(test_path, 'solid_bending.bdf')

instantiate the model

.. code-block:: python

    >>> from pyNastran.bdf.bdf import BDF
    >>> model = BDF()
    >>> model.read_bdf(bdf_filename, xref=True)
    >>> f = open('junk.out', 'w')

given a Node, get the Elements Attached to that Node

assume node 55

doesnt support 0d/1d elements yet

.. code-block:: python

    >>> nid_to_eids_map = model.get_node_id_to_element_ids_map()
    >>> eids = nid_to_eids_map[55]

convert to elements instead of element IDs

.. code-block:: python

    >>> elements = []
    >>> for eid in eids:
    >>>     elements.append(model.Element(eid))
    >>> print("eids = %s" % eids)
    >>> print("elements =\n %s" % elements)
