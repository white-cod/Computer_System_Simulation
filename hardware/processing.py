class CPU:
    def __init__(self, cores: int, frequency_ghz: float):
        self.cores = cores
        self.frequency_ghz = frequency_ghz
        self.state = "IDLE"

    def execute_instructions(self, task: str, required_cores: int = 1):
        if required_cores > self.cores:
            print(f"CPU: Warning! Task '{task}' requires {required_cores} cores, but only {self.cores} available. Performance will be degraded.")
        self.state = "PROCESSING"
        print(
            f"CPU: Executing task '{task}' with {self.cores} cores at {self.frequency_ghz}GHz.")

    def request_data_from_ram(self):
        print("CPU: Requesting required data from RAM.")


class GPU:
    def render_graphics(self, details: str):
        print(
            f"GPU: Rendering graphics for '{details}' (loading textures and generating frames).")
