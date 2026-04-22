class CoolingSystem:
    def __init__(self, target_temp: int, max_noise_db: int):
        self.target_temp = target_temp
        self.max_noise_db = max_noise_db
        self.state = "OFF"

    def passive_cooling(self):
        self.state = "PASSIVE"
        print(
            f"CoolingSystem: Fans at minimum speed. Maintaining temp <= {self.target_temp}°C quietly (<{self.max_noise_db}dB).")

    def active_cooling(self):
        self.state = "ACTIVE"
        print(
            f"CoolingSystem: Fans at maximum speed! High load detected. Noise level may reach {self.max_noise_db}dB.")

    def stop_cooling(self):
        self.state = "OFF"
        print("CoolingSystem: Cooling stopped.")
