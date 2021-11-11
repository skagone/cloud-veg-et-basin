import os
import sys
import rasterio
from api_veget.preprocessing_aoi.gridmeister import GridMeister




if __name__ == '__main__':

    # get extent from study area - QGIS is easy for manually getting it.
    # shape file extent from this shapefile: r'Z:\Projects\DRB\shapefiles\drb_bnd_polygon_4326WGS84.shp'
    study_shape_ext = (-76.7887773384868950, 38.3604674808432833, -72.6996183842973664, 42.8096389027553528)

    r'Z:\Projects\DRB\shapefiles\drb_bnd_polygon_4326WGS84.shp'
    # ...from an old script:
    darin_extent = (-77.4226093565661415, 38.3565890497327118, -73.2480170973858122, 42.7829967799980722)

    testfile = r'Z:\Projects\DRB\model_output\yrs150_run100521\annual\eta\etasw_1967.tif'
    # get raster resolution from a test file
    with rasterio.open(testfile, 'r') as src:
        meta = src.meta
        print('meta')
        print(meta)
        print(meta['transform'])
        print(meta['transform'][0])
        xres = meta['transform'][0]
        print(meta['transform'][4])
        yres = meta['transform'][4]
        print(type(meta['transform']))

    tile = 'delaware'
    print('creating chips for delaware river basin')

    # instantiate the gridmeister object
    gm = GridMeister(tile, raster_extent=darin_extent, x_raster_res=xres, y_raster_res=yres)

    # output location for chip files
    chip_output = r'Z:\Projects\DRB\Greg_LCLU\chip_shapes_II'
    if not os.path.exists(chip_output):
        os.mkdir(chip_output)

    # make the chips form the chiplist using gridmeister
    lst = gm.chip_list(max_pixels=1000000)
    print('resulting chip list \n', lst)

    if lst == None:
        gm.create_chip_shp(ul_lat=None, ul_lon=None, out_location=chip_output, unit_chip=True)
    else:
        for i, l in enumerate(lst):
            gm.create_chip_shp(l[0], l[-1], out_location=chip_output, chip_number=i)



