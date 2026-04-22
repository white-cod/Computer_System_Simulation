class InputSystem:
    def __init__(self, has_ukr_layout: bool, mouse_dpi: int):
        self.has_ukr_layout = has_ukr_layout
        self.mouse_dpi = mouse_dpi

    def register_action(self, action: str):
        if "ukr" in action.lower() and not self.has_ukr_layout:
            print("InputSystem: Error: Cannot input Ukrainian text, layout not supported.")
            return None
        print(f"InputSystem: Translating '{action}' to digital signal.")
        return action


class OutputSystem:
    def __init__(self, resolution_p: str, refresh_rate_hz: int):
        self.resolution_p = resolution_p
        self.refresh_rate_hz = refresh_rate_hz
        self.state = "STANDBY"

    def display_image(self, image_data: str, required_refresh_rate: int = 60):
        self.state = "ACTIVE"
        if required_refresh_rate > self.refresh_rate_hz:
            print(f"OutputSystem: Warning! Monitor refresh rate ({self.refresh_rate_hz}Hz) is lower than requested ({required_refresh_rate}Hz). Visual tearing may occur.")
        print(
            f"OutputSystem: Displaying '{image_data}' at {self.resolution_p} and {self.refresh_rate_hz}Hz.")

    def play_sound(self, sound_data: str):
        print(f"OutputSystem: Playing sound '{sound_data}'.")
