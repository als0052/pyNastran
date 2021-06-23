#############################
Calling pyNastran from MATLAB
#############################

pyNastran also supports MATLAB through the MATLAB/Python interface. [Information about setting up MATLAB with Python can be found here.](http://www.mathworks.com/help/MATLAB/MATLAB-engine-for-python.html?s_tid=gn_loc_drop)

Note About Speed
****************
There are two ways to pull large data from Python to Nastran.

   1.  Use the MATLAB-Python Interface
   2.  Do an MATLAB call to Python, dump your OP2 results matrices using to hdf5 (using h5py) and load them into and load them MATLAB. It's recommended that you don't use scipy's MAT reader as it seems to be buggy, not to mention that hdf5 has replaced the MAT format in MATLAB.

Intuitively, it seems to that Option #1 should be faster, but for large problems, that doesn't seem to be the case.  Then again, Option #1, would be probably be better for any geometry related operation.  In other words, test it.

Working around MATLAB's oddities
********************************
Replace the base redirectstdout.m file (that for my installation is located in the following folder):

    ``C:\Program Files\MATLAB\MATLAB Production Server\R2015a\toolbox\MATLAB\external\interfaces\python\+python\+internal\redirectstdout.m``

with this file:

    https://github.com/SteveDoyle2/pyNastran/tree/master/docs/pyNastran_in_MATLAB_example/redirectstdout/redirectstdout.m

Also, instead of imports like:

    >>> import py.pyNastran.op2.op2.OP2

use:

    >>> import py.pyNastran.op2.op2.OP2.*
    >>> clear
    >>> import py.pyNastran.op2.op2.OP2.*
    >>> clear import
    >>> import py.pyNastran.op2.op2.OP2

If you don't need all this insanity, please post and say what you did.

.. toctree::
   :maxdepth: 1
   
   ./matlab_examples/example_1.rst
   ./matlab_examples/example_2.rst
