import sys
from swotann.swot_ml import SWOT_ML

SWOT_net = SWOT_ML()
filename = sys.argv[1]
output_filename = sys.argv[2]

'''The following lines train a network from
data written a .csv format. The trained network is saved
in a folder called 'Pretrained Network'.'''
SWOT_net.import_data_from_csv(filename)
SWOT_net.train_SWOT_network(output_filename)
