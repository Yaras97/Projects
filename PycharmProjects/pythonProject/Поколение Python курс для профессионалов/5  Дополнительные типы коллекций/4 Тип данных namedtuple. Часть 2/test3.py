from collections import namedtuple
PcHardware = namedtuple('PcHardware', 'cpu,gpu,motherboard,ram', defaults=[None, None])
print(PcHardware._field_defaults)
print(PcHardware)