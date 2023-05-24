from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Channel:
    extern_id: str
    name: str
    url: str
    title: str = None
    description: str = None
    poster: str = None


@dataclass
class VideoSource:
    extern_id: str
    original: dict
    width: int
    height: int
    size: int
    url: str
    mime: str
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
    tags: list[str] = field(default_factory=list)
