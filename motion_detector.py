import cv2

# To initialize the system camera (change the index to 0 if 1 doesn't work)
cap = cv2.VideoCapture(0)

# To create the background subtractor
bg_sub = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    
    if not ret:
        break  # To break if the camera fails to capture the frame
    
    # The background subtractor to get the foreground mask
    fgmask = bg_sub.apply(frame)

    # To display the original camera feed and the foreground mask
    cv2.imshow('Original', frame)
    cv2.imshow('Foreground', fgmask)

    # To break the loop if the escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
