from mbientlab.metawear import MetaWear, libmetawear
from mbientlab.warble import *

device = MetaWear('C7:CF:3D:0E:D9:0E')
device.connect()

pattern= LedPattern(repeat_count= Const.LED_REPEAT_INDEFINITELY)
libmetawear.mbl_mw_led_load_preset_pattern(byref(pattern), LedPreset.BLINK)
libmetawear.mbl_mw_led_write_pattern(device.board, byref(pattern), LedColor.GREEN)
libmetawear.mbl_mw_led_play(device.board)
