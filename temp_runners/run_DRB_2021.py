from vegetLib.vegetLib.veget import VegET
import os

"""
This runner was made on 11/10/2021 to run a Baseline condition 2020 for VegET using some ForeSCE scenarios
"""

config_root = r'Z:\Projects\DRB\Greg_LCLU'
shape_root = r'Z:\Projects\DRB\Greg_LCLU\chip_shapes'

#tile_lst = ['N1.shp', 'N2.shp', 'N3.shp', 'N4.shp', 'N5.shp', 'N6.shp', 'N7.shp', 'N8.shp', 'N9.shp', 'N10.shp']

# # testing
tile_lst = ['chip_0.shp']
#config_list = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10']

# # testing
config_list = ['chip_0']

for conf, tile in zip(config_list, tile_lst):
    tilename = tile.split('.')[0]
    shapefile = os.path.join(shape_root, tile)
    config_path = os.path.join(config_root, conf)

    veggie = VegET(veget_config_path=config_path,
                   tile=tilename,
                   shp=shapefile)
    print(veggie)
    veggie.run_veg_et()