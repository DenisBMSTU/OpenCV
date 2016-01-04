import cv2
import numpy as np

#######   training part    ############### 
samples = np.loadtxt('generalsamples.data',np.float32)
responses = np.loadtxt('generalresponses.data',np.float32)
responses = responses.reshape((responses.size,1))

model = cv2.KNearest()
model.train(samples,responses)

############################# testing part  #########################
image_load = cv2.imread('pic/1.png')
crop_image = image_load[40:60, 56:655]
im = cv2.resize(crop_image,None,fx=4.5, fy=4.5, interpolation = cv2.INTER_CUBIC)

out = np.zeros(im.shape,np.uint8)
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
massOfRetal = []

dct = {}
for cnt in contours:
	if cv2.contourArea(cnt)>50:
		[x,y,w,h] = cv2.boundingRect(cnt)
		if  h>32:
			cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
			roi = thresh[y:y+h,x:x+w]
			roismall = cv2.resize(roi,(10,10))
			roismall = roismall.reshape((1,100))
			roismall = np.float32(roismall)
			retval, results, neigh_resp, dists = model.find_nearest(roismall, k = 1)
			massOfRetal.append(retval)
			#stringSTR = str(int((results[0][0])))
			#stringINT = int((results[0][0]))
			string = chr(int((results[0][0])))
			cv2.putText(out,string,(x,y+h),0,1,(0,255,0))		
			dct[x] = string


#print massOfRetal
#newMass = []
#for i in range(0, len(massOfRetal)):
#	if type(massOfRetal[i])==float:
#		massOfRetal[i] = chr(int(massOfRetal[i]))
#		newMass.append(massOfRetal[i])
#	elif type(massOfRetal[i])==int:
#		massOfRetal[i] = chr(massOfRetal[i])
#		newMass.append(massOfRetal[i])
#	else:
#		newMass.append(massOfRetal[i])
#print massOfRetal[::-1]

#print "-----------"
arrKeys = dct.keys()
arrKeys.sort()
arrOut = []
for i in range(0, len(arrKeys)):
	if arrKeys[i] in dct:
		arrOut.append(dct[arrKeys[i]])
print arrOut

cv2.imshow('im',im)
cv2.imshow('out',out)
cv2.waitKey(0)
