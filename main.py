import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


######################
# Fuzzy variables
######################
outside_temperature = ctrl.Antecedent(np.arange(-10, 51, 1), 'outside_temperature')
biologic_temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'biologic_temperature')
penguins_number = ctrl.Antecedent(np.arange(5, 50, 1), 'penguins_number')
air_conditioning = ctrl.Consequent(np.arange(-10, 51, 1), 'air_conditioning')

#########################
# Membershipt functions
#########################

penguins_number.automf(number=3, names=['low', 'average', 'crowded'])

# Outside temperature on Cº
outside_temperature['cold'] = fuzz.trapmf(outside_temperature.universe, [-10, -10, 15, 20])
# Hour of the day
outside_temperature['warm'] = fuzz.trimf(outside_temperature.universe, [18, 25 , 30])
# Number of penguins on the zoo enclosure 
outside_temperature['hot'] = fuzz.trapmf(outside_temperature.universe, [28, 35, 50, 50])

# Biologic temperature on Cº
biologic_temperature['cool dead'] = fuzz.trapmf(biologic_temperature.universe, [0, 0, 20, 30])
biologic_temperature['good'] = fuzz.gaussmf(biologic_temperature.universe, 38, 5)
biologic_temperature['hot dead'] = fuzz.trapmf(biologic_temperature.universe, [42, 45, 50, 55])

# Outside temperature on Cº
air_conditioning['cold'] = fuzz.trapmf(air_conditioning.universe, [-10, -10, 15, 25])
# Hour of the day
air_conditioning['warm'] = fuzz.trimf(air_conditioning.universe, [18, 25, 30])
# Number of penguins on the zoo enclosure 
air_conditioning['hot'] = fuzz.trapmf(air_conditioning.universe, [25, 35, 50, 50])

####################
# STORE FIGURES
####################

# Dictionary of all antecedents and consequents
folder = "./figures"
variables = {
    'outside_temperature': outside_temperature,
    'biologic_temperature': biologic_temperature,
    'penguins_number': penguins_number
}

for var_name, var in variables.items():
    var.view()
    filename = f"{folder}/{var_name}_membership.png"
    plt.savefig(filename)
    print(f"Saved {filename}")
    
    plt.close()

########################
# Horn Clauses
########################
rule1 = ctrl.Rule(outside_temperature['hot'] & penguins_number['crowded'] | biologic_temperature['hot dead'], air_conditioning['cold'])
rule2 = ctrl.Rule(outside_temperature['warm'] & penguins_number['average'] | biologic_temperature['good'], air_conditioning['warm'])
rule3 = ctrl.Rule(outside_temperature['cold'] & penguins_number['low'] | biologic_temperature['cool dead'], air_conditioning['hot'])

air_conditioning_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

########################
# Desfuzzification
########################
result = ctrl.ControlSystemSimulation(air_conditioning_ctrl)
result.input['outside_temperature'] = 6.5
result.input['penguins_number'] = 9.8
result.input['biologic_temperature'] = 20

# Crunch the numbers
result.compute()

air_conditioning.view(sim=result)
filename = f"{folder}/air_conditioning.png"
plt.savefig(filename)
plt.close()

print(round(result.output['air_conditioning'], 2))

