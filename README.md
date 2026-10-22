# CTF Challenges

Small, self-contained capture-the-flag rooms you play in your own terminal.
No servers, no sign-ups: download a room, unpack it, and start looking around.
Each flag looks like `flag{...}`.

| Room | Challenge Rating | Est. time | Download |
|---|---|---|---|
| [Escape Room](escape-room/) | 🟢 CR 1 · Tavern Quest | 15–45 min | [`escape-room.tar.gz`](escape-room/escape-room.tar.gz) |

More rooms are on the way. The dungeon is still being dug.

## Challenge Ratings

Every room gets a rating, so you know whether to grab a torch or summon your
whole party.

| | Rating | What you're walking into |
|---|---|---|
| 🟢 | **CR 1 · Tavern Quest** | A gentle first adventure. If you can `ls`, `cd` and `cat`, you're ready to roll. Clues point the way, and nothing bites (hard). |
| 🟡 | **CR 5 · Dungeon Delve** | Traps start chaining together. You'll need a few tricks from your spellbook and the patience to read the fine print. |
| 🔴 | **CR 10 · Boss Fight** | Several techniques stacked, very few hints, and at least one red herring that looks *very* convincing. Bring potions. |
| 🟣 | **CR 20 · Legendary** | For seasoned adventurers only. Expect misdirection, layered encodings and a puzzle or two that will cost you sleep. |

Ratings are the dungeon master's best guess. If a room felt way harder or
easier than its rating, open an issue and say so (spoiler-free, please).

## How to play

You need a **Linux or macOS** terminal. On Windows, use
[WSL](https://learn.microsoft.com/windows/wsl/install); some tricks rely on
Linux file behavior that Windows Explorer hides.

```sh
# 1. Look before you unpack: list what's inside first. Always a good habit.
tar -tvzf escape-room.tar.gz

# 2. Unpack it and step inside
tar -xzf escape-room.tar.gz
cd escape-room

# 3. Read the briefing, then you're on your own
cat README.txt
```

**Nothing in these rooms ever needs to be run.** Everything is plain text and
ordinary archives: inspect, don't execute. If a step seems to want you to run
an unknown file, you've found a trap, not a solution.

## Checking your answer

Each room's page lists the SHA-256 hash of its flag. Hash your answer and
compare:

```sh
echo -n 'flag{your_answer_here}' | sha256sum      # Linux / WSL
echo -n 'flag{your_answer_here}' | shasum -a 256  # macOS
```

Matching hash: natural 20, you've escaped. No match: the dice were not kind,
keep looking. The hash can't be turned back into the flag, so it gives nothing
away.

## House rules

- **No spoilers** in issues, pull requests or discussions. Let other people
  have the "aha" moment.
- Stuck? Re-read the room's briefing. Every clue you need is inside the room.
- Found something broken (an unsolvable step, a typo in a clue)? Open an
  issue describing *where*, without posting the solution.

## License

The rooms and this repository are licensed under
[CC BY 4.0](LICENSE): share them, remix them, use them in a class or a club,
just give credit to **rk-secops**.
