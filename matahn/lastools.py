import subprocess32 as subprocess
from matahn import app

def lasmerge(filenames, x_min, y_min, x_max, y_max, outname):
	q = ['wine', app.config['LASMERGE_BINARY'], '-inside', str(x_min), str(y_min), str(x_max), str(y_max), '-olaz', '-o', outname, '-i'] + filenames
	subprocess.call(q)
	return outname

def lasinfotxt(filename):
	subprocess.call(['wine', app.config['LASINFO_BINARY'], '-nmm', '-nv', '-nc', filename, '-otxt'])
	return filename[:-3]+'txt'

