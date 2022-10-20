from dataclasses import dataclass
from datetime import datetime


@dataclass
class Channel:
    name: str
    url: str
    title: str = None
    description: str = None
    poster: str = None


@dataclass
class VideoSource:
    original: dict
    width: int
    height: int
    size: int
    url: str
    fps: int = None


@dataclass
class Video:
    extern_id: str
    original: dict
    title: str
    poster: str
    duration: int
    published: datetime
    sources: list[VideoSource]
    description: str = None
    tags: list[str] = list
