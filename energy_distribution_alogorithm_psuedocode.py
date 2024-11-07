class EnergySource:
    def __init__(self, type, capacity):
        self.type = type
        self. capacity = capacity
        self.status = "active" 

    def deactivate(self):
        self.status = "inacitve"

    def activate(self):
        self.status = "active"

    def add_energy_source(type, capacity):
        new_source = EnergySource (type, capacity)

    def remove_energy_source(type, capacity):
        global energy_sources
    
    def total_energy_source(type, capacity):
        total_energy = sum(source.capacity for source in energy_sources if source.status = "active")
        return total_energy
    
    def optimise_distibution(demand): 
        total_energy = calculate_total_energy()
        if total_energy >= demand:
            #Distibute energy to areas, storing excess if necessary
            print("Energy is sufficient. Distibuting energy.")
        else: 
            #Use stored energy or reduce consumption
            print ("Energy is insuficient. Optimising distribution")
            #Adjust energy distibution accordingly 
            