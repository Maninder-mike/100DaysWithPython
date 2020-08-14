from timeit import repeat


def run_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" if algorithm != 'sorted' else ""

    stmt = f"{algorithm}, {array}"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    return f"Algorithm: {algorithm}, Minimum execution time: {min(times)}"
