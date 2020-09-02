from PIL import Image
import glob
import os

#Function to resize image, preserving aspect ratio
def resizeAspect(im, size):
    w,h = im.size
    aspect=min(size[0]/float(w), size[1]/float(h))
    return im.resize((int(w*aspect),int(h*aspect)),Image.ANTIALIAS)

img_width = 406
img_height = 350

imgList = glob.glob('./images/*.jpg')                  #Find all png images in a directory

for img in imgList:                                    #Loop through all found images
    im = Image.open(img)                               #open the image
    print("resizing:",os.path.basename(img))
    w,h = im.size                                      #Get image width and height
    if min(w,h)<img_width:                             #Check if either dimension is smaller then 600
        im=resizeAspect(im,(img_width,img_width))      #Re-size Image
        w,h = im.size                                  #update image size
    center = [int(w / 2.0), int(h / 2.0)]              #Calculate Center
    box = (center[0] - (img_width / 2), center[1] - (img_height / 2), center[0] + (img_width / 2), center[1] + (img_height / 2)) #Defines a box where you want it to be cropped
    croppedIm = im.crop(box)                           #Crop the image
    #croppedIm.show()                                  #Show the cropped image
    fileName, fileExtension=os.path.splitext(img)
    croppedIm.save(fileName+'_crop.jpg', "JPEG")       #Save the cropped image