# Mystery Island: The Lost Lighthouse

A beginner-friendly Python text-adventure project for the Learn2Earn EASY track.

> **Project status: In progress.** The game implementation and automated tests are not yet present. This repository starts with the project brief and development plan; the learner should implement and understand the game logic.

## Mission
After a storm, the player is stranded on Mystery Island. The lighthouse beacon is dark, and the player must explore the island, collect useful items, solve the bridge and lighthouse challenges, and restore the beacon before running out of energy.

## Requirements checklist
- [ ] Display the game title and instructions.
- [ ] Ask for the player's name.
- [ ] Provide a repeating menu that ends on victory, defeat, or quit.
- [ ] Include Beach, Jungle, Cave, Old Bridge, and Lighthouse.
- [ ] Track player name, current location, energy (starting at 5), and inventory.
- [ ] Allow the player to collect rope and lantern only once each.
- [ ] Include at least three meaningful decisions with consequences.
- [ ] Require rope to cross the bridge and lantern to restore the lighthouse beacon.
- [ ] Reject unexpected input without crashing or changing game state.
- [ ] Show a clear ending and offer a replay with a fresh player state.
- [ ] Include at least eight meaningful automated tests.

## Planned project structure

```text
Mystery_Island/
├── main.py              # Terminal interaction and game loop
├── game.py              # Testable game rules and state changes
├── tests/
│   └── test_game.py     # Automated tests using unittest
├── README.md            # Project instructions and learning evidence
└── .gitignore
```

## Prerequisites
- Python 3.10 or later
- Git (for version control)
- No third-party Python packages are required; use the Python standard library.

## Run the game
Once main.py has been implemented, run:

```bash
python main.py
```

## Run the tests
Once the test suite has been implemented, run:

```bash
python -m unittest discover -s tests -v
```

## Agreed game-design rules to decide and document
- Map route: Beach → Jungle → Cave → Old Bridge → Lighthouse. Add return routes where appropriate.
- The player begins with 5 energy points.
- Only successful, legal actions that the game design defines as energy-consuming should reduce energy.
- Invalid or rejected actions must not consume energy or mutate the player's state.
- Energy must never become negative. Using the final energy point on a legal action should trigger defeat unless that action completes the objective.
- A new replay must reset location, energy, inventory, and outcome flags.
- The same player state and action should always produce the same result.

## Suggested development sequence
1. Build and explain the Beach menu and quit option.
2. Add the location map and legal movement.
3. Add inventory and unique item collection.
4. Add bridge and lighthouse requirements.
5. Add energy, victory, defeat, quit, and replay rules.
6. Write and run at least eight meaningful unit tests, including edge cases.
7. Demonstrate a winning path, a losing path, invalid-input recovery, and replay reset.

## Learning evidence
Keep two learning-log entries in your own words. For each entry, record: **topic → what the tutor explained → your experiment → your conclusion**. Also complete this reflection before submission:

> The Python concept I understand now that I did not understand before is ...

## Known limitations
The game code and tests have not yet been added. The run and test commands above become usable after those files are implemented. Do not treat this repository as a finished submission until the checklist, demonstrations, and tests have been completed and reviewed.