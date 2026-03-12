import google.generativeai as genai
from PIL import Image

def get_text_from_image_gemini(image_path, api_key):
    """
    Extracts text from an image using the Gemini API.

    Args:
        image_path: Path to the image file.
        api_key: Your Gemini API key.

    Returns:
        The extracted text as a string, or None if there was an error.
    """
    try:
        # Configure the Gemini API
        genai.configure(api_key=api_key)

        # Load the Gemini Pro Vision model
        model = genai.GenerativeModel('gemini-2.5-flash')

        # Load the image using PIL
        img = Image.open(image_path)

        # Prepare the prompt
        prompt = "What text is in the captcha image?"  # Customize this prompt as needed

        # Generate content using the Gemini Pro Vision model
        response = model.generate_content([prompt, img])

        # Check for errors
        if response.prompt_feedback and response.prompt_feedback.block_reason:
            print(f"Error: Prompt was blocked. Reason: {response.prompt_feedback.block_reason}")
            return None

        # Extract the text from the response
        extracted_text = response.text.strip()

        return extracted_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example Usage (replace with your actual image path and API key)
image_path = "captcha-img1.jpg"  # Replace with the path to your image
api_key = "AIzaSyD9iMkzVlxqiq7_YQoTFtvSipxiV2kMFk0"  # Replace with your actual API key

extracted_text = get_text_from_image_gemini(image_path, api_key)

if extracted_text:
    print("Extracted Text:", extracted_text)
else:
    print("Text extraction failed.")