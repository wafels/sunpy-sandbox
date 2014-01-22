#
# Code to download JP2 files
#
from sunpy.net.helioviewer import HelioviewerClient
from sunpy.map import Map
import os

hv = HelioviewerClient()
datasources = hv.get_data_sources()
get_files = False
directory = '/home/ireland/hv/sunpy_hv_test_images/'
#directory = '/home/ireland/hv/TRACE_test_images/'
# print a list of datasources and their associated ids
files = [] 
if get_files:

   for observatory, instruments in datasources.items():
        for inst, detectors in instruments.items():
            for det, measurements in detectors.items():
                for meas, params in measurements.items():
                    print("%s %s: %d" % (observatory, params['nickname'], params['sourceId']))
                    filepath = hv.download_jp2('2013/06/24 17:31:30',
                                               observatory=observatory,
                                               instrument=inst,
                                               detector=det,
                                               measurement=meas,
                                               directory=directory)
                    files.append(filepath)
else:
    flist = os.listdir(directory)
    for fl in flist:
        files.append(os.path.join(directory, fl))

files = sorted(files)

n = len(files)


for f in files:
    print f
    m = Map(f)
    m.peek()
