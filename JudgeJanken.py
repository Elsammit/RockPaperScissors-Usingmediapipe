import Define

class Judge:
    m_Define = Define.Define()
    JudgeResult = ""
    def JudgeWinOrLose(self,handsType,partnerType):
        print("me:",handsType," partner:",partnerType)
        if handsType == self.m_Define.HANDSHAPE_ROCK and partnerType == self.m_Define.HANDSHAPE_PAPPER or \
            handsType == self.m_Define.HANDSHAPE_PAPPER and partnerType == self.m_Define.HANDSHAPE_SCISSOR or \
            handsType == self.m_Define.HANDSHAPE_SCISSOR and partnerType == self.m_Define.HANDSHAPE_ROCK:
                self.JudgeResult = self.m_Define.YOULOSE
        elif handsType == self.m_Define.HANDSHAPE_ROCK and partnerType == self.m_Define.HANDSHAPE_SCISSOR or \
            handsType == self.m_Define.HANDSHAPE_PAPPER and partnerType == self.m_Define.HANDSHAPE_ROCK or \
            handsType == self.m_Define.HANDSHAPE_SCISSOR and partnerType == self.m_Define.HANDSHAPE_PAPPER:
                self.JudgeResult = self.m_Define.YOUWIN
        else:
            self.JudgeResult = self.m_Define.YOUDRAW

if __name__ == '__main__':
    m_Define = Define.Define()
    m_judge = Judge()
    list = [ m_Define.HANDSHAPE_ROCK, m_Define.HANDSHAPE_PAPPER, m_Define.HANDSHAPE_SCISSOR]

    for i in list:
        for j in list:
            result = m_judge.JudgeWinOrLose(i,j)