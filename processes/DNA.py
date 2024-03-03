from PIL import Image # manipulate
import numpy as np # store array
#CGGC
rule_1 = {'A': '00', 'T': '11', 'C': '01', 'G': '10'}
rule_2 = {'A': '00', 'T': '11', 'C': '10', 'G': '01'}
rule_3 = {'A': '01', 'T': '10', 'C': '00', 'G': '11'}
rule_4 = {'A': '01', 'T': '10', 'C': '11', 'G': '00'}
rule_5 = {'A': '10', 'T': '01', 'C': '00', 'G': '11'}
rule_6 = {'A': '10', 'T': '01', 'C': '11', 'G': '00'}
rule_7 = {'A': '11', 'T': '00', 'C': '01', 'G': '10'}
rule_8 = {'A': '11', 'T': '00', 'C': '10', 'G': '01'}
rules = [rule_1,
        rule_2,
        rule_3,
        rule_4,
        rule_5,
        rule_6,
        rule_7,
        rule_8]

comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def encode(img, number):
    encoding_rule = rules[number-1]
    encoding_rule_reversed = {value: key for key, value in encoding_rule.items()}
    # Get the size of the original image
    M, N = img.size

    # Convert the image to a NumPy array
    img_array = np.array(img)
    # Convert each element to 8-bit binary and store it as a string
    binary_strings = np.vectorize(lambda x: format(x, '08b'))(img_array)
    rgb=[]
    for i in range(3):
        # Flatten the original array
        flattened_array = np.concatenate(binary_strings[:,:,i])

        # Repeat each element four times consecutively
        repeated_array = np.repeat(flattened_array, 4)

        # Reshape the repeated array to the desired shape (4x24)
        reshaped_array = repeated_array.reshape((M, 4*N))

        # Iterate over each row and modify elements based on column index
        for row in range(reshaped_array.shape[0]):
            for col in range(reshaped_array.shape[1]):
                if col % 4 == 0:
                    reshaped_array[row, col] = encoding_rule_reversed.get(reshaped_array[row, col][:2], reshaped_array[row, col][:2])
                elif col % 4 == 1:
                    reshaped_array[row, col] = encoding_rule_reversed.get(reshaped_array[row, col][2:4], reshaped_array[row, col][2:4])
                elif col % 4 == 2:
                    reshaped_array[row, col] = encoding_rule_reversed.get(reshaped_array[row, col][4:6], reshaped_array[row, col][4:6])
                elif col % 4 == 3:
                    reshaped_array[row, col] = encoding_rule_reversed.get(reshaped_array[row, col][6:], reshaped_array[row, col][6:])
        rgb.append(reshaped_array)
        #print('------')
        #print(reshaped_array)

    rgb_image_array = np.stack((rgb[0], rgb[1], rgb[2]), axis=-1)
    return rgb_image_array

def decode(img, number):
    encoding_rule = rules[number-1]

    # Iterate over each row and modify elements based on column index
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            img[row, col, 0] = encoding_rule.get(img[row, col, 0], img[row, col, 0]) 
            img[row, col, 1] = encoding_rule.get(img[row, col, 1], img[row, col, 1]) 
            img[row, col, 2] = encoding_rule.get(img[row, col, 2], img[row, col, 2]) 
                       
    rgb=[]
    for i in range(3):
        # Flatten the original array
        flattened_array = np.concatenate(img[:,:,i])

        # combine into 8 bit binary
        result_array = np.core.defchararray.add(flattened_array[::4], np.core.defchararray.add(flattened_array[1::4], np.core.defchararray.add(flattened_array[2::4], flattened_array[3::4])))

        # Convert each element to decimal
        decimal_array = np.array([int(binary, 2) for binary in result_array])
        
        # Reshape the repeated array to the desired shape (4x24)
        reshaped_array = decimal_array.reshape((512, 512))
        
        reshaped_array = reshaped_array.astype(np.uint8)
        #print(type(reshaped_array[0,1]))
        #print(reshaped_array)
        #print("----------")
        rgb.append(reshaped_array)

    rgb_image_array = np.stack((rgb[0], rgb[1], rgb[2]), axis=-1)    
    # Create a new image from the result array
    rgb_image = Image.fromarray(rgb_image_array, "RGB")

    # Save or display the reconstructed image
    # rgb_image.save("decode.jpg")
    
    
    return rgb_image


def complementary(img,log_map):    
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            if log_map[row,col] == 1:
                img[row, col, 0] = comp.get(img[row,col,0], img[row][col][0])
                img[row, col, 1] = comp.get(img[row,col,1], img[row][col][1])
                img[row, col, 2] = comp.get(img[row,col,2], img[row][col][2])
    #print(img)
    #print("------")
    return img