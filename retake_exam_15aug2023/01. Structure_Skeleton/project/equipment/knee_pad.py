from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    TYPE = 'KneePad'
    PROTECTION = 120
    PRICE = 15.0

    def __init__(self):
        super().__init__(protection=KneePad.PROTECTION, price=KneePad.PRICE)

    def increase_price(self):
        self.price *= 1.2
