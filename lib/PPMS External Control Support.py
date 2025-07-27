import numpy as np
import math

def process_DC_basic_buffer(voltage):
	output = np.zeros(2)
	output[0] = np.mean(voltage)
	output[1] = np.std(voltage)
	return output

def process_DC_buffer(time, voltage, t, tpad):
	time = np.array(time)*1000	# all timestamps in millisecond now on
	t = t*1000.0
	voltage = np.array(voltage)
	output = np.zeros(2)
	index = 0
	nvpos = 0
	nvneg = 0
	vpos = np.array([])
	vneg = np.array([])

	done_vpos = False
	tpos_min = tpad
	tpos_max = 0.5*t-tpad
	tneg_min = 0.5*t+tpad
	tneg_max = t-tpad
	# print("Finding postive voltage:")
	while done_vpos == False:
		if (time[index]>tpos_min):
			if(time[index]<tpos_max):
				vpos = np.append(vpos,voltage[index])
				# print(time[index],voltage[index])
			else:
				done_vpos =  True
				# print("Finding negative voltages:")
		index = index + 1
	while done_vpos == True:
		if (time[index]>tneg_min):
			if (time[index]<tneg_max):
				vneg = np.append(vneg,voltage[index])
				# print(time[index],voltage[index])
			else:
				done_vpos = False
		index = index + 1
	output[0] = (np.mean(vpos)-np.mean(vneg))/2
	output[1] = (np.std(vpos)+np.std(vneg))/2
	# print time
	# print vpos
	# print vneg
	# print np.mean(vpos)
	# print np.mean(vneg)
	return output



# ### Test process_DC_buffer
# voltage = [0.1,0.2,1,1,1,1,1,1,1,1,0.3,-0.2,-1,-1,-1,-1,-1,-1,-1,-1,0]
# time = np.linspace(0,2.05,21)
# t = 2
# tpad = 50
# print(process_DC_buffer(time,voltage,t,tpad))