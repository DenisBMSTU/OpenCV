import sys

import numpy as np
import cv2

#################      read and change image        ###################
image_load = cv2.imread('pic/1.png')
crop_image = image_load[40:60, 56:655]
im = cv2.resize(crop_image,None,fx=4.5, fy=4.5, interpolation = cv2.INTER_CUBIC)
im3 = im.copy()

gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #translate to white-black
blur = cv2.GaussianBlur(gray,(5,5),0) #filter Gauss
thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)

#################      Now finding Contours         ###################

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) #find countours

samples =  np.empty((0,100)) #create empty array
responses = [] 
keys = [i for i in range(0,1300)] #figurs (0,1,2..9)

for cnt in contours:
	if cv2.contourArea(cnt)>50: #draws rectangle
		[x,y,w,h] = cv2.boundingRect(cnt) #(x,y) - top-left coordinate of the rectangle  							
											#and (w,h) - width and height. 
		if  h>30:
			cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
			roi = thresh[y:y+h,x:x+w] #region Of interest
			roismall = cv2.resize(roi,(10,10)) #resize find region of interest
			cv2.imshow('norm',im) 
			key = cv2.waitKey(0)
			if key == 27:  #escape to quit
				sys.exit()
			else:
				if key in keys:
					responses.append(chr(key))
					sample = roismall.reshape((1,100))
					samples = np.append(samples,sample,0)


responses = np.array(responses)
responses = responses.reshape((responses.size,1))
print "training complete"
newMass = []
#################      save samples and responsees         ###################
for i in range(0, len(responses)):
	responses[i] = "".join(responses[i])
	print responses[i]
	newMass.append(responses[i][0])
for i in range(0, len(newMass)):
	newMass[i] = ord(newMass[i])
print newMass
np.savetxt('generalsamples.data',samples)
np.savetxt('generalresponses.data',newMass)

