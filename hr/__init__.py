import importlib.metadata

try:
    __version__ = importlib.metadata.version(str(__package__))
except importlib.metadata.PackageNotFoundError:
    # package is not installed
    pass
