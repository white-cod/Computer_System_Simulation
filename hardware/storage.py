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
        self.used_memory_gb = 0
        self.capacity_gb = capacity_gb
        self.read_speed_mb_s = read_speed_mb_s
        self.saved_files = []

    def read_os_files(self, os_size_mb: int = 1000):
        print(
            f"{self.storage_type}: Reading OS files at ~{self.read_speed_mb_s} MB/s...")
        time_to_read = os_size_mb / self.read_speed_mb_s
        if time_to_read > 2:
            print(f"{self.storage_type}: Booting might take a while ({time_to_read:.1f}s).")
        return "OS_Kernel"

    def save_user_data(self, data: str, data_size_gb: int):
        print(type(data))
        if self.used_memory_gb + data_size_gb > self.capacity_gb:
            print(
                f"{self.storage_type}: Not enough storage to save '{data}'. Required: {data_size_gb}GB, Available: {self.capacity_gb - self.used_memory_gb}GB.")
            return
        self.used_memory_gb += data_size_gb
        print(f"{self.storage_type}: Saving user data '{data}' permanently. Data size: {data_size_gb}GB")


        self.saved_files.append(data)
