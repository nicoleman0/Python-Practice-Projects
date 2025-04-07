class Shipping:
    def __init__(self, weight):
        self.weight = weight

    def ground_shipping(self):
        if self.weight <= 2:
            cost_ground = self.weight * 1.5 + 20
        elif self.weight <= 6:
            cost_ground = self.weight * 3.0 + 20
        elif self.weight <= 10:
            cost_ground = self.weight * 4.0 + 20
        else:
            cost_ground = self.weight * 4.75 + 20
        return cost_ground

    def drone_shipping(self):
        if self.weight <= 2:
            cost_drone = self.weight * 4.5
        elif self.weight <= 6:
            cost_drone = self.weight * 9.0
        elif self.weight <= 10:
            cost_drone = self.weight * 12.0
        else:
            cost_drone = self.weight * 14.25
        return cost_drone

    def premium_shipping(self):
        return 125.00

    def cheapest_shipping_method(self):
        ground = self.ground_shipping()
        drone = self.drone_shipping()
        premium = self.premium_shipping()
        if ground < drone and ground < premium:
            return f"Ground shipping is cheapest: ${ground}"
        elif drone < ground and drone < premium:
            return f"Drone shipping is cheapest: ${drone}"
        else:
            return f"Ground shipping premium is cheapest: ${premium}"


class PremiumShipping(Shipping):
    def __init__(self, weight):
        super().__init__(weight)
        self.premium_cost = 125.00

    def premium_shipping(self):
        return self.premium_cost


weight = 11.2
shipping = Shipping(weight)
print(f"Ground Shipping Premium: ${shipping.premium_shipping()}")

print(shipping.cheapest_shipping_method())
