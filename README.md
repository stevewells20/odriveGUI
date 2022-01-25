# odriveGUI

## Framework for creating GUI's for Odrive FOC platform

Current State: Unstable Alpha -> Everything about it will change

odriveGUI consists of a class based system for easily creating GUI's using DearPyGui. The main feature added by this system is breaking up the objects provided by odrive by purpose, and handling a lot of the boilerplate of adding that to DPG.

## Example

```python
import dearpygui.dearpygui as dpg
import odrive

from odriveEnums import *
from odriveClasses import *

drv = odrive.find_any()

dpg.create_context()
dpg.create_viewport()

dpg.setup_dearpygui()

with dpg.window(tag="Axis", label="Axis", width=400, pos=(800,0)):
    is_ready = ReadOnly(name="is_ready", creator=dpg.add_checkbox, callback=lambda: drv.axis0.encoder.is_ready)

with dpg.window(tag="Encoder", label="Encoder", width=400):

    pos_estimate = ReadOnly(name="pos_estimate", creator=dpg.add_input_float, callback=lambda: drv.axis0.encoder.pos_estimate)
    vel_estimate = ReadOnly(name="vel_estimate", creator=dpg.add_input_float, callback=lambda: drv.axis0.encoder.vel_estimate)

dpg.show_viewport()

while dpg.is_dearpygui_running():
    for cb in cb_update_list:
        cb.update()
    dpg.render_dearpygui_frame()



dpg.destroy_context()

```
