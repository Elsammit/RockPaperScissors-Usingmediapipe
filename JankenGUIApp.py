import dearpygui.dearpygui as dpg
import numpy as np
import cv2
import time

class JankenGUI:
    getImgFunction = ""
    getResult = ""
    FinishGUI = False

    def __init__(self) -> None:
        dpg.create_context()
        dpg.create_viewport(max_width=1500, max_height=1500)
        dpg.setup_dearpygui()
    
    def GetImageFunc(self,func):
        self.getImgFunction = func

    def GetJudgeResult(self,func):
        self.getResult = func

    def DispGuiApp(self):
        image = self.getImgFunction()
        image_width, image_height = image.shape[1], image.shape[0]

        with dpg.font_registry(show=False):
            dpg.add_font("./cambria.ttc", 50, tag="ttf-font")

        with dpg.texture_registry(show=False):
            dpg.add_raw_texture(image_width, image_height, self.getImgFunction(), tag="texture_tag", format=dpg.mvFormat_Float_rgb, use_internal_label=False)

        with dpg.window(label="",pos=[10,10],width=1500, height=1500):
            dpg.add_image("texture_tag")
            dpg.add_text(tag="result")
            dpg.bind_item_font(dpg.last_item(), "ttf-font")

        dpg.show_viewport()

        gameCnt = 0
        while dpg.is_dearpygui_running():
            img = cv2.resize(self.getImgFunction() , (image_width, image_height))
            data = np.flip(img, 2)
            data = data.ravel()
            data = np.asfarray(data, dtype='f')
            texture_data = np.true_divide(data, 255.0)
  
            dpg.set_value("texture_tag", texture_data)
            dpg.set_value("result", self.getResult())

            time.sleep(0.001)

            dpg.render_dearpygui_frame()

            if gameCnt == 3:
                self.FinishGUI = True
            else:
                gameCnt+=1

        dpg.destroy_context()
        self.FinishGUI = True

if __name__ == '__main__':
    m_JankenGUI = JankenGUI()
    m_JankenGUI.DispGuiApp()