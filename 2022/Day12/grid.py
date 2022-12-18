from math import ceil, log10


class Grid:

    START = "S"
    STOP = "E"

    START_VALUE = "a"
    STOP_VALUE = "z"

    @staticmethod
    def __read_input_file(path_in):
        if path_in is None:
            return None
        else:
            with open(path_in, "r") as input_file:
                return tuple(input_file.readlines())

    @staticmethod
    def __find_char(char, lines):
        for line in lines:
            if char in line:
                return line.index(char), lines.index(line)

    @staticmethod
    def __get_value_of_char(char):
        return ord(char.lower()) - 97

    def __init__(self, path_in=None):
        lines = self.__read_input_file(path_in)
        self.start = self.__find_char(self.START, lines)
        self.stop = self.__find_char(self.STOP, lines)

        self.__contents = self.__generate_contents(lines)
        self.__height = len(self.__contents)
        self.__width = 0 if self.__height == 0 else len(self.__contents[0])

    def __str__(self):
        if self.__contents:
            spacing = ceil(log10(self.maximum))
            single_format = "{:" + str(spacing) + "} "
            full_format = single_format * (self.__width - 1)
            return "\n".join(
                full_format.format(*row) for row in self.__contents
            )

        else:
            return "Grid()"

    def __generate_contents(self, lines):
        if lines is None:
            return tuple()
        else:
            return tuple(
                tuple(self.__get_value_of_char(c) for c in line) for line in lines
            )

    def access(self, coordinates):
        x, y = coordinates
        if x > self.__width or x < 0 or y > self.__height or y < 0:
            msg = f"{type(self).__name__} index out of range, indices must be positive"
            raise IndexError(msg)
        else:
            return self.__contents[y][x]

    @property
    def maximum(self):
        try:
            return max(
                max(row for row in self.__contents)
            )
        except ValueError:
            return 0

    @property
    def minimum(self):
        try:
            return min(
                min(row for row in self.__contents)
            )
        except ValueError:
            return 0

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
