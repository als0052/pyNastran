######################
Building Documentation
######################

If you don't want to use build the docs, just see `docs <https://pynastran-git.readthedocs.io/en/latest/>`_

Install extra packages (for Documentation)
******************************************

Install `GraphViz  <https://www.graphviz.org/>`_

Install additional python packages:

.. code-block:: console

  pip install Sphinx
  pip install alabaster
  pip install numpydoc

.. I think this makes more sense in installation.rst?

.. Installation From Source
.. ========================
.. 
.. pyNastran is meant to an easy package to install once you have the required Python modules.
.. It's a pure Python package so you shouldn't have too many problems.
.. 
.. Installing from source is recommened if:
..  - You want the most recent version (see installation.rst-master)
..  - You want easier access to the source
..  - You're on an air-gapped machine
.. 
.. Overview
.. --------
..  * Install Python (see :doc:`installation_release`)
.. 
..    * skip the ``pip install pyNastran`` step
..  * Install Sphinx, GraphViz, alabaster **(for documentation)**
.. 
..  * Install Git
..  * Clone pyNastran-master from Github
..  * Install pyNastran
.. 
.. 
.. 
.. Install Git
.. ===========
.. 
..  * Download & install `Git <http://git-scm.com/>`_
..  * Download a GUI for Git (optional)
..     * `TortoiseGit <https://tortoisegit.org/>`_ (recommended for Windows)
.. 
.. 
.. Install pyNastran
.. =================
.. There are two ways to install the master/dev version of pyNastran
.. 
..  1. Download the most recent `zip version <https://github.com/SteveDoyle2/pyNastran/archive/master.zip>`_
.. 
..  2. Clone pyNastran (see below).  Using Git allows you to easily update to the
..     latest dev version when you want to as well as push any commits of your own.
.. 
.. If you don't want the gui, use ``setup_no_gui.py`` instead of ``setup.py``.
.. 
.. .. code-block:: console
.. 
..   >>> python setup.py install
.. 
.. or:
.. 
.. .. code-block:: console
.. 
..   >>> python setup_no_gui.py install
.. 
.. 
.. Cloning pyNastran using TortoiseGit
.. ===================================
.. Right-click in a folder and select ``Git Clone``.
.. 
.. .. image:: clone.png
.. 
.. Enter the above information.  If desired, click the branch box and and enter a branch name
.. and click ``OK``.
.. 
.. Cloning pyNastran Using Command Line
.. ====================================
.. Checkout/clone the dev code by typing **(preferred)**:
.. 
.. .. code-block:: console
.. 
..   >>> git clone https://github.com/SteveDoyle2/pynastran
.. 
.. 
.. To checkout a branch
.. 
.. .. code-block:: console
.. 
..   >>> git.exe clone --branch 1.3 --progress -v "https://github.com/SteveDoyle2/pyNastran.git" "C:\\work\\pyNastran_1.3"


Build Docs
**********
.. Navigate to ``pyNastran/docs_sphinx`` directory on the command line.

Navigate to ``pyNastran/docs/html_docs`` directory on the command line. Use the ``make html`` Sphinx command to update the .html pages. Alternatively use ``make clean html && make html`` to generate a brand new copy of the .html files.

.. code-block:: console

  >>> make html
