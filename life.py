import argparse
import pygame
import random
from collections import defaultdict

# ----- Config Parsing -----
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', type=int, default=60)
    parser.add_argument('--height', type=int, default=30)
    parser.add_argument('--fps', type=int, default=10)
    return parser.parse_args()

# ----- Game Logic -----
def next_gen(live_cells, width, height):
    neighbor_counts = defaultdict(int)
    for x, y in live_cells:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    neighbor_counts[(nx, ny)] += 1
    new_live = set()
    for cell, count in neighbor_counts.items():
        if count == 3 or (count == 2 and cell in live_cells):
            new_live.add(cell)
    return new_live

# ----- Save & Load -----
def save_pattern(live_cells, filename='patterns.txt'):
    with open(filename, 'w') as f:
        for x, y in live_cells:
            f.write(f"{x},{y}\n")

def load_pattern(filename='patterns.txt'):
    cells = set()
    try:
        with open(filename, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    x, y = map(int, line.strip().split(','))
                    cells.add((x, y))
    except FileNotFoundError:
        pass
    return cells

# ----- Main Pygame Loop -----
def main():
    args = parse_args()
    CELL_SIZE = 20
    WIDTH, HEIGHT = args.width, args.height
    SCREEN_W, SCREEN_H = WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 18)

    live_cells = set()
    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                elif event.key == pygame.K_n:
                    live_cells = next_gen(live_cells, WIDTH, HEIGHT)
                elif event.key == pygame.K_c:
                    live_cells.clear()
                elif event.key == pygame.K_r:
                    live_cells = {(random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)) for _ in range((WIDTH*HEIGHT)//5)}
                elif event.key == pygame.K_s:
                    save_pattern(live_cells)
                elif event.key == pygame.K_l:
                    live_cells = load_pattern()

        if running:
            live_cells = next_gen(live_cells, WIDTH, HEIGHT)

        # Draw cells
        screen.fill((0, 0, 0))
        for x, y in live_cells:
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (0, 255, 0), rect)

        # Draw grid
        for x in range(0, SCREEN_W, CELL_SIZE):
            pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, SCREEN_H))
        for y in range(0, SCREEN_H, CELL_SIZE):
            pygame.draw.line(screen, (40, 40, 40), (0, y), (SCREEN_W, y))

        # Draw FPS & cell count
        gen_text = f"Live cells: {len(live_cells)}   |   {'Running' if running else 'Paused'}"
        text_surface = font.render(gen_text, True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

        pygame.display.flip()
        clock.tick(args.fps)

if __name__ == '__main__':
    main()
