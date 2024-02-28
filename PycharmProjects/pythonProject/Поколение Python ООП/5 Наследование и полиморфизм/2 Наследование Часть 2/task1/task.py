class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = 8.99


class SilverPlan(BasicPlan):
    has_HD = True
    has_UHD = False
    num_of_devices = 2
    price = 12.99


class GoldPlan(BasicPlan):
    has_HD = True
    has_UHD = True
    num_of_devices = 4
    price = 15.99


print(BasicPlan.can_stream)
print(BasicPlan.can_download)
print(BasicPlan.has_SD)
print(BasicPlan.has_HD)
print(BasicPlan.has_UHD)
print(BasicPlan.num_of_devices)
print(BasicPlan.price)
