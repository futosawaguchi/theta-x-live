import cv2
import numpy as np
import requests
from utils import get_camera_url, get_auth


def main():
    payload = {"name": "camera.getLivePreview"}
    response = requests.post(
        get_camera_url(),
        json=payload,
        auth=get_auth(),
        stream=True,
    )

    if response.status_code != 200:
        print(f"Failed to start live preview: {response.status_code}")
        return

    print("Live preview started. Press 'q' to quit.")

    buf = b""
    for chunk in response.iter_content(chunk_size=1024):
        buf += chunk
        start = buf.find(b"\xff\xd8")
        end = buf.find(b"\xff\xd9")
        if start != -1 and end != -1:
            jpg = buf[start : end + 2]
            buf = buf[end + 2 :]
            frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            if frame is not None:
                cv2.imshow("THETA X Live", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
