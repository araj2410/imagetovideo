import cv2
import os

def create_video_from_images(image_folder, output_video_path, fps=30):
    # Get list of all image files in the folder
    image_files = sorted(os.listdir(image_folder))

    # Check if folder is empty
    if not image_files:
        print("No images found in the directory.")
        return

    # Filter out non-image files (optional: adjust based on your use case)
    image_files = [f for f in image_files if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'tiff'))]

    # If no images were found after filtering
    if not image_files:
        print("No valid image files found in the directory.")
        return

    # Read the first image to get the dimensions for the video
    first_image = cv2.imread(os.path.join(image_folder, image_files[0]))
    if first_image is None:
        print(f"Error reading the first image: {image_files[0]}")
        return

    # Get the dimensions (height, width) of the first image
    height, width, _ = first_image.shape

    # Create a VideoWriter object to write the video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' codec for .mp4 video
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Loop through all images and add them to the video
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)

        # Check if the image was loaded correctly
        if image is None:
            print(f"Error reading image: {image_path}")
            continue

        # Resize image if necessary (optional)
        image = cv2.resize(image, (width, height))  # Uncomment to resize all images to the first image size

        # Write the image to the video file
        video_writer.write(image)

    # Release the video writer and finish
    video_writer.release()
    print(f"Video successfully saved to: {output_video_path}")

# Example usage
image_folder = '/Users/rajeev/Desktop/TempVideos'  # Update this path
output_video_path = '/Users/rajeev/Desktop/TempVideos/output_video.mp4'  # Update the desired output path and filename
create_video_from_images(image_folder, output_video_path, fps=1)
