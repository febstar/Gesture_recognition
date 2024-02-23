import mediapipe as mp
import cv2
from import1 import gestlogic


class VIDEO:
    def __init__(self):
        self.dict = ''
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()

        self.cap = cv2.VideoCapture(0)

        # Initialize variables for gesture recognition
        self.gesture_text = ""

        while self.cap.isOpened():
            # STEP 3: Read a frame from the video capture.
            ret, self.frame = self.cap.read()
            if not ret:
                break

            # STEP 4: Convert the frame to RGB.
            frame_rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

            # STEP 5: Process the frame to detect hand landmarks.
            self.results = self.hands.process(frame_rgb)
            self.gestures()
            if self.results.multi_hand_landmarks:
                for hand_landmarks in self.results.multi_hand_landmarks:
                    # Draw landmarks on the image
                    mp.solutions.drawing_utils.draw_landmarks(self.frame, hand_landmarks,
                                                              self.mp_hands.HAND_CONNECTIONS)
                    gestlogic(hand_landmarks, self, cv2)

            # STEP 7: Display the frame.
            cv2.imshow("Hand Landmarks", self.frame)

            # Break the loop when 'q' is pressed.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # STEP 8: Release the video capture object and close all windows.
        self.cap.release()
        cv2.destroyAllWindows()

    def gestures(self, **args):

        return args



