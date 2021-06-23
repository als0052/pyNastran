# -*- coding: utf-8 -*-
# =========================================================================== #
# pyNastran documentation build configuration file, created by                #
# sphinx-quickstart on Sun Jan 07 19:17:52 2018.                              #
#                                                                             #
# This file is execfile()d with the current directory set to its containing   #
# dir.                                                                        #
#                                                                             #
# Note that not all possible configuration values are present in this         #
# autogenerated file.                                                         #
#                                                                             #
# All configuration values have a default; values that are commented out      #
# serve to show the default.                                                  #
#                                                                             #
# Modifications                                                               #
# -------------                                                               #
# (02-18-2021) (als0052) Reformated some things and tried to mostly pep-8     #
#                        things.                                              #
# (06-23-2021) (als0052) Uncomment numpydoc extension to get sphinx to run?   #
# =========================================================================== #

import sys
import os.path

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
cwd = os.getcwd()

if on_rtd:
    pkg_path = os.path.join(os.path.dirname(cwd), 'pyNastran')
else:
    import pyNastran
    pkg_path = pyNastran.__path__[0]

print ("cwd", cwd)
print ("pkg_path", pkg_path)
sys.stdout.flush()
sys.path.append(os.path.dirname(cwd))
sys.path.append(os.path.dirname(pkg_path))
sys.path.append(pkg_path)
sys.path.append(os.path.join(pkg_path, 'bdf'))
sys.path.append(os.path.join(pkg_path, 'op2'))
sys.path.append(os.path.join(pkg_path, 'f06'))

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# ------------------------------------------------
# 3rd party modules don't work, so we hack them in
# ------------------------------------------------
MOCK_MODULES = [
    'pandas',
    'PySide',
    'numpy.distutils.core',
    'numpy.distutils',
    'matplotlib',
    'wx',
    'docopt',
	# 'numpy', 'numpy.linalg','numpy.__version__',
    # 'numpydoc',
    # 'vtk', 'PyQt4', 'PySide',
    'numpydoc',
    # 'openmdao',
    # 'openmdao.main.api',
    # 'openmdao.util',
    # 'openmdao.util.doctools',
    # 'openmdao.lib.datatypes.api',
    # 'openmdao.lib.components',
    # 'openmdao.lib.drivers.api',
    # 'openmdao.lib.components.nastran.nastran',
    # 'openmdao.examples.bar3simulation.bar3',
    # 'openmdao.examples.bar3simulation.bar3_wrap_f',
    # 'nastranwrapper.nastran',
    # 'nastranwrapper',
    # 'nastranwrapper.test.nastranwrapper_test_utils',
    ]
try:
    import scipy
except ImportError:
    MOCK_MODULES += ['scipy', 'scipy.linalg', 'scipy.sparse', 
	                 'scipy.integrate', 'scipy.interpolate', 
					 'scipy.spatial']

MOCK_MODULES += ['qtpy', 'qtpy.QtWidgets', 'qtpy.QtCore', 'qtpy.Qsci', 'qtpy.compat',
                 'qtpy.QtGui', 'imageio']

## requires the mock module in Python 2.x
# pip install mock
# conda install mock

load_mock = True
if load_mock:
    from six import PY2
    if PY2:
        from mock import MagicMock
    else:
        from unittest.mock import MagicMock


    class Mock(MagicMock):
        @classmethod
        def __getattr__(cls, name):
            if name in ['__path__', 'pi', '_string', '__get__', '__set__']:
                return Mock()
            # print('MOCK cls=%r name=%r' % (cls, name))
            return MagicMock()
    sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

if not on_rtd:
    MOCK_MODULES = []

# -------------------------------------------------------------------------
# -- General configuration ------------------------------------------------
# -------------------------------------------------------------------------
# needs_sphinx = '1.0'
extensions = [
    'IPython.sphinxext.ipython_console_highlighting', # for notebooks
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',  # equations
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.autosummary',
    'numpydoc',
	'nbsphinx',  # for including jupyter notebooks
    # 'sphinx.ext.coverage',
    # 'sphinx.ext.napolean',
]

ipython_mplbackend = None  # don't require matplotlib
numpydoc_show_class_members = False  # suppress warnings
todo_include_todos = True

# show class docstring and __init__ docstring
autoclass_content = 'both'
inheritance_graph_attrs = dict(size='""')
templates_path = ['_templates']
source_suffix = '.rst'
# source_encoding = 'utf-8-sig'
master_doc = 'index'
version = '1.4-dev'
release = '1.4-dev'

# General information about the project.
project = 'pyNastran' + u' ' + version
author = 'Steven Doyle'
copyright = '2021, ' + author

language = None
today_fmt = '%B %d, %Y'
exclude_patterns = ['_build']
html_style = 'css/my_theme.css' 
# default_role = None
add_function_parentheses = True
# add_module_names = True
# show_authors = False
pygments_style = 'sphinx'
# modindex_common_prefix = []

