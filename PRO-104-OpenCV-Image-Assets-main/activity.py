import cv2
import  numpy as np

image = cv2.imread("images/butterfly.jpg")
# cv2.putText(image,"bon voyage!",(50,50),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale= 1,color = (0,0,255))
# print(image)
# cv2.imshow("butterfly", image)
# cv2.waitKey(0)

black = np.zeros([600,600])
# row = black[1:2]
# column = black[:, 1:2]
# print(row)
# print(column)
black[200:400,200:400] = 255
cv2.imshow("a black and white square", black)
cv2.waitKey(0)







