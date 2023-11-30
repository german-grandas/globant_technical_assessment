import os

from flask import Flask, jsonify, render_template, send_file

from .controllers.statistics_controller import StatisticsController
from .controllers.data_controller import DataController
from .helpers import get_all_berries_info

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/allBerryStats")
def get_all_berry_stats():
    all_berries_info = get_all_berries_info()
    processed_data = DataController.process_berry_info(all_berries_info)
    response_data = StatisticsController.get_statistics(processed_data)

    return jsonify(response_data)


@app.route("/getBerriesHistogram")
def get_berries_histogram():
    all_berries_info = get_all_berries_info()

    processed_data = DataController.process_berry_info(all_berries_info)

    statistics_data = StatisticsController.get_statistics(processed_data)
    histogram_stream = StatisticsController.create_histogram(statistics_data)

    return send_file(
        histogram_stream,
        mimetype="image/png",
        as_attachment=True,
        download_name="histogram.png",
    )
