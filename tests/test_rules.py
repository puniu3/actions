# pytest test file
# English comments included

from game.state import GameState

def test_legal_move():
    """Test that a valid move is considered legal."""
    state = GameState.from_fen("start")
    # 'e2e4' is treated as a legal move by our dummy rule engine
    assert state.is_legal_move("e2e4")  # Valid move should pass

def test_illegal_move():
    """Test that an invalid move is considered illegal."""
    state = GameState.from_fen("start")
    # 'bad' has length 3, so it should be considered illegal
    assert not state.is_legal_move("bad")  # Invalid move should fail
