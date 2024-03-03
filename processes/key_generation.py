import hashlib # hashing
import numpy as np # store array

def xor_binary_strings(str1, str2):
    result = ''
    for bit1, bit2 in zip(str1, str2):
        result += '1' if bit1 != bit2 else '0'
    return result

def logistic_map(x,a,b):
    result = (a*x*(1-x)+(4-a)*np.cos(b*np.arccos(x))/4)%1
    return result

def sine_map(x,a,b):
    result = (a*np.sin(np.pi*x)+(4-a)*np.cos(b*np.arccos(x))/4)%1
    return result

def sha3_keccak(img):
    # Open the image file in binary mode
    binary_data = img.tobytes()

    # Calculate the Keccak-256 hash
    keccak256_hash = hashlib.sha3_256(binary_data).hexdigest()
    binary_string = format(int(keccak256_hash, 16), '0256b')
    return binary_string

def generate_map(a,b,x0, a0, x1, a1):
    # Create a 2D array with size [512][4*512] filled with zeros
    array_size_log = (512, 4 * 512)
    array_size_sine = (512, 512)
    log_map_res = np.zeros(array_size_log)
    sine_map_res = np.zeros(array_size_sine)


    #create log array
    for i in range(a):
        x0 = logistic_map(x0,a0,b)  # Replace with your actual math operation

    for i in range(4 * 512):
        # Iterate over columns (inner loop)
        for j in range(512):
            # You can perform operations or assign values within the loop
            x0 = logistic_map(x0,a0,b)
            temp=0
            if (x0>0.5) :
                temp=1
            log_map_res[j, i] = temp
    # Reshape the repeated array to the desired shape (512, 4*512)
    log_map_res_2d = log_map_res.reshape((512, 4*512))


    #create sine array
    for i in range(a):
        x1 = sine_map(x1,a1,b)  # Replace with your actual math operation

    for i in range(512):
        # Iterate over columns (inner loop)
        for j in range(512):
            # You can perform operations or assign values within the loop
            x1 = sine_map(x1,a1,b)
            sine_map_res[j,i] = x1
    # Reshape the repeated array to the desired shape (512, 512)
    sine_map_0_255 = np.floor((sine_map_res * 1e15) % 256)  # 0-255 mapping
    sine_map_res_2d = sine_map_0_255.reshape((512, 512))
    return {'log_map' : log_map_res_2d,
           'sine_map': sine_map_res_2d}

def secret_key(sha3, x0, a0, x1, a1):
    # seperate 256 bit into 32 arrays
    array_size = 8
    k = [sha3[i:i+array_size] for i in range(0, len(sha3), array_size)]
    
    '''
    for i, array in enumerate(k):
        print(f"Array {i + 1}: {array}")
    '''

    # perform XOR k 9-16
    result_xor_9_16 = k[8]
    for binary_str in k[9:16]:  # Adjust the range to select the first 8 elements
        result_xor_9_16 = xor_binary_strings(result_xor_9_16, binary_str)
    decimal_number_9_16 = int(result_xor_9_16, 2)
    
    # perform XOR k 1-8
    result_xor_1_8 = k[0]
    for binary_str in k[1:8]:  # Adjust the range to select the first 8 elements
        result_xor_1_8 = xor_binary_strings(result_xor_1_8, binary_str)
    decimal_number_1_8 = int(result_xor_1_8, 2)

    # perform XOR k 1-32
    result_xor_1_32 = k[0]
    for binary_str in k[1:32]:  # Adjust the range to select the first 8 elements
        result_xor_1_32 = xor_binary_strings(result_xor_1_32, binary_str)
    decimal_number_1_32 = int(result_xor_1_32, 2)

    # convert k to decimal, sum all, and modulo 256
    sumOfK = sum(int(binary_str, 2) for binary_str in k) % 256

    '''
    print(decimal_number_9_16)
    print(decimal_number_1_8)
    print(decimal_number_1_32)
    print(sumOfK)
    '''

    res=[]
    
    for i in range(2):
        x0=(x0+decimal_number_9_16/128)/3
        a0=(a0+decimal_number_1_8/32)/3
        x1=(x1+decimal_number_1_32/128)/3
        a1=(a1+sumOfK/32)/3
        temp={'x0':x0,
            'a0':a0,
            'x1':x1,
            'a1':a1}
        res.append(temp)

    return res
