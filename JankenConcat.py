import PartnerHands
import hands
import JudgeJanken
import threading
import cv2
import time
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import Define

class ConcatImage:
    m_PartnerHands = PartnerHands.Pertner()
    m_hands = hands.hands()
    m_Judge = JudgeJanken.Judge()
    m_Define = Define.Define()
    concatImg = ""
    StartConcat = False
    IsViewConcatImg = False
    FinishConcat = False

    def InitCpuHand(self):
        thread2 = threading.Thread(target=self.m_PartnerHands.PartnerLoop, args=(self.m_Judge.JudgeWinOrLose, self.GetHandPattern, ))
        thread2.start()

    def InitMyHand(self):
        thread1 = threading.Thread(target=self.m_hands.HandsLoop, args=(self.InitCpuHand,))
        thread1.start()

    def GetHandPattern(self):
        return self.m_PartnerHands.rsp, self.m_hands.rsp

    def ConcatLoopThread(self):
        thread3 = threading.Thread(target=self.LoopConcatImage)
        thread3.start()

    def GetConcatImage(self):
        return self.concatImg

    def GetResult(self):
        return self.m_Judge.JudgeResult

    def LoopConcatImage(self):
        while True:
            if self.m_PartnerHands.StartFlg == True:
                resultImage = cv2.resize(self.m_PartnerHands.result_img, (self.m_hands.after_img.shape[1], self.m_hands.after_img.shape[0]))
                self.concatImg = cv2.hconcat([self.m_hands.after_img, resultImage]) 
                
                '''
                img_pil = Image.fromarray(self.concatImg)
                draw = ImageDraw.Draw(img_pil)
                draw.text((10, 20), self.m_Judge.JudgeResult, font = self.m_Define.FONT, fill = (255,0,255))
                self.concatImg = np.array(img_pil)
                '''
                self.StartConcat = True

                if self.IsViewConcatImg == True:
                    cv2.imshow('Result Main', self.concatImg)
                    
                if self.FinishConcat == True:
                    self.m_hands.FinishFlg = True
                    self.m_PartnerHands.FinishFlg = True
                    break