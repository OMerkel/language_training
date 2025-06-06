"""
This script reads out loud a language training text from a data/*.toml
in target language using the gTTS (Google Text-to-Speech) library.

Dependencies:
    - gtts: Install via `uv add gtts`
    - pygame: Install via `uv add pygame`
    - time: Standard library for time-related functions
    - tomllib: Standard library for reading TOML files
    - Optional: Standard library for optional type hinting
    - BytesIO: Standard library for handling byte streams

Usage:
    Run the script to generate and play the audio.
    The script will read a text string from a TOML file,
    convert it to speech, and play the audio using pygame.
    The script will also print the text in both source and
    target language to the console.
    The script will pause for a few seconds between each
    text-to-speech conversion to allow the user to read
    the text before it is spoken.
"""
import os
import argparse
from io import BytesIO
import tomllib
import time
from typing import Optional

from gtts import gTTS  # type: ignore
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame   # noqa, pylint: disable=wrong-import-position


def generate_audio(text: str, lang: str = 'it') -> BytesIO:
    """Generate a BytesIO object from text using gTTS.
    Args:
        text (str): The text to convert to speech.
        lang (str): The language code for the text. Default is 'it' (Italian).
    Returns:
        BytesIO: A BytesIO object containing the audio data.
    """
    # Create a gTTS object
    tts = gTTS(text=text, lang=lang)
    # Save the audio to a BytesIO object instead of a file
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes


def play_audio(audio_bytes: BytesIO) -> None:
    """Play the audio BytesIO object using pygame.
    Args:
        audio_bytes (BytesIO): The BytesIO object containing the audio data.
    Returns:
        None
    """
    # Initialize the mixer
    pygame.mixer.init()
    # Load the audio file
    pygame.mixer.music.load(audio_bytes)
    time.sleep(1)
    # Play the audio file
    pygame.mixer.music.play()
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    # Stop the mixer
    pygame.mixer.music.stop()
    pygame.mixer.quit()


def lookup_text(file: Optional[str] = None,
                lang_1: str = "de-DE",
                lang_2: str = "it-IT") -> list[dict[str, str]]:
    """Lookup text from a file.
    Args:
        file (str): The path to the file containing the text.
        lang_1 (str): The language code for the first language.
                      Default is 'de-DE'.
        lang_2 (str): The language code for the second language.
                      Default is 'it-IT'.
    Returns:
        list[dict[str, str]]: List of dict holding text in both languages.
    """
    if not file:
        return [
            {
                lang_1: "Guten Morgen! Ich habe den 67. Platz erreicht.",
                lang_2: "Buongiorno! Ho raggiunto il sessantasettesimo posto."
            },
            {
                lang_1: "Ich habe ein Buch gelesen.",
                lang_2: "Ho letto un libro."
            },
            {
                lang_1: "Ein Wasser, bitte.",
                lang_2: "Un'acqua, per favore."
            },
            {
                lang_1: "Schönen Nachmittag!",
                lang_2: "Buon pomeriggio!"
            },]
    text: list[dict[str, str]] = []
    with open(file, "rb") as f:
        data: dict[str, dict[str, str]] = tomllib.load(f)
    # Assuming the structure of the TOML file is known
    # and we want to extract specific keys
    for key in data:
        first_lang: str = data[key][lang_1]
        second_lang: str = data[key][lang_2]
        text.append({lang_1: first_lang, lang_2: second_lang})
    # with open(file, 'r', encoding='utf-8') as file:
    #     for line in file:
    #         text.append(line.strip())
    return text


def main(source_lang: str = "de-DE", target_lang: str = "it-IT",
         toml_file: str = "data/conjugation.toml") -> None:
    """Main function to execute the script.
    Args:
        source_lang (str): The source language code. Default is 'de-DE'.
        target_lang (str): The target language code. Default is 'it-IT'.
        toml_file (str): The path to the TOML file.
                         Default is 'data/conjugation.toml'.
    Returns:
        None
    """
    # Print a greeting message
    print("Hello from language-training!")

    # text = lookup_text()
    text = lookup_text(toml_file, source_lang, target_lang)
    for i in text:
        print(f"{i[source_lang]=}", end=" ")
        time.sleep(5)
        try:
            command: str = input("Press Enter to continue... ")
        except EOFError:
            print("\nEOF received, exiting.")
            return
        if command == "exit":
            return
        print(f"{i[target_lang]=}")
        time.sleep(1)
        language: str = target_lang.split("-")[0]
        audio_bytes: BytesIO = generate_audio(i[target_lang], language)
        play_audio(audio_bytes=audio_bytes)
        time.sleep(2)


def argparse_args() -> argparse.Namespace:
    """Parse command line arguments.
    Args:
        None
    Returns:
        argparse.Namespace: The parsed command line arguments.
    """
    description = "Read out loud a language training text."
    default_file = "data/conjugation.toml"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--source_lang", type=str, default="de-DE",
                        help="Source language code (default: de-DE)")
    parser.add_argument("--target_lang", type=str, default="it-IT",
                        help="Target language code (default: it-IT)")
    parser.add_argument("--toml_file", type=str, default=default_file,
                        help=f"Path to TOML file (default: {default_file})")
    args = parser.parse_args()
    return args


def validate_args(args: argparse.Namespace) -> None:
    """Validate command line arguments.
    Args:
        args (argparse.Namespace): The parsed command line arguments.
    Returns:
        None
    Raises:
        ValueError: If the TOML file does not have a .toml extension,
                    or if the source and target language codes are not
                    provided, or if they are the same, or if they are
                    unsupported.
    """
    if not args.toml_file.endswith(".toml"):
        raise ValueError("The TOML file must have a .toml extension.")
    if not args.source_lang or not args.target_lang:
        raise ValueError("Both source and target "
                         "language codes must be provided.")
    if args.source_lang == args.target_lang:
        raise ValueError("Source and target language codes must be different.")
    supported_langs = ['de-DE', 'en-US', 'fr-FR', 'es-ES', 'it-IT', 'pt-PT',
                       'ru-RU', 'ja-JP', 'zh-CN', 'ko-KR', 'nl-NL', 'sv-SE',
                       'tr-TR', 'pl-PL', 'sr-RS', 'ro-RO']
    if args.source_lang not in supported_langs:
        raise ValueError(f"Unsupported source language: {args.source_lang}."
                         f" Supported languages are: {supported_langs}")
    if args.target_lang not in supported_langs:
        raise ValueError(f"Unsupported target language: {args.target_lang}."
                         f" Supported languages are: {supported_langs}")


if __name__ == "__main__":  # pragma: no cover
    command_line_args = argparse_args()
    validate_args(command_line_args)
    main(source_lang=command_line_args.source_lang,
         target_lang=command_line_args.target_lang,
         toml_file=command_line_args.toml_file)
