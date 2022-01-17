import JankenConcat
import JankenGUIApp

if __name__ == '__main__':
    m_ConcatImage = JankenConcat.ConcatImage()
    m_JankenGUI = JankenGUIApp.JankenGUI()

    m_ConcatImage.InitMyHand()
    m_ConcatImage.ConcatLoopThread()
    m_JankenGUI.GetImageFunc(m_ConcatImage.GetConcatImage)
    while True:
        if m_ConcatImage.StartConcat == True:
            break

    m_JankenGUI.DispGuiApp()