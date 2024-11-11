from typing import Callable
from requests import Request, Response


def expose(
    inference_function: Callable[[Request], Response],
    port: int = 10000,
    hangup_function: Callable[[], None] = None,
    hangup_timeout_sec: int = 1800,
    hangup_interval_sec: int = 60,
):
    pass
