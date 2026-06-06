import pytest

from exceptions import InvalidCommandError


def test_invalid_command():

    with pytest.raises(
        InvalidCommandError
    ):

        raise InvalidCommandError()