class vehicle:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
        pass
    def get_info(self):
        return "The car brand is: {}, The car model is: {}".format(self.brand, self.model)
class car(vehicle):
    def __init__(self, brand, model, fuel_type) -> None:
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        
