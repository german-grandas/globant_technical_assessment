class DataController:
    @staticmethod
    def process_berry_info(berries_info):
        data = []
        for berry in berries_info:
            berry_name = berry.get("name")
            growth_time = berry.get("growth_time")

            tmp = {"name": berry_name, "growth_time": growth_time}
            data.append(tmp)

        return data
