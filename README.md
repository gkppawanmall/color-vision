Color Vision Deficiency (CVD) Image Processing

This repository contains Python scripts for simulating and compensating for color vision deficiency (CVD) in images. It also includes scripts to evaluate image quality using PSNR, MSE, and SSIM metrics.

Overview

CVD_Compensation_algo.py – Compensates for color vision deficiency by adjusting image colors to make them more distinguishable for people with CVD.

CVD_sumulation.py – Simulates how images appear to individuals with color vision deficiency.

PSNR.py – Calculates Peak Signal-to-Noise Ratio (PSNR) to measure the quality of compressed or recolored images compared to the original.

rmstwoimage.py – Computes Mean Squared Error (MSE) between two images to quantify the difference.

SSIM.py – Calculates Structural Similarity Index (SSIM) between two images to evaluate perceptual quality.

Requirements

Python 3.x

OpenCV (cv2)

NumPy

Matplotlib

scikit-image

Pillow (PIL)

Pandas

Installation

# Install dependencies
pip install -r requirements.txt

Usage

1. CVD_Compensation_algo.py

python CVD_Compensation_algo.py

Compensates images to improve color differentiation for colorblind users.

2. CVD_sumulation.py

python CVD_sumulation.py

Simulates how images appear to individuals with color vision deficiency.

3. PSNR.py

python PSNR.py

Calculates PSNR between original and recolored/CVD simulated images.

4. rmstwoimage.py

python rmstwoimage.py

Computes Mean Squared Error (MSE) between two sets of images.

5. SSIM.py

python SSIM.py

Calculates Structural Similarity Index (SSIM) between original and processed images.

Outputs

CVD_Compensation_algo.py and CVD_sumulation.py: Processed images saved in the current directory.

PSNR.py, rmstwoimage.py, and SSIM.py: Outputs comparison metrics in the console.
