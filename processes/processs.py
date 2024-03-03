from PIL import Image # manipulate
def padding(img):
    # Create a new blank image with the desired size (512x512)
    new_img = Image.new("RGB", (512, 512), color="white")
    # Paste the original image onto the new image with padding
    new_img.paste(img, (0,0))

    # display the new image
    """ new_img.show() """
    return new_img

def preProcessing(img):
    if(img.width!=512 and img.height!=512):
        img = padding(img)
        
    # Print the size
    # print("Image size:", img.size)
    return img

def postProcessing(img, width, height):
    unpadded_img = img.crop((0,0, width, height))
    """ unpadded_img.show() """
    return unpadded_img