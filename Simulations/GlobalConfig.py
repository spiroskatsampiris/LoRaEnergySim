import numpy as np

############### SIMULATION SPECIFIC PARAMETERS ###############
start_with_fixed_sf = False
start_sf = 7

transmission_rate_id = '0.1'
transmission_rate_bit_per_ms = (12*8)/(60*60*1000)  # 12*8 bits per hour (1 typical packet per hour)
simulation_time = 24 * 60 * 60 * 1000 * 100
cell_size = 1000
adr = True
confirmed_messages = True

payload_sizes = range(5, 55, 5)
path_loss_variances = [7.9]  # [0, 5, 7.8, 15, 20]

MAC_IMPROVEMENT = False
num_locations = 500
num_of_simulations = 1000
locations_file = "Locations/"+"{}_locations_{}_sim.pkl".format(num_locations, num_of_simulations)

############### SIMULATION SPECIFIC PARAMETERS ###############

############### DEFAULT PARAMETERS ###############
LOG_ENABLED = True
MAX_DELAY_BEFORE_SLEEP_MS = 500
PRINT_ENABLED = False
MAX_DELAY_START_PER_NODE_MS = np.round(simulation_time / 10)
track_changes = True
middle = np.round(cell_size / 2)

############### DEFAULT PARAMETERS ###############
