import os
from pathlib import Path


class Action:
    def __init__(self, source: str):
        self.source = source
        self.source_path = Path(__file__).parent / "data" / self.source

    def __call__(self) -> None:
        pass


class PointToFile(Action):
    def __call__(self) -> None:
        print(self.source_path)


get_makefile = PointToFile("tuxpkg.mk")
get_debian_rules = PointToFile("debianrules.mk")


class RunScript(Action):
    def __call__(self) -> None:
        os.execv(str(self.source_path), [self.source])


create_repository = RunScript("create-repository")
release = RunScript("release")
