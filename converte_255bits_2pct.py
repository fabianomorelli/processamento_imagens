from osgeo import gdal
import numpy as np
from osgeo.gdalconst import *
import os

# Define o local de trabalho onde estao os arquivos a serem processados
os.getcwd()
os.chdir( '/mnt/c/Users/fmorelli/Documents/avaliacao_algoritimo/221_074/221_074_t2')
os.listdir()

# Input Dataset
ids = gdal.Open('teste_cog.tif', GA_ReadOnly)

ids.RasterCount
ids.RasterXSize
ids.RasterYSize

# Recupera os dados de uma banda especifica
b1 = ids.GetRasterBand(1)

# Recupera os valores na forma de uma array multidimensional
arr1 = b1.ReadAsArray(0,0, ids.RasterXSize, ids.RasterYSize)

# Realiza o calculo para determinar os valores de 2 e 98%
p2, p98 = np.percentile(arr1, (2, 98))

# Normaliza os valores da imagem para ficar entre 0 e 1
raster = (arr1 -p2) / (p98 - p2)

# Prepara para gravar o arquivo de saida
ofile = 'arq_saida.tif'
driver = gdal.GetDriverByName('GTiff')
odataset = driver.Create( ofile, ids.RasterXSize, ids.RasterYSize, 1, gdal.GDT_Float32,  options = [ 'BIGTIFF=YES'])
odataset.GetRasterBand(1).WriteArray(raster)

# Fecha os arquivos de entrada e saída
odataset = None
ids = None