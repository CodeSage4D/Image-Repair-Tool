from PIL import Image, ImageOps
import os

def remove_image_background(image):
    """
    Remove the background from the image using Pillow's ImageOps.

    Args:
        image (PIL.Image): Input image.

    Returns:
        PIL.Image: Image with the background removed.
    """
    # Convert image to RGBA mode if it's not already
    if image.mode != "RGBA":
        image = image.convert("RGBA")

    # Split the image into RGB and alpha channels
    r, g, b, a = image.split()

    # Invert the RGB channels
    r = ImageOps.invert(r)
    g = ImageOps.invert(g)
    b = ImageOps.invert(b)

    # Recombine the RGB channels with the original alpha channel
    return Image.merge("RGBA", (r, g, b, a))


def process_single_image(input_image_path):
    """
    Process a single image: remove background and save with same format and size.

    Args:
        input_image_path (str): Path to the input image.
    """
    # Open the input image
    input_image = Image.open(input_image_path)

    # Remove background
    processed_image = remove_image_background(input_image)

    # Save the processed image with the same format and size
    output_path = os.path.splitext(input_image_path)[0] + "_processed" + os.path.splitext(input_image_path)[1]
    processed_image.save(output_path)
    print(f"Processed image saved at: {output_path}")

def process_images_in_folder(folder_path):
    """
    Process all images in a folder: remove background and save with same format and size.

    Args:
        folder_path (str): Path to the folder containing images.
    """
    # List all files in the folder
    files = os.listdir(folder_path)

    # Process each image file
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            process_single_image(file_path)

def main():
    # Ask the user whether to process a single image or a folder
    choice = input("Enter '1' to process a single image or '2' to process images in a folder: ")

    if choice == '1':
        input_image_path = input("Enter the path to the input image: ")
        process_single_image(input_image_path)
    elif choice == '2':
        folder_path = input("Enter the path to the folder containing images: ")
        process_images_in_folder(folder_path)
    else:
        print("Invalid choice. Please enter either '1' or '2'.")

if __name__ == "__main__":
    main()
