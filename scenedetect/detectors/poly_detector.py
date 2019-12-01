# Third-Party Library Imports
import numpy
import cv2

# PySceneDetect Library Imports
from scenedetect.scene_detector import SceneDetector


class PolyDetector(SceneDetector):
    
     def __init__(self):
         super(PolyDetector, self).__init__()
         self._metric_keys = ['delta_example']
         self.cli_name = 'detect-poly'