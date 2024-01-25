#!/usr/bin/python3
""" Log parsing script. """

import sys


def print_stats(stats: dict, file_size: int) -> None:
    """
    Print file size and status code statistics.

    Parameters:
    - stats (dict): Dictionary containing status code counts.
    - file_size (int): Total file size.
    Returns:
    None
    """
    print("File size: {:d}".format(file_size))
    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))


if __name__ == '__main__':
    # Initialize variables
    file_size, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    try:
        # Iterate through lines in the input
        for line in sys.stdin:
            count += 1
            data = line.split()

            # Extract status code and update statistics
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except IndexError:
                pass

            # Extract file size and update total file size
            try:
                file_size += int(data[-1])
            except (IndexError, ValueError):
                pass

            # Print statistics every 10 lines
            if count % 10 == 0:
                print_stats(stats, file_size)

        # Print final statistics
        print_stats(stats, file_size)

    except KeyboardInterrupt:
        # Handle keyboard interrupt by printing current statistics
        print_stats(stats, file_size)
        raise
