from pathlib import Path


def run():
    path = Path(__file__).parent / "data" / "tuxpkg.mk"
    assert path.exists()
    print(path)
