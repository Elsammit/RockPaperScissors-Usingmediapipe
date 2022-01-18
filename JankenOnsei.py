import time
from playsound import playsound
import winsound
import Define

m_Define = Define.Define()

class Onsei():
    onseiStatus = 0
    def jankenOnsei(self, HandsDecision):
        self.onseiStatus = 0
        time.sleep(0.4)
        winsound.PlaySound(m_Define.JANKEN_JANWAV, winsound.SND_FILENAME)
        self.onseiStatus = 1
        HandsDecision()
        winsound.PlaySound(m_Define.JANKEN_PONWAV, winsound.SND_FILENAME)
        self.onseiStatus = 2

if __name__ == '__main__':
    m_Onsei = Onsei()
    m_Onsei.jankenOnsei()
