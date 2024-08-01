# Opening gate system

## Overview

This project represents the core of an automated gate opening system, built using a hexagonal architecture. The system processes image frames from two cameras (inside and outside view) to determine whether to open the gate. It integrates various technologies to detect vehicles, recognize license plates, and control the gate.

### Features

- **Inside View Frame Source Handling**: Captures frames from an inside view camera (e.g., IP camera) and uses custom-trained machine learning models to check if a vehicle is present and whether it is approaching. If the vehicle is detected and approaching, a signal is sent to open the gate.
- **Outside View Frame Source Handling**: Captures frames from an outside view camera (e.g., IP camera) to detect and read license plates. If the license plate matches pre-approved numbers, the gate is opened.
- **Custom Machine Learning Models**:
  - **Vehicle Detection**: Uses a Keras-trained model to detect vehicles in frames.
  - **Vehicle Approach Detection**: Another Keras model is used to analyze whether the detected vehicle is approaching.
  - **License Plate Recognition**: YOLO is used for license plate detection, and EasyOCR for reading the license plate numbers.
- **Gate Control**: Integrates with an ESP-01 module to send signals for opening or closing the gate based on the detected conditions.
- **REST API for License Plate Management**: A Flask server provides an API to manage the list of approved license plates.

## Technologies Used
- **Programming Language**: Python
- **Machine Learning frameworks and libraries**:
  - Keras (for custom vehicle detection and approach models)
  - YOLO (for license plate detection)
  - EasyOCR (for optical character recognition of license plates)
- **Camera**: IP Cameras (for both frame sources)
- **Microcontroller**: ESP-01 (for gate control)
- **Web Framework**: Flask (for REST API)
- **Architecture**: Hexagonal Architecture
