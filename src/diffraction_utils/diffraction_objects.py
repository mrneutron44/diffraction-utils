import uuid


class DiffractionObject:
    """Class for storing and manipulating diffraction data.

    This class is copied from diffpy.utils.
    DiffractionObject stores data produced from X-ray, neutron,
    and electron scattering experiments. The object can transform
    between different scattering quantities such as q (scattering vector),
    2θ (two-theta angle), and d (interplanar spacing), and perform various
    operations like scaling, addition, subtraction, and comparison for equality
    between diffraction objects.

    Attributes
    ----------
    scat_quantity : str
        The type of scattering experiment (e.g., "x-ray", "neutron"). Default
        is an empty string "".
    wavelength : float
        The wavelength of the incoming beam, specified in angstroms (Å).
        Default is none.
    name: str
        The name or label for the scattering data. Default is an empty string
        "".
    qmin : float
        The minimum q value.
    qmax : float
        The maximum q value.
    tthmin : float
        The minimum two-theta value.
    tthmax : float
        The maximum two-theta value.
    dmin : float
        The minimum d-spacing value.
    dmax : float
        The maximum d-spacing value.
    """

    def __init__(
        self,
        xarray,
        yarray,
        xtype,
        wavelength=None,
        scat_quantity="",
        name="",
        metadata={},
    ):
        """Initialize a DiffractionObject instance.

        Parameters
        ----------
        xarray : ndarray
            The independent variable array containing "q", "tth", or "d" values.
        yarray : ndarray
            The dependent variable array corresponding to intensity values.
        xtype : str
            The type of the independent variable in `xarray`. Must be one of
            {*XQUANTITIES}.
        wavelength : float, optional, default is None.
            The wavelength of the incoming beam, specified in angstroms (Å)
        scat_quantity : str, optional, default is an empty string "".
            The type of scattering experiment (e.g., "x-ray", "neutron").
        name : str, optional, default is an empty string "".
            The name or label for the scattering data.
        metadata : dict, optional, default is an empty dictionary {}
            The additional metadata associated with the diffraction object.

        Examples
        --------
        Create a DiffractionObject for X-ray scattering data:
        >>> import numpy as np
        >>> from diffpy.utils.diffraction_objects import DiffractionObject
        ...
        >>> x = np.array([0.12, 0.24, 0.31, 0.4])  # independent variable (e.g., q)  # noqa: E501
        >>> y = np.array([10, 20, 40, 60])  # intensity values
        >>> metadata = {
        ...     "sample": "rock salt from the beach",
        ...     "composition": "NaCl",
        ...     "temperature": "300 K,",
        ...     "experimenters": "Phill, Sally"
        ... }
        >>> do = DiffractionObject(
        ...     xarray=x,
        ...     yarray=y,
        ...     xtype="q",
        ...     wavelength=1.54,
        ...     scat_quantity="x-ray",
        ...     name="beach_rock_salt_1",
        ...     metadata=metadata
        ... )
        >>> print(do.metadata)
        """

        self._uuid = uuid.uuid4()
        self._input_data(
            xarray, yarray, xtype, wavelength, scat_quantity, name, metadata
        )

    def _input_data(
        self, xarray, yarray, xtype, wavelength, scat_quantity, name, metadata
    ):
        if len(xarray) != len(yarray):
            raise ValueError(
                "'xarray' and 'yarray' are different lengths.  They must "
                "correspond to each other and have the same length. "
                "Please re-initialize 'DiffractionObject'"
                "with valid 'xarray' and 'yarray's"
            )
        self.scat_quantity = scat_quantity
        self.wavelength = wavelength
        self.metadata = metadata
        self.name = name
        self._input_xtype = xtype