# ------------------------------------------------------------------------------
# -- Options for HTML output ---------------------------------------------------
# ------------------------------------------------------------------------------

# Trying to get better line spacing with nested bulleted lists
#   See also https://stackoverflow.com/a/56822558/11895567
html4_writer = True

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
if on_rtd:
    html_theme = 'sphinx_rtd_theme'
else:
    if 0:
        html_theme = 'napolean' # classic/alabaster/numpydoc/sphinx_rtd_theme
        html_theme_path = []
    elif 0:
        html_theme = 'default'
    else:
        import sphinx_rtd_theme
        html_theme = 'sphinx_rtd_theme' # classic/alabaster/numpydoc/sphinx_rtd_theme
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    # napolean handles mixed sphinx (alabaster) and numpydoc docstring formats

# html_theme_options = {}
# html_theme_path = []
# html_title = None
# html_short_title = None
html_logo = 'logo.png'
# html_favicon = None
html_static_path = ['_static']
# html_last_updated_fmt = '%b %d, %Y'
# html_use_smartypants = True
# html_additional_pages = {}
# html_domain_indices = True
# html_use_index = True
# html_split_index = False
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True
# html_use_opensearch = ''
# html_file_suffix = None

# Output file base name for HTML help builder.
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html', 'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html', 'donate.html',]}

# -------------------------------------------------------------------------
# -- Options for HTMLHelp output ------------------------------------------
# -------------------------------------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyNastrandoc'

# -------------------------------------------------------------------------
# -- Options for LaTeX output ---------------------------------------------
# -------------------------------------------------------------------------
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'a4',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (master_doc, 'pyNastran.tex', u'pyNastran Documentation', 
	u'Steven Doyle', 'manual')]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True

# -------------------------------------------------------------------------
# -- Options for manual page output ---------------------------------------
# -------------------------------------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pynastran', u'pyNastran Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False

# -------------------------------------------------------------------------
# -- Options for Texinfo output -------------------------------------------
# -------------------------------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'pyNastran', u'pyNastran Documentation',
     author, 'pyNastran', 'Nastran BDF/F06/OP2/OP4 '
     'File reader/editor/writer/viewer.', 'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# -------------------------------------------------------------------------
# -- Options for Epub output ----------------------------------------------
# -------------------------------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'pyNastran'
epub_author = u'Steven Doyle'
epub_publisher = u'pyNastran'
epub_copyright = u'2019, Steven Doyle'

# The language of the text. It defaults to the language option
# or en if the language is not set.
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
# epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
# epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
# epub_tocdepth = 3

# Allow duplicate toc entries.
# epub_tocdup = True

def passer(app, what, name, obj, options, lines):
    pass

def purge_todos(app, env, docname):
    """http://www.sphinx-doc.org/en/stable/extdev/tutorial.html"""
    if not hasattr(env, 'todo_all_todos'):
        return
    env.todo_all_todos = [todo for todo in env.todo_all_todos
                          if todo['docname'] != docname]

