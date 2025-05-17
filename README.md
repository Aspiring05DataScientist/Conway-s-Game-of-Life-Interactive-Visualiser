# 🧬 Conway’s Game of Life – Interactive Visualiser

This is a Python implementation of Conway's Game of Life with an interactive visual interface using **Pygame**. It simulates the behavior of living cells based on simple rules of life and death.

## 🎯 Project Features

- 2D grid of cells, each either alive or dead
- Visualised using **Pygame**
- **Command-line arguments** for grid size and speed
- **Interactive controls**:
  - `Space`: Play / Pause the simulation
  - `N`: Step forward one generation
  - `R`: Randomly fill the board with live cells
  - `C`: Clear the board
  - `S`: Save current pattern to `patterns.txt`
  - `L`: Load pattern from `patterns.txt`
- Live cell counter and FPS display

---

## ⚙️ How to Run

### 1. Install dependencies

Make sure Python and Pygame are installed:

```bash
pip install pygame
