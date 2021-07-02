# PySteganography 
#### A simple toolset for image encoding and decoding using steganography.

## Features

- Image encoding and decoding
- Exporting encoded images


Installation: ```pip install pysteganography```

## Examples 
Encode an image: <br>
```from pysteganography.stegano import encode  ``` <br>
```encoded_image = encode(img_url, string_to_encode)``` <br>
Numpy image arrays, determined from reading an image through OpenCV or PIL, can also be used: <br>
```encoded_image = encode(img, string_to_encode)``` <br>
The encoded image can also be saved locally by modifying the optional parameters: <br>
```encoded_image = encode(img_url, string_to_encode, True, encoded_image_path)``` <br>

Decode an image: <br>
```from pysteganography.stegano import decode  ``` <br>
```decoded = decode(img_url)``` <br>
Numpy image arrays, determined from reading an image through OpenCV or PIL, can also be decoded: <br>
```decoded = decode(img)```  <br>

Get the maximum number of bytes in a message that can be encrypted for a given image:<br>
```from pysteganography.stegano import get_max_bytes  ``` <br>
```max_bytes = get_max_bytes(img_url)``` <br>
Numpy image arrays, determined from reading an image through OpenCV or PIL, can also be used in the same manner: <br>
```max_bytes = get_max_bytes(img)``` <br>

