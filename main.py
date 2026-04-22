from core import Computer
from actors import User
from hardware.power import PowerSupply
from hardware.motherboard import Motherboard
from hardware.processing import CPU, GPU
from hardware.storage import RAM, PersistentStorage
from hardware.cooling import CoolingSystem
from hardware.io_systems import InputSystem, OutputSystem


def main():
    print("=== Creating Computer Components ===")
    psu = PowerSupply(capacity=600, input_voltage=230)
    mobo = Motherboard(network_ifaces=["Wi-Fi 6", "Bluetooth 5.0", "Ethernet"])
    cpu = CPU(cores=8, frequency_ghz=3.2)
    gpu = GPU()
    ram = RAM(capacity_gb=32)
    ssd = PersistentStorage(
        storage_type="SSD", capacity_gb=1024, read_speed_mb_s=3500)
    cooling = CoolingSystem(target_temp=35, max_noise_db=40)
    input_sys = InputSystem(has_ukr_layout=True, mouse_dpi=3200)
    output_sys = OutputSystem(resolution_p="2560x1440", refresh_rate_hz=144)

    print("=== Assembling Computer ===")
    my_computer = Computer(
        power_supply=psu,
        motherboard=mobo,
        cpu=cpu,
        gpu=gpu,
        ram=ram,
        storage=ssd,
        cooling=cooling,
        input_sys=input_sys,
        output_sys=output_sys
    )

    print("=== Creating User ===")
    user = User("Alex")

    print("\n" + "="*30)
    print("=== BEGIN SIMULATION ===")
    print("="*30)

    print("\n[Attempt to use when OFF]")
    user.input_command(my_computer, "Open Browser")

    print("\n[Powering ON]")
    user.press_power_button(my_computer)

    print("\n[Rendering Video]")
    user.input_command(my_computer, "Render video 'Project.mp4'")

    print("\n[Saving Work]")
    my_computer.save_work("Project.mp4")

    print("\n[Shutting Down]")
    my_computer.turn_off()


if __name__ == "__main__":
    main()
