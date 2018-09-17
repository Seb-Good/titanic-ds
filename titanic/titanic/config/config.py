"""Config variables for the project."""
import os

WORKING_DIR = (
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.realpath(__file__)
            )
        )
    )
)

DATA_DIR = os.path.join(WORKING_DIR, 'data', 'raw')
