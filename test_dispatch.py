from dispatcher import dispatch_command


def test_play():
    result = dispatch_command("PLAY", 0.95)
    assert result["status"] == "executed"


def test_pause():
    result = dispatch_command("PAUSE", 0.95)
    assert result["status"] == "executed"


def test_volume_up():
    result = dispatch_command("VOLUME_UP", 0.95)
    assert result["status"] == "executed"


def test_volume_down():
    result = dispatch_command("VOLUME_DOWN", 0.95)
    assert result["status"] == "executed"


def test_next_track():
    result = dispatch_command("NEXT_TRACK", 0.95)
    assert result["status"] == "executed"


def test_prev_track():
    result = dispatch_command("PREV_TRACK", 0.95)
    assert result["status"] == "executed"


def test_scroll_up():
    result = dispatch_command("SCROLL_UP", 0.95)
    assert result["status"] == "executed"


def test_scroll_down():
    result = dispatch_command("SCROLL_DOWN", 0.95)
    assert result["status"] == "executed"


def test_click():
    result = dispatch_command("CLICK", 0.95)
    assert result["status"] == "executed"


def test_double_click():
    result = dispatch_command("DOUBLE_CLICK", 0.95)
    assert result["status"] == "executed"


def test_right_click():
    result = dispatch_command("RIGHT_CLICK", 0.95)
    assert result["status"] == "executed"


def test_move_left():
    result = dispatch_command("MOVE_LEFT", 0.95)
    assert result["status"] == "executed"


def test_move_right():
    result = dispatch_command("MOVE_RIGHT", 0.95)
    assert result["status"] == "executed"


def test_move_up():
    result = dispatch_command("MOVE_UP", 0.95)
    assert result["status"] == "executed"


def test_move_down():
    result = dispatch_command("MOVE_DOWN", 0.95)
    assert result["status"] == "executed"