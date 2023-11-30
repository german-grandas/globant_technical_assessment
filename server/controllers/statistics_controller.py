import statistics
from io import BytesIO


import matplotlib.pyplot as plt


class StatisticsController:
    @staticmethod
    def get_statistics(data):
        berries_names = [berry["name"] for berry in data]
        growth_times = [berry["growth_time"] for berry in data]

        min_growth_time = min(growth_times)
        median_growth_time = statistics.median(growth_times)
        max_growth_time = max(growth_times)
        variance_growth_time = statistics.variance(growth_times)
        mean_growth_time = statistics.mean(growth_times)
        frequency_growth_time = {
            time: growth_times.count(time) for time in set(growth_times)
        }

        response = {
            "berries_names": berries_names,
            "min_growth_time": min_growth_time,
            "median_growth_time": median_growth_time,
            "max_growth_time": max_growth_time,
            "variance_growth_time": variance_growth_time,
            "mean_growth_time": mean_growth_time,
            "frequency_growth_time": frequency_growth_time,
        }

        return response

    def create_histogram(data):
        growth_times = data.get("frequency_growth_time")

        plt.bar(
            growth_times.keys(),
            growth_times.values(),
            color="blue",
            edgecolor="black",
        )

        plt.xlabel("Growth Time")
        plt.ylabel("Frequency")
        plt.title("Distribution of Berry Growth Times")

        image_stream = BytesIO()
        plt.savefig(image_stream, format="png")
        image_stream.seek(0)

        return image_stream
