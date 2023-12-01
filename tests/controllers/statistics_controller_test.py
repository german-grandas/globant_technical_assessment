import unittest
from unittest.mock import patch, MagicMock
from server.controllers.statistics_controller import (
    StatisticsController,
)


class TestStatisticsController(unittest.TestCase):
    @staticmethod
    def get_mock_data():
        return [
            {"name": "berry1", "growth_time": 5},
            {"name": "berry2", "growth_time": 8},
            {"name": "berry3", "growth_time": 5},
        ]

    def test_get_statistics(self):
        data = self.get_mock_data()

        expected_response = {
            "berries_names": ["berry1", "berry2", "berry3"],
            "min_growth_time": 5,
            "median_growth_time": 5,
            "max_growth_time": 8,
            "variance_growth_time": 3,
            "mean_growth_time": 6,
            "frequency_growth_time": {8: 1, 5: 2},
        }

        actual_response = StatisticsController.get_statistics(data)
        self.assertEqual(actual_response, expected_response)

    @patch("matplotlib.pyplot.savefig")
    def test_create_histogram(self, mock_savefig):
        data = {"frequency_growth_time": {8: 1, 5: 2, 12: 3}}

        mock_image_stream = MagicMock()
        with patch(
            "server.controllers.statistics_controller.BytesIO",
            return_value=mock_image_stream,
        ):
            image_stream = StatisticsController.create_histogram(data)

        mock_savefig.assert_called_once_with(mock_image_stream, format="png")

        self.assertEqual(image_stream, mock_image_stream)
