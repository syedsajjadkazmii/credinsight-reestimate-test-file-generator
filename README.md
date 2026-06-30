# Reestimate Test File Generator

Generates reestimate model input files by replicating the 32 canonical loans from the base files to any target count (e.g. 150 loans for QA testing).

## Prerequisites

- Python 3.9 or later

## Setup

```bash
cd reestimate-test-files-generation
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -e .
```

## Usage

Generate 150 loans (output goes to `output-files-150-loans/`):

```bash
reestimate-generate 150
```

Generate 69 loans with explicit paths:

```bash
reestimate-generate 69 --input-dir base-files --output-dir output-files-69-loans
```

Alternative via Python module:

```bash
python -m reestimate_file_generator 150
```

### Options

| Argument | Description |
|----------|-------------|
| `count` | Target number of loans (required, must be >= 1) |
| `--input-dir` | Directory with base Excel files (default: `base-files`) |
| `--output-dir` | Output directory (default: `output-files-{count}-loans`) |
| `-v`, `--verbose` | Print loan ID mapping and per-file row counts |

## Output

The script writes 7 Excel files into the output directory, mirroring the base file names. Each clone gets a new unique loan ID (e.g. `MA-16011`) with identical data to its source loan across all files.

Upload the generated files from the output directory to the reestimate model for QA testing.

## How it works

1. Reads the 32 canonical loan IDs from `Loan_Portfolio Characteristics (5).xlsx`.
2. Filters all files to those 32 loans (drops extra IDs present in some base files).
3. For counts above 32, clones loans round-robin from the base set with new sequential IDs starting at `MA-16011`.
4. Validates that every output loan appears consistently across all 7 files.
