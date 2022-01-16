import dearpygui.dearpygui as dpg
import numpy as np
import cv2
import time

dpg.create_context()
dpg.create_viewport(max_width=550, max_height=360)
dpg.setup_dearpygui()

vid = cv2.VideoCapture(0)
ret, img = vid.read()
frame_rate = int(vid.get(cv2.CAP_PROP_FPS))
img = cv2.resize(img , (480, 270))

with dpg.texture_registry(show=False):
    dpg.add_raw_texture(480, 270, img, tag="texture_tag", format=dpg.mvFormat_Float_rgb, use_internal_label=False)

with dpg.window(label="Main window",pos=[10,10]):
    dpg.add_image("texture_tag")

dpg.show_viewport()

while dpg.is_dearpygui_running():
    ret, img = vid.read()
    if ret == True:
        img = cv2.resize(img , (480, 270))
        data = np.flip(img, 2)
        data = data.ravel()
        data = np.asfarray(data, dtype='f')
        texture_data = np.true_divide(data, 255.0)
            
        dpg.set_value("texture_tag", texture_data)

        time.sleep(1/frame_rate)

    dpg.render_dearpygui_frame()

dpg.destroy_context()
