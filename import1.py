def gestlogic(a, y, z):
    gesture_text = ''
    thumb_tip_x = a.landmark[y.mp_hands.HandLandmark.THUMB_TIP].x
    index_tip_x = a.landmark[y.mp_hands.HandLandmark.INDEX_FINGER_TIP].x
    middle_tip_x = a.landmark[y.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
    ring_tip_x = a.landmark[y.mp_hands.HandLandmark.RING_FINGER_TIP].x
    pinky_tip_x = a.landmark[y.mp_hands.HandLandmark.PINKY_TIP].x
    thumb_tip_y = a.landmark[y.mp_hands.HandLandmark.THUMB_TIP].y
    index_tip_y = a.landmark[y.mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip_y = a.landmark[y.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip_y = a.landmark[y.mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip_y = a.landmark[y.mp_hands.HandLandmark.PINKY_TIP].y
    if (
            thumb_tip_x < index_tip_x < middle_tip_x < ring_tip_x < pinky_tip_x
    ):
        gesture_text = "Paper"
    elif (
            index_tip_y < middle_tip_y < pinky_tip_y and
            ring_tip_y > middle_tip_y
    ):
        gesture_text = "Scissors"

    # Display gesture text on the hand
    z.putText(y.frame, gesture_text, (
        int(a.landmark[0].x * y.frame.shape[1]), int(a.landmark[0].y * y.frame.shape[0])),
              z.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, z.LINE_AA)