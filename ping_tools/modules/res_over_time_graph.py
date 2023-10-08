import matplotlib.pyplot as plt
import os
import datetime
import json


def print_graph_time(res: dict, filename=None, graph_file=True, graph_data=False):
    if filename is None:
        filename = "responses_over_time-" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    if not os.path.exists("graphs"):
        os.mkdir("graphs")

    # print("Responses over time graph:")

    # Extract data from the dictionary
    times = res['times']
    timestamps = res['timestamps']

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the response count over time
    ax.plot(timestamps, times, marker='o', linestyle='-')

    # Set labels and title
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Response Count')
    ax.set_title('Responses Over Time')

    # export the graph to a file
    if graph_file:
        fig.savefig("graphs/" + filename, dpi=300, bbox_inches='tight')
    if graph_data:
        with open("graphs/" + filename + ".json", "w") as f:
            json.dump(res, f)
    fig.show()


if __name__ == "__main__":
    print("This is a module for ping_tools")
