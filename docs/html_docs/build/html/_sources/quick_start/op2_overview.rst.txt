############
OP2 Overview
############

The examples and demos below are meant as a tutorial on how to use the pyNastran ``pyNastran.op2.op2.OP2`` class. 

The OP2 is preferred as it is much faster and easier to parse. How fast? 

- 2 GB OP2 in 4 seconds
- 8 GB file in 15 seconds
- 60 GB file in 1-2 minutes

.. note:: A static model is a SOL 101 or SOL 144. A dynamic/"transient" solution is any transient/modal/load step/frequency based solution (e.g. 103, 109, 145)

.. toctree::
   :maxdepth: 2
   
   ./op2_examples/op2_demos.rst
   ./op2_examples/op2_examples.rst
