#!/usr/bin/env python3
"""CLI for predicting maternal risk."""
import argparse


def main():
    parser = argparse.ArgumentParser(description="Predict maternal risk")
    parser.add_argument("--model", help="Path to model", required=False)
    parser.add_argument("--input", help="Path to input data", required=False)
    parser.add_argument("--output", help="Output path", required=False)
    parser.add_argument("--config", help="Path to config", required=False)
    args = parser.parse_args()
    try:
        from maternal_risk import predict

        predict.run_prediction(
            model=args.model,
            input_data=args.input,
            output=args.output,
            config=args.config,
        )
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    main()
