from dataclasses import dataclass
from datetime import datetime


@dataclass
class VideoSource:
    width: int
    height: int
    fps: int
    size: int
    url: str
    original: dict


@dataclass
class Video:
    extern_id: str
    title: str
    poster: str
    duration: int
    original: dict
    published: datetime
    tags: list[str]
    sources: list[VideoSource]
