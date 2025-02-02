from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Union, Tuple, Annotated, Literal
    from colour import Color
    import numpy as np

    # Abbreviations for a common types
    ManimColor = Union[str, Color, None]
    RangeSpecifier = Tuple[float, float, float] | Tuple[float, float]

    # These are various alternate names for np.ndarray meant to specify
    # certain shapes.
    # 
    # In theory, these annotations could be used to check arrays sizes
    # at runtime, but at the moment nothing actually uses them, and
    # the names are here primarily to enhance readibility and allow
    # for some stronger type checking if numpy has stronger typing
    # in the future
    FloatArray = np.ndarray[int, np.dtype[np.float64]]
    Vect2 = Annotated[FloatArray, Literal[2]]
    Vect3 = Annotated[FloatArray, Literal[3]]
    Vect4 = Annotated[FloatArray, Literal[4]]
    VectN = Annotated[FloatArray, Literal["N"]]
    Matrix3x3 = Annotated[FloatArray, Literal[3, 3]]
    Vect2Array = Annotated[FloatArray, Literal["N", 2]]
    Vect3Array = Annotated[FloatArray, Literal["N", 3]]
    Vect4Array = Annotated[FloatArray, Literal["N", 4]]
