.. _bdf-example-2-printing-nodes:

#########################
Example 2: Printing Nodes
#########################
This example will demonstate:

 - writing cards

our model:

.. code-block:: python

    >>> import pyNastran
    >>> pkg_path = pyNastran.__path__[0]
    >>> test_path = os.path.join(pkg_path, '..', 'models', 'solid_bending')
    >>> bdf_filename = os.path.join(test_path, 'solid_bending.bdf')

instantiate the model:

.. code-block:: python

    >>> from pyNastran.bdf.bdf import BDF
    >>> model = BDF()
    >>> model.read_bdf(bdf_filename, xref=True)
    >>> f = open('junk.out', 'w')

Method 1 - using objects
************************

GRIDs

.. code-block:: python

    >>> for nid,node in sorted(model.nodes.items()):
    >>>     f.write(node.write_card(size=8, is_double=False))

GRIDSET

.. code-block:: python

    >>> if model.gridSet:
    >>>     f.write(model.gridSet.write_card(size=8, is_double=False))

SPOINTs

.. code-block:: python

    >>> if model.spoints:
    >>>     f.write(model.spoints.write_card(size=8, is_double=False))

CORDx

.. code-block:: python

    >>> for cid,coord in sorted(model.coords.items()):
    >>>     if cid != 0:  # if CID=0 is the global frame, skip it
    >>>         f.write(coord)

Method 2 - using built-in methods
*********************************

    >>> model._write_nodes(f)
    >>> model._write_coords(f)
