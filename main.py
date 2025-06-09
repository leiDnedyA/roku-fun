import json
from openai import OpenAI
import speech_recognition as sr
from util.get_media_id import get_media_deep_link_options
from util.roku_connection import scan_roku_ip, test_connection
from util.roku_commands import launch_deep_link_from_obj
from util.openai_setup import system_prompt, tools

client = OpenAI()

def recognize_speech_from_mic(recognizer, microphone):
    """
    Capture speech from the microphone and return the transcribed text.
    """
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for your request...")
        audio = recognizer.listen(source)

    response = {"success": True, "error": None, "transcription": None}
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

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
    # Initialize speech recognizer and microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # 1. Listen for user prompt
    speech_result = recognize_speech_from_mic(recognizer, microphone)
    if not speech_result["success"]:
        print(f"ERROR: {speech_result['error']}")
        return
    if speech_result["transcription"] is None:
        print("Didn't catch that. Please try again.")
        return

    raw_text = speech_result["transcription"]
    print(f"Heard: {raw_text}")
    show_title = raw_text
    """

    raw_text = input("> ")
    launch_media_from_prompt(raw_text)


if __name__ == "__main__":
    main()
