import asyncio
import os
import yaml
from yaml.loader import SafeLoader
import shutil

print('hellow world')

project_root = r'Z:\Projects\DRB\Greg_LCLU'

# root directory of sample configs...
cfg_root = r'Z:\Projects\DRB\Greg_LCLU\sample_configs'

# root directory of shapefiles that make up the run...
shp_root = r'Z:\Projects\DRB\Greg_LCLU\chip_shapes'


chiplist = []
dirlist = []
for f in os.listdir(shp_root):
    if f.endswith('.shp'):
        chiplist.append(os.path.join(shp_root,f))
        chpname = f.split('.')[0]
        dirlist.append(os.path.join(project_root, chpname))

print(chiplist)
print(dirlist)

run_param_path = os.path.join(cfg_root, 'run_param.yml')
path_param_path = os.path.join(cfg_root, 'path_param.yml')
model_param_path = os.path.join(cfg_root, 'model_param.yml')

for c, d in zip(chiplist, dirlist):
    if not os.path.exists(d):
        os.mkdir(d)
    with open(path_param_path, 'r') as rfile:
        data = yaml.load(rfile, SafeLoader)
        print(data)
        new_outroot = d
        data['out_root'] = new_outroot
        nppp = os.path.join(new_outroot, 'path_param.yml')
        # if you want more changes to the file, do them here
        with open(nppp, 'w') as wfile:
            yaml.dump(data, wfile)

    with open(run_param_path, 'r') as rfile:
        data = yaml.load(rfile, SafeLoader)
        print(data)
        new_shapefile = c
        data['shapefile'] = new_shapefile
        nrpp = os.path.join(d, 'run_param.yml')
        # if you want more changes to the file, do them here
        with open(nrpp, 'w') as wfile:
            yaml.dump(data, wfile)

    with open(model_param_path, 'r') as rfile:
        data = yaml.load(rfile, SafeLoader)
        print(data)
        nmpp = os.path.join(d, 'model_param.yml')
        # if you want more changes to the file, do them here ( No changes to model params)
        with open(nmpp, 'w') as wfile:
            yaml.dump(data, wfile)





