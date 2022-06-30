"""
Goal of Task 2:
    Implement a helper function to transform the label format into the required format in YOLOv3.
"""


import numpy as np


def xywh2xyxy_np(xywh):
    """
    input:
        xywh (type: np.ndarray, shape: (n,4), dtype: int16): n bounding boxes with the xywh format (center based)

    output:
        xyxy (type: np.ndarray, shape: (n,4), dtype: int16): n bounding boxes with the xyxy format (edge based)
    """

    # Task:
    # ToDo: Implement the conversion of all n bounding boxes from xywh format (center x, center y, width w, height h)
    #   to the xyxy format (top left corner x, top left corner y, bottom right corner x, bottom right corner y).
    # Hints:
    #   - All values are in pixel, ranging from 0 to 352 (exclusive).
    #   - The first dimension of xywh is n (number of input boxes) and not 1.
    #   - The dtype of the resulting array is int16. Floor the xyxy pixel values to the next integer AFTER
    #     the calculation (example: xywh = np.asarray([1, 1, 1, 1]) transforms to xyxy = np.asarray([0, 0, 1, 1])).
    ########################
    #  Start of your code  #
    ########################
    n = xywh.shape[0]
    xyxy = np.zeros_like(xywh)
    for i in range(0, n):
        xyxy[i, 0] = np.floor(1.0 * xywh[i, 0] - 0.5 * xywh[i, 2])
        xyxy[i, 1] = np.floor(1.0 * xywh[i, 1] - 0.5 * xywh[i, 3])
        xyxy[i, 2] = np.floor(1.0 * xywh[i, 0] + 0.5 * xywh[i, 2])
        xyxy[i, 3] = np.floor(1.0 * xywh[i, 1] + 0.5 * xywh[i, 3])

    ########################
    #   End of your code   #
    ########################

    return xyxy


if __name__ == "__main__":
    # Execute this file to check your output of this example
    xywh_example = np.asarray([[150, 120, 20, 10], [258, 89, 55, 45]], dtype=np.int16)
    your_xyxy = xywh2xyxy_np(xywh_example)
    print(f"Your xyxy: {your_xyxy}")
    print(f"Your xyxy shape: {your_xyxy.shape}")
    print(f"Your xyxy dtype: {your_xyxy.dtype}")

# 258 + 55 / 2 = 258 + 27.5 = 285.5 = 285
# 258 - 55 / 2 = 258 - 27.5 = 230.5 = 230
# 89 - 45 / 2 = 89 - 22.5 = 66.5 = 66
# 89 + 45 / 2 = 89 + 22.5 = 111.5 = 111
# 1 - 1 / 2 = 1 - 0.5 = 1 - 0 = 1
