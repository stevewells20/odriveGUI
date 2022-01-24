import dearpygui.dearpygui as dpg
from odriveEnums import *

cb_update_list = []

class BaseWidget:
    def __init__(self, name):
        self.name = name
        self.widget = None


class ReadOnly(BaseWidget):
    def __init__(self, name, creator, callback):
        super().__init__(name)
        self.callback = callback
        cb_update_list.append(self)
        self.widget = creator(
            label=self.name,
            default_value=self.callback()
        )

    def update(self):
        dpg.set_value(self.widget, self.callback())


class ReadWrite(BaseWidget):
    def __init__(self, name, reference_obj, creator, callback):
        super().__init__(name)
        self.callback = callback
        self.reference_obj = reference_obj
        self.widget = creator(
            label=self.name,
            default_value=reference_obj,
            callback=self.update,
            on_enter=True,
        )

    def update(self):
        val = float(dpg.get_value(self.widget))
        self.callback(val)


class ReadWriteEnumList(BaseWidget):

    def __init__(self, name, reference_obj, creator, callback, enumclass):
        super().__init__(name)
        self.callback = callback
        self.reference_obj = reference_obj
        self.enumclass = enumclass

        self.widget = creator(
            label=self.name,
            default_value=self.enumclass(reference_obj).name,
            items=[e.name for e in self.enumclass],
            callback=self.update
        )

    def update(self, sender, app_data, user_data=None):
        val = self.enumclass[app_data].value
        self.callback(val)


class ReadOnlyEnumList(BaseWidget):

    def __init__(self, name, reference_obj, creator, callback, enumclass):
        super().__init__(name)
        self.callback = callback
        self.reference_obj = reference_obj
        self.enumclass = enumclass
        cb_update_list.append(self)
        self.widget = creator(
            label=self.name,
            default_value=reference_obj,
            items=[e.name for e in self.enumclass],
            callback=self.update
        )

    def update(self):
        val = self.callback()
        val2 = self.enumclass(val).name
        dpg.set_value(self.widget, val2)


class FunctionButton(BaseWidget):

    def __init__(self, name, callback):
        super().__init__(name)
        self.callback = callback
        self.widget = dpg.add_button(
            label=self.name,
            callback=self.update
        )

    def update(self):
        self.callback()


