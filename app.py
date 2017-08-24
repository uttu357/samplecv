import cv2
import cvfy

app = cvfy.register('nongh:0.0.0.0:9290704:8000:9001:0.0.0.0:8000')

@cvfy.crossdomain
@app.listen()
def grayscale():

    all_image_paths = cvfy.getImageArray()
#    all_texts = cvfy.getTextArray()
    image_1_path = all_image_paths[0]
    image_2_path = all_image_paths[1]
#    text_1 = all_texts[0]
#    text_2 = all_texts[1]
        
    cvfy.sendTextArrayToTerminal(['Loading Image...'])
    image_1 = cv2.imread(image_1_path)
    image_2 = cv2.imread(image_2_path)

    cvfy.sendTextArrayToTerminal(['Image Loaded successfully']);

    gray_image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
    gray_image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)

    cvfy.sendTextArrayToTerminal(['Converting RGB Image to Grayscale']);

#    cvfy.sendTextArray(["sucess", "falure"])
    cvfy.sendImageArray([gray_image_1, gray_image_2], mode = 'numpy_array')

    cvfy.sendTextArrayToTerminal([
        'Operation completed successfully',
        image_1_path,
        image_2_path
        ]);

    return 'OK'

app.run()
