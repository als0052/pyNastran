.. _bdf-example-1-readwrite:

#####################
Example 1: Read/Write
#####################
this example will demonstate:

 - reading the BDF

 - getting some basic information

 - writing the BDF

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
    >>> model.read_bdf(bdf_filename)

For unicode:

  The standard encoding is utf-8, but most English decks should use latin1 and will fail with utf-8.

  If you just have ascii, then you don't need to worry about the encoding.

.. code-block:: python

    >>> model.read_bdf(bdf_filename, encoding='latin1')

print information about the model

.. code-block:: python

    >>> print(model.get_bdf_stats())
    ---BDF Statistics---
    SOL 101
    
    bdf.loads[1]
      FORCE:   23
    
    bdf.loads[2]
      LOAD:    1
    
    bdf.params
      PARAM    : 2
    
    bdf.nodes
      GRID     : 72
    
    bdf.elements
      CTETRA   : 186
    
    bdf.properties
      PSOLID   : 1
    
    bdf.materials
      MAT1     : 1
    
    bdf.coords
      CORD2R   : ???

write the file

.. code-block:: python

    >>> bdf_filename_out = os.path.join(test_path, 'solid_bending_out.bdf')
    >>> model.write_bdf(bdf_filename_out)

looking at the output

.. code-block:: python

    >>> print(file_slice(bdf_filename_out, 94, 100))
    GRID          71         .500008 1.61116      3.
    GRID          72         .500015 1.00001      3.
    $ELEMENTS_WITH_PROPERTIES
    PSOLID         1       1
    CTETRA         1       1       8      13      67      33
    CTETRA         2       1       8       7      62      59

write the file with large field format; double precision

.. code-block:: python

    >>> bdf_filename_out2 = os.path.join(test_path, 'solid_bending_out2.bdf')
    >>> model.write_bdf(bdf_filename_out2, size=16, is_double=False)
    >>> print(file_slice(bdf_filename_out2, 166, 175))
    GRID*                 71                         .500008         1.61116
    *                     3.
    GRID*                 72                         .500015         1.00001
    *                     3.
    $ELEMENTS_WITH_PROPERTIES
    PSOLID         1       1
    CTETRA         1       1       8      13      67      33
    CTETRA         2       1       8       7      62      59
    CTETRA         3       1       8      45      58      66

write the file with large field format; double precision

.. code-block:: python

    >>> bdf_filename_out3 = os.path.join(test_path, 'solid_bending_out3.bdf')
    >>> model.write_bdf(bdf_filename_out3, size=16, is_double=True)
    >>> print(file_slice(bdf_filename_out3, 166, 175))
    GRID*                 71                5.0000800000D-011.6111600000D+00
    *       3.0000000000D+00
    GRID*                 72                5.0001500000D-011.0000100000D+00
    *       3.0000000000D+00
    $ELEMENTS_WITH_PROPERTIES
    PSOLID         1       1
    CTETRA         1       1       8      13      67      33
    CTETRA         2       1       8       7      62      59
    CTETRA         3       1       8      45      58      66
