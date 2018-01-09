# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ImageType(Model):
    """An object providing possible image types and matching confidence levels.

    :param clip_art_type: Confidence level that the image is a clip art.
    :type clip_art_type: float
    :param line_drawing_type: Confidence level that the image is a line
     drawing.
    :type line_drawing_type: float
    """

    _attribute_map = {
        'clip_art_type': {'key': 'clipArtType', 'type': 'float'},
        'line_drawing_type': {'key': 'lineDrawingType', 'type': 'float'},
    }

    def __init__(self, clip_art_type=None, line_drawing_type=None):
        super(ImageType, self).__init__()
        self.clip_art_type = clip_art_type
        self.line_drawing_type = line_drawing_type
