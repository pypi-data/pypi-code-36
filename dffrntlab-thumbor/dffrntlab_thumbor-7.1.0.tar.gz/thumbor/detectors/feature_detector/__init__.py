#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com

import cv2
import numpy as np

from thumbor.detectors import BaseDetector
from thumbor.point import FocalPoint
from thumbor.utils import logger


class Detector(BaseDetector):

    def detect(self, callback):
        engine = self.context.modules.engine
        try:
            img = np.array(
                engine.convert_to_grayscale(
                    update_image=False,
                    with_alpha=False
                )
            )
        except Exception as e:
            logger.exception(e)
            logger.warn('Error during feature detection; skipping to next detector')
            self.next(callback)
            return

        points = cv2.goodFeaturesToTrack(
            img,
            maxCorners=20,
            qualityLevel=0.04,
            minDistance=1.0,
            useHarrisDetector=False,
        )
        if points is not None:
            for point in points:
                x, y = point.ravel()
                self.context.request.focal_points.append(FocalPoint(x.item(), y.item(), 1))
            callback()
        else:
            self.next(callback)
