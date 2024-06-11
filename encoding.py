import cv2 as cv
import face_recognition
import pickle
import os

#importing images
folderpath= 'photos'
pathlist= os.listdir(folderpath)
#print(pathlist)

imglist= []
stundeid=[]

for path in pathlist:
    imglist.append(cv.imread(os.path.join(folderpath,path)))
    print(path)
    print(os.path.splitext(path)[0])
    stundeid.append(os.path.splitext(path)[0])
print(stundeid)

#

def findenc(imgagelist):
    encodelist = []
    for img in imgagelist:
        img =cv.cvtColor(img,cv.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        encodelist.append(encode)

    return encodelist

print("encodinf started")
encodelistknown = findenc(imglist)
#print(encodelistknown)
encodelistknownid= [encodelistknown,stundeid]
print('encoding complete')


file = open("encodefile.p",'wb')
pickle.dump(encodelistknownid,file)
file.close()
print('file saved')