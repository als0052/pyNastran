.. _bdf-example-4-get-element-id-type:

################################
Example 4: Get Element ID & Type
################################
Print the Element ID and its type(e.g. CQUAD4, CTRIA3, etc.) to a file

.. note:: This skips rigidElements

This example will demonstate:

 - accessing element type information

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

Method 1 - using objects
************************

    >>> for eid,element in sorted(model.elements.items()):
    >>>     msg = 'eid=%s type=%s\n' %(eid, element.type)
    >>> f.write(msg)
