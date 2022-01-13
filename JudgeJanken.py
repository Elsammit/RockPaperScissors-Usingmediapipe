import Define

class Judge:
    m_Define = Define.Define()
    def JudgeWinOrLose(self,handsType,partnerType):
        result = self.m_Define.YOUWIN
        if handsType == self.m_Define.HANDSHAPE_ROCK and partnerType == self.m_Define.HANDSHAPE_PAPPER or \
            handsType == self.m_Define.HANDSHAPE_PAPPER and partnerType == self.m_Define.HANDSHAPE_SCISSOR or \
            handsType == self.m_Define.HANDSHAPE_SCISSOR and partnerType == self.m_Define.HANDSHAPE_ROCK:
                result = self.m_Define.YOULOSE
        elif handsType == self.m_Define.HANDSHAPE_ROCK and partnerType == self.m_Define.HANDSHAPE_SCISSOR or \
            handsType == self.m_Define.HANDSHAPE_PAPPER and partnerType == self.m_Define.HANDSHAPE_ROCK or \
            handsType == self.m_Define.HANDSHAPE_SCISSOR and partnerType == self.m_Define.HANDSHAPE_PAPPER:
                result = self.m_Define.YOUWIN
        else:
            result = self.m_Define.YOUDRAW
        print(result)
        
        return result

if __name__ == '__main__':
    m_Define = Define.Define()
    m_judge = Judge()
    list = [ m_Define.HANDSHAPE_ROCK, m_Define.HANDSHAPE_PAPPER, m_Define.HANDSHAPE_SCISSOR]

    for i in list:
        for j in list:
            result = m_judge.JudgeWinOrLose(i,j)
            print("me:",i," you:",j," result:",result)