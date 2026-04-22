class Memory:
    pass


class BIOS(Memory):
    def run_diagnostics(self):
        print("BIOS: Running hardware diagnostics (POST)... OK.")
        return True

    def load_bootloader(self):
        print("BIOS: Loading bootloader and transferring control to OS...")


class RAM(Memory):
    def __init__(self, capacity_gb: int):
        self.capacity_gb = capacity_gb
        self.data_cache = []

    def load_data(self, data: str):
        print(
            f"RAM: Loading '{data}' into memory ({self.capacity_gb}GB total).")
        self.data_cache.append(data)

    def clear_memory(self):
        print("RAM: Clearing memory (volatile data wiped).")
        self.data_cache.clear()


class PersistentStorage(Memory):
    def __init__(self, storage_type: str, capacity_gb: int, read_speed_mb_s: int):
        self.storage_type = storage_type
        self.capacity_gb = capacity_gb
        self.read_speed_mb_s = read_speed_mb_s
        self.saved_files = []

    def read_os_files(self):
        print(
            f"{self.storage_type}: Reading OS files at ~{self.read_speed_mb_s} MB/s...")
        return "OS_Kernel"

    def save_user_data(self, data: str):
        print(f"{self.storage_type}: Saving user data '{data}' permanently.")
        self.saved_files.append(data)
