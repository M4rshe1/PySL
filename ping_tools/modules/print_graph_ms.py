def print_graph_ms(res: dict):
    # print(res)
    print("  Response time graph:")

    # Initialize a list to store counts for each threshold range
    threshold_counts = [0] * 12  # Initialize with zeros for each 10ms range

    for t in res['times']:
        if t == 0:
            threshold_counts[0] += 1
        elif t < 10:
            threshold_counts[1] += 1  # Count values less than 10 ms
        elif t >= 100:
            threshold_counts[-1] += 1
        else:
            # Count values within the specified range
            for i in range(10, 100, 10):
                if i <= t < i + 10:
                    threshold_counts[i + 1 // 10] += 1

    # Print counts for values less than 10 ms
    # print(res)
    print(f"         lost | {threshold_counts[0]} {'#' * threshold_counts[0]}")
    print(f"   {'<10ms':>10} | {threshold_counts[1]} {'#' * threshold_counts[1]}")

    # Print counts for other threshold ranges
    for i in range(2, 11):
        print(f"    {i * 10 - 10:>3}-{i * 10:<3}ms | {threshold_counts[i + 1]} {'#' * threshold_counts[i + 1]}")
    print(f"       >100ms | {threshold_counts[-1]} {'#' * threshold_counts[-1]}\n")


if __name__ == "__main__":
    print("This is a module for ping_tools")