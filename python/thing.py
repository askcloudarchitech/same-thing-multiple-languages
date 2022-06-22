"""Python 3"""
# install python:
# already on MacOS / UNIX?
# TODO: Windows install instructions

class Thing:
    """Something."""

    def __init__(self, color: str, shape: str) -> None:
        """Construct class."""
        self._color = color
        self._shape = shape

    def set_color(self, color) -> None:
        """Set color."""
        self._color = color

    def set_shape(self, shape) -> None:
        """Set shape."""
        self._shape = shape

    def get_color(self) -> str:
        """Set color."""
        return self._color

    def print_color(self) -> None:
        """Print color."""
        print(self._color)

    def print_shape(self) -> None:
        """Print shape."""
        print(self._shape)

    def is_it_red(self) -> bool:
        """Check if thing is red."""
        if self._color.lower() == "red":
            return True
        return False


def red_blue_counts(things: list[Thing]) -> None:
    """Provide counts of red and blue."""
    red_count = 0
    blue_count = 0

    # python 3.10 has pattern matching but went with if / else since this it's
    # more traditional (and in older version of python)
    for thing in things:
        if thing.get_color() == "red":
            red_count += 1
        elif thing.get_color() == "blue":
            blue_count += 1

    print(f"blue: {blue_count} \nred: {red_count} \n")


def main():
    """Run main function."""
    things = []
    things.append(Thing("red", "square"))
    things.append(Thing("blue", "round"))
    things.append(Thing("red", "round"))

    for thing in things:
        thing.print_color()
        if thing.is_it_red():
            print("it's red")
        else:
            print("it's not red")

    red_blue_counts(things)


if __name__ == "__main__":
    main()
