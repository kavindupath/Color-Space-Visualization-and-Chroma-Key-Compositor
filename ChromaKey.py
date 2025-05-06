import cv2
import numpy as np
import sys

# Load the image and color space as input
first_argument = sys.argv[1]
second_argument= sys.argv[2]
 
def Task_01():
    """
    This function is based on the task 01 of this assignment. 
    We read an image, convert it to a specified color space (such as CIE-XYZ, CIE-Lab, YCrCb, or HSB), 
    and display the original color image alongside its color components in a single viewing window.
    """
    image = cv2.imread(second_argument)

    # Get the dimensions of the image
    height, width = image.shape[:2]
    aspect_ratio = width / height

    # Convert image to different color spaces based on user input
    if(first_argument == "-XYZ"):
        image_converted = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)
    elif(first_argument == "-Lab"):
        image_converted = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    elif(first_argument == "-YCrCb"):
        image_converted = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    elif(first_argument == "-HSB"):
        image_converted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)   
    else:
        raise ValueError("Unsupported color space")
    
    # Split the channels
    channel_1, channel_2, channel_3 = cv2.split(image_converted)

    # keep the channel as a 3-channel image for concatenation purposes 
    channel_1_gray = cv2.cvtColor(channel_1, cv2.COLOR_GRAY2BGR)
    channel_2_gray = cv2.cvtColor(channel_2, cv2.COLOR_GRAY2BGR)
    channel_3_gray = cv2.cvtColor(channel_3, cv2.COLOR_GRAY2BGR)

    # resize the image based on aspect ratio
    def resize_image(image,target_width = 1280):
        new_height = int(target_width / aspect_ratio)
        return cv2.resize(image, (target_width, new_height))
    
    image_resize = resize_image(image)
    channel_1_gray_resize = resize_image(channel_1_gray)
    channel_2_gray_resize = resize_image(channel_2_gray)
    channel_3_gray_resize = resize_image(channel_3_gray)

    # Stack the original image and the channel images
    top_row = np.hstack((image_resize, channel_1_gray_resize))
    bottom_row = np.hstack((channel_2_gray_resize,channel_3_gray_resize))

    # Combine the two rows vertically
    combined_image = np.vstack((top_row, bottom_row))
    cv2.namedWindow("Original Image and the {0} channel images. Aspect ratio: {1}".format(first_argument, round(aspect_ratio,2)), cv2.WINDOW_NORMAL) 
    cv2.resizeWindow("Original Image and the {0} channel images. Aspect ratio: {1}".format(first_argument, round(aspect_ratio,2)), 1280, 720) 
    cv2.imshow("Original Image and the {0} channel images. Aspect ratio: {1}".format(first_argument, round(aspect_ratio,2)),combined_image)
    cv2.waitKey(0)


def Task_02():
    """
    This function is based on the task 02 of this assignment. 
    We will extract a person from a green screen photo using chroma keying (e.g., hue and chroma information) and place the person 
    in the middle-bottom of a scenic photo, ensuring the combined photo is the same size as the scenic photo without any distortion. 
    It display the original green screen photo, the extracted person on a white background, the scenic photo, and the final combined photo,
    all within a single viewing window.
    """
    background_image= cv2.imread(first_argument)
    green_image = cv2.imread(second_argument) 

    # Get the dimensions of the image
    height, width = green_image.shape[:2]
    aspect_ratio = width / height

    # resize the image based on aspect ratio
    def resize_image(image,target_width = 1280):
        new_height = int(target_width / aspect_ratio)
        return cv2.resize(image, (target_width, new_height))

    green_image_copy =np.copy(green_image)
    green_image_copy=resize_image(green_image_copy)

    # Convert the image to HSV color space and get the upper and lower bounds for the green color
    green_image_hsv = cv2.cvtColor(green_image_copy, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])
    
    # create the mask- pixels that are in the given range set to white(255)
    mask =cv2.inRange(green_image_hsv,lower_green, upper_green)

    # Resize the mask
    mask= resize_image(mask)

    # set the dimension of the mask to 3 (For concatination purposes)
    mask_grey = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    # inverse the mask- set the 255 values to 0, 0 values to 255
    mask_inverse=cv2.bitwise_not(mask)
   
    # bitwise AND - intersecting reigion of original image and inversed masked image
    masked_image = cv2.bitwise_and(green_image_copy, green_image_copy, mask=mask_inverse)
    masked_image = resize_image(masked_image)
    
    # Create a white background with the same size as the green screen image
    white_background = np.full_like(green_image_copy, 255)

    # Bitwise AND - intersecting region of white background and the inverse masked image
    person_on_white_background = cv2.bitwise_and(white_background, white_background, mask=mask)

    # Combine the person with the white background
    masked_person_with_white_bg = cv2.add(person_on_white_background, masked_image)
    masked_person_with_white_bg =resize_image(masked_person_with_white_bg)

    # Resize the background image
    background_image =resize_image(background_image)

    # Use bitwise_and to apply the inverse mask to the black background
    background_image_black = cv2.bitwise_and(background_image, background_image, mask=mask)

    # Combine the two images
    added_image = cv2.add(background_image_black, masked_image)

    # Stack the original image and the masked images
    top_row = np.hstack((green_image_copy, masked_person_with_white_bg))
    bottom_row = np.hstack((background_image,added_image))

    # Combine the two rows vertically
    combined_image = np.vstack((top_row, bottom_row))

    cv2.namedWindow("Combined image. Aspect ratio: {0}".format(round(aspect_ratio,2)), cv2.WINDOW_NORMAL) 
    cv2.resizeWindow("Combined image. Aspect ratio: {0}".format(round(aspect_ratio,2)), 1280, 720) 
    cv2.imshow("Combined image. Aspect ratio: {0}".format(round(aspect_ratio,2)),combined_image)
 
    cv2.waitKey(0)


try:
    # Check whether there is a 'dot' in first argument. If so run the Task 02
    if('.' in first_argument):
        Task_02()
    # If there is no 'dot' in the first argument run the Task 01
    else:
        Task_01()
except Exception as e:
        print(f"An error occurred: {e}")


