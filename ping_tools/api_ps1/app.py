import os
from flask import Flask, request, send_from_directory, render_template
import json
import matplotlib.pyplot as plt
# from io import BytesIO
import datetime


app = Flask(__name__, template_folder="templates")

# Set the folder where graphs will be stored
GRAPH_FOLDER = "graphs"
ALLOWED_EXTENSIONS = {'json'}
app.config['GRAPH_FOLDER'] = GRAPH_FOLDER
# Check if the graph folder exists, and create it if not
if not os.path.exists(GRAPH_FOLDER):
    os.makedirs(GRAPH_FOLDER)


def gen_graph(data, file_path):
    # Create a figure for the graph
    plt.figure(figsize=(10, 6))

    for i, entry in enumerate(data, 1):
        plt.plot(entry["timestamps"], entry["times"], marker='o', linestyle='-', label=f"Request {str(i)}")
    plt.xlabel('Timestamp (seconds)')
    plt.ylabel('Ping Time (ms)')
    plt.title('Ping Results')
    plt.legend()

    # Save the graph to the specified file path
    plt.savefig(file_path, format="png")


@app.route("/ping-graph", methods=["GET", "POST"])
def ping_graph():
    return render_template("ping_graph.html")


@app.route("/api/ping-graph", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        try:
            # Check if the 'file' field is in the request
            # return str(request.files['file'])
            if 'file' not in request.files:
                return "No file part", 400

            # get the file from the request
            file = request.files['file']

            # Check if the file is empty
            if file.filename == '':
                return "No selected file", 400

            if file:
                # Generate a unique file name based on the current date and time
                filename = f"ping_data_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
                # Generate a graph and save it to the GRAPH_FOLDER
                # return file.read()
                gen_graph(json.loads(file.read()), os.path.join(GRAPH_FOLDER, filename))

                # Provide a download link for the generated graph
                graph_link = f"/graphs/{filename}"

                # create download button
                return (f"<a href='{graph_link}' title='Click to download graph'>"
                        f"<img src='{graph_link}' style='width: 100vw; height: 100vh;'></a>"
                        f"<style>body{{margin: 0; padding: 0;overflow: hidden;}}</style>")

        except Exception as e:
            return "Error: " + str(e)
    else:
        return "GET request received at /api/ping-graph"


@app.route("/graphs/<path:path>", methods=["GET"])
def send_graph(path):
    return send_from_directory(GRAPH_FOLDER, path)


if __name__ == "__main__":
    app.run(debug=True, port=6969)
