import cv2 
img = cv2.imread('image/imagelow.jpg')
# print(img)
# print(type(img))


#Display
cv2.imshow('Our image',img)

# Display for longer duration or to copy keyboard input
# cv2.waitKey(5)
# cv2.waitKey(50)
# cv2.waitKey(500)
# cv2.waitKey(5000)
# cv2.waitKey(0)

# x = cv2.waitKey(0)
# print("keypress--",x)

# other option
# cv2.pollKey()
#cv2.waitKeyEx()

#Destroy
cv2.destroyAllWindows()

# Limition 
# img = cv2.imread('image/imagelow.jpg')
# cv2.imshow("our image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# img = cv2.imread('image/imagehigh.jpg')
# cv2.imshow("our image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Different slicing
# img = cv2.imread('image/imagelow.jpg')
# img_modified=img[0:,0:200]
# cv2.imshow("our image",img_modified)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# display ndarray

# # Black image
import numpy as np
# matrx = np.zeros((500,500),dtype='uint8')
# cv2.imshow("our image",matrx)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import random
# matrx = np.zeros((800,800,3),dtype='uint8')


# for i in range(800):
#     for j in range(800):
#         matrx[i,j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        
        
# cv2.imshow("our image",matrx)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# import random
# matrx = np.zeros((800,800,3),dtype='uint8')


# for i in range(800):
#     for j in range(800):
#         matrx[i,j]=[random.randint(0,100),random.randint(0,100),random.randint(0,100)]
        
        
# cv2.imshow("our image",matrx)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
