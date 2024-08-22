# IoT-Based Smart Camera Module with Face Recognition

This project is an IoT-based smart camera module that uses Python for real-time face recognition. It leverages OpenCV and the `face_recognition` library to identify individuals from a pre-encoded set of face data, providing a basis for smart surveillance and attendance systems.

## Project Overview

The project is composed of three key Python scripts:

1. **`encoding.py`**: Encodes images of faces into a format that can be used for recognition.
2. **`basic.py`**: Sets up the camera and verifies that the encoded face data is loaded correctly.
3. **`main.py`**: Runs the main application, capturing video, recognizing faces, and displaying the IDs of recognized individuals.

## Features

- **Real-Time Face Recognition**: Detects and identifies faces in real-time from a video feed.
- **Customizable Resolution**: Supports multiple camera resolutions to adapt to different hardware setups.
- **IoT Integration**: Designed for integration into IoT environments, making it suitable for smart home or security applications.

## Hardware Requirements

- **Raspberry Pi** (or similar IoT device)
- **Camera Module** compatible with the IoT device
- **Internet Connection** for remote monitoring (optional)

## Software Requirements

Ensure you have Python installed on your IoT device along with the following Python packages:

- OpenCV
- face_recognition
- pickle
- os

### Install the required Python libraries using pip:

```bash
pip install opencv-python face_recognition
```
## Setup Instructions
------------------

### Step 1: Prepare Face Images

-   Create a directory named `photos`.
-   Place images of individuals to be recognized in this directory.
-   Name each image file according to the individual's ID (e.g., `john_doe.jpg`).

### Step 2: Encode the Faces

Run the `encoding.py` script to generate encodings for all faces in the `photos` directory:
```bash
`python encoding.py`
```
This will create a file named `encodefile.p` containing the face encodings and their corresponding IDs.

### Step 3: Verify Setup

Use the `basic.py` script to ensure that your camera is functioning correctly and that the encoded file loads without errors:
```bash
`python basic.py`
```
### Step 4: Run the Smart Camera Module

Execute the `main.py` script to start the face recognition system:
```bash
`python main.py`
```
This script will capture video from the camera, detect faces, and display the ID of any recognized individual.

## How It Works
------------

### Encoding Faces

The `encoding.py` script reads images from the `photos` folder, encodes each face using the `face_recognition` library, and saves these encodings along with their corresponding IDs into `encodefile.p`.

### Face Recognition

The `main.py` script captures video, detects faces, compares them to the known encodings, and displays the recognized person's ID on the screen.

### IoT Integration

This smart camera module can be integrated into an IoT ecosystem for tasks such as:

-   **Smart Surveillance**: Monitor and identify individuals in real-time.
-   **Automated Attendance**: Track attendance in classrooms or workplaces.
-   **Home Automation**: Trigger events when specific individuals are recognized.

## Troubleshooting
---------------

-   **Resolution Issues**: If the camera fails to set the desired resolution, the system will revert to a default resolution.
-   **Missing Files**: Ensure `encodefile.p` exists before running the main application.

## Future Enhancements
-------------------

-   **Remote Monitoring**: Add features for monitoring video feed and recognized faces over the internet.
-   **Advanced Analytics**: Integrate AI for more complex behavioral analytics.
-   **Energy Efficiency**: Optimize for low-power operation on IoT devices.
