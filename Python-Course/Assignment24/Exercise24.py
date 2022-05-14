import numpy as np
import cv2
import tensorflow as tf
from functools import partial
import time
from TFLiteFaceDetector import UltraLightFaceDetecion
import sys
import math

class CoordinateAlignmentModel():
    def __init__(self, filepath, marker_nums=106, input_size=(192, 192)):
        self._marker_nums = marker_nums
        self._input_shape = input_size
        self._trans_distance = self._input_shape[-1] / 2.0

        self.eye_bound = ([35, 41, 40, 42, 39, 37, 33, 36],
                          [89, 95, 94, 96, 93, 91, 87, 90])

        # tflite model init
        self._interpreter = tf.lite.Interpreter(model_path=filepath)
        self._interpreter.allocate_tensors()

        # model details
        input_details = self._interpreter.get_input_details()
        output_details = self._interpreter.get_output_details()

        # inference helper
        self._set_input_tensor = partial(self._interpreter.set_tensor,
                                         input_details[0]["index"])
        self._get_output_tensor = partial(self._interpreter.get_tensor,
                                          output_details[0]["index"])

        self.pre_landmarks = None

    def _calibrate(self, pred, thd, skip=6):
        if self.pre_landmarks is not None:
            for i in range(pred.shape[0]):
                if abs(self.pre_landmarks[i, 0] - pred[i, 0]) > skip:
                    self.pre_landmarks[i, 0] = pred[i, 0]
                elif abs(self.pre_landmarks[i, 0] - pred[i, 0]) > thd:
                    self.pre_landmarks[i, 0] += pred[i, 0]
                    self.pre_landmarks[i, 0] /= 2

                if abs(self.pre_landmarks[i, 1] - pred[i, 1]) > skip:
                    self.pre_landmarks[i, 1] = pred[i, 1]
                elif abs(self.pre_landmarks[i, 1] - pred[i, 1]) > thd:
                    self.pre_landmarks[i, 1] += pred[i, 1]  
                    self.pre_landmarks[i, 1] /= 2
        else:
            self.pre_landmarks = pred

    def _preprocessing(self, img, bbox, factor=3.0):


        maximum_edge = max(bbox[2:4] - bbox[:2]) * factor
        scale = self._trans_distance * 4.0 / maximum_edge
        center = (bbox[2:4] + bbox[:2]) / 2.0
        cx, cy = self._trans_distance - scale * center

        M = np.array([[scale, 0, cx], [0, scale, cy]])

        cropped = cv2.warpAffine(img, M, self._input_shape, borderValue=0.0)
        inp = cropped[..., ::-1].astype(np.float32)

        return inp[None, ...], M

    def _inference(self, input_tensor):
        self._set_input_tensor(input_tensor)
        self._interpreter.invoke()

        return self._get_output_tensor()[0]

    def _postprocessing(self, out, M):
        iM = cv2.invertAffineTransform(M)
        col = np.ones((self._marker_nums, 1))

        out = out.reshape((self._marker_nums, 2))

        out += 1
        out *= self._trans_distance

        out = np.concatenate((out, col), axis=1)

        return out @ iM.T  # dot product

    def get_landmarks(self, image, detected_faces=None):

        for box in detected_faces:
            inp, M = self._preprocessing(image, box)
            out = self._inference(inp)
            pred = self._postprocessing(out, M)

            yield pred






if __name__ == '__main__':
#left eye = 35-42 , right eye = 81-96


    fd = UltraLightFaceDetecion("weights/RFB-320.tflite",
        conf_threshold=0.88)
    fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

#face detector & face alignment
    image = cv2.imread('./input/Picture2.jpg')
    color = (125, 255, 125)
    image = cv2.resize(image, (0, 0), fx = 2, fy = 2)
    rows = image.shape[0]
    cols = image.shape[1]

    mask = np.zeros((rows, cols), dtype = 'uint8')


  

    boxes, scores = fd.inference(image)

    for pred in fa.get_landmarks(image, boxes):
        pred_int = np.round(pred).astype(np.int)
        landmarks_left_eye = []
        landmarks_right_eye = []
        landmarks_lips = []
        for i in [35, 36, 33, 37, 39, 42, 40, 41]:
            landmarks_left_eye.append(tuple(pred_int[i]))
        for j in [89, 95, 94, 96, 93, 91, 87, 90]:
            landmarks_right_eye.append(tuple(pred_int[j]))
        for k in [52, 55, 53, 58, 69, 68, 67, 71, 63]:
            landmarks_lips.append(tuple(pred_int[k]))
  
        landmarks_left_eye = np.array(landmarks_left_eye)
        landmarks_right_eye = np.array(landmarks_right_eye)
        landmarks_lips = np.array(landmarks_lips)
      
        cv2.drawContours(mask, [landmarks_left_eye], -1, (255, 255, 255), -1)
        cv2.drawContours(mask, [landmarks_right_eye], -1, (255, 255, 255), -1 )
        cv2.drawContours(mask, [landmarks_lips], -1, (255, 255, 255), -1)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for i, contour in enumerate(contours):
        rect = cv2.minAreaRect(contour)
        (x, y), (w ,h), a  = rect
        box = cv2.boxPoints(rect)
        box = np.int0(box) 
 
        rect2 = cv2.drawContours(mask, [box], 0, (1, 0, 0), 1)
        x, y, w, h = np.int0(box[0][0]), np.int0(box[0][1]), np.int0(box[1][0])-np.int0(box[0][0]), np.int0(box[2][1]-box[0][1])
        box = image[y:y+h, x:x+w]
        w1 = math.floor(w/2)
        h1 = math.floor(h/2)
        w2 = w*2
        h2 = h*2
        if w%2 == 1:
            w2-=1
        if h%2 == 1:
            h2-=1
        box = cv2.resize(box, (w2, h2))
        image[y-h1:y+h+h1, x-w1:x+w+w1] = box
 
    cv2.imwrite('./output/result3.jpg', image)
    cv2.imshow("result3.jpg", image)
    cv2.waitKey()
    
