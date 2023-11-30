"""Initial documentation of SampleProject."""

from importlib.metadata import version as _version


try:
    __version__ = _version("jmct-sampleproject")
except Exception:
    # Local copy or not installed with setuptools.
    # Disable minimum version checks on downstream libraries.
    __version__ = "999"
