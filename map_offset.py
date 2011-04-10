#!/usr/bin/env python
#coding=utf-8
import pdb,pickle,math
'''
offset={}
f=open('offset_min1.txt')
for l in f.readlines():
	p = l.strip('\n').split(',')
	offset[(float(p[0].strip('"')),float(p[1].strip('"')))]=(float(p[4].strip('"')),float(p[5].strip('"')))
pickle.dump(offset,f1)
f.close()
'''
f1=open('gps2gmap.offset','r')
offset = pickle.load(f1)
f1.close()

def gps2gmap(lat,lng):
	base_lat,base_lng = float("%.1f" % lat),float("%.1f" % lng)
	if offset.get((base_lng,base_lat)):
		offset_lng,offset_lat = offset.get((base_lng,base_lat))
		new_lng,new_lat = lng + offset_lng,lat + offset_lat
		return (new_lat,new_lng)
	else:
		return lat,lng

def gps2bmap(lat,lng):
	pass

def gps2sgmap(lat,lng):
	pass

def latlng_dis(lat1,lng1,lat2,lng2):
	radlat1,radlat2,radlng1,radlng2 = lat1 * math.pi/180.0,lat2 * math.pi/180.0,lng1 * math.pi/180.0,lng2 * math.pi/180.0
	a = radlat1 - radlat2
	b = radlng1 - radlng2
	s = 2 * math.asin(math.sqrt(math.pow(math.sin(a/2),2)+math.cos(radlat1)*math.cos(radlat2) *math.pow(math.sin(b/2),2)))
	s *= 6378.137
	s *= 1000
	return s

if __name__ == "__main__":
	print gps2gmap(39.902869,116.223233)
