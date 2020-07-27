from celery.decorators import task

import gdal

@task(name="sum_two_numbers")
def add(x, y):
    data = gdal.Open('MFW_2020199_090E030N_P14x3D3OT.tif')
    data_array = data.ReadAsArray()
    
    return data_array