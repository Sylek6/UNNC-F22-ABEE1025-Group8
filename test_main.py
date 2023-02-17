from room import Room
import csv

# software run path
eplus_run_path = './energyplus9.5/energyplus'
# idf file path
idf_path = './1ZoneUncontrolled_win_1.idf'
output_dir = '20321316'

parameter_key = (['WindowMaterial:SimpleGlazingSystem',
                  'SimpleWindow:DOUBLE PANE WINDOW',
                  'solar_heat_gain_coefficient'], ['WindowMaterial:SimpleGlazingSystem',
                                                   'SimpleWindow:DOUBLE PANE WINDOW',
                                                   'u_factor'])

# the vals of the window solar_heat_gain_coefficient, e.g. [25/100, 30/100...70/100]
vals_one_region = [(i / 100) for i in range(25, 75, 5)]

# the vals of the window u_factor, e.g. [10/10, 15/10...20/10]
vals_two_region = [(i / 10) for i in range(10, 25, 5)]

max_sum = 0.0
optimal_vals_pair = ()
for i in range(len(vals_one_region)):
    for j in range(len(vals_two_region)):
        vals_pair = (vals_one_region[i], vals_two_region[j])
        # new object - instance and set parameters and values
        room_instance = Room(eplus_run_path, idf_path, output_dir, parameter_key, vals_pair)
        # call simulation program
        csv_path = room_instance.run_two_simulation_helper()
        f = open('./'+csv_path, 'r')
        reader = csv.reader(f)
        # skip the first row
        next(reader)
        sum = 0.0
        for line in reader:
            sum += float(line[8])

        if sum > max_sum:
            max_sum = sum
            optimal_vals_pair = vals_pair

print('The optimal values pair is', optimal_vals_pair)



