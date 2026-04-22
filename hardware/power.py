class PowerSupply:
    def __init__(self, capacity: int, input_voltage: int = 220):
        self.capacity = capacity
        self.input_voltage = input_voltage
        self.is_on = False

    def supply_power(self) -> bool:
        print(
            f"PowerSupply: Providing stable power from {self.input_voltage}V input. Capacity is {self.capacity}W.")
        self.is_on = True
        return True

    def cut_power(self):
        print("PowerSupply: Cutting power to all components.")
        self.is_on = False
