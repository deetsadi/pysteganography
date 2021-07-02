import cv2
import numpy as np

def to_binary(data):
    #Convert 'data' to binary and then to a string
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data ])
    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")

def get_max_bytes(image_name):
    if type(image_name) == str:
      image = cv2.imread(image_name)
    else:
      image = image_name.copy()
    # maximum bytes to encode
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    return n_bytes

def encode(image_name, secret_data, save=False, output_image_name=""):
    # read the image
    if type(image_name) == str:
      image = cv2.imread(image_name)
    else:
      image = image_name.copy()
    # maximum bytes to encode
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    if len(secret_data) > n_bytes:
        raise ValueError("[!] Insufficient bytes, need bigger image or less data.")
    # add stopping criteria
    secret_data += "====="
    data_index = 0
    # convert data to binary
    binary_secret_data = to_binary(secret_data)
    # size of data to hide
    data_len = len(binary_secret_data)
    # least significant bit (LSB) modification
    for row in image:
        for pixel in row:
            # convert RGB values to binary format
            r, g, b = to_binary(pixel)
            # modify the least significant bit only if there is still data to store
            if data_index < data_len:
                # least significant red pixel bit
                pixel[0] = int(r[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # least significant green pixel bit
                pixel[1] = int(g[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # least significant blue pixel bit
                pixel[2] = int(b[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            # if data is encoded, just break out of the loop
            if data_index >= data_len:
                break
    if save:
      cv2.imwrite(output_image_name, image)

    return image


def decode(image_name):
    # read the image
    if type(image_name) == str:
      image = cv2.imread(image_name)
    else:
      image = image_name.copy()
    binary_data = ""
    for row in image:
        for pixel in row:
            r, g, b = to_binary(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    # split by 8-bits
    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
    # convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "=====":
            break
    return decoded_data[:-5]
