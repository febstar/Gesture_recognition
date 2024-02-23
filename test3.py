import mediapipe as mp
import cv2

# STEP 1: Create a Hands object.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# STEP 2: Open a video capture object.
cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera.

# Initialize variables for gesture recognition
gesture_text = ""

while cap.isOpened():
    # STEP 3: Read a frame from the video capture.
    ret, frame = cap.read()
    if not ret:
        break

    # STEP 4: Convert the frame to RGB.
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # STEP 5: Process the frame to detect hand landmarks.
    results = hands.process(frame_rgb)

    # STEP 6: Draw landmarks on the frame.
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks on the image
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Check for the Open Hand gesture (all fingers extended)
            # Check for the Open Hand gesture (all fingers extended and wide apart)
            if (
                    hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[
                mp_hands.HandLandmark.INDEX_FINGER_TIP].x and
                    hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x < hand_landmarks.landmark[
                mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x and
                    hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x < hand_landmarks.landmark[
                mp_hands.HandLandmark.RING_FINGER_TIP].x and
                    hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x < hand_landmarks.landmark[
                mp_hands.HandLandmark.PINKY_TIP].x
            ):
                gesture_text = "Paper"
            else:
                gesture_text = ""

            # Display gesture text on the hand
            cv2.putText(frame, gesture_text, (int(hand_landmarks.landmark[0].x * frame.shape[1]), int(hand_landmarks.landmark[0].y * frame.shape[0])), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # STEP 7: Display the frame.
    cv2.imshow("Hand Landmarks", frame)

    # Break the loop when 'q' is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# STEP 8: Release the video capture object and close all windows.
cap.release()
cv2.destroyAllWindows()
