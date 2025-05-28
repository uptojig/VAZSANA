# Claw Machine Backend

This repository contains a simple command line tool for recording
operations of a token-based claw machine arcade. The tool keeps track of
cash exchanges, stock entries for each machine and play results. Data is
stored in `data.json` in the repository root.

## Installation
The project does not require external dependencies and works with
Python 3.8+.

## Usage
Run the command line interface using:

```bash
python -m clawmachine.cli <command> [options]
```

Main commands:

- `add-machine NAME` – register a new machine.
- `cash-in AMOUNT` – record a cash exchange and calculate tokens.
- `stock MACHINE_ID QUANTITY COST` – add stock to a machine with
  specified unit cost.
- `play MACHINE_ID TOKENS REWARDS` – log a play result (tokens used and
  rewards taken).
- `report-cash YYYY-MM-DD` – show total cash exchanged for a day.

Example workflow:

```bash
python -m clawmachine.cli add-machine "Teddy Bear"
python -m clawmachine.cli cash-in 1000
python -m clawmachine.cli stock 1 20 50
python -m clawmachine.cli play 1 15 3
python -m clawmachine.cli report-cash $(date +%F)
```

Promotions for cash exchange are predefined in `data.json` on first run:

- 1,000 baht ⇒ 55 tokens
- 2,000 baht ⇒ 115 tokens
- 4,000 baht ⇒ 240 tokens
