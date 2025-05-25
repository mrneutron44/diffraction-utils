import pytest
import numpy as np
from diffraction_utils.diffraction_objects import DiffractionObject as DO


@pytest.mark.parametrize(
    "xarray, yarray, xtype, wavelength, scat_quantity, name, metadata",
    [
        (
            np.array([0.1, 0.2, 0.3]),
            np.array([10, 20, 30]),
            "q",
            1.54,
            "x-ray",
            "sample1",
            {"sample": "NaCl"},
        ),
        (
            np.array([10, 20, 30]),
            np.array([5, 15, 25]),
            "tth",
            1.0,
            "neutron",
            "sample2",
            {"temperature": "300 K"},
        ),
    ],
)
def test_diffraction_object_init(
    xarray, yarray, xtype, wavelength, scat_quantity, name, metadata
):
    do = DO(xarray, yarray, xtype, wavelength, scat_quantity, name, metadata)

    assert do.scat_quantity == scat_quantity
    assert do.wavelength == wavelength
    assert do.name == name
    assert hasattr(do, "_uuid")
