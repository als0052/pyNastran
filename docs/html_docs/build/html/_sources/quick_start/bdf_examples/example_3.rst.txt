.. _bdf-example-3-printing-elements-properties:

#######################################
Example 3: Printing Elements/Properties
#######################################
Print the Element ID and associated Node and Property to an Output File

.. note:: This skips rigidElements

This example will demonstate:

 - using the BDF class to write cards/properties

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

    >>> for eid, element in sorted(model.elements.items()):
    >>>     f.write(element.write_card(size=8, is_double=False))
    >>> for pid, prop in sorted(model.properties.items()):
    >>>     f.write(prop.write_card(size=8, is_double=False))

Method 2 - using built-in method
********************************

    >>> model._write_elements_properties(f)

Method 3 - using built-in methods
*********************************

    >>> model._write_elements(f)
    >>> model._write_properties(f)

.. todo:: one of method 3 and method 2 does not work?
