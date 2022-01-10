import PartnerHands
import hands
import threading
import cv2
import time
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import Define

m_Define = Define.Define()

def JudgeWinOrLose(handsType,partnerType):
    result = m_Define.YOUWIN
    if handsType == m_Define.HANDSHAPE_ROCK and partnerType == m_Define.HANDSHAPE_PAPPER or \
        handsType == m_Define.HANDSHAPE_PAPPER and partnerType == m_Define.HANDSHAPE_SCISSOR or \
        handsType == m_Define.HANDSHAPE_SCISSOR and partnerType == m_Define.HANDSHAPE_ROCK:
            result = m_Define.YOULOSE
    elif handsType == m_Define.HANDSHAPE_ROCK and partnerType == m_Define.HANDSHAPE_SCISSOR or \
        handsType == m_Define.HANDSHAPE_PAPPER and partnerType == m_Define.HANDSHAPE_ROCK or \
        handsType == m_Define.HANDSHAPE_SCISSOR and partnerType == m_Define.HANDSHAPE_PAPPER:
            result = m_Define.YOUWIN
    else:
        result = m_Define.YOUDRAW
    print(result)
    
    return result

if __name__ == '__main__':
    m_hands = hands.hands()
    thread1 = threading.Thread(target=m_hands.HandsLoop)
    thread1.start()
    m_PartnerHands = PartnerHands.Pertner()
    result = ""

    while True:
        if m_hands.StartFlg == True:
            thread2 = threading.Thread(target=m_PartnerHands.PartnerLoop)
            thread2.start()
            time.sleep(0.5)
            break

    while True:
        if m_hands.StartFlg == True and m_PartnerHands.StartFlg == True:
            
            if m_PartnerHands.JankenResult == True:
                print("hands:",m_hands.rsp,", partner:",m_PartnerHands.rsp)
                result = JudgeWinOrLose(m_hands.rsp,m_PartnerHands.rsp)
            
            resultImage = cv2.resize(m_PartnerHands.result_img, (m_hands.after_img.shape[1], m_hands.after_img.shape[0]))
            concatImg = cv2.hconcat([m_hands.after_img, resultImage]) 
            
            img_pil = Image.fromarray(concatImg)
            draw = ImageDraw.Draw(img_pil)
            draw.text((10, 20), result, font = m_Define.FONT, fill = (255,0,255))
            concatImg = np.array(img_pil)
            
            cv2.imshow('Result Main', concatImg)

            if cv2.waitKey(5) & 0xFF == 27:
                m_hands.FinishFlg = True
                m_PartnerHands.FinishFlg = True
                break