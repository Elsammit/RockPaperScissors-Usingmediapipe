import time
from playsound import playsound
import winsound
import Define

m_Define = Define.Define()

class Onsei():
    onseiFiles = [m_Define.JANKEN_JANWAV,m_Define.JANKEN_PONWAV]
    onseiStatus = 0
    def jankenOnsei(self):
        time.sleep(0.4)
        for onsei in self.onseiFiles:
            winsound.PlaySound(onsei, winsound.SND_FILENAME)
            self.onseiStatus += 1

if __name__ == '__main__':
    m_Onsei = Onsei()
    m_Onsei.jankenOnsei()
