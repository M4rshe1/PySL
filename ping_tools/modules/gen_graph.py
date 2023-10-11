import matplotlib.pyplot as plt


def gen_graph(data, filename):
    # Create a figure for the first scan
    plt.figure(figsize=(10, 6))
    for entry in data:
        plt.plot(entry["timestamps"], entry["times"], marker='o', linestyle='-', label=f"Request {entry['req']}")
    plt.xlabel('Timestamp (seconds)')
    plt.ylabel('Ping Time (ms)')
    plt.title('Ping Times Over Time (First Scan)')
    plt.legend()

    # export as image
    plt.savefig("graphs/" + filename, dpi=300, bbox_inches='tight')

    # Show the plot
    plt.show()
