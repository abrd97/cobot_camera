import cv2

def resize_image(input_path, output_path, size):
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    resized_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    cv2.imwrite(output_path, resized_img)

if __name__ == "__main__":
    input_image_path = 'gt/gt_2024-09-04_14-22-54_1.png'
    output_image_path = 'gt/resized_image.png'
    
    resize_image(input_image_path, output_image_path, (224, 224))
