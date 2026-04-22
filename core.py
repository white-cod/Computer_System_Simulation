from hardware.power import PowerSupply
from hardware.cooling import CoolingSystem
from hardware.storage import BIOS, RAM, PersistentStorage
from hardware.processing import CPU, GPU
from hardware.io_systems import InputSystem, OutputSystem
from hardware.motherboard import Motherboard
from software import OperatingSystem


class Computer:
    def __init__(self, power_supply: PowerSupply, motherboard: Motherboard,
                 cpu: CPU, gpu: GPU, ram: RAM, storage: PersistentStorage,
                 cooling: CoolingSystem, input_sys: InputSystem, output_sys: OutputSystem,
                 os: OperatingSystem):
        self.power_supply = power_supply
        self.motherboard = motherboard
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.storage = storage
        self.cooling = cooling
        self.input_sys = input_sys
        self.output_sys = output_sys
        self.os = os
        self.bios = BIOS()
        self.state = "OFF"

    def turn_on(self):
        if self.state != "OFF":
            print("Computer is already turning on or turned on.")
            return

        self.state = "Booting"
        print(f"--- System Booting ---")
        self.power_supply.supply_power()
        self.motherboard.synchronize_buses()
        self.bios.run_diagnostics()
        os_data = self.storage.read_os_files(os_size_mb=2500)
        self.ram.load_data(os_data)
        self.bios.load_bootloader()

        if self.os.boot(self.ram, self.storage):
            self.state = "Ready to work"
        else:
            self.state = "Boot Failed"
            
        print(f"--- System State: {self.state} ---\n")

    def process_user_task(self, command: str, required_cores: int = 4, required_iface: str = None):
        if self.state not in ("Ready to work", "Ready"):
            print("Computer must be Ready to process a task!")
            return

        self.state = "Working"
        print(f"--- Processing Task: {command} ---")
        signal = self.input_sys.register_action(command)
        if signal is None:
            return
            
        self.motherboard.route_data("InputSystem", "CPU", signal, required_iface)

        self.cooling.active_cooling(current_temp=65)

        self.cpu.request_data_from_ram()
        self.os.execute_program(command, required_cores, self.cpu)

        self.gpu.render_graphics(command)
        self.output_sys.display_image(command, required_refresh_rate=144)

        self.cooling.passive_cooling()
        self.state = "Ready to work"
        print(f"--- Task Finished. State: {self.state} ---\n")

    def save_work(self, data_name: str, data_size_gb: int):
        if self.state not in ("Ready to work", "Ready"):
            print("Cannot save right now!")
            return

        print(f"--- Saving Work: {data_name} ---")
        print("Reading final data from RAM cache...")
        self.storage.save_user_data(data_name, data_size_gb)
        print("--- Save Complete ---\n")

    def turn_off(self):
        if self.state == "OFF":
            print("Computer is already off.")
            return

        print("--- Shutting Down ---")
        self.ram.clear_memory()
        print("Sending shutdown signal to Motherboard and Power Supply...")
        self.cooling.stop_cooling()
        self.power_supply.cut_power()
        self.state = "OFF"
        print(f"--- System State: {self.state} ---\n")
