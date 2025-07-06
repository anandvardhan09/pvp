# Fighting Game

A simple 2D fighting game built with Python and Pygame featuring two-player combat with basic mechanics like movement, jumping, attacking, and health management.

## Features

- **Two-player local multiplayer**
- **Character movement and jumping**
- **Attack system with collision detection**
- **Health bars for both players**
- **Character facing direction based on opponent position**
- **Gravity physics**
- **Attack cooldown system**

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

Run the game with:
```bash
python src/main.py
```

### Controls

**Player 1 (Left side):**
- `A` - Move left
- `D` - Move right
- `UP` - Jump
- `Left Shift` - Attack

**Player 2 (Right side):**
- `Left Arrow` - Move left
- `Right Arrow` - Move right
- `UP` - Jump
- `Right Shift` - Attack

### Game Mechanics

- Each player starts with 100 health points
- Successful attacks deal 5 damage
- Players automatically face their opponent
- Attacks have a cooldown period to prevent spam
- Players can only jump when above a certain height threshold
- Gravity affects all players

## File Structure

```
├── .gitignore
├── requirements.txt
├── README.md
└── src/
    └── main.py
```

## Game Rules
- Players can move freely within the screen boundaries
- Health decreases when hit by opponent attack

## Development Notes

- The game runs at 60 FPS
- Screen resolution is 1200x600 pixels
- Characters are 120x150 pixels in size
- Attack range is 1.5 times the character width

## Future Enhancements

Potential improvements that could be added:
- Special moves and combos
- Sound effects and music
- Multiple character selection
- AI opponent
- Menu system
- Power-ups or special abilities

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes.
