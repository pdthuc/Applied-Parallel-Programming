import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from numba import cuda
import math

class ConvolutionFilter():
    """Converts input image to grayscale and applies various convolution filters"""

    def __init__(self, image):
        self.image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        self.sharpen = np.array(([0, -1, 0],
                                 [-1,  5, -1],
                                 [0, -1, 0]))

        self.sobelX = np.array([[-1, 0, 1],
                                [-2, 0, 2],
                                [-1, 0, 1]])

        self.sobelY = np.array(([-1, -2, -1],
                                [0,  0,  0],
                                [1,  2,  1]))

        self.laplacian = np.array(([0,  1, 0],
                                   [1, -4, 1],
                                   [0,  1, 0]))

    def __convolution(self, image_roi, kernel):
        # This function convolves the input kernel on the input image region of interest 

        kernel_dimension = len(kernel)
        pixel_sum = 0

        for i in range(kernel_dimension):
            for j in range(kernel_dimension):
                pixel_kernel_value = image_roi[i, j]*kernel[i, j]
                pixel_sum = pixel_sum+pixel_kernel_value

        if pixel_sum < 0:
            return 0
        else:
            return pixel_sum % 255

    def __applyFilter(self, kernel):
        """ Returns convolved image 
        Applies the input convolution filter onto the image 
        """

        image = self.image
        filtered_image = np.zeros(image.shape)
        image_rows, image_cols = image.shape
        delta_rows = kernel.shape[0] // 2 
        delta_cols = kernel.shape[1] // 2
        for i in range(image_rows):
          for j in range(image_cols):
            s = 0
            for k in range(kernel.shape[0]):
                for l in range(kernel.shape[1]):
                    i_k = i - k + delta_rows
                    j_l = j - l + delta_cols
                    if (i_k >= 0) and (i_k < image_rows) and (j_l >= 0) and (j_l < image_cols):  
                        s += kernel[k, l] * image[i_k, j_l]
            if s > 0:
              filtered_image[i, j] = s % 255
            else:
              filtered_image[i, j] = 0

        return filtered_image

    @cuda.jit
    def kernelApplyFilter(result, mask, image):
       
      i, j = cuda.grid(2) 
      
      image_rows, image_cols = image.shape
      if (i >= image_rows) or (j >= image_cols): 
          return
      
      delta_rows = mask.shape[0] // 2 
      delta_cols = mask.shape[1] // 2
      
      s = 0
      for k in range(mask.shape[0]):
          for l in range(mask.shape[1]):
              i_k = i - k + delta_rows
              j_l = j - l + delta_cols
              if (i_k >= 0) and (i_k < image_rows) and (j_l >= 0) and (j_l < image_cols):  
                  s += mask[k, l] * image[i_k, j_l]
      if s > 0:
        result[i, j] = s % 255
      else:
        result[i, j] = 0

    def applySharpen(self):
        """Returns image convolved with Sharpening filter"""
        kernel = self.sharpen
        filtered_image = self.__applyFilter(kernel)
        return filtered_image

    def applySobelX(self):
        """Returns image convolved with SobelX filter"""
        kernel = self.sobelX
        filtered_image = self.__applyFilter(kernel)
        return filtered_image

    def applySobelY(self):
        """Returns image convolved with SobelY filter"""
        kernel = self.sobelY
        filtered_image = self.__applyFilter(kernel)
        return filtered_image

    def applyLaplacian(self, use_deivce = False):
        """Returns image convolved with Laplacian filter"""
        image = self.image
        kernel = self.laplacian
        filtered_img = np.zeros((image.shape[0],image.shape[1]))

        if use_deivce == False:
          filtered_img = self.__applyFilter(kernel)
        else:
          block_size = (32, 32)
          grid_size = (math.ceil(image.shape[1] / block_size[0]), 
                      math.ceil(image.shape[0] / block_size[1]))
          self.kernelApplyFilter[grid_size, block_size](filtered_img, kernel, image)
        return filtered_img

    def applyCannyEdge(self):
        """Returns image convolved with CannyEdge filter"""

        filtered_image = cv2.Canny(self.image, 50, 240)
        return filtered_image
