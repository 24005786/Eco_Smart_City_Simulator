#Procedural functions for the energy distrubution system
energy_sources = ()

def add_energy_source(name, type, capacity):
    """Adds a new energy source with a specific capacity (in kWh)."""
    energy_sources(name) = ("type": type, "capacity": capacity, "active": True)

def remove_energy_source(name):
    """Removes an energy source."""
    if name in energy_sources:
        energy_sources(name)("active") = False

def calculate_distrubution(demand):
    """Calculates distribution based upon the total energy supply and demand."""
    total_energy = sum(
        source["capacity"] for source in energy_sources.value() if source ["active"])
    if demand <= total_energy:
        print(f"Energy demanded of {demand} kWh met with {total_energy} kWh available. ")
    else:
        print(f"Energy demand of {demand} kWh exceeds supply of {total_energy} kWh.")


class EnergySource:
    def __init__(self, name, source_type, capacity):
        self.name = name
        self.source_type = source_type 
        self.capacity = capacity
        self.active = True
    
    def deactivate(self):
        """"Deactivate this energy source."""
        self.active = False

class DistributionGrid:
    def __init__ (self):
        self.sources = ()

        def add_source (self, name, source_type, capacity):
            """Add a new energy source to the grid."""
            self.sources(name) = EnergySource (name, source_type, capacity)
        
        def remove_source (self, demand): 
            """Deactivate an existing energy source."""
            total_energy = sum(
                source.capacity for source in self.sources.values() if source.activate)
            if demand <= total_energy:
                return f"Demand of {demand} kWh met with {total_energy} kWh available."
            else:
                return f"Demand of {demand} kWh exceeds supply of {total_energy} kWh."
    

import tkinter as tk 
from tkinter import messagebox

class EnergyDistributionSystem:
    def __init__(self, root):
        self.grid = DistributionGrid()
        self.root = root
        self.root.title("Eco-Smart City Energy Distibution")

        #Add Source
        self.source_name = tk.StringVar()
        self.source_type = tk.StringVar()
        self.source_capacity = tk.Int.var()
        tk.Label (root, text= "Energy Source Name:").pack()
        tk.Entry (root, textvariable=self.source_name).pack()
        tk.Label (root, text= "Energy Source Type (solar,wind,hydro):")
        tk.Entry (root, textvariable = self.source_type).pack()
        tk.Label (root, textvariable = "Energy Source Capacity (kWh):"). pack()
        tk.Entry (root, textvariable = self.source_capacity).pack()
        tk.Button (root, text = "Add Source", command = self.add_source).pack()

        #Remove Source
        self.remove_name = tk.StringVar()
        tk.Label (root,text = "Remove Source Name:").pack()
        tk.Entry (root, textvariable = self.remove_name).pack()
        tk.Button (root, text = "Remove Source", command = self.remove_source).pack()

        #Demand Distribution Check
        self.demand = tk.IntVar()
        tk.Label (root, text = "Enter Demand (kWh):").pack()
        tk.Entry (root, textvariable = self.demand).pack()
        tk.Button (root, text = "Check Distribution", command = self.check_distribution).pack()

    def add_source(self):
        name = self.source_name.get()
        source_type = self.source_type.get()
        capacity = self.source_capacity.get()
        self.grid.add_source = (name, source_type, capacity)
        messagebox.showinfo ("Success", f"Added" {name} as {source_type} with {capacity} kWh capacity"))
    
    def remove_source(self): 
        name = self.remove_name.get()
        self.grid.remove_source(name)
        messagebox.showinfo ("Success", f "Removed" {name} from DistributionGrid")
    
    def check_distribution(self:
        demand = self.demand.get()
        result = self.grid.calculate_distrubution
        messagebox.showinfo ("Distibution Result", result)