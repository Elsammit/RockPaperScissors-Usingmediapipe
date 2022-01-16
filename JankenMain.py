import PartnerHands
import hands
import JudgeJanken
import threading
import cv2
import time
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import Define

m_PartnerHands = PartnerHands.Pertner()
m_hands = hands.hands()

def InitCpuHand():
    thread2 = threading.Thread(target=m_PartnerHands.PartnerLoop, args=(m_Judge.JudgeWinOrLose, GetHandPattern, ))
    thread2.start()

def InitMyHand():
    thread1 = threading.Thread(target=m_hands.HandsLoop, args=(InitCpuHand,))
    thread1.start()

def GetHandPattern():
    return m_hands.rsp, m_PartnerHands.rsp

if __name__ == '__main__':
    InitMyHand()
    
    m_Judge = JudgeJanken.Judge()
    result = ""
    m_Define = Define.Define()

    while True:
        if m_PartnerHands.StartFlg == True:
            resultImage = cv2.resize(m_PartnerHands.result_img, (m_hands.after_img.shape[1], m_hands.after_img.shape[0]))
            concatImg = cv2.hconcat([m_hands.after_img, resultImage]) 
            
            img_pil = Image.fromarray(concatImg)
            draw = ImageDraw.Draw(img_pil)
            draw.text((10, 20), m_Judge.JudgeResult, font = m_Define.FONT, fill = (255,0,255))
            concatImg = np.array(img_pil)
            
            cv2.imshow('Result Main', concatImg)

            if cv2.waitKey(5) & 0xFF == 27:
                m_hands.FinishFlg = True
                m_PartnerHands.FinishFlg = True
                break