from PIL import Image # manipulate
from IPython.display import display # show image

from .key_generation import generate_map, secret_key, sha3_keccak
from .decomposition_and_permutation import decomposition_and_permutation
from .substitution import substitution
from .DNA import encode, decode, complementary
from .bitwise_XOR import bitwise_XOR
from .processs import preProcessing, postProcessing

def convert_to_jpg(img):
    img = img.convert("RGB")
    return img

def encrypt(plain_img, a, b, x0, a0, x1, a1, prime, k1, k2):
    height = plain_img.height
    width = plain_img.width
    plain_img = preProcessing(plain_img)
    plain_img = convert_to_jpg(plain_img)
    hashing = sha3_keccak(plain_img)
    key = secret_key(hashing, x0, a0, x1, a1)
    for i in range(2):
        map = generate_map(a, b, key[i]['x0'], key[i]['a0'], key[i]['x1'], key[i]['a1'])
        p1 = decomposition_and_permutation(plain_img, prime[i], False) # img
        p2 = substitution(p1, False) #img
        p3 = encode(p2, k1) # array
        p4 = complementary(p3, map['log_map']) # array
        p5 = decode(p4, k2) # img
        p6 = bitwise_XOR(p5, map['sine_map']) # img
        plain_img = p6
    res={
        'height':height,
        'width':width,
        'hash':hashing,
        'image':p6,
    }
    return res

def decrypt(plain_img, a, b, x0, a0, x1, a1, prime, k1, k2, hashing, width, height):
    plain_img = convert_to_jpg(plain_img)

    # decrypt
    key = secret_key(hashing, x0, a0, x1, a1)
    for i in range(1,-1,-1):
        map = generate_map(a, b, key[i]['x0'], key[i]['a0'], key[i]['x1'], key[i]['a1'])
        d1 = bitwise_XOR(plain_img, map['sine_map'])
        d2 = encode(d1, k2)
        d3 = complementary(d2, map['log_map'])
        d4 = decode(d3, k1)
        d5 = substitution(d4, True)
        d6 = decomposition_and_permutation(d5, prime[i], True)
        plain_img = d6
    d6 = postProcessing(d6, width, height)
    
    res={
        'height':height,
        'width':width,
        'hash':hashing,
        'image':d6
    }
    return res