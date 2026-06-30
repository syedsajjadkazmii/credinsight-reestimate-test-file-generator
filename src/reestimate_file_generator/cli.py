import argparse
import sys
from pathlib import Path

from reestimate_file_generator.config import PORTFOLIO_FILENAME
from reestimate_file_generator.replicator import generate_files, validate_result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate reestimate model input files by replicating base loans.",
    )
    parser.add_argument(
        "count",
        type=int,
        help="Target number of loans to generate (>= 1)",
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("base-files"),
        help="Directory containing base Excel files (default: base-files)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory (default: output-files-{count}-loans)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print loan ID mapping and per-file statistics",
    )
    args = parser.parse_args(argv)

    if args.count < 1:
        print("Error: count must be at least 1", file=sys.stderr)
        return 1

    input_dir = args.input_dir
    if not input_dir.is_dir():
        print(f"Error: input directory not found: {input_dir}", file=sys.stderr)
        return 1

    portfolio_path = input_dir / PORTFOLIO_FILENAME
    if not portfolio_path.exists():
        print(f"Error: portfolio file not found: {portfolio_path}", file=sys.stderr)
        return 1

    output_dir = args.output_dir or Path(f"output-files-{args.count}-loans")

    try:
        result = generate_files(input_dir, output_dir, args.count)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    errors = validate_result(result)
    if errors:
        print("Validation failed:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"Generated {args.count} loans in {result.output_dir.resolve()}")

    print("\nFile summary:")
    print(f"  {'File':<60} {'Rows':>6} {'Loans':>6}")
    print(f"  {'-'*60} {'-'*6} {'-'*6}")
    for filename, stats in result.file_stats.items():
        print(f"  {filename:<60} {stats['rows']:>6} {stats['unique_loans']:>6}")

    if args.verbose:
        clones = [a for a in result.assignments if a.output_id != a.source_id]
        print(f"\nLoan assignments: {len(result.assignments)} total, {len(clones)} clones")
        if clones:
            print("\nClone mapping (new_id -> source_id):")
            for a in clones:
                print(f"  {a.output_id} <- {a.source_id}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
