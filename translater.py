from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

if __name__ == "__main__":
    # Example usage
    text_to_translate = input("Enter the text to translate: ")
    target_language = input("Enter the target language (e.g., fr for French): ")

    translated_text = translate_text(text_to_translate, target_language)
    
    print(f"\nOriginal Text: {text_to_translate}")
    print(f"Translated Text ({target_language}): {translated_text}")
