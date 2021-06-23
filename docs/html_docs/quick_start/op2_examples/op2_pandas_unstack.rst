#################################
Manipulating the Pandas DataFrame
#################################

The Jupyter notebook for this demo can be found in: 

- docs/quick_start/demo/op2_pandas_unstack.ipynb 
- https://github.com/SteveDoyle2/pyNastran/tree/master/docs/quick_start/demo/op2_pandas_unstack.ipynb

This example will use pandas unstack. The unstack method on a DataFrame moves on index level from rows to columns. First let’s read in some data:

.. code:: ipython3

    import os
    import pyNastran
    pkg_path = pyNastran.__path__[0]
    from pyNastran.op2.op2 import read_op2
    import pandas as pd
    pd.set_option('precision', 2)
    
    op2_filename = os.path.join(pkg_path, '..', 'models', 'iSat', 'iSat_launch_100Hz.op2')
    from pyNastran.op2.op2 import read_op2
    isat = read_op2(op2_filename, build_dataframe=True, debug=False, skip_undefined_matrices=True)

.. raw:: html

    <text style=color:green>INFO:    op2_scalar.py:1588           op2_filename = 'c:\\nasa\\m4\\formats\\git\\pynastran\\pyNastran\\..\\models\\iSat\\iSat_launch_100Hz.op2'
    </text>

.. parsed-literal::

    self.cannot apply column_names=['Mode', 'Freq'] to RealStrainEnergyArray: 'QUAD4'
    self.cannot apply column_names=['Mode', 'Freq'] to RealStrainEnergyArray: 'TRIA3'
    self.cannot apply column_names=['Mode', 'Freq'] to RealStrainEnergyArray: 'HEXA'
    self.cannot apply column_names=['Mode', 'Freq'] to RealStrainEnergyArray: 'BAR'
    self.cannot apply column_names=['Mode', 'Freq'] to RealStrainEnergyArray: 'BUSH'

.. code:: ipython3

    cbar = isat.cbar_force[1].data_frame

.. code:: ipython3

    cbar.head()

.. include:: ./table_12.rst.txt

First I’m going to pull out a small subset to work with

.. code:: ipython3

    csub = cbar.loc[3323:3324,1:2]
    csub

.. include:: ./table_13.rst.txt

I happen to like the way that’s organized, but let’s say that I want the have the item descriptions in columns and the mode ID’s and element numbers in rows. To do that, I’ll first move the element ID’s up to the columns using a .unstack(level=0) and the transpose the result:

.. code:: ipython3

    csub.unstack(level=0).T

.. include:: ./table_14.rst.txt

unstack requires unique row indices so I can’t work with CQUAD4 stresses as they’re currently output, but I’ll work with CHEXA stresses. Let’s pull out the first two elements and first two modes:

.. code:: ipython3

    chs = isat.chexa_stress[1].data_frame.loc[3684:3685,1:2]
    chs

.. include:: ./table_15.rst.txt

Now I want to put ElementID and the Node ID in the rows along with the Load ID, and have the items in the columns:

.. code:: ipython3

    cht = chs.unstack(level=[0,1]).T
    cht

.. include:: ./table_16.rst.txt

Maybe I’d like my rows organized with the modes on the inside. I can do that by swapping levels:

We actually need to get rid of the extra rows using dropna():

.. code:: ipython3

    cht = cht.dropna()
    cht

.. include:: ./table_17.rst.txt

.. code:: ipython3

    # mode, eigr, freq, rad, eids, nids # initial
    # nids, eids, eigr, freq, rad, mode # final
    
    cht.swaplevel(0,4).swaplevel(1,5).swaplevel(2,5).swaplevel(4, 5)

.. include:: ./table_18.rst.txt


Alternatively I can do that by first using reset_index to move all the index columns into data, and then using set_index to define the order of columns I want as my index:

.. code:: ipython3

    cht.reset_index().set_index(['ElementID','NodeID','Mode','Freq']).sort_index()

.. include:: ./table_19.rst.txt
