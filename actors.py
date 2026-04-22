class User:
    def __init__(self, name: str):
        self.name = name

    def press_power_button(self, computer):
        print(f"{self.name}: Pressing the power button.")
        computer.turn_on()

    def input_command(self, computer, command: str):
        print(f"{self.name}: Typing command '{command}'.")
        computer.process_user_task(command)

    def move_mouse(self, computer, coords: tuple):
        print(f"{self.name}: Moving mouse to {coords}.")
