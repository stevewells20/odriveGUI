import dearpygui.dearpygui as dpg
# import time
# import polling2
from copy import copy

import odrive
from odrive import enums

from odriveEnums import *
from odriveClasses import *

drv = odrive.find_any()
ax0 = drv.axis0
# ax1 = drv.axis1

dpg.create_context()
dpg.create_viewport(
    title='The Works',

    # width=600,
    # height=200,
)

dpg.setup_dearpygui()

with dpg.window(tag="Axis", label="Axis", width=400, pos=(800,0)):
    is_ready = ReadOnly(name="is_ready", creator=dpg.add_checkbox, callback=lambda: ax0.encoder.is_ready)
    requested_state = ReadWriteEnumList(
        name="requested_state",
        reference_obj=ax0.current_state,
        creator=dpg.add_listbox, # add_listbox
        callback=lambda x: setattr(ax0, "requested_state", x),
        enumclass=AxisState
    )
    error_state = ReadOnlyEnumList(
        name="error_state",
        reference_obj=ax0.error,
        creator=dpg.add_radio_button,
        callback=lambda: ax0.error,
        enumclass=AxisError
    )
    clear_error = FunctionButton(
        name="clear_errors",
        callback=lambda: ax0.clear_errors(),
    )


with dpg.window(tag="Encoder", label="Encoder", width=400):

    pos_estimate = ReadOnly(name="pos_estimate", creator=dpg.add_input_float, callback=lambda: ax0.encoder.pos_estimate)
    vel_estimate = ReadOnly(name="vel_estimate", creator=dpg.add_input_float, callback=lambda: ax0.encoder.vel_estimate)



    # requested_state = ReadWrite(
    #     name="requested_state",
    #     reference_obj=copy(ax0.requested_state),
    #     creator=dpg.add_input_int,
    #     callback=lambda x: setattr(ax0, "requested_state", x)
    # )


with dpg.window(tag="Controller", label="Controller", width=400, pos=(400,0)):
    current_state = ReadOnly(
        name="current_state",
        creator=dpg.add_input_text,
        callback=lambda: AxisState(ax0.current_state).name
    )


    input_pos = ReadWrite(
        name="input_pos",
        reference_obj=ax0.controller.input_pos,
        creator=dpg.add_input_int,
        callback=lambda x: setattr(ax0.controller, "input_pos", x)
    )
    input_vel = ReadWrite(
        name="input_vel",
        reference_obj=ax0.controller.input_vel,
        creator=dpg.add_input_int,
        callback=lambda x: setattr(ax0.controller, "input_vel", x)
    )
    control_mode = ReadWriteEnumList(
        name="control_mode",
        reference_obj=ax0.controller.config.control_mode,
        creator=dpg.add_listbox, # add_listbox
        callback=lambda x: setattr(ax0.controller.config, "control_mode", x),
        enumclass=ControlMode
    )
    input_mode = ReadWriteEnumList(
        name="input_mode",
        reference_obj=ax0.controller.config.input_mode,
        creator=dpg.add_listbox, # add_listbox
        callback=lambda x: setattr(ax0.controller.config, "input_mode", x),
        enumclass=InputMode
    )

    vel_setpoint = ReadOnly(name="vel_setpoint", creator=dpg.add_input_float, callback=lambda: ax0.controller.vel_setpoint)



dpg.show_viewport()
# dpg.set_primary_window("Primary Window", True)


# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    # print("this will run every frame")
    # print("about to update")
    for cb in cb_update_list:
        cb.update()
        # print('updated ', cb)
    # print('updated all cbs')
    dpg.render_dearpygui_frame()



dpg.destroy_context()



