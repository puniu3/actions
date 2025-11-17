# Minimal game state for pytest example
# English comments included
# test comment

class GameState:
    @staticmethod
    def from_fen(fen: str):
        """Create and return a new GameState from a FEN-like string.
        This is a stub for demonstration purposes.
        """
        return GameState()

    def is_legal_move(self, move: str) -> bool:
        """Very simple rule: any move of length 4 is considered legal.
        In a real game engine, you would check full game rules here.
        """
        return len(move) == 4
