#!/usr/bin/env python3
"""Generate Aariso0's pixel-art GitHub mascot as a dependency-free SVG."""
from pathlib import Path

W, H = 48, 56
GRID = [['.' for _ in range(W)] for _ in range(H)]

# Palette sampled from the general look of Aariso0's GitHub avatar:
# vivid blue hair, warm skin, charcoal/navy jacket and a muted shirt.
PALETTE = {
    '.': None,
    'o': '#172235',  # deep outline / darkest shadow
    'n': '#26364d',  # jacket shadow
    'j': '#354b67',  # jacket base
    'l': '#52708e',  # jacket highlights
    'b': '#1768c8',  # blue hair shadow
    'B': '#2588f2',  # blue hair base
    'C': '#69b7ff',  # hair highlight
    's': '#b96f4c',  # skin shadow
    'S': '#e6a477',  # skin base
    'T': '#ffd0a5',  # skin highlight
    'g': '#657487',  # shirt shadow
    'G': '#a8b4c2',  # shirt base
    'w': '#e5edf5',  # shirt highlight
    'p': '#1b2638',  # trousers
    'P': '#34435a',  # trouser highlight
    'q': '#101827',  # shoe sole
    'Q': '#52627a',  # shoe highlight
    'x': '#9acfff',  # tiny accent pixels
}


def rect(x: int, y: int, width: int, height: int, color: str) -> None:
    for yy in range(y, y + height):
        for xx in range(x, x + width):
            if 0 <= xx < W and 0 <= yy < H:
                GRID[yy][xx] = color


def put(x: int, y: int, color: str) -> None:
    if 0 <= x < W and 0 <= y < H:
        GRID[y][x] = color


def hline(x: int, y: int, width: int, color: str) -> None:
    rect(x, y, width, 1, color)


# Ground shadow and small floating pixels.
rect(13, 52, 24, 1, 'o')
rect(17, 53, 16, 1, 'n')
put(7, 25, 'x'); put(9, 22, 'x'); put(38, 18, 'x'); put(40, 21, 'l')
put(36, 8, 'x'); put(11, 8, 'l')

# Legs and shoes.
rect(17, 37, 7, 12, 'p')
rect(26, 37, 7, 12, 'p')
rect(18, 39, 2, 8, 'P')
rect(27, 39, 2, 8, 'P')
rect(15, 48, 10, 3, 'o')
rect(25, 48, 10, 3, 'o')
rect(16, 47, 8, 3, 'Q')
rect(26, 47, 8, 3, 'Q')
rect(16, 50, 9, 1, 'q')
rect(26, 50, 9, 1, 'q')
rect(18, 47, 3, 1, 'w')
rect(28, 47, 3, 1, 'w')

# Torso / jacket silhouette.
rect(14, 25, 21, 14, 'o')
rect(15, 26, 19, 12, 'j')
rect(15, 27, 4, 10, 'n')
rect(30, 27, 4, 10, 'n')
rect(19, 27, 11, 11, 'g')
rect(20, 27, 9, 10, 'G')
rect(21, 28, 7, 8, 'w')
# Jacket lapels and seams.
rect(18, 27, 3, 8, 'l')
rect(28, 27, 3, 8, 'l')
rect(19, 27, 2, 2, 'j')
rect(28, 27, 2, 2, 'j')
rect(20, 34, 9, 1, 'g')
put(17, 31, 'l'); put(17, 34, 'l'); put(31, 31, 'l'); put(31, 34, 'l')
put(22, 30, 'g'); put(26, 30, 'g')
put(23, 33, 'G'); put(24, 33, 'G')

