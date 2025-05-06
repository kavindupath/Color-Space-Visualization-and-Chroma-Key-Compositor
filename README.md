# Color-Space-Visualization-and-Chroma-Key-Compositor
# Task One - Color Space Component Visualization

This task demonstrates the conversion of a color image into different color spaces (e.g., CIE-XYZ, CIE-Lab, YCrCb, HSB) and visualizes their individual components (channels) in gray-scale.

📌 Objective
- Read an image using OpenCV.
- Convert it to a specified color space (e.g., Lab, XYZ, YCrCb, HSB).
- Display:
  - The original image.
  - Three individual channels (C1, C2, C3) as gray-scale images.
- Arrange all images in a single display window in the layout

  Supported Color Spaces
- **CIE-XYZ**
- **CIE-Lab**
- **YCrCb**
- **HSB (HSV in OpenCV)**

# Task Two - Chroma Key (Green Screen Extraction and Background Replacement)

This task demonstrates Chroma Keying, a common technique in video and photo editing, to extract a subject from a green screen image and blend them into a scenic background without distortion.

📌 Objective
- Extract the subject from a green screen photo using Chroma key techniques (based on Hue and/or other color properties).
- Overlay the subject onto a scenic photo:
  - Output image must match the scenic photo size.
  - Subject should be horizontally centered.
  - Subject should be vertically aligned to the **bottom**.
  - No scaling/distortion applied to subject.


🛠 Dependencies

- Python 3.x
- OpenCV
- NumPy
