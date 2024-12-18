import cv2 
# syntex
# img= cv2.imread(path,flag)


#without identifier
# img=cv2.imread('first.jpg')
# print(img)


# Present Folder
# img = cv2.imread('./first.jpg')
# print(img)


# Child folder

# img = cv2.imread('./image/first.jpg')
# print(img)





# Double Backslac
# img = cv2.imread('D:\\AI\\Computer Vision\\open-cv-practice-with-magnet-brain\\image\\first.jpg')
# print(img)


# Raw String
# img = cv2.imread(r'D:\AI\Computer Vision\open-cv-practice-with-magnet-brain\image\first.jpg')
# print(img)



# img = cv2.imread('D:/AI/Computer Vision/open-cv-practice-with-magnet-brain/image/first.jpg')
# print(img)



#FLAG
# flag: The flag specifies the way how the image should be read.
# cv2.IMREAD_COLOR – It specifies to load a color image. Any transparency of image will be neglected. It is the default flag. Alternatively, we can pass integer value 1 for this flag.
# cv2.IMREAD_GRAYSCALE – It specifies to load an image in grayscale mode. Alternatively, we can pass integer value 0 for this flag. 
# cv2.IMREAD_UNCHANGED – It specifies to load an image as such including alpha channel. Alternatively, we can pass integer value -1 for this flag.


# 1-->cv.IMREAD_COLOR
# 0-->cv.IMREAD_GRAYSCALE
# -1-->cv.IMREAD_UNCHANGED


# img=cv2.imread('first.jpg',0)
# img=cv2.imread('first.jpg',1)
# img=cv2.imread('first.jpg',-1)



# img=cv2.imread('first.jpg',cv2.IMREAD_COLOR)
# img=cv2.imread('first.jpg',cv2.IMREAD_GRAYSCALE)
# img=cv2.imread('first.jpg',cv2.IMREAD_UNCHANGED)




#Return
# img=cv2.imread('first.jpg',cv2.IMREAD_COLOR)
# print(img)
# print(type(img))



# print(cv2.imread('first.jpg'))
# print('........................')
# print(cv2.imread('first.jpg',1))



# print(cv2.imread('first.jpg',1))
# print('...............................')


# print(cv2.imread('first.jpg',0))
# print('...............................')

# print(cv2.imread('first.jpg',-1))


# img=cv2.imread('first.jpg',1)
# print(img)
# print("..............................")
# print(img[0])

# This prints the first row of pixels in the image (index 0 along the height axis).
# print(len(img[0]))
# This prints the length of the first row, i.e., the number of pixels in the width of the image.

# print(img[1])
# This prints the second row of pixels in the image (index 1 along the height axis), just like img[0], but for the second row.

# print(len(img[1]))

# print(img[:,0])
# This prints all the pixel values in the first column of the image (index 0 along the width axis)

# print(len(img[:,0]))


# print(img[:,0])
# print(len(img[:,1]))


# print(img[:,:,0])
# print(len(img[:,:,0]))


img=cv2.imread('first.jpg',0)
print(img)
# print("..............................")
# print(img[0])
# print('..........................')
# print(img[1])
print('..........................')
print(len(img[0]))

# print('..........................')
# print(img[:,0])



