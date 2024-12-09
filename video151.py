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



img=cv2.imread('first.jpg',cv2.IMREAD_COLOR)
img=cv2.imread('first.jpg',cv2.IMREAD_GRAYSCALE)
img=cv2.imread('first.jpg',cv2.IMREAD_UNCHANGED)




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


img=cv2.imread('first.jpg',1)
print(img)
print("..............................")
# print(img[0])
# print(len(img[0]))
# print(img[1])

# print(len(img[1]))

print(img[:,0])
print(len(img[:,0]))