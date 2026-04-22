class Motherboard:
    def __init__(self, network_ifaces: list):
        self.network_ifaces = network_ifaces

    def synchronize_buses(self):
        print(
            f"Motherboard: Synchronizing buses. Network interfaces matched: {', '.join(self.network_ifaces)}.")

    def route_data(self, source: str, destination: str, data: str):
        print(
            f"Motherboard: Routing '{data}' from {source} to {destination} via internal buses.")
