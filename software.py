class OperatingSystem:
    def __init__(self, name: str, required_ram_gb: int, required_storage_gb: int):
        self.name = name
        self.required_ram_gb = required_ram_gb
        self.required_storage_gb = required_storage_gb
        self.is_running = False

    def boot(self, ram, storage):
        if ram.capacity_gb < self.required_ram_gb:
            print(f"OS {self.name}: Boot failed. Not enough RAM! Requires {self.required_ram_gb}GB, has {ram.capacity_gb}GB.")
            return False
        
        if storage.capacity_gb - storage.used_memory_gb < self.required_storage_gb:
            print(f"OS {self.name}: Boot failed. Not enough storage for OS swap/cache! Requires {self.required_storage_gb}GB.")
            return False
            
        self.is_running = True
        print(f"OS {self.name}: Successfully booted and took control.")
        return True

    def execute_program(self, program_name: str, required_cores: int, cpu):
        if not self.is_running:
            print(f"OS {self.name}: Cannot execute '{program_name}', OS is not running.")
            return
        
        print(f"OS {self.name}: Dispatching '{program_name}' to CPU...")
        cpu.execute_instructions(program_name, required_cores)
