#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import datetime as dt
from urllib.request import urlretrieve, urlopen, URLError

import os
here = os.path.dirname(os.path.realpath(__file__))
HOME = os.getenv('HOME')


## Get screen resolution
com = "xdpyinfo | grep dimensions"
res = os.popen(com).read().split()[1]


model_svg = here + '/background_%s.svg'%(res)
tmp_png = '/tmp/test.png'
desk_back = here + '/background.png'


now = dt.datetime.now()


#### Images
## Europe
# now
url1 = 'http://www.meteo.be/meteo/view/en/113200-ajaxcontroller.html/6723383/image.jpg?position=19&extraid='
# 1h ago
url2 = 'http://www.meteo.be/meteo/view/en/113200-ajaxcontroller.html/6723383/image.jpg?position=18&extraid='

## Frentes from aemet
url3 = 'http://www.aemet.es/imagenes_d/eltiempo/prediccion/modelos_num/hirlam/%s00+012_ww_isx0w012.gif'%(now.strftime('%Y%m%d'))


try: a,b = urlretrieve(url1, here+'/europe-0.jpg')
except: pass
#try: a,b = urlretrieve(url2, here+'/europe-1.jpg')
#except: pass
try: a,b = urlretrieve(url3, here+'/frentes.gif')
except: pass


com = 'inkscape --export-png=%s %s &&'%(tmp_png,model_svg)
com += ' mv %s %s'%(tmp_png,desk_back)
os.system(com)

