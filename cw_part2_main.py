from parametric_simulation import run_one_simulation_helper
from parametric_simulation import run_one_parameter_parametric

eplus_run_path = '../eplus_test/energyplus9.5/energyplus'
idf_path = '../eplus_test/1ZoneUncontrolled_win_1.idf'
parameter_key = ['WindowMaterial:SimpleGlazingSystem', 'SimpleWindow:DOUBLE PANE WINDOW', 'solar_heat_gain_coefficient']
import numpy as np

parameter_vals = np.arange(0.25, 0.75, 0.02)
output_dir = '../eplus_test/param_exp_1'
run_one_parameter_parametric(eplus_run_path, idf_path, output_dir,
	                             parameter_key, parameter_vals)