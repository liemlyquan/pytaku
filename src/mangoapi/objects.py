from dataclass import dataclass

@dataclass
class Chapter
    id: int
    name: str
    volume: int
    group: List[str]
    

@dataclass
class Title:
    id: int
    name: str
    site: str
    cover_ext: str
    alt_names: List[str]
    descriptions: List[str]
    description_format: str
    is_webhook: bool

