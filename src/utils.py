import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_camera_url() -> str:
    ip = os.getenv("THETA_IP", "192.168.1.1")
    return f"http://{ip}/osc/commands/execute"


def get_auth() -> requests.auth.HTTPDigestAuth:
    serial = os.getenv("THETA_SERIAL")
    if not serial:
        raise ValueError("THETA_SERIAL is not set in .env")
    password = os.getenv("THETA_PASSWORD", serial)
    username = f"THETA{serial}"
    return requests.auth.HTTPDigestAuth(username, password)


def camera_request(command: str, params: dict = None) -> requests.Response:
    payload = {"name": command}
    if params:
        payload["parameters"] = params
    return requests.post(
        get_camera_url(),
        json=payload,
        auth=get_auth(),
    )
