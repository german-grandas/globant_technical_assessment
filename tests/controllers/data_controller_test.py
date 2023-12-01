import unittest

from server.controllers.data_controller import (
    DataController,
)


class TestDataController(unittest.TestCase):
    @staticmethod
    def get_mock_data():
        return [
            {"name": "berry1", "growth_time": 10},
            {"name": "berry2", "growth_time": 10},
            {"name": "berry3", "growth_time": 10},
        ]

    def test_process_berry_info(self):
        berries_info = self.get_mock_data()

        expected_data = [
            {"name": "berry1", "growth_time": 10},
            {"name": "berry2", "growth_time": 10},
            {"name": "berry3", "growth_time": 10},
        ]

        actual_data = DataController.process_berry_info(berries_info)

        self.assertEqual(actual_data, expected_data)
