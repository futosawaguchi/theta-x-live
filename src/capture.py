import time
from utils import camera_request


def take_picture() -> dict:
    response = camera_request("camera.takePicture")
    data = response.json()
    print(f"take_picture: {data}")
    return data


def start_capture() -> dict:
    response = camera_request("camera.startCapture")
    data = response.json()
    print(f"start_capture: {data}")
    return data


def stop_capture() -> dict:
    response = camera_request("camera.stopCapture")
    data = response.json()
    print(f"stop_capture: {data}")
    return data


if __name__ == "__main__":
    print("Taking a picture...")
    take_picture()
    time.sleep(2)
    print("Done.")