# Raised arm on the viewer's left, with a sleeve stepping up toward the hand.
# Shoulder, upper arm, forearm and cuff.
rect(12, 26, 5, 5, 'o')
rect(11, 24, 5, 5, 'j')
rect(9, 22, 5, 4, 'j')
rect(8, 19, 4, 5, 'n')
rect(9, 19, 2, 3, 'l')
rect(8, 18, 3, 2, 'o')
rect(7, 17, 3, 2, 'S')
rect(6, 15, 3, 3, 'S')
rect(7, 14, 2, 2, 'T')
# Individual fingers / waving silhouette.
put(6, 13, 'T'); put(7, 12, 'T'); put(8, 13, 'T')
put(5, 14, 'S'); put(5, 15, 'T'); put(6, 16, 'T')
put(9, 14, 'S'); put(10, 15, 'T')
put(9, 17, 'S'); put(8, 17, 's')
rect(10, 21, 2, 2, 'l')

# Relaxed right arm and hand.
rect(32, 27, 5, 7, 'o')
rect(33, 28, 3, 7, 'j')
rect(34, 34, 3, 4, 's')
rect(34, 34, 2, 3, 'S')
put(35, 34, 'T')

# Neck and face.
rect(21, 22, 8, 5, 's')
rect(22, 22, 6, 4, 'S')
rect(23, 23, 3, 2, 'T')
rect(18, 14, 14, 10, 'o')
rect(19, 14, 12, 9, 'S')
rect(20, 15, 10, 7, 'S')
rect(21, 15, 7, 6, 'T')
# Ears.
rect(17, 18, 3, 3, 's'); rect(18, 18, 2, 2, 'S')
rect(30, 18, 3, 3, 's'); rect(30, 18, 2, 2, 'S')
# Face features: brows, eyes, nose, understated smile.
rect(21, 17, 2, 1, 'o'); rect(27, 17, 2, 1, 'o')
put(22, 18, 'o'); put(27, 18, 'o')
put(25, 19, 's')
rect(24, 21, 3, 1, 's')
put(25, 20, 'T')

# Hair cap, spikes and fringe: bright blue silhouette close to the profile avatar.
rect(17, 11, 16, 6, 'o')
rect(18, 10, 14, 6, 'b')
rect(19, 9, 11, 6, 'B')
rect(20, 8, 9, 5, 'B')
rect(22, 7, 5, 2, 'C')
rect(17, 10, 4, 4, 'B')
rect(15, 12, 4, 3, 'b')
rect(16, 11, 3, 3, 'B')
rect(20, 6, 3, 3, 'B')
rect(25, 6, 3, 3, 'B')
rect(29, 8, 3, 4, 'b')
rect(31, 10, 3, 3, 'o')
# Hair fringe over forehead.
rect(19, 13, 4, 3, 'b')
rect(22, 14, 4, 2, 'B')
rect(26, 13, 4, 3, 'b')
rect(23, 13, 2, 2, 'C')
put(18, 12, 'C'); put(21, 9, 'C'); put(27, 10, 'C')
put(29, 13, 'B'); put(19, 14, 'B')

# Collar and a tiny shirt detail.
rect(20, 25, 9, 2, 'o')
rect(21, 25, 7, 1, 'G')
put(24, 26, 'w')


def render_svg() -> str:
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<svg xmlns="http://www.w3.org/2000/svg" width="384" height="448" viewBox="0 0 48 56" role="img" aria-labelledby="title desc" shape-rendering="crispEdges">',
        '  <title id="title">Aariso0 pixel-art mascot</title>',
        '  <desc id="desc">A blue-haired developer character waving, wearing a charcoal blue jacket and grey shirt.</desc>',
    ]
    for y, row in enumerate(GRID):
        for x, symbol in enumerate(row):
            color = PALETTE[symbol]
            if color:
                parts.append(f'  <rect x="{x}" y="{y}" width="1" height="1" fill="{color}"/>')
    parts.append('</svg>')
    return '\n'.join(parts) + '\n'


if __name__ == '__main__':
    output = Path(__file__).with_name('mascot.svg')
    output.write_text(render_svg(), encoding='utf-8')
    print(f'Wrote {output}')
