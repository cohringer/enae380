import time
import easygopigo3 as easy
gpg=easy.EasyGoPiGo3()
ds=gpg.init_distance_sensor()
def dancePiGo():
	gpg.drive_cm(10)
	gpg.drive_degrees(-450)
	gpg.drive_cm(-10)
	dance()
	"""
	d=ds.read_mm()
	a=d
	while d!>a-10:
		#move forward
		d=ds.read_mm()
	#spin
	while d!=a:
		#move backward
	"""
def peakTrough():
	minDis=100000000000
	maxDis=0
	while time.time()<5:
		d=ds.read_mm()
		if d<minDis:
			minDis=d
		elif d>maxDis:
			maxDis=d
	return (minDis,maxDis)	
def physLimit( x ):
	while ds.read_mm()<x:
		gpg.forward()

def timeLimit( t, spd ):
	gpg.set_speed(spd)
	while time.time()<t:
		gpg.forward()
def closeCall():
	pass

def escape():
	pass

def joey( x ):
	pass
def dance():
	gpg.drive_degrees(60)
	time.sleep(10)
	gpg.drive_degrees(-120)
	time.sleep(10)
	gpg.drive_degrees(120)
	time.sleep(10)
	gpg.drive_degrees(-60)