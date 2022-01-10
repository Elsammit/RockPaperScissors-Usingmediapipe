import cv2
import threading
import JankenOnsei 
import random
import time
import Define

m_Define = Define.Define()
m_Onsei = JankenOnsei.Onsei()

class Pertner:
    looretCnt = 1000
    filePath = m_Define.HANDSHAPE_ROCK_IMG
    result_img = cv2.imread(m_Define.HANDSHAPE_ROCK_IMG)
    StartFlg = False
    JankenResult = False
    rsp = ""
    FinishFlg = False
    testFlg = False

    def StartOnseiThread(self):
        thread1 = threading.Thread(target=m_Onsei.jankenOnsei)
        thread1.start()

    def GetHandsMat(self, cnt):
        if cnt % 10 <= 2:
            self.filePath = m_Define.HANDSHAPE_ROCK_IMG
            self.rsp = m_Define.HANDSHAPE_ROCK
        elif cnt % 10 <= 5:
            self.filePath = m_Define.HANDSHAPE_SCISSORS_IMG
            self.rsp = m_Define.HANDSHAPE_SCISSOR
        elif cnt % 10 <= 9:
            self.filePath = m_Define.HANDSHAPE_PAPPERS_IMG
            self.rsp = m_Define.HANDSHAPE_PAPPER

    def PartnerHands(self):
        if m_Onsei.onseiStatus == 0:
            self.GetHandsMat(self.looretCnt)
            if self.looretCnt > 1000:
                self.looretCnt = 0
        elif m_Onsei.onseiStatus == 1:
            x = random.randint(0,5)
            self.GetHandsMat(x)
            self.JankenResult = True
            m_Onsei.onseiStatus += 1
        elif m_Onsei.onseiStatus == 2:
            self.JankenResult = False
        elif m_Onsei.onseiStatus == 3:
            m_Onsei.onseiStatus = 0
            self.StartOnseiThread()
            
            self.JankenResult = False
            self.looretCnt = 0
            time.sleep(0.1)

        resultImage = cv2.imread(self.filePath)

        return resultImage
    
    def PartnerLoop(self):
        m_Onsei.onseiStatus = 3
        while True:
            self.looretCnt += 1
            self.result_img = self.PartnerHands()
            self.StartFlg = True

            time.sleep(0.01)

            if self.FinishFlg == True:
                break

            if __name__ == '__main__':
                cv2.imshow('Partner Hands', self.result_img)
                if cv2.waitKey(10) & 0xFF == 27:
                    break

if __name__ == '__main__':
    m_Pertner = Pertner()    
    m_Pertner.PartnerLoop()           