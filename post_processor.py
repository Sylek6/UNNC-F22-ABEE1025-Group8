# Date: 2022-10-31
# Author: Keyue Zhu

import pandas as pd
import datetimes as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

def eplus_to_datetime(date_str):
	if date_str[-8:-6] != '24':
		dt_obj = pd.to_datetime(date_str)
	else: 
		date_str = date_str[0:-8] + '00' + date_str[-6:]
		dt_obj = pd.to_datetime(date_str) + dt.timedelta(days=1)
	return dt_obj

def plot_1D_results(output_paths, plot_column_name, y_axis_title, plot_title):
	fig. axs = plt.subplots(1, 1, figsize=(20,10))
	fontsize = 20
	for item in ['Environment:Site Outdoor Air Drybulb Temperature [C](TimeStep)', 'ZONE ONE:Zone Windows Total Transmitted Solar Radiation Rate [W](TimeStep)', 'ZN001:WALL001:Surface Outside Face Sunlit Fraction [](TimeStep)', 'ZN001:WALL001:Surface Outside Face Incident Solar Radiation Rate per Area [W/m2](TimeStep)', 'ZN001:WALL001:WIN001:Surface Outside Face Sunlit Fraction [](TimeStep)', 'ZN001:WALL001:WIN001:Surface Outside Face Incident Solar Radiation Rate per Area [W/m2](TimeStep)', 'ZN001:WALL001:WIN001:Surface Window Transmitted Solar Radiation Rate [W](TimeStep)','ZN001:WALL001:Surface Inside Face Temperature [C](TimeStep)', 'ZN001:WALL001:Surface Outside Face Temperature [C](TimeStep)', 'ZN001:WALL001:WIN001:Surface Inside Face Temperature [C](TimeStep)', 'ZN001:WALL001:WIN001:Surface Outside Face Temperature [C](TimeStep)', 'ZONE ONE:Zone Mean Air Temperature [C](TimeStep)']
	this_path =  ../UNNC-F22-ABEE1025-Group8/eplusout.csv
	this_df = pd.read_csv(../UNNC-F22-ABEE1025-Group8/eplusout.csv)
	this_df['Date/Time'] = '2002' + this_df['Date/Time']
	this_df['Date/Time'] = this_df['Date/time'].apply(eplus_to_datetime)
	data_st_date = this_df.iloc[0]['Date/Time']
	data_ed_date = this_df.iloc[-1]['Date/Time']
	date_list = this_df['Date/Time']
	this_y = this_df[item].values
    axs.plot(date_list, this_y,
            alpha = 0.7,
            linestyle = '--',
            linewidth = 2,
            label = item)
datetime_ax_loc = mdates.HourLocator()  
datetime_ax_fmt = mdates.DateFormatter('%H:%M')
axs.xaxis.set_major_locator(datetime_ax_loc)
axs.xaxis.set_major_formatter(datetime_ax_fmt)
for tick in axs.xaxis.get_major_ticks():
    tick.label.set_fontsize(fontsize*0.8) 
for tick in axs.yaxis.get_major_ticks():
    tick.label.set_fontsize(fontsize*0.8) 
axs.tick_params('x', labelrotation=45)
axs.set_xlabel('Time (%s to %s)'%(data_st_date, data_ed_date),
              fontsize = fontsize)
axs.set_ylabel('Air Temperature (C)',
              fontsize = 10)
axs.legend(fontsize = 10)
plt.lengend
plt.xlabel
plt.ylabel
plt.show()