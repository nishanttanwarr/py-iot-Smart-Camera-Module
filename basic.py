import cv2  
import pickle
import face_recognition


# Check openCV version and backend
print(cv2._version_)
#imgback= cv2.imread('photos/frame.png')

# Open camera (adjust index if needed)
cap = cv2.VideoCapture(0)

# Query supported resolutions
supported_resolutions = []
for i in range(19):
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH + i)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT + i)
    if width > 0 and height > 0:
        supported_resolutions.append((width, height))

# Select a supported resolution (e.g., closest to desired)
chosen_res = (640, 480)  # Example choice

# Set resolution
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, chosen_res[0])
ret &= cap.set(cv2.CAP_PROP_FRAME_HEIGHT, chosen_res[1])

#if not ret:
    #sprint("Error setting resolution")
    # Consider retrying with another resolution or logging an error



#load the file
print("loading encjded file")
file= open("encodefile.p",'rb')
encodelistknownid= pickle.load(file)
file.close()
encodelistknown,studentid= encodelistknownid
#print(studentid)
print("file loaded")