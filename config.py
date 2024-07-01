from pathlib import Path

import yaml


class Config:
    client_id: str

    def __init__(
        self,
        client_id: str,
    ):
        kwargs = locals().copy()
        kwargs.pop("self")
        self.__dict__.update(kwargs)

    @classmethod
    def from_path(cls, path: Path) -> "Config":
        data = yaml.load(path.read_text("utf-8"), yaml.FullLoader)
        if data is None:
            raise Exception("config is none")

        return cls(**data)


config = Config.from_path(Path("config.yaml"))
