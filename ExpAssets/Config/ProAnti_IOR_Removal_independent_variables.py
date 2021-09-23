from klibs.KLIndependentVariable import IndependentVariableSet

ProAnti_IOR_Removal_ind_vars = IndependentVariableSet()

ProAnti_IOR_Removal_ind_vars.add_variable(name='cue_loc', d_type=str, values=['left', 'right'])
ProAnti_IOR_Removal_ind_vars.add_variable(name='target_loc', d_type=str, values=['left', 'right'])
ProAnti_IOR_Removal_ind_vars.add_variable(name='target_type', d_type=str, values=['cross', 'x'])
ProAnti_IOR_Removal_ind_vars.add_variable(name='removal_trial', d_type=bool, values=[True, False])