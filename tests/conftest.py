import logging
import os

import pytest
from faker import Faker

fake = Faker()

LOGGER = logging.getLogger(__name__)

TESTS_DIR = os.path.dirname(__file__)


@pytest.fixture(scope="function")
def some_fixture():
    """Description of Fixture"""

    # Setup
    # do your setup things here ...

    yield

    # Teardown / Cleanup
    # perform cleanup here
