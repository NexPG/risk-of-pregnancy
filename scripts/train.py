#!/usr/bin/env python3
"""CLI for training maternal risk model."""
import argparse


def main():
    parser = argparse.ArgumentParser(description="Train maternal risk model")
    parser.add_argument("--config", help="Path to config file", required=False)
    parser.add_argument("--data", help="Path to dataset", required=False)
    parser.add_argument("--output", help="Output directory", required=False)
    parser.add_argument("--random-state", type=int, help="Random state", required=False)
    args = parser.parse_args()
    # Training logic will be implemented in src.maternal_risk.train
    try:
        from maternal_risk import train

        train.run_training(
            config=args.config,
            data=args.data,
            output=args.output,
            random_state=args.random_state,
        )
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    main()
