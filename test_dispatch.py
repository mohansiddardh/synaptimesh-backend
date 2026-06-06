from dispatcher import dispatch_command


def test_play():
    assert dispatch_command(
        "PLAY",
        0.95
    )["status"] == "executed"


def test_pause():
    assert dispatch_command(
        "PAUSE",
        0.95
    )["status"] == "executed"


def test_volume_up():
    assert dispatch_command(
        "VOLUME_UP",
        0.95
    )["status"] == "executed"


def test_volume_down():
    assert dispatch_command(
        "VOLUME_DOWN",
        0.95
    )["status"] == "executed"


def test_scroll_up():
    assert dispatch_command(
        "SCROLL_UP",
        0.95
    )["status"] == "executed"


def test_scroll_down():
    assert dispatch_command(
        "SCROLL_DOWN",
        0.95
    )["status"] == "executed"


def test_move_left():
    assert dispatch_command(
        "MOVE_LEFT",
        0.95
    )["status"] == "executed"


def test_move_right():
    assert dispatch_command(
        "MOVE_RIGHT",
        0.95
    )["status"] == "executed"


def test_click():
    assert dispatch_command(
        "CLICK",
        0.95
    )["status"] == "executed"