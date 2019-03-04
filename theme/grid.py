from itertools import repeat


class Grid:
    """Prints data in a grid format"""

    def __init__(self, cells, padding=2):
        self.cells = cells
        self.padding = padding

    def _column_widths(self, num_lines, num_columns):
        widths = list(repeat(0, num_columns))

        for index, cell in enumerate(self.cells):
            index = index // num_lines
            widths[index] = max(widths[index], len(cell))

        return {"lines": num_lines, "widths": widths}

    def _width_dimensions(self, max_width):
        num_cells = len(self.cells)

        if num_cells == 0:
            return {"lines": 0, "widths": []}

        if num_cells == 1:
            cell = self.cells[0]

            if len(cell) <= max_width:
                return {"lines": 1, "widths": [len(cell)]}
            else:
                return None

        for num_lines in range(1, num_cells):
            num_columns = num_cells // num_lines
            if num_cells % num_lines != 0:
                num_columns += 1

            total_seperator_width = (num_columns - 1) * self.padding
            if max_width < total_seperator_width:
                continue

            adjusted_width = max_width - total_seperator_width

            potential_dimensions = self._column_widths(num_lines, num_columns)
            if sum(potential_dimensions["widths"]) < adjusted_width:
                return potential_dimensions

    def fit_to(self, max_width):
        """Return a string containing the formatted grid fitted to a
        specified max_width"""

        dimensions = self._width_dimensions(max_width)
        string = ""

        if dimensions is not None:
            lines = dimensions["lines"]
            widths = dimensions["widths"]

            for line_count in range(lines):
                for width_count, width in enumerate(widths):
                    index = line_count + lines * width_count
                    if index >= len(self.cells):
                        continue

                    cell = self.cells[index]
                    if width_count == len(widths) - 1:
                        string += cell
                    else:
                        assert width >= len(cell)
                        string += f"{cell:<{width}}{' ' * self.padding}"
                string += "\n"
        else:
            for cell in self.cells:
                string += cell + "\n"

        return string
