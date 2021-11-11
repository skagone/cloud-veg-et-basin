import os
import sys
from api_veget.preprocessing_aoi.gridmeister import GridMeister


tile_cust=os.getcwd()
tile_cust=tile_cust.split('/')[-1]
tile = 'run_'+tile_cust

optimize=True
if len(sys.argv) > 2:
    if 'no' in sys.argv[2]:
        optimize = False;


gm = GridMeister(tile)

chip_list = gm.chip_list()

print(chip_list)

if not chip_list == None:
    for chip in chip_list:
            gm.create_chip_shp(chip)

else:
    gm.cre

gm.build_docker_run_bash(chip_list, optimize)



