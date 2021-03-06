import pytest
import rca
import numpy as np

from rca.aux import create_masks


def test_create_az_mask_ppi_returns_array():
    """ Tests whether create_az_mask_ppi returns an np array object
    """

    input_array = np.arange(118, 122)
    input_azi = 120
    radar_band = "c"

    ret_value = create_masks.create_az_mask_ppi(input_azi, input_array, radar_band)
    assert type(ret_value) == np.ndarray


def test_create_az_mask_ppi_correctly_finds_azi():
    """ Tests whether create_az_mask_ppi correctly indentifies the array element nearest
        the specified azimuth value
    """

    input_array = np.arange(119, 121)
    input_azi = 120
    radar_band = "c"

    ret_value = create_masks.create_az_mask_ppi(input_azi, input_array, radar_band)
    print(ret_value)
    assert ret_value[1] == True, "Correct azimuth was not identified"
    assert ret_value[0] == False, "Improper azimuths were set to true"


def test_create_az_mask_ppi_handles_0_and_360():
    """ Tests whether create_az_mask_ppi correctly handles the case of the specified azimuth
        being 0 or 360
    """

    input_array = np.array([-0.0, 0, 0.52, 359, 359.8, 360, 360.6])
    input_azi = 0.0
    radar_band = "c"

    ret_value = create_masks.create_az_mask_ppi(input_azi, input_array, radar_band)
    print(input_array)
    print(ret_value)

    # assert  ret_value[0] == False, 'Mishandling of -0.0, not identified as equal to 0.'
    assert ret_value[1] == True, "Correct azimuth not identified"
    assert (
        ret_value[2] == False or ret_value[3] == False
    ), "Improper azimuths set to true"
    assert (
        ret_value[3] == True or ret_value[4] == True or ret_value[5] == True
    ), "Mishandling of azimuths near 360."


def test_create_az_mask_rhi_returns_array():
    """ Tests whether create_az_mask_rhi returns an np array object
    """

    input_array = np.arange(118, 122)
    input_azi = 120
    radar_band = "c"

    ret_value = create_masks.create_az_mask_rhi(input_azi, input_array, radar_band)
    assert type(ret_value) == np.ndarray


def test_create_az_mask_rhi_correctly_finds_azi():
    """ Tests whether create_az_mask_rhi correctly indentifies the array element nearest
        the specified azimuth value
    """

    input_array = np.arange(117.0, 121.0)
    input_azi = 120
    radar_band = "c"

    ret_value = create_masks.create_az_mask_rhi(input_azi, input_array, radar_band)
    print(ret_value)
    assert ret_value[-1] == True, "Correct azimuth was not identified"
    assert ret_value[0] == False, "Improper azimuths were set to true"


def test_create_az_mask_rhi_handles_0_and_360():
    """ Tests whether create_az_mask_rhi correctly handles the case of the specified azimuth
        being 0 or 360
    """

    input_array = np.array([-0.0, 0, 0.52, 356, 359.8, 360, 360.6])
    input_azi = 0.0
    radar_band = "c"

    ret_value = create_masks.create_az_mask_rhi(input_azi, input_array, radar_band)
    print(input_array)
    print(ret_value)

    # assert  ret_value[0] == False, 'Mishandling of -0.0, not identified as equal to 0.'
    assert ret_value[1] == True, "Correct azimuth not identified"
    assert (
        ret_value[2] == False or ret_value[3] == False
    ), "Improper azimuths set to true"
    assert (
        ret_value[3] == True or ret_value[4] == True or ret_value[5] == True
    ), "Mishandling of azimuths near 360."
