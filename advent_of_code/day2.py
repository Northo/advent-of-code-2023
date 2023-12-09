from dataclasses import dataclass

from advent_of_code.util import get_input_text

@dataclass(frozen=True, slots=True)
class Draw:
    red: int = 0
    green: int = 0
    blue: int = 0

    @classmethod
    def from_line(cls, line: str) -> "cls":
        # Line should be on format
        # 3 blue, 4 red
        counts = {}
        for part in line.split(","):
            count, color = part.strip().split(" ")
            counts[color.strip()] = int(count.strip())
        return Draw(**counts)

@dataclass(frozen=True, slots=True)
class Game:
    """Results from one game."""
    id: int
    draws: list[Draw]

    @classmethod
    def from_line(cls, line: str) -> "cls":
        # Line should look like
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        id_part, draw_part = line.split(":")

        # id part
        assert id_part.startswith("Game ")
        assert len(id_part.split(" ")) == 2
        id = int(id_part.split(" ")[1])

        # Draws
        draws = []
        for draw in draw_part.split(";"):
            draws.append(Draw.from_line(draw))
        return Game(
            id=id,
            draws=draws
        )

    def is_compatible_with(self, red: int, green: int, blue: int) -> bool:
        """Is the game compatible with given numbers?"""
        return all(
            draw.red <= red and draw.green <= green and draw.blue <= blue
            for draw in self.draws
        )

    def minimal_compatible_bag(self):
        return {
            "red": max(draw.red for draw in self.draws),
            "green": max(draw.green for draw in self.draws),
            "blue": max(draw.blue for draw in self.draws),
        }

def main():
    input = get_input_text(2)
    games = (Game.from_line(line) for line in input.strip().split('\n'))

    minimal_bags = (game.minimal_compatible_bag() for game in games)
    
    answer = sum(
        bag["red"] * bag["green"] * bag["blue"]
        for bag in minimal_bags
    )

    print(answer)

if __name__ == "__main__":
    main()