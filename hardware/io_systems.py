class InputSystem:
    def __init__(self, has_ukr_layout: bool, mouse_dpi: int):
        self.has_ukr_layout = has_ukr_layout
        self.mouse_dpi = mouse_dpi

    def register_action(self, action: str):
        print(f"InputSystem: Translating '{action}' to digital signal.")
        return action


class OutputSystem:
    def __init__(self, resolution_p: str, refresh_rate_hz: int):
        self.resolution_p = resolution_p
        self.refresh_rate_hz = refresh_rate_hz
        self.state = "STANDBY"

    def display_image(self, image_data: str):
        self.state = "ACTIVE"
        print(
            f"OutputSystem: Displaying '{image_data}' at {self.resolution_p} and {self.refresh_rate_hz}Hz.")

    def play_sound(self, sound_data: str):
        print(f"OutputSystem: Playing sound '{sound_data}'.")
