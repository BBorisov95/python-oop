from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    TYPE = 'ElbowPad'
    PROTECTION = 90
    PRICE = 25.0

    def __init__(self):
        super().__init__(protection=ElbowPad.PROTECTION, price=ElbowPad.PRICE)

    def increase_price(self):
        self.price *= 1.1
