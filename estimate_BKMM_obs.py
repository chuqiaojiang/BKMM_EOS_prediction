import sys
import eos
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  
import uproot

import matplotlib
from matplotlib import rcParams
import matplotlib.pyplot as plt

matplotlib.use('pdf')
matplotlib.rcParams['text.usetex'] = False
matplotlib.rcParams['axes.formatter.use_mathtext'] = False


Q2edges = [1.00 , 2.00 , 4.30 , 8.68  , 10.09 , 12.86 , 14.18 , 16.00 , 18.00 , 22.0]

afb_sm = [0, 0, 0, 0, 0, 0, 0, 0, 0]
fh_sm = [0, 0, 0, 0, 0, 0, 0, 0, 0]
bf_sm = [0, 0, 0, 0, 0, 0, 0, 0, 0]
acp_sm = [0, 0, 0, 0, 0, 0, 0, 0, 0]

mean_afb_sm = [0, 0, 0, 0, 0, 0, 0, 0, 0]
mean_fh_sm = [0, 0, 0, 0, 0, 0, 0, 0, 0]
mean_bf_sm = [0, 0, 0, 0, 0, 0, 0, 0, 0]
mean_acp_sm = [0, 0, 0, 0, 0, 0, 0, 0, 0]

afb_err_sm = [0, 0, 0, 0, 0, 0, 0, 0, 0]
fh_err_sm = [0, 0, 0, 0, 0, 0, 0, 0, 0]
bf_err_sm = [0, 0, 0, 0, 0, 0, 0, 0, 0]
acp_err_sm = [0, 0, 0, 0, 0, 0, 0, 0, 0]

obs_afb_err_sm = []
obs_fh_err_sm  = []
obs_bf_err_sm  = []
obs_acp_err_sm = []

kl = 0
kr = 0

parameters = eos.Parameters.Defaults()
kinematics = eos.Kinematics(q2_min=1, q2_max=2)
options    = eos.Options({'l':'mu', 'q':'u', 'form-factors':'BFW2010', 'model':'SM', 'tag':'GP2004'})


