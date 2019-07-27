import cv2
img = cv2.imread("test.jpeg")
b,r,g = cv2.split(img)
img2 = cv2.merge((r,g,b))

dimensions = img.shape

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
 
print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)



#cv2.imshow('Image1',img)
#cv2.imshow('Image2',img2)

edges = cv2.Canny(img,100,200)
print(edges)
 
cv2.imshow("Edge Detected Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()