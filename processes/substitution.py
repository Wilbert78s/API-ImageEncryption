from PIL import Image # manipulate
from IPython.display import display # show image
import numpy as np # store array

s_box_1 = [
    105, 	197, 	63, 	16, 	136, 	75, 	70, 	74, 	220, 	96, 	100, 	125, 	167, 	98, 	108, 	148, 	
    242, 	5, 	254, 	93, 	13, 	78, 	253, 	45, 	144, 	12, 	35, 	196, 	226, 	179, 	230, 	44, 	
    123, 	204, 	15, 	41, 	176, 	0, 	165, 	64, 	11, 	217, 	163, 	59, 	56, 	62, 	134, 	140, 	
    235, 	250, 	49, 	77, 	131, 	252, 	239, 	157, 	244, 	214, 	129, 	248, 	177, 	113, 	10, 	152, 	
    103, 	231, 	51, 	130, 	139, 	32, 	73, 	7, 	219, 	33, 	200, 	156, 	146, 	192, 	232, 	191, 	233, 	
    202, 	187, 	23, 	241, 	246, 	216, 	158, 	31, 	161, 	17, 	94, 	53, 	9, 	206, 	117, 	249, 	89, 	
    127, 	24, 	195, 	46, 	43, 	162, 	80, 	6, 	48, 	209, 	54, 	119, 	149, 	65, 	92, 	102, 	212, 	
    135, 	36, 	203, 	28, 	126, 	27, 	132, 	210, 	172, 	85, 	145, 	22, 	224, 	34, 	188, 	50, 	25, 	
    67, 	225, 	88, 	182, 	84, 	81, 	69, 	240, 	228, 	104, 	143, 	72, 	8, 	86, 	60, 	3, 	171, 	205, 	
    238, 	55, 	61, 	245, 	79, 	83, 	222, 	58, 	147, 	142, 	121, 	37, 	124, 	4, 	87, 	183, 	1, 	199, 	
    243, 	166, 	180, 	118, 	114, 	91, 	29, 	184, 	169, 	189, 	110, 	101, 	47, 	170, 	251, 	40, 	186, 	
    18, 	97, 	229, 	155, 	174, 	236, 	153, 	247, 	150, 	106, 	237, 	168, 	193, 	66, 	2, 	112, 	215, 	14, 	
    120, 	201, 	21, 	213, 	38, 	95, 	52, 	198, 	57, 	109, 	208, 	178, 	255, 	218, 	211, 	30, 	227, 	
    190, 	76, 	90, 	82, 	173, 	99, 	42, 	39, 	185, 	194, 	159, 	111, 	138, 	137, 	116, 	181, 	141, 	
    154, 	160, 	175, 	115, 	68, 	26, 	122, 	20, 	221, 	164, 	71, 	107, 	207, 	234, 	128, 	133, 	151, 	
    223, 	19, 
    ]

s_box_2 = [
    113, 	197, 	63, 	8, 	144, 	83, 	70, 	82, 	220, 	96, 	100, 	125, 	167, 	98, 	116, 	140, 	234, 	5, 	
    254, 	93, 	21, 	86, 	253, 	53, 	136, 	20, 	35, 	196, 	226, 	171, 	230, 	52, 	123, 	212, 	23, 	
    49, 	168, 	0, 	165, 	64, 	19, 	217, 	163, 	59, 	56, 	62, 	134, 	148, 	243, 	250, 	41, 	85, 	131, 	
    252, 	247, 	157, 	236, 	206, 	129, 	248, 	169, 	105, 	18, 	152, 	103, 	231, 	43, 	130, 	147, 	32, 	
    81, 	7, 	219, 	33, 	208, 	156, 	138, 	192, 	240, 	191, 	241, 	210, 	187, 	15, 	233, 	238, 	216, 	158, 	
    31, 	161, 	9, 	94, 	45, 	17, 	214, 	109, 	249, 	89, 	127, 	24, 	195, 	54, 	51, 	162, 	72, 	6, 	
    40, 	201, 	46, 	111, 	141, 	65, 	92, 	102, 	204, 	135, 	36, 	211, 	28, 	126, 	27, 	132, 	202, 	
    180, 	77, 	137, 	14, 	224, 	34, 	188, 	42, 	25, 	67, 	225, 	88, 	174, 	76, 	73, 	69, 	232, 	
    228, 	112, 	151, 	80, 	16, 	78, 	60, 	3, 	179, 	213, 	246, 	47, 	61, 	237, 	87, 	75, 	222, 	58, 	
    139, 	150, 	121, 	37, 	124, 	4, 	79, 	175, 	1, 	199, 	235, 	166, 	172, 	110, 	106, 	91, 	29, 	184, 	177, 	
    189, 	118, 	101, 	55, 	178, 	251, 	48, 	186, 	10, 	97, 	229, 	155, 	182, 	244, 	153, 	239, 	142, 	114, 	
    245, 	176, 	193, 	66, 	2, 	104, 	207, 	22, 	120, 	209, 	13, 	205, 	38, 	95, 	44, 	198, 	57, 	117, 	200, 	
    170, 	255, 	218, 	203, 	30, 	227, 	190, 	84, 	90, 	74, 	181, 	99, 	50, 	39, 	185, 	194, 	159, 	119, 	146, 	
    145, 	108, 	173, 	149, 	154, 	160, 	183, 	107, 	68, 	26, 	122, 	12, 	221, 	164, 	71, 	115, 	215, 	242, 	128, 	
    133, 	143, 	223, 	11, 
]

