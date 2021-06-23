############
OP2 Overview
############

This is meant as a tutorial on how to use the pyNastran ``pyNastran.op2.op2.OP2`` class. This page runs through examples relating to the OP2. The OP2 is preferred as it is much faster and easier to parse.  How fast?  You can read a 2 GB OP2 in 4 seconds, an 8 GB file in 15 seconds, and a 60 GB file in 1-2 minutes.

.. note:: A static model is a SOL 101 or SOL 144. A dynamic/"transient" solution is any transient/modal/load step/frequency based solution (e.g. 103, 109, 145).


The **head**/**tail**/**file_slice** methods can be found at:

    https://github.com/SteveDoyle2/pyNastran/blob/v0.7/docs_sphinx/manual/py_docs/bdf_doc.py

These examples can be found at:

    https://github.com/SteveDoyle2/pyNastran/blob/v0.7/docs_sphinx/manual/py_docs/op2_doc.py

.. todo:: update where to get the head, tail, file_slice code from


.. toctree::
   :maxdepth: 2
   
   ./op2_examples/op2_demos.rst
   ./op2_examples/op2_examples.rst
