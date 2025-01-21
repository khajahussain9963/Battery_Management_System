class BatteryManagementSystem:
    def __init__(self, cell_count):
        self.cell_count = cell_count
        self.cell_voltages = [13] * cell_count  
        self.cell_temperatures = [25] * cell_count
        self.current = 0
        self.soc = 100
        self.soh = 100
        self.issues = []

    def update_parameters(self, voltages, temperatures, current, soc, soh):
        self.cell_voltages = voltages
        self.cell_temperatures = temperatures
        self.current = current
        self.soc = soc
        self.soh = soh
        self.issues.clear()
        self.check_for_issues()

    def check_for_issues(self):
        # Voltage checks
        for idx, voltage in enumerate(self.cell_voltages):
            if voltage < 3.0:
                self.issues.append(f"Cell {idx + 1}: Under-voltage ({voltage}V)")
            elif voltage > 4.2:
                self.issues.append(f"Cell {idx + 1}: Over-voltage ({voltage}V)")

        # Temperature checks
        for idx, temp in enumerate(self.cell_temperatures):
            if temp < 0:
                self.issues.append(f"Cell {idx + 1}: Too cold ({temp}°C)")
            elif temp > 60:
                self.issues.append(f"Cell {idx + 1}: Overheating ({temp}°C)")

        # Current check
        if abs(self.current) > 50:  # Example limit
            self.issues.append(f"Excessive current detected: {self.current}A")

        # SoC check
        if self.soc < 20:
            self.issues.append("Low state of charge (SOC < 20%)")

        # SoH check
        if self.soh < 80:
            self.issues.append("Degraded state of health (SOH < 80%)")

    def display_issues(self):
        if not self.issues:
            print("Battery is operating normally.")
        else:
            print("Battery Issues Detected:")
            for issue in self.issues:
                print(f"  - {issue}")


# Example usage
bms = BatteryManagementSystem(cell_count=4)
# Update with hypothetical values
bms.update_parameters(
    voltages=[3.8, 3.2, 2.9, 4.3],  
    temperatures=[25, -5, 65, 30],  
    current=60,  
    soc=15,  
    soh=75  
)
bms.display_issues()