s_box_3 = [
    105, 	195, 	63, 	16, 	136, 	77, 	70, 	76, 	218, 	96, 	98, 	123, 	167, 	100, 	106, 	146, 	244, 	
    3, 	254, 	91, 	11, 	78, 	251, 	43, 	144, 	10, 	37, 	194, 	228, 	181, 	230, 	42, 	125, 	202, 	15, 	
    41, 	176, 	0, 	163, 	64, 	13, 	217, 	165, 	61, 	56, 	62, 	134, 	138, 	237, 	252, 	49, 	75, 	133, 	
    250, 	239, 	155, 	242, 	214, 	129, 	248, 	177, 	113, 	12, 	152, 	103, 	231, 	53, 	132, 	141, 	32, 	
    73, 	7, 	221, 	33, 	200, 	154, 	148, 	192, 	232, 	191, 	233, 	204, 	189, 	23, 	241, 	246, 	216, 	158, 	
    31, 	161, 	17, 	94, 	51, 	9, 	206, 	115, 	249, 	89, 	127, 	24, 	197, 	46, 	45, 	164, 	80, 	6, 	
    48, 	209, 	54, 	119, 	147, 	65, 	90, 	102, 	210, 	135, 	34, 	205, 	26, 	126, 	29, 	130, 	212, 	
    170, 	83, 	145, 	22, 	224, 	36, 	186, 	52, 	25, 	69, 	225, 	88, 	182, 	82, 	81, 	67, 	240, 	
    226, 	104, 	143, 	72, 	8, 	86, 	58, 	5, 	173, 	203, 	238, 	55, 	59, 	243, 	79, 	85, 	222, 	60, 	
    149, 	142, 	121, 	35, 	122, 	2, 	87, 	183, 	1, 	199, 	245, 	166, 	178, 	118, 	116, 	93, 	27, 	184, 	
    169, 	187, 	110, 	99, 	47, 	172, 	253, 	40, 	188, 	20, 	97, 	227, 	157, 	174, 	234, 	153, 	247, 	
    150, 	108, 	235, 	168, 	193, 	68, 	4, 	112, 	215, 	14, 	120, 	201, 	19, 	211, 	38, 	95, 	50, 	198, 	
    57, 	107, 	208, 	180, 	255, 	220, 	213, 	30, 	229, 	190, 	74, 	92, 	84, 	171, 	101, 	44, 	39, 	
    185, 	196, 	159, 	111, 	140, 	137, 	114, 	179, 	139, 	156, 	160, 	175, 	117, 	66, 	28, 	124, 	18, 	
    219, 	162, 	71, 	109, 	207, 	236, 	128, 	131, 	151, 	223, 	21, 
]

s_box_4 = [
    120, 	46, 	245, 	1, 	66, 	232, 	140, 	200, 	79, 	24, 	28, 	125, 	182, 	152, 	92, 	7, 	155, 	36, 	
    223, 	109, 	100, 	204, 	127, 	116, 	3, 	68, 	176, 	14, 	154, 	179, 	158, 	84, 	249, 	78, 	228, 	
    112, 	19, 	0, 	54, 	8, 	224, 	107, 	178, 	241, 	81, 	213, 	134, 	70, 	250, 	219, 	49, 	108, 	162, 	
    95, 	254, 	103, 	31, 	143, 	34, 	91, 	51, 	57, 	192, 	67, 	188, 	190, 	177, 	130, 	226, 	16, 	
    104, 	164, 	235, 	48, 	74, 	71, 	131, 	10, 	90, 	247, 	122, 	202, 	243, 	165, 	59, 	159, 	75, 	
    199, 	229, 	50, 	33, 	205, 	53, 	96, 	206, 	61, 	123, 	105, 	253, 	65, 	170, 	212, 	240, 	146, 	
    9, 	132, 	17, 	43, 	149, 	189, 	39, 	40, 	77, 	156, 	15, 	166, 	20, 	234, 	69, 	221, 	225, 	6, 	
    139, 	86, 	45, 	35, 	133, 	26, 	144, 	87, 	145, 	97, 	168, 	58, 	73, 	151, 	13, 	41, 	44, 	
    27, 	30, 	88, 	230, 	72, 	64, 	141, 	85, 	160, 	242, 	110, 	222, 	181, 	117, 	63, 	236, 	169, 	
    207, 	209, 	163, 	198, 	121, 	52, 	93, 	4, 	173, 	183, 	32, 	174, 	187, 	150, 	23, 	157, 	153, 	233, 	
    101, 	83, 	114, 	119, 	220, 	60, 	244, 	210, 	251, 	80, 	211, 	129, 	56, 	62, 	227, 	214, 	94, 	
    99, 	191, 	135, 	216, 	126, 	82, 	42, 	136, 	128, 	25, 	175, 	196, 	89, 	106, 	37, 	47, 	148, 	
    237, 	21, 	142, 	113, 	124, 	11, 	147, 	255, 	203, 	171, 	197, 	186, 	215, 	76, 	201, 	137, 	118, 	
    184, 	208, 	180, 	115, 	138, 	231, 	252, 	194, 	98, 	29, 	55, 	102, 	195, 	18, 	246, 	185, 	12, 	
    193, 	217, 	5, 	111, 	22, 	172, 	248, 	238, 	218, 	2, 	38, 	167, 	239, 	161, 
]
# Create an array filled with values from the S-box
s_box_array_1 = bytearray(s_box_1)
s_box_array_2 = bytearray(s_box_2)
s_box_array_3 = bytearray(s_box_3)
s_box_array_4 = bytearray(s_box_4)
# Combine the S-box arrays into a list
s_box_arrays = [s_box_array_1, s_box_array_2, s_box_array_3, s_box_array_4]

