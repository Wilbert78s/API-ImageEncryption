from PIL import Image # manipulate
from IPython.display import display # show image
import numpy as np # store array

def bitwise_XOR(img, sine_map):
    # Convert the image to a NumPy array
    img_array = np.array(img)
    #print("sebelum XOR")
    #print(img_array)
    #print("------------")
    '''
    if img_array.shape == sine_map.shape:
        print("Arrays have the same size.")
    else:
        print("Arrays do not have the same size.")
    '''
    rgb=[]
    img_array = img_array.astype(np.uint8)
    sine_map = sine_map.astype(np.uint8)
    for i in range(3):
        # Perform XOR operation
        result_array = np.bitwise_xor(img_array[:,:,i], sine_map)
        rgb.append(result_array)

    rgb_image_array = np.stack((rgb[0], rgb[1], rgb[2]), axis=-1)  
    #print(result_array)
    #sprint("------------")
    # Create a new image from the result array
    result_image = Image.fromarray(rgb_image_array, "RGB")

    # Save or display the reconstructed image
    # result_image.save("XOR.jpg")
    return result_image