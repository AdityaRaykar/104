import cv2
img = cv2.imread("solar-system.jpg")

cv2.imshow("Solar-System",img)


cv2.putText(img," Sun",(100,100),cv2.ACCESS_FAST,1 ,color=(255,255,255))
cv2.putText(img," Mercury",(100,300),cv2.ACCESS_FAST,1 ,color=(255,255,255))
cv2.putText(img," Venus",(250,300),cv2.ACCESS_FAST,1 ,color=(255,255,255))
cv2.putText(img," Earth",(350,300),cv2.ACCESS_FAST,1 ,color=(255,255,255))
cv2.putText(img,"Mars",(450,300),cv2.ACCESS_FAST,1 ,color=(255,255,255))
cv2.putText(img," Jupiter",(550,300),cv2.ACCESS_FAST,1 ,color=(255,255,255))
cv2.putText(img," Saturn",(650,300),cv2.ACCESS_FAST,1 ,color=(255,255,255))
cv2.putText(img,"Uranus",(750,300),cv2.ACCESS_FAST,1 ,color=(255,255,255))


cv2.waitKey(0)

cv2.imwrite("Solar.jpg",img)