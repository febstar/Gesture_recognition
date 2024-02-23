import mediapipe as mp
import cv2

# STEP 2: Create a HandLandmarker object.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# STEP 3: Load the input image.
image = cv2.imread("models/img.png")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# STEP 4: Detect hand landmarks from the input image.
results = hands.process(image_rgb)

# STEP 5: Process the classification result. In this case, visualize it.
if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        # Draw landmarks on the image
        mp.solutions.drawing_utils.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

# Display the image
cv2.imshow("Hand Landmarks", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