analysis_args = {
    'priors': [
     { 'parameter': 'B->K::a^f+_0@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
     { 'parameter': 'B->K::a^f+_1@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
     { 'parameter': 'B->K::a^f+_2@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
     { 'parameter': 'B->K::a^f+_3@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
     { 'parameter': 'B->K::a^f+_4@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
     { 'parameter': 'B->K::a^f0_0@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
     { 'parameter': 'B->K::a^f0_1@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
     { 'parameter': 'B->K::a^f0_2@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
     { 'parameter': 'B->K::a^f0_3@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
     { 'parameter': 'B->K::a^f0_4@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
     { 'parameter': 'B->K::a^fT_0@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
     { 'parameter': 'B->K::a^fT_1@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
     { 'parameter': 'B->K::a^fT_2@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
     { 'parameter': 'B->K::a^fT_3@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
     { 'parameter': 'B->K::a^fT_4@BFW2010', 'min':  -1, 'max':   1,  'type': 'uniform'},
    ],
    'likelihood': [
        'B->K::FormFactors[parametric,BFW]@GRvDV:2023A',
    ]
}

analysis = eos.Analysis(**analysis_args)


temp_tag = 'GvDV2020'
for k in range(0,9):
	kl = k
	kr = k+1
	#if Q2edges[kr] < 15.0 :
	#	temp_tag = 'GvDV2020'
	#else :
	#	temp_tag = 'GP2004'
	options    = eos.Options({'l':'mu', 'q':'u', 'form-factors':'BFW2010', 'model':'SM', 'tag':temp_tag, 'nonlocal-formfactors':'GvDV2020'})
	#afb_sm[k] = (eos.Observable.make('B->Kll::A_FB', analysis.parameters, eos.Kinematics(q2_min=Q2edges[kl], q2_max=Q2edges[kr]), options)).evaluate()
	#fh_sm[k]  = (eos.Observable.make('B->Kll::F_H' , analysis.parameters, eos.Kinematics(q2_min=Q2edges[kl], q2_max=Q2edges[kr]), options)).evaluate()
	#bf_sm[k]  = (eos.Observable.make('B->Kll::BR'  , analysis.parameters, eos.Kinematics(q2_min=Q2edges[kl], q2_max=Q2edges[kr]), options)).evaluate()
	#acp_sm[k] = (eos.Observable.make('B->Kll::A_CP', analysis.parameters, eos.Kinematics(q2_min=Q2edges[kl], q2_max=Q2edges[kr]), options)).evaluate()
	obs_afb_err_sm.append(eos.Observable.make('B->Kll::A_FB', analysis.parameters, eos.Kinematics(q2_min=Q2edges[kl], q2_max=Q2edges[kr]), options))
	obs_fh_err_sm.append(eos.Observable.make('B->Kll::F_H' ,  analysis.parameters, eos.Kinematics(q2_min=Q2edges[kl], q2_max=Q2edges[kr]), options))
	obs_bf_err_sm.append(eos.Observable.make('B->Kll::BR'  ,  analysis.parameters, eos.Kinematics(q2_min=Q2edges[kl], q2_max=Q2edges[kr]), options))
	obs_acp_err_sm.append(eos.Observable.make('B->Kll::A_CP', analysis.parameters, eos.Kinematics(q2_min=Q2edges[kl], q2_max=Q2edges[kr]), options))
	#afb_sm[k] = obs_afb_err_sm[k].evaluate()
	#fh_sm[k]  =  obs_fh_err_sm[k].evaluate()
	#bf_sm[k]  =  obs_bf_err_sm[k].evaluate()
	#acp_sm[k] = obs_acp_err_sm[k].evaluate()


n_samples = 1000
pre_N = 300

par_list = ['A_FB', 'F_H', 'BR', 'A_CP']
obs_list = [obs_afb_err_sm, obs_fh_err_sm, obs_bf_err_sm, obs_acp_err_sm]
pred_list = [afb_sm, fh_sm, bf_sm, acp_sm]
err_list  = [afb_err_sm, fh_err_sm, bf_err_sm, acp_err_sm]
mean_list = [mean_afb_sm, mean_fh_sm, mean_bf_sm, mean_acp_sm]

par_samples = {'A_FB':[] , 'F_H':[] , 'BR':[] , 'A_CP':[]}
log_samples = {'A_FB':[] , 'F_H':[] , 'BR':[] , 'A_CP':[]}
obs_samples = {'A_FB':[] , 'F_H':[] , 'BR':[] , 'A_CP':[]}


for i,ipar in enumerate(par_list):
	print ('generating observable sample ', ipar)
	for k in range(0,9):
		print ('generating in q2 bin ', k)
		tmp_parameter_samples, tmp_log, tmp_observable_samples = analysis.sample(N=n_samples, pre_N=pre_N, observables=[obs_list[i][k]])
		(par_samples[ipar]).append(tmp_parameter_samples)
		(log_samples[ipar]).append(tmp_log)
		(obs_samples[ipar]).append(tmp_observable_samples)
		print(tmp_observable_samples)






#x_range_dict = {
#    'A_FB': [-0.05,0.05],
#    'F_H': [-0.05,0.05],
#    'BR': [-0.05,0.05],
#    'A_CP': [-0.05,0.05],
#}
#
#for i,ipar in enumerate(par_list):
#	plot_args = {
#		'plot': {
#			'x': { 'label': r'$%s$'%ipar,  'range': [x_range_dict[ipar][0],  x_range_dict[ipar][1]] },
#			'legend': { 'location': 'upper center' }
#		},
#		'contents': [
#		{ 'label': r'%s, bin0'%ipar,'type': 'histogram', 'bins': 50, 'data': { 'samples': obs_samples[ipar][0] }},
#		{ 'label': r'%s, bin1'%ipar,'type': 'histogram', 'bins': 50, 'data': { 'samples': obs_samples[ipar][1] }},
#		{ 'label': r'%s, bin2'%ipar,'type': 'histogram', 'bins': 50, 'data': { 'samples': obs_samples[ipar][2] }},
#		{ 'label': r'%s, bin3'%ipar,'type': 'histogram', 'bins': 50, 'data': { 'samples': obs_samples[ipar][3] }},
#		{ 'label': r'%s, bin4'%ipar,'type': 'histogram', 'bins': 50, 'data': { 'samples': obs_samples[ipar][4] }},
#		{ 'label': r'%s, bin5'%ipar,'type': 'histogram', 'bins': 50, 'data': { 'samples': obs_samples[ipar][5] }},
#		{ 'label': r'%s, bin6'%ipar,'type': 'histogram', 'bins': 50, 'data': { 'samples': obs_samples[ipar][6] }},
#		{ 'label': r'%s, bin7'%ipar,'type': 'histogram', 'bins': 50, 'data': { 'samples': obs_samples[ipar][7] }},
#		{ 'label': r'%s, bin8'%ipar,'type': 'histogram', 'bins': 50, 'data': { 'samples': obs_samples[ipar][8] }},
#		]
#	}
#	eos.plot.Plotter(plot_args, 'sampling_'+ipar+'.png').plot()




for i,ipar in enumerate(par_list):
	plt.cla()
	for k in range(0,9):
		plt.hist( obs_samples[ipar][k], bins=100, alpha=0.6, label=("bin{}".format(k)) )
	plt.legend(loc='upper right')
	plt.savefig("{}.pdf".format(ipar))


for i,ipar in enumerate(par_list):
	for k in range(0,9):
		kl = k
		kr = k+1
		mean = np.average(obs_samples[ipar][k])
		std  = np.sqrt(np.var(obs_samples[ipar][k]))
		(err_list[i])[k] = std
		(mean_list[i])[k] = mean


print("afb_sm: ")
print(mean_afb_sm)
print("\n")
print("fh_sm: ")
print(mean_fh_sm)
print("\n")
print("bf_sm: ")
print(mean_bf_sm)
print("\n")
print("acp_sm: ")
print(mean_acp_sm)
print("\n")
print("afb_err_sm: ")
print(afb_err_sm)
print("\n")
print("fh_err_sm: ")
print(fh_err_sm)
print("\n")
print("bf_err_sm: ")
print(bf_err_sm)
print("\n")
print("acp_err_sm: ")
print(acp_err_sm)
print("\n")
