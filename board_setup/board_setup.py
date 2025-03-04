"""
board_setup.py

This module contains the BoardSetup class responsible for:
 - Initializing and resetting a 2D board (0 = water, 1..7 = ship ID)
 - Placing ships according to a dict {ship_id: count}
 - Providing board statistics and individual tile lookups
"""

import random


def _generate_shape(spec: dict) -> list:
    shape_type = random.choice(spec['shapes'])
    size = spec['size']

    if shape_type == 'I':
        return [(i, 0) for i in range(size)]
    elif shape_type == 'L':
        return [(0, i) for i in range(size)] + [(1, size-1)]
    elif shape_type == 'T':
        return [(i, 0) for i in range(3)] + [(1, 1)]
    elif shape_type == 'Z':
        return random.choice([
            [(0,0), (1,0), (1,1), (2,1)],
            [(0,1), (1,1), (1,0), (2,0)]
        ])
    elif shape_type == 'TT':
        return [(0,0), (1,0), (2,0), (3,0), (2,1), (2,2)]
    return []


def _generate_l_shape() -> list:
    """Generates different variations of L-shaped ships with explicit coordinates"""
    variants = [
        # Vertical leg + horizontal base
        [(0, 0), (0, 1), (0, 2), (1, 2)],  # classic L shape
        [(0, 0), (1, 0), (2, 0), (2, 1)],  # rotated L shape
        # Horizontal base + vertical leg
        [(0, 0), (1, 0), (2, 0), (0, 1)],  # mirrored L shape
        [(0, 0), (0, 1), (1, 1), (2, 1)]   # inverted L shape
    ]
    return random.choice(variants)


def _rotate_shape(shape: list, degrees: int, x: int, y: int) -> list:
    rotated = []
    for dx, dy in shape:
        if degrees == 90:
            dx, dy = -dy, dx
        elif degrees == 180:
            dx, dy = -dx, -dy
        elif degrees == 270:
            dx, dy = dy, -dx
        rotated.append((x + dx, y + dy))
    return rotated


class BoardSetup:
    def __init__(self, rows: int, cols: int, ships_dict: dict[int, int]):
        """
        Initializes the game board with specified dimensions and ship configuration.
        
        Parameters:
        rows (int): Number of rows in the game board
        cols (int): Number of columns in the game board
        ships_dict (dict): Dictionary mapping ship IDs to their quantities
        """
        # Store basic board configuration
        self.rows = rows
        self.cols = cols
        self.ships_dict = ships_dict
        
        # Initialize empty board (0 = water, 1-7 = ship IDs)
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        
        # Define ship specifications including size and possible shapes
        self.ship_specs = {
            1: {'size': 2, 'shapes': ['I']},  # Smallest ship
            2: {'size': 3, 'shapes': ['I']},  # Medium ship
            3: {'size': 4, 'shapes': ['I']},  # Large ship
            4: {'size': 4, 'shapes': ['T']},  # T-shaped ship
            5: {'size': 4, 'shapes': ['L']},  # L-shaped ship
            6: {'size': 4, 'shapes': ['Z']},  # Z-shaped ship
            7: {'size': 6, 'shapes': ['TT']}  # Special TT-shaped ship
        }

    def get_board(self) -> list[list[int]]:
        """
        Returns the current 2D board state.
        0 = water, 1..7 = specific ship ID.
        """
        return [row.copy() for row in self.board]

    def get_tile(self, x: int, y: int) -> int:
        """
        Returns the value at board coordinate (x, y).
        0 = water, or 1..7 = ship ID.
        
        Raises an IndexError if the coordinates are out of bounds.
        Note: x is column, y is row.
        """
        if not (0 <= x < self.cols and 0 <= y < self.rows):
            raise IndexError("Coordinates out of bounds")
        return self.board[y][x]

    def place_ships(self) -> list[list[int]]:
        ship_ids = sorted(self.ships_dict.keys(), key=lambda x: self.ship_specs[x]['size'], reverse=True)
        
        for ship_id in ship_ids:
            count = self.ships_dict[ship_id]
            for _ in range(count):
                if not self._try_place_ship(ship_id):
                    raise ValueError(f"Cannot place ship {ship_id}")
        return self.board

    def _try_place_ship(self, ship_id: int) -> bool:
        spec = self.ship_specs[ship_id]
        max_attempts = 69000  # Increased number of attempts
        
        for _ in range(max_attempts):
            # Generate all possible variations for L shape
            if ship_id == 5:
                shape = _generate_l_shape()
            else:
                shape = _generate_shape(spec)
                
            if not shape:
                continue
                
            x = random.randint(0, self.cols - 1)
            y = random.randint(0, self.rows - 1)
            orientation = random.choice([0, 90, 180, 270])
            
            cells = _rotate_shape(shape, orientation, x, y)
            if cells and self._is_valid_placement(cells):
                for cx, cy in cells:
                    self.board[cy][cx] = ship_id
                return True
        return False

    def _is_valid_placement(self, cells: list) -> bool:
        """Checks if ship placement is valid by verifying:
        1. All cells are within board boundaries
        2. No collisions with existing ships
        3. No direct adjacency with other ships
        """
        for x, y in cells:
            # Boundary check
            if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
                return False
            # Collision check
            if self.board[y][x] != 0:
                return False
            
            # Adjacency check (only direct neighbors)
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < self.cols and 0 <= ny < self.rows:
                    if self.board[ny][nx] != 0:
                        return False
        return True

    def reset_board(self) -> None:
        """
        Resets the board back to all 0 (water).
        """
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def board_stats(self) -> dict:
        """
        Calculates and returns basic statistics about the current board state.
        
        Returns:
        dict: Contains counts of empty and occupied spaces
        """
        occupied = sum(cell != 0 for row in self.board for cell in row)
        return {
            "empty_spaces": self.rows * self.cols - occupied,
            "occupied_spaces": occupied
        }