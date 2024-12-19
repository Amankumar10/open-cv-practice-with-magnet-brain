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

# 42:24