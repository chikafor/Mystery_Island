# Mystery Island: The Lost Lighthouse

A beginner-friendly Python text-adventure project for the Learn2Earn EASY track.

**Project status: Implementation complete; final documentation and submission review pending.**

## Mission

After a storm, the player is stranded on Mystery Island. The lighthouse beacon is dark, and the player must explore the island, collect useful items, overcome challenges, and restore the beacon before running out of energy.

## Game Features

- Displays the game title and instructions.
- Asks for the player's name.
- Provides a repeating menu with options to move, view inventory, or quit.
- Includes five locations: Beach, Jungle, Cave, Old Bridge, and Lighthouse.
- Tracks the player's name, location, energy, inventory, and game status.
- Allows collection of Rope and Lantern.
- Includes meaningful decisions with different consequences.
- Requires Rope and Lantern to complete the mission.
- Rejects invalid input without reducing energy.
- Supports winning, losing, quitting, and replaying.
- Resets the player's state when a new game begins.

## Project Structure

```text
Mystery_Island/
├── main.py
├── game.py
├── tests/
│   └── test_game.py
├── README.md
└── .gitignore
```

### File Responsibilities

- `main.py`: Handles player interaction, menus, and the game loop.
- `game.py`: Contains game rules, movement, decisions, energy management, and inventory operations.
- `tests/test_game.py`: Contains automated tests using Python's unittest framework.
- `README.md`: Provides project instructions and learning evidence.
- `.gitignore`: Excludes unnecessary generated files from Git.

## Prerequisites

- Python 3.10 or later.
- Git for version control.
- No third-party Python packages are required.

## How to Run the Game

Clone the repository and navigate into the project directory.

Run:

```bash
python3 main.py
```

You can also use `python main.py` if your system maps `python` to Python 3.

## How to Run the Tests

Run:

```bash
python3 -m unittest discover -s tests -v
```

**Current test result:** 29 tests passed.

## Game Rules and Design Decisions

- The player starts at the Beach with 5 energy points.
- The island follows a one-way route:

  Beach → Jungle → Cave → Old Bridge → Lighthouse.

- The Rope is collected automatically when the player begins at the Beach.
- The Lantern can be collected by searching the Cave.
- Successful movement costs 1 energy point.
- Taking the Jungle shortcut costs 1 additional energy point.
- Rushing across the Old Bridge costs 1 additional energy point.
- Invalid or rejected actions do not consume energy.
- Energy must not become negative.
- Reaching zero energy before completing the mission results in defeat.
- The player needs both Rope and Lantern to win.
- A new game resets the player's location, energy, inventory, and outcome state.
- The Cave search does not consume additional energy.

## Testing and Verification

The project currently has 29 passing automated tests.

The following gameplay scenarios have also been demonstrated:

- Successful winning path.
- Losing path caused by energy exhaustion.
- Invalid movement input.
- Safe Jungle decision.
- Lantern collection.
- Careful bridge decision.
- Replay with fresh player state.

## Known Limitations

- The island currently uses a fixed, one-way route.
- Players cannot travel backwards between locations.
- The game runs in the terminal and does not have a graphical interface.
- The game does not currently provide persistent saved-game functionality.

## Learning Evidence

The project includes two learning-log entries and a final personal reflection.

- `docs/learning-log-1.md`
- `docs/learning-log-2.md`
- `docs/reflection.md`

Final reflection:

> The Python concept I understand now that I did not understand before is ...

## Final Submission Checklist

- [x] Game title and instructions.
- [x] Player name input.
- [x] Five required locations.
- [x] Player state and energy tracking.
- [x] Item collection and inventory.
- [x] Meaningful decisions.
- [x] Movement and energy rules.
- [x] Winning and losing conditions.
- [x] Invalid-input handling.
- [x] Replay functionality.
- [x] At least eight automated tests.
- [x] Winning and losing gameplay demonstrations.
- [x] Two learning-log entries.
- [x] Final personal reflection.
- [x] Final GitHub submission evidence.

## Final Submission Evidence

- Repository: https://github.com/chikafor/Mystery_Island
- Final commit: 8caf1634bb800b34ab64edf0f2fc0bfd15c19415
- Branch: main
- Python version: 3.12.3
- Automated tests: 29 passed