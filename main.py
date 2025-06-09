import json
import time
from openai import OpenAI
import speech_recognition as sr
from util.get_media_id import get_media_deep_link_options
from util.roku_connection import scan_roku_ip, test_connection
from util.roku_commands import launch_deep_link_from_obj
from util.openai_setup import system_prompt, tools

client = OpenAI()

def recognize_speech_from_mic(recognizer, microphone, timeout=5):
    """
    Capture speech from the microphone and return the transcribed text.
    """
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            return {"success": False, "error": "Timeout", "transcription": None}

    response = {"success": True, "error": None, "transcription": None}
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response


def listen_for_wake_word(recognizer, microphone, wake_word="hey remote"):
    """
    Listen for the wake word in the background.
    Returns True if wake word is detected, False otherwise.
    """
    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=1, phrase_time_limit=3)
        
        try:
            text = recognizer.recognize_google(audio).lower()
            if wake_word.lower() in text:
                return True
        except (sr.RequestError, sr.UnknownValueError):
            pass
    except sr.WaitTimeoutError:
        pass
    
    return False


def launch_media_from_prompt(prompt: str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[system_prompt, {
            "role": "user",
            "content": prompt
        }],
        tools=tools
    )

    response_text = completion.choices[0].message.content
    if response_text:
        print(response_text)

    tool_calls = completion.choices[0].message.tool_calls

    roku_ip = scan_roku_ip()
    if not test_connection(roku_ip):
        print("Failed to connect to Roku. Check network and IP.")
        return

    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.function.name == 'launch_media':
                args = json.loads(tool_call.function.arguments)
                media_name = args.get('media_name')
                channel_name = args.get('channel_name').upper().strip()
                deep_link_options = get_media_deep_link_options(media_name)
                deep_link_data = next(filter(lambda option: option.get('channel_name').upper().strip() == channel_name,
                                             deep_link_options), None)
                if deep_link_data:
                    print(f"Launching '{media_name}' on '{channel_name}'")
                    launch_deep_link_from_obj(roku_ip, deep_link_data)


def main():
    """
    Listen in the background for wake word, then capture command.
    """
    # Initialize speech recognizer and microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    # Adjust for ambient noise once at startup
    print("Adjusting for ambient noise...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
    
    print("Background listening started. Say 'Hey, Remote' to activate...")
    print("Press Ctrl+C to exit.")
    
    try:
        while True:
            # Listen for wake word
            if listen_for_wake_word(recognizer, microphone):
                print("Wake word detected! Listening for your command...")
                
                # Listen for the actual command
                speech_result = recognize_speech_from_mic(recognizer, microphone, timeout=10)
                
                if not speech_result["success"]:
                    if speech_result["error"] == "Timeout":
                        print("Didn't hear a command. Going back to listening for wake word...")
                    else:
                        print(f"ERROR: {speech_result['error']}")
                    continue
                
                if speech_result["transcription"] is None:
                    print("Didn't catch that. Going back to listening for wake word...")
                    continue
                
                raw_text = speech_result["transcription"]
                print(f"Command heard: {raw_text}")
                
                # Process the command
                launch_media_from_prompt(raw_text)
                
                print("\nListening for 'Hey, Remote' again...")
            
            # Small delay to prevent excessive CPU usage
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("\nExiting...")


if __name__ == "__main__":
    main()
