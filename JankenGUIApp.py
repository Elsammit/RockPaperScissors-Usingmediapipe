import dearpygui.dearpygui as dpg
import numpy as np
import cv2
import time

class JankenGUI:
    getImgFunction = ""

    def __init__(self) -> None:
        dpg.create_context()
        dpg.create_viewport(max_width=550, max_height=360)
        dpg.setup_dearpygui()
    
    def GetImageFunc(self,func):
        self.getImgFunction = func

    def DispGuiApp(self):
        with dpg.texture_registry(show=False):
            dpg.add_raw_texture(480, 270, self.getImgFunction(), tag="texture_tag", format=dpg.mvFormat_Float_rgb, use_internal_label=False)

        with dpg.window(label="Main window",pos=[10,10]):
            dpg.add_image("texture_tag")

        dpg.show_viewport()

        while dpg.is_dearpygui_running():
            img = cv2.resize(self.getImgFunction() , (480, 270))
            data = np.flip(img, 2)
            data = data.ravel()
            data = np.asfarray(data, dtype='f')
            texture_data = np.true_divide(data, 255.0)
                
            dpg.set_value("texture_tag", texture_data)

            time.sleep(1/100)

            dpg.render_dearpygui_frame()

        dpg.destroy_context()

if __name__ == '__main__':
    m_JankenGUI = JankenGUI()
    m_JankenGUI.DispGuiApp()