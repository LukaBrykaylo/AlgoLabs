import unittest

from src.gas_management import gas_management


class GasManagementTest(unittest.TestCase):
    def test_with_two_gas_stations(self):
        cities = ["Львів", "Стрий", "Долина", "Богородчани", "Луцьк"]
        gas = ["Львів", "Стрий"]
        active_gas = [["Львів", "Долина"], ["Львів", "Богородчани"], [
            "Стрий", "Богородчани"], ["Стрий", "Луцьк"], ["Богородчани", "Луцьк"]]

        result = gas_management(cities, gas, active_gas)
        self.assertEqual(result, [['Львів', ['Стрий']], ['Стрий', ['Долина', 'Львів']]])

    def test_with_all_routes(self):
        cities = ["Львів", "Стрий", "Долина", "Богородчани", "Луцьк"]
        gas = ["Львів", "Стрий", "Луцьк"]
        active_gas = [["Львів", "Долина"], ["Львів", "Богородчани"],
             ["Стрий", "Богородчани"], ["Стрий", "Луцьк"], ["Богородчани", "Луцьк"], ["Луцьк", "Львів"], ["Луцьк", "Стрий"]]

        result = gas_management(cities, gas, active_gas)
        self.assertEqual(result, [])


if __name__ == "main":
    unittest.main()