# Rearranged these so they're in rough alphabetic order. Hope the order 
# didn't matter!!! - als0052; 02-18-2021
exclusions = (
	'__weakref__',  # special-members
	'__doc__', '__module__', '__dict__',  # undoc-members
	'__builtins__', '_field_map',
	'zip', 'range',
	
	'_add_aecomp_object', '_add_aefact_object', '_add_aelink_object',
	'_add_aelist_object', '_add_aeparm_object', '_add_aero_object',
	'_add_aeros_object', '_add_aestat_object', '_add_aesurf_object',
	'_add_aesurfs_object', '_add_ao_object', '_add_aset_object',
	'_add_axic_object', '_add_bcrpara_object', '_add_bctadd_object',
	'_add_bctpara_object', '_add_bctset_object', '_add_bset_object',
	'_add_bsurf_object', '_add_bsurfs_object', '_add_caero_object',
	'_add_axif_object', '_add_baror_object', '_add_bconp_object',
	'_add_beamor_object', '_add_blseg_object', '_add_csuper_object',
	'_add_csupext_object', '_add_gridb_object', '_add_normal_object',
	'_add_radcav_object', '_add_radmtx_object', '_add_radset_object',
	'_add_ringfl_object', '_add_sebndry_object', '_add_sebulk_object',
	'_add_seconct_object', '_add_seelt_object', '_add_seexcld_object',
	'_add_selabel_object', '_add_seload_object', '_add_seloc_object',
	'_add_sempln_object', '_add_senqset_object', '_add_setree_object',
	'_add_view3d_object', '_add_view_object', '_add_card_hdf5',
	'_add_card_helper', '_add_card_helper_hdf5', '_add_cmethod_object',
	'_add_constraint_mpc_object', '_add_constraint_mpcadd_object',
	'_add_constraint_spc_object', '_add_constraint_spcadd_object',
	'_add_constraint_spcoff_object', '_add_convection_property_object'
	'_add_coord_object', '_add_creep_material_object', '_add_cset_object',
	'_add_csschd_object', '_add_damper_object', '_add_darea_object',
	'_add_dconstr_object', '_add_ddval_object', '_add_delay_object',
	'_add_deqatn_object', '_add_desvar_object', '_add_diverg_object',
	'_add_dlink_object', '_add_dload_entry', '_add_dload_object',
	'_add_dmi_object', '_add_dmig_object', '_add_dmij_object',
	'_add_dmiji_object', '_add_dmik_object', '_add_doptprm_object',
	'_add_dphase_object', '_add_dresp_object', '_add_dscreen_object',
	'_add_dtable_object', '_add_dti_object', '_add_dvcrel_object',
	'_add_dvgrid_object', '_add_dvmrel_object', '_add_dvprel_object',
	'_add_element_object', '_add_epoint_object', '_add_flfact_object',
	'_add_flutter_object', '_add_freq_object', '_add_gust_object',
	'_add_hyperelastic_material_object', '_add_load_combination_object',
	'_add_load_object', '_add_lseq_object', '_add_mass_object',
	'_add_material_dependence_object', '_add_method_object', 
	'_add_mkaero_object', '_add_monpnt_object', '_add_nlparm_object',
	'_add_nlpci_object', '_add_node_object', '_add_nsm_object',
	'_add_nsmadd_object', '_add_nxstrat_object' '_add_omit_object',
	'_add_paero_object', '_add_param_object', '_add_pbusht_object',
	'_add_pdampt_object', '_add_pelast_object', '_add_phbdy_object',
	'_add_plotel_object', '_add_point_object', '_add_property_mass_object',
	'_add_property_object', '_add_qset_object', '_add_random_table_object',
	'_add_rigid_element_object', '_add_ringax_object', '_add_rotor_object',
	'_add_sebset_object', '_add_secset_object', '_add_seqgp_object',
	'_add_seqset_object', '_add_seset_object', '_add_sesuport_object',
	'_add_set_object', '_add_seuset_object', '_add_spline_object',
	'_add_spoint_object', '_add_structural_material_object', 
	'_add_suport1_object', '_add_suport_object', '_add_table_object',
	'_add_table_sdamping_object', '_add_tabled_object', '_add_tablem_object',
	'_add_tempd_object', '_add_tf_object', '_add_thermal_bc_object',
	'_add_thermal_element_object', '_add_thermal_load_object',
	'_add_thermal_material_object', '_add_tic_object', '_add_trim_object',
	'_add_tstep_object', '_add_tstepnl_object', '_add_uset_object',
	'_add_convection_property_object', '_add_coord_object',
	'_add_nxstrat_object', '_add_omit_object', '_add_column', 
	'_add_column_uaccel',

	'_cross_reference_aero', '_cross_reference_constraints', 
	'_cross_reference_coordinates', '_cross_reference_elements',
	'_cross_reference_loads', '_cross_reference_masses',
	'_cross_reference_materials', '_cross_reference_nodes',
	'_cross_reference_nodes_with_elements', '_cross_reference_optimization',
	'_cross_reference_properties', '_cross_reference_sets',
	'_clean_comment', '_clean_comment_bulk',

	'_eq_nodes_build_tree', '_eq_nodes_find_pairs', '_eq_nodes_setup',

	'_find_aero_location', 
	'_fill_abaqus_case',
	'_format_comment', 

	'_get_bdf_stats_loads', '_get_card_name', '_get_coords_to_update',
	'_get_dvprel_ndarrays', '_get_forces_moments_array', '_get_maps',
	'_get_npoints_nids_allnids', '_get_rigid', '_get_temperatures_array',
	'_get_field_helper', '_get_dtype',

	'_is_same_fields',

	'_mass_properties_new',
	'_make_card_parser', 
	
	'_node_ids',

	'_output_helper',

	'_parse_cards',	'_parse_cards_hdf5', '_parse_dynamic_syntax',
	'_parse_pynastran_header', '_parse_pynastran_header', '_parse_results',
	'_parse_primary_file_header', 
	'_prep_comment',
	'_prepare_bctset', '_prepare_cdamp4', '_prepare_chexa',
	'_prepare_cmass4', '_prepare_conv', '_prepare_convm',
	'_prepare_cord1c', '_prepare_cord1r', '_prepare_cord1s',
	'_prepare_cpenta', '_prepare_cpyram', '_prepare_ctetra',
	'_prepare_dequatn', '_prepare_dmi', '_prepare_dmig',
	'_prepare_dmij', '_prepare_dmiji', '_prepare_dmik',
	'_prepare_dmix', '_prepare_dti', '_prepare_grdset',
	'_prepare_nsm', '_prepare_nsml', '_prepare_pdamp',
	'_prepare_pelas', '_prepare_pmass', '_prepare_pvisc',
	'_prepare_radbc', '_prepare_radm', '_prepare_tempax',
	'_prepare_tempd', 

	'_read_inviscid_pressure', '_read_bdf_cards', '_read_bdf_helper',
	'_reduce_dload_case', '_reduce_load_case',
	'_reset_indices', '_reset_type_to_slot_map',

	'_safe_cross_reference_aero', '_safe_cross_reference_constraints',
	'_safe_cross_reference_elements', '_safe_cross_reference_loads',
	'_set_pybdf_attributes', 

	'_transform_node_to_global_array', '_transform_node_to_local',
	'_transform_node_to_local_array', '_transform',
	'_test_update_fields',
	
	'_uncross_reference_aero', '_uncross_reference_constraints'
	'_uncross_reference_coords', '_uncross_reference_elements',
	'_uncross_reference_loads', '_uncross_reference_masses',
	'_uncross_reference_materials', '_uncross_reference_nodes',
	'_uncross_reference_optimization', '_uncross_reference_properties',
	'_uncross_reference_sets', '_uncross_reference_constraints',
	'_uncross_reference_coords',
	'_update_field_helper',
	
	'_verify_bdf', '_verify',

	'_write_aero', '_write_aero_control', '_write_case_control_deck',
	'_write_common', '_write_constraints', '_write_contact',
	'_write_coords', '_write_dloads', '_write_dmigs',
	'_write_dynamic', '_write_elements', '_write_elements_interspersed',
	'_write_executive_control_deck', '_write_flutter', '_write_grids',
	'_write_gust', '_write_header', '_write_loads',
	'_write_masses', '_write_materials', '_write_nodes',
	'_write_nsm', '_write_optimization', '_write_params',
	'_write_properties', '_write_reject_message', '_write_rejects',
	'_write_rigid_elements', '_write_sets', '_write_static_aero',
	'_write_superelements', '_write_tables', '_write_thermal',
	'_write_thermal_materials', '_write_sort1_as_sort1', 
	'_write_sort1_as_sort2', '_write_sort2_as_sort1', '_write_sort2_as_sort2',

	'add_sort1', 'add_sort2', 'add_new_transient',
	'add_op2_data',
	'deprecated', 'deprecated',
	'print_raw_card', 'print_repr_card',
	'transform_node_from_local_to_local',
	'transform_node_from_local_to_local_array', 'transform_node_to_global',
	'transform_node_to_global_assuming_rectangular', 
	'transform_node_to_global_no_xref', 'transform_node_to_local', 
	'transform_node_to_local_array', 'transform_vector_to_global', 
	'transform_vector_to_global_array', 
	'transform_vector_to_global_assuming_rectangular', 
	'transform_vector_to_global_no_xref',
	'transform_vector_to_local',

	'AddMethods', 'AddCards', 
	'BDF_', 'BDFMethods', 'BDFAttributes',
	'DevUtils',
	'OP2Common', 'Op2Codes', 'F06Writer', 'OP2_Scalar',
	'SafeXrefMesh', 'XrefMesh', 'GetMethods', 
	'TestCoords', 'TestNodes', 'TestAero', 'TestConstraints', 'TestSets',
	'TestDEQATN', 'TestDynamic', 'TestRods', 'TestBars', 'TestBeams',
	'TestContact', 'TestDMIG', 'TestElements', 'TestMassElements',
	'TestMethods', 'TestNsm', 'TestLoads', 'TestMaterials', 'TestOther',
	'TestOpt', 'TestRigid', 'TestSprings', 'TestDampers', 'TestSolids',
	'TestShells', 'TestTables', 'TestThermal', 'TestAxi', 'TestBdfUtils',
	'Testfield_writer_8', 'TestBaseCard', 'CaseControlTest', 'TestMeshUtils',
	'TestConvert', 'TestRenumber', 'TestRemoveUnused', 'TestMass', 
	'TestLoadSum', 'TestPatran', 'TestReadWrite', 'TestOpenMDAO', 
	'TestAssignType', 'TestFastGUI', 'TestNastranGUI', 'TestUgridGui', 
	'TestMsgMesh', 'TestF06Formatting',
	'UnXrefMesh',
	'WriteMesh',
)

def maybe_skip_member(app, what, name, obj, skip, options):
    exclude = name in exclusions
    if not on_rtd and not exclude:
        # print(app, what, name, obj, skip, options)
        print(what, name, obj, skip, options)
    return skip or exclude

def setup(app):
    app.connect('autodoc-process-docstring', passer)
    app.connect('env-purge-doc', purge_todos)
    app.connect('autodoc-skip-member', maybe_skip_member)
