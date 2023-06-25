# Import necessary libraries
import cv2
import numpy as np
from keras.models import load_model

# Load trained model
model = load_model('keras_model.h5')

# Set up class labels
class_labels = ['10', '20', '50', '100', '200', '500', '2000']

# Set up video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Preprocess frame
    frame = cv2.resize(frame, (320, 160))
    frame = np.expand_dims(frame, axis=0)
    frame = frame / 255.0

    # Make prediction
    pred = model.predict(frame)

    # Get predicted class label
    pred_label = class_labels[np.argmax(pred)]

    # Display predicted class label on frame
    cv2.putText(frame, pred_label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
