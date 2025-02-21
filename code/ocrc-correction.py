import os
import json
import openai
from openai import chat
import argparse

## GET YOUR API KEY
################################################################
config_file = "keys.json"

# Check if config.json exists
if not os.path.exists(config_file):
    print(f"Error: '{config_file}' not found. Please create the file and add your OpenAI API key.")
    exit(1)  # Exit the script with an error code

# Load API key from config.json
try:
    with open(config_file, "r") as f:
        config = json.load(f)
except json.JSONDecodeError:
    print(f"Error: '{config_file}' is not a valid JSON file. Please check its format.")
    exit(1)

# Retrieve API key
api_key = config.get("OPENAI_API_KEY")

if not api_key:
    print(f"Error: API key not found in '{config_file}'. Ensure it contains: {{\"OPENAI_API_KEY\": \"your-key-here\"}}")
    exit(1)

# Set OpenAI API key
openai.api_key = api_key

# Test API call
# try:
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "system", "content": "Say hello!"}]
#     )
#     print(response["choices"][0]["message"]["content"])
# except Exception as e:
#     print("Error: Unable to connect to OpenAI API. Please check your API key and internet connection.")
#     print(f"Details: {e}")

def split_into_chunks(text, max_tokens=1500):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        current_length += len(word) + 1
        if current_length > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word) + 1
        else:
            current_chunk.append(word)
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def correct_text_with_gpt(text, ln):
    system_prompt = "You are a helpful assistant that corrects OCR text for spelling, grammar, and minor parsing errors."
    user_prompt = f"Please correct any OCR errors (in {ln}) in the following text:\n\n{text}"

    response = chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.0,
    )

    corrected_text = response.choices[0].message.content
    return corrected_text

def correct_large_text(text, ln):
    chunks = split_into_chunks(text, max_tokens=1500)
    corrected_chunks = []
    for chunk in chunks:
        corrected_text = correct_text_with_gpt(chunk, ln)
        corrected_chunks.append(corrected_text)
    return "\n".join(corrected_chunks)


def main():
    parser = argparse.ArgumentParser(
        description="Correct text in a given language."
    )
    # Define command-line arguments:
    parser.add_argument(
        "--input", 
        type=str, 
        required=True, 
        help="Path to the txt file with the text."
    )
    parser.add_argument(
        "--ln", 
        type=str, 
        default="English", 
        help="Text language"
    )
    parser.add_argument(
        "--output", 
        type=str, 
        default="output-corrected.txt", 
        help="Output file path and name for corrected txt"
    )

    args = parser.parse_args()
    input_text = args.input
    language = args.ln
    output_file = args.output

    try:
        with open(input_text, "r", encoding="utf-8") as file:
            raw_text = file.read()
            clean_text = correct_large_text(raw_text, "Italian")
            try:
                with open(output_file, "w", encoding="utf-8") as file:
                    file.write(clean_text)
                    print(f"Text successfully saved to '{output_file}'.")
            except Exception as e:
                print(f"Error: Could not write to the file. Details: {e}")
    except FileNotFoundError:
        print(f"Error: The file '{input_text}' was not found.")
    except Exception as e:
        print(f"Error: An unexpected issue occurred: {e}")


if __name__ == "__main__":
    main()