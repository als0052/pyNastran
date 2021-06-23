.. _bdf-example-6-get-elements-by-property-id:

######################################
Example 6: Get Elements by Property ID
######################################
This example will demonstate:

 - getting a list of elements that have a certain property

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

Creating a List of Elements based on a Property ID

assume pid=1

.. code-block:: python

    >>> pid_to_eids_map = model.get_property_id_to_element_ids_map()
    >>> eids4  = pid_to_eids_map[4] # PSHELL
    >>> print("eids4 = %s" % eids4)
    eids4 = [6, 7, 8, 9, 10, 11]

convert to elements instead of element IDs

.. code-block:: python

    >>> elements4 = []
    >>> for eid in eids4:
    >>>     elements4.append(model.Element(eid))

just to verify

.. code-block:: python

    >>> elem = model.elements[eids4[0]]
    >>> print(elem.pid)
    PSHELL         4       1     .25       1               1
