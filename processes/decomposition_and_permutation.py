from PIL import Image # manipulate
from IPython.display import display # show image
import numpy as np # store array

def decomposition_and_permutation(original_image,p1,reversed_image):
    # Convert the image to a NumPy array for easier manipulation
    image_array = np.array(original_image)

    # Dimensions of the original image
    original_height, original_width = image_array.shape[:2]

    # Dimensions of the smaller patches
    patch_size = 64
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
    
    # Save or process the smaller patches as needed
    '''for idx, patch in enumerate(small_patches):
        patch_image = Image.fromarray(patch, "RGBA")
        patch_image.save(f"patch_{idx + 1}.png")  # Save each patch to a separate file
    '''

    swapped_patches=np.empty_like(small_patches)
    b=np.zeros(64)
    for i in range(64):
        b[i]=(p1*(i+1))%64
        if(reversed_image == False):
            swapped_patches[i]=small_patches[int(b[i])]
        else:
            swapped_patches[int(b[i])]=small_patches[i]

    '''
    for idx, patch in enumerate(swapped_patches):
        patch_image = Image.fromarray(patch, "L")
        patch_image.save(f"patch_{idx + 1}.jpg")  # Save each patch to a separate file
    '''
    
    # Dimensions of the smaller patches
    patch_size = 64
    num_patches_row = original_height // patch_size
    num_patches_col = original_width // patch_size

    # Initialize an empty array for the reconstructed image
    reconstructed_image = np.empty_like(image_array, dtype=np.uint8)

    # Combine the swapped patches into the reconstructed image
    patch_index = 0
    for i in range(num_patches_row):
        for j in range(num_patches_col):
            start_row = i * patch_size
            end_row = (i + 1) * patch_size
            start_col = j * patch_size
            end_col = (j + 1) * patch_size

            # Get the swapped patch and place it in the reconstructed image
            reconstructed_image[start_row:end_row, start_col:end_col,:] = swapped_patches[patch_index]

            # Move to the next swapped patch
            patch_index += 1

    
    # Convert the reconstructed image array to a PIL Image
    reconstructed_image = Image.fromarray(reconstructed_image, "RGB")
    #reconstructed_image.show(title="Grayscale Image")
    # Save or display the reconstructed image
    # reconstructed_image.save("permutasi.jpg")
    
    return reconstructed_image
