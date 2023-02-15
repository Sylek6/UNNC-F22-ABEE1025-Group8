# Date of first creation: 2023-02-15
# This file is for OOP structure to write a basic strcuture for the optimization
# Author: Yuanxin Yang
class Room:
	""" 
	this class is used to calculated the highest 
	average indoor air temperature from two set of parameter 
	values of two arbitrary simulation model parameters

    """
	def __init__(self, eplus_run_path, idf_path, output_dir, parameter_key, parameter_vals):

		self._eplus_run_path = eplus_run_path
		self._idf_path = idf_path
		self._output_dir = output_dir
		self._parameter_key = parameter_key
		self._parameter_vals = parameter_vals

	def run_one_simulation_helper(self):
		"""
		This is a helper function to run one simulation with the changed
		value of the parameter_key 
		"""
		######### step 1: convert an IDF file into JSON file #########
		convert_json_idf(self._eplus_run_path, self._idf_path)
		epjson_path = self._idf_path.split('.idf')[0] + '.epJSON'

		######## step 2: load the JSON file into a JSON dict #########
		with open(epjson_path) as epJSON:
			epjson_dict = json.load(epJSON)
	
		######### step 3: change the JSON dict value #########
		# ['WindowMaterial:SimpleGlazingSystem',
		#							'SimpleWindow:DOUBLE PANE WINDOW',
		#							'solar_heat_gain_coefficient']
		inner_dict = epjson_dict
		for i in range(len(self._parameter_key)):
			if i < len(self._parameter_key) - 1:
				inner_dict = inner_dict[self._parameter_key[i]]
		inner_dict[self._parameter_key[-1]] = self._parameter_val
	
		######### step 4: dump the JSON dict to JSON file #########
		with open(epjson_path, 'w') as epjson:
			json.dump(epjson_dict, epjson)

		######### step 5: convert JSON file to IDF file #########
		convert_json_idf(self._eplus_run_path, epjson_path)
	
		######### step 6: run simulation #########
		run_eplus_model(self._eplus_run_path, self._idf_path, self._output_dir)

		return self._output_dir + './eplusout.csv'