def sub_Sbox(idx, img):
    # Select the appropriate S-box array based on the index    
    s_box_array = s_box_arrays[idx]
    
    # Substitute image pixels with S-box values
    substituted_image_array = np.zeros_like(img, dtype=np.uint8)
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            substituted_image_array[i, j,0] = s_box_array[img[i, j,0]]
            substituted_image_array[i, j,1] = s_box_array[img[i, j,1]]
            substituted_image_array[i, j,2] = s_box_array[img[i, j,2]]
    
    return substituted_image_array
    

def sub_Sbox_reverse(idx, img):  
     # Select the appropriate S-box array based on the index
    s_box_array = s_box_arrays[idx]

    # Reverse the substitution using the S-box
    reversed_image_array = np.zeros_like(img, dtype=np.uint8)
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):    
            #reversed_image_array[0,0]-=1
            # Convert the int32 value to uint8
            find = img[i,j,0].astype(np.uint8)        
            reversed_image_array[i, j,0] = s_box_array.index(find)

            find = img[i,j,1].astype(np.uint8)        
            reversed_image_array[i, j,1] = s_box_array.index(find)

            find = img[i,j,2].astype(np.uint8)        
            reversed_image_array[i, j,2] = s_box_array.index(find)
    return reversed_image_array


def substitution(img, reversed_sub):
    # Convert the image to a NumPy array for easier manipulation
    image_array = np.array(img)

    # Dimensions of the original image
    original_height, original_width = image_array.shape[:2]

    # Dimensions of the smaller patches
    patch_size = 256
    num_patches_row = original_height // patch_size
    num_patches_col = original_width // patch_size

    # Initialize a list to store the smaller patches
    small_patches = []

    # Extract smaller patches
    for i in range(num_patches_row):
        for j in range(num_patches_col):
            start_row = i * patch_size
            end_row = (i + 1) * patch_size
            start_col = j * patch_size
            end_col = (j + 1) * patch_size

            patch = image_array[start_row:end_row, start_col:end_col,:]
            small_patches.append(patch)
    
    '''
        for idx, patch in enumerate(small_patches):
            patch_image = Image.fromarray(patch, "L")
            patch_image.save(f"patch_{idx + 1}.jpg")  # Save each patch to a separate file
    '''
 
    if(reversed_sub == False):
        sub_img = np.array([sub_Sbox(idx, patch) for idx, patch in enumerate(small_patches)])
    else:
        sub_img = np.array([sub_Sbox_reverse(idx, patch) for idx, patch in enumerate(small_patches)])
    
    # Dimensions of the smaller patches
    patch_size = 256
    num_patches_row = 512 // patch_size
    num_patches_col = 512 // patch_size

    # Initialize an empty array for the reconstructed image
    reconstructed_image = np.zeros_like(img, dtype=np.uint8)

    # Combine the swapped patches into the reconstructed image
    patch_index = 0
    for i in range(num_patches_row):
        for j in range(num_patches_col):
            start_row = i * patch_size
            end_row = (i + 1) * patch_size
            start_col = j * patch_size
            end_col = (j + 1) * patch_size

            # Get the swapped patch and place it in the reconstructed image
            reconstructed_image[start_row:end_row, start_col:end_col,:] = sub_img[patch_index]

            # Move to the next swapped patch
            patch_index += 1

    #print(reconstructed_image)
    #print("--------------------")
    # Convert the reconstructed image array to a PIL Image
    reconstructed_image = Image.fromarray(reconstructed_image, "RGB")

    # Save or display the reconstructed image
    # reconstructed_image.save("substitusi.jpg")
    
    return reconstructed_image
