#################################
Transient DataFrames in PyNastran
#################################

The Jupyter notebook for this demo can be found in: 

- docs/quick_start/demo/op2_pandas_DataFrames.ipynb 
- https://github.com/SteveDoyle2/pyNastran/tree/master/docs/quick_start/demo/op2_pandas_DataFrames.ipynb

We’ll use standard pyNastran methods to load a model. We’ll set ``build_dataframe=True`` to make pandas objects

.. code:: ipython3

    import os
    import pandas as pd
    pd.set_option('precision', 3)
    
    import pyNastran
    pkg_path = pyNastran.__path__[0]
    from pyNastran.op2.op2 import read_op2
    from pyNastran.utils.nastran_utils import run_nastran
    
    bdf_filename = os.path.join(pkg_path, '..', 'models', 'iSat', 'iSat_launch_100Hz.dat')
    op2_filename = os.path.join(pkg_path, '..', 'models', 'iSat', 'iSat_launch_100Hz.op2')
    if not os.path.exists(op2_filename):
        run_nastran(bdf_filename)
        assert os.path.exists(op2_filename)
    
    isat = read_op2(op2_filename, build_dataframe=True, debug=False, skip_undefined_matrices=True,
                    exclude_results='*strain_energy')


.. raw:: html

    <text style=color:green>INFO:    op2_scalar.py:1588           op2_filename = 'c:\\nasa\\m4\\formats\\git\\pynastran\\pyNastran\\..\\models\\iSat\\iSat_launch_100Hz.op2'
    </text>

Get a list of all objects:

.. code:: ipython3

    print(isat.get_op2_stats(short=True))

.. parsed-literal::

    op2_results.force.cbush_force[1]
    op2_results.force.cbar_force[1]
    op2_results.force.cquad4_force[1]
    op2_results.stress.chexa_stress[1]
    op2_results.strain.chexa_strain[1]
    eigenvectors[1]
    mpc_forces[1]
    grid_point_forces[1]
    cquad4_stress[1]
    cquad4_strain[1]
    cquad4_composite_stress[1]
    ctria3_composite_stress[1]
    cquad4_composite_strain[1]
    ctria3_composite_strain[1]
    

Access the DataFrames

.. code:: ipython3

    eigenvalues = None
    if len(isat.eigenvalues):
        print(isat.eigenvalues.keys())
        eigenvalues         = isat.eigenvalues[u'ISAT_SM_LAUNCH_4PT MODES TO 100 HZ'].data_frame
    eigenvectors            = isat.eigenvectors[1].data_frame
    mpc_forces              = isat.mpc_forces[1].data_frame
    grid_point_forces       = isat.grid_point_forces[1].data_frame
    cbar_force              = isat.cbar_force[1].data_frame
    cbush_force             = isat.cbush_force[1].data_frame
    cquad4_force            = isat.cquad4_force[1].data_frame
    cquad4_stress           = isat.cquad4_stress[1].data_frame
    chexa_stress            = isat.chexa_stress[1].data_frame
    cquad4_composite_stress = isat.cquad4_composite_stress[1].data_frame
    ctria3_composite_stress = isat.ctria3_composite_stress[1].data_frame
    cquad4_strain           = isat.cquad4_strain[1].data_frame
    chexa_strain            = isat.chexa_strain[1].data_frame
    cquad4_composite_strain = isat.cquad4_composite_strain[1].data_frame
    ctria3_composite_strain = isat.ctria3_composite_strain[1].data_frame
    #del isat

Now list each of the objects and be amazed!

.. code:: ipython3

    eigenvalues

.. code:: ipython3

    eigenvectors

.. include:: ./table_1.rst.txt

.. code:: ipython3

    mpc_forces

.. include:: ./table_2.rst.txt

Well maybe be less amazed by this one. If you know pandas and can fix it, here’s the code :) It’s supposed to have the Eigenvalues, Freq, and Cycles, at the top.

.. code:: ipython3

    import numpy as np
    import pandas as pd
    
    def build_dataframe_gpf(self):
        headers = self.get_headers()
        #name = self.name
        if self.is_unique:
            ntimes = self.data.shape[0]
            nnodes = self.data.shape[1]
            nvalues = ntimes * nnodes
            node_element = self.node_element.reshape((ntimes * nnodes, 2))
            if self.nonlinear_factor is not None:
                column_names, column_values = self._build_dataframe_transient_header()
                #column_names = [column_names[0]]
                #column_values = [column_values[0]]
    
                column_values2 = []
                for value in column_values:
                    values2 = []
                    #print(value)
                    for valuei in value:
                        values = np.ones(nnodes) * valuei
                        values2.append(values)
                    values3 = np.vstack(values2).ravel()
                    column_values2.append(values3)
                df1 = pd.DataFrame(column_values2).T
                df1.columns = column_names
                return df1
                #df1.columns.names = column_names
                #self.data_frame.columns.names = column_names            
                
                df2 = pd.DataFrame(node_element)
                df2.columns = ['NodeID', 'ElementID']
                df3 = pd.DataFrame(self.element_names.ravel())
                df3.columns = ['ElementType']
    
                dfs = [df2, df3]
                for i, header in enumerate(headers):
                    df = pd.DataFrame(self.data[:, :, i].ravel())
                    df.columns = [header]
                    dfs.append(df)
                data_frame = df1.join(dfs)
                #print(data_frame)
            else:
                df1 = pd.DataFrame(node_element)
                df1.columns = ['NodeID', 'ElementID']
                df2 = pd.DataFrame(self.element_names[0, :])
                df2.columns = ['ElementType']
                df3 = pd.DataFrame(self.data[0])
                df3.columns = headers
                data_frame = df1.join([df2, df3])
                #print(data_frame)
        else:
            node_element = [self.node_element[:, 0], self.node_element[:, 1]]
            if self.nonlinear_factor is not None:
                column_names, column_values = self._build_dataframe_transient_header()
                data_frame = pd.Panel(self.data, items=column_values, major_axis=node_element, minor_axis=headers).to_frame()
                data_frame.columns.names = column_names
                data_frame.index.names = ['NodeID', 'ElementID', 'Item']
            else:
                data_frame = pd.Panel(self.data, major_axis=node_element, minor_axis=headers).to_frame()
                data_frame.columns.names = ['Static']
                data_frame.index.names = ['NodeID', 'ElementID', 'Item']
        return data_frame
    
    # print(isat.grid_point_forces[1])
    grid_point_forces2 = build_dataframe_gpf(isat.grid_point_forces[1])
    
    # print(grid_point_forces2)

.. code:: ipython3

    grid_point_forces

.. include:: ./table_3.rst.txt

.. code:: ipython3

    cbar_force

.. include:: ./table_4.rst.txt

.. code:: ipython3

    cbush_force

.. include:: ./table_5.rst.txt

.. code:: ipython3

    cquad4_force

.. include:: ./table_6.rst.txt

.. code:: ipython3

    cquad4_stress

.. include:: ./table_7.rst.txt

.. code:: ipython3

    chexa_stress

.. include:: ./table_8.rst.txt

.. code:: ipython3

    cquad4_composite_stress

.. code:: ipython3

    ctria3_composite_stress

.. code:: ipython3

    cquad4_strain

.. include:: ./table_9.rst.txt

.. code:: ipython3

    chexa_stress

.. include:: ./table_10.rst.txt

.. code:: ipython3

    chexa_strain

.. include:: ./table_11.rst.txt

.. code:: ipython3

    cquad4_composite_strain

.. code:: ipython3

    ctria3_composite_strain
