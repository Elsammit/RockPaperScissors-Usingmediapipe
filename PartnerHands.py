import cv2
import threading
import JankenOnsei 
import random
import time
import Define

m_Define = Define.Define()
m_Onsei = JankenOnsei.Onsei()

class Pertner:
    looretCnt = 0
    filePath = m_Define.HANDSHAPE_ROCK_IMG
    result_img = cv2.imread(m_Define.HANDSHAPE_ROCK_IMG)
    StartFlg = False
    rsp = ""
    FinishFlg = False
    JudgeFunc = ""
    GetPatternFunc = ""
    thread1 = threading.Thread(target=m_Onsei.jankenOnsei)

    def StartOnseiThread(self):
        self.thread1 = threading.Thread(target=m_Onsei.jankenOnsei, args=(self.HandsDecision,))
        self.thread1.start()

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

    def HandsDecision(self):
        x = random.randint(0,5)
        self.GetHandsMat(x)
        time.sleep(0.5)
        mehand,cpuhand = self.GetPatternFunc()
        self.JudgeFunc(mehand,cpuhand)

    def PartnerHands(self):
        if m_Onsei.onseiStatus == True:
            self.GetHandsMat(self.looretCnt)
        else:
            self.thread1.join()
            self.StartOnseiThread()
            
            self.looretCnt = 0
            time.sleep(0.1)
        
        resultImage = cv2.imread(self.filePath)

        return resultImage
    
    def PartnerLoop(self, func, getPattern):
        self.StartOnseiThread()
        self.JudgeFunc = func
        self.GetPatternFunc = getPattern
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