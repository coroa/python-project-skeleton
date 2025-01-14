"""Performs general tests."""
from sampleproject.libs import samplemodule as SM


def test_true():
    """Just asserts True."""
    assert True


def test_sampleclass():
    """Test samplemodule SampleClass true method."""
    s = SM.SampleClass()
    assert s.true() is True


def test_sampleclass_false():
    """Test samplemodule SampleClass false classmethod."""
    assert SM.SampleClass.false() is False


def test_undoc_func():
    """Test the undocumented function."""
    SM.this_is_and_undocumented_function("some")
