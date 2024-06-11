import cv2
import pickle
import face_recognition

# ... (Existing Code:  OpenCV version check, camera setup, resolution handling)
# Check OpenCV version and backend
print(cv2._version_)

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
# Consider adding user input here for better compatibility
chosen_res = (640, 480)  # Example choice

# Set resolution
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, chosen_res[0])
ret &= cap.set(cv2.CAP_PROP_FRAME_HEIGHT, chosen_res[1])

if not ret:
    print("Error setting resolution. Using default instead.")


# Load encoded data and student IDs
try:
  with open("encodefile.p", "rb") as file:
    encodelistknown, studentid = pickle.load(file)
except FileNotFoundError:
  print("Encoding file not found. Please create or load 'encodefile.p'.")
  exit()

print("File loaded successfully.")

# Adjustable Parameters
DISTANCE_THRESHOLD = 0.7
  # Threshold for recognizing a face

# Capture video frames and perform facial recognition
while True:
  ret, frame = cap.read()

  if ret:
    # Resize frame for efficiency  
    frame = cv2.resize(frame, (0, 0), fx=0.9, fy=0.9)

    # Convert to RGB for face_recognition
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces and encode them
    face_locations = face_recognition.face_locations(frame_rgb)
    face_encodings = face_recognition.face_encodings(frame_rgb, face_locations)

    # Compare detected faces to known encodings
    for face_encoding, face_location in zip(face_encodings, face_locations):
      matches = face_recognition.compare_faces(encodelistknown, face_encoding)
      face_distances = face_recognition.face_distance(encodelistknown, face_encoding)

      # Get index of closest match, if any, within the threshold
      best_match_index = None
      min_distance = float("inf")
      for i, (match, distance) in enumerate(zip(matches, face_distances)):
        if match and distance < min_distance and distance <= DISTANCE_THRESHOLD: 
          min_distance = distance
          best_match_index = i

      # Identify if a match is found within the threshold 
      if best_match_index is not None:
        identified_person_id = studentid[best_match_index]

        # Draw box and label
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, top - 35), (right, top), (0, 0, 255), cv2.FILLED)
        cv2.putText(frame, identified_person_id, (left + 6, top - 6), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow("Video", frame)

  # Check for 'q' key press to quit
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

# Release resources
cap.release()
cv2.destroyAllWindows()