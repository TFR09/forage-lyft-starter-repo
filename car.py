from service import Servicable

class Car(Servicable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        service = self.engine.needs_service() or self.battery.needs_service()
        return service