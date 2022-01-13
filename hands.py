import cv2
import mediapipe as mp
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import time
import Define

class hands:
    m_Define = Define.Define()
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands
    after_img = cv2.imread(m_Define.HANDSHAPE_ROCK_IMG)
    StartFlg = False
    rsp = ""
    FinishFlg = False

    def HandShape(self, hand_landmarks, image):
        image_width, image_height = image.shape[1], image.shape[0]
        index_finger = [
            int(hand_landmarks.landmark[8].y * image_height),
            int(hand_landmarks.landmark[6].y * image_height)
        ]

        index_middle = [
            int(hand_landmarks.landmark[12].y * image_height),
            int(hand_landmarks.landmark[10].y * image_height)
        ]

        index_ring = [
            int(hand_landmarks.landmark[16].y * image_height),
            int(hand_landmarks.landmark[14].y * image_height)
        ]

        index_pinky = [
            int(hand_landmarks.landmark[20].y * image_height),
            int(hand_landmarks.landmark[18].y * image_height) 
        ]        

        fingersList = [index_finger, index_middle, index_ring, index_pinky]

        return fingersList

    def JudgeRPS(self, fingersList):
        hand_ret = ""
        if fingersList[0][0] > fingersList[0][1] and fingersList[1][0] > fingersList[1][1] and \
            fingersList[2][0] > fingersList[2][1] and fingersList[3][0] > fingersList[3][1]:
            hand_ret = self.m_Define.HANDSHAPE_ROCK
        elif fingersList[2][0] > fingersList[2][1] and fingersList[3][0] > fingersList[3][1]:
            hand_ret = self.m_Define.HANDSHAPE_SCISSOR
        else:
            hand_ret = self.m_Define.HANDSHAPE_PAPPER

        return hand_ret

    def HandsLoop(self):
        cap = cv2.VideoCapture(0)
        with self.mp_hands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:

            while cap.isOpened():
                success, image = cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    continue

                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                before_image = image.copy()

                results = hands.process(image)
                
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        self.mp_drawing.draw_landmarks(
                            image,
                            hand_landmarks,
                            self.mp_hands.HAND_CONNECTIONS,
                            self.mp_drawing_styles.get_default_hand_landmarks_style(),
                            self.mp_drawing_styles.get_default_hand_connections_style())
                        fingerList = self.HandShape(hand_landmarks, image)
                        self.rsp = self.JudgeRPS(fingerList)
                        
                self.after_img = cv2.flip(image - before_image, 1)
                img_pil = Image.fromarray(self.after_img)
                draw = ImageDraw.Draw(img_pil)
                draw.text((10, 350), self.rsp, font = self.m_Define.FONT, fill = (255,0,255))
                self.after_img = np.array(img_pil)
                self.StartFlg = True

                if self.FinishFlg == True:
                    break
                
                time.sleep(0.01)
                
                if __name__ == '__main__':
                    cv2.imshow('MediaPipe Hands', self.after_img)
                    if cv2.waitKey(5) & 0xFF == 27:
                        break

        cap.release()

if __name__ == '__main__':
    m_hands = hands()
    m_hands.HandsLoop()