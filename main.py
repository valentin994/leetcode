from argparse import ArgumentParser
import sys
import time
import subprocess


def run_and_time_file(target_file: str, number_of_executions: int, verbose: bool):
    command = [sys.executable, target_file]
    kwargs = {} if verbose else {"stdout": subprocess.DEVNULL}
    for i in range(number_of_executions):
        try:
            start = time.perf_counter()
            subprocess.run(command, check=True, **kwargs)
        except Exception as err:
            print(f"Could not run the file exception: {err}")
        finally:
            total_time = time.perf_counter() - start
            print("-" * 40)
            print(f"Run: {i + 1} execution time: {total_time:.4f} seconds")
            print("-" * 40)


def main():
    parser = ArgumentParser(
        prog="Time execution",
        description="Used to time execution of files",
    )
    parser.add_argument("filename")
    parser.add_argument("-c", "--count", nargs="?", const=1, type=int)
    parser.add_argument("-v", "--verbose", nargs="?", const=False, type=bool)
    args = parser.parse_args()
    run_and_time_file(args.filename, args.count, args.verbose)


if __name__ == "__main__":
    main()
