from openai import OpenAI
import speech_recognition as sr
from util.get_media_id import get_disney_plus_play_id, get_media_deep_link_options
from util.roku_connection import scan_roku_ip, test_connection
from util.roku_commands import launch_deep_link, launch_deep_link_from_obj, launch_disney_plus_content

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
    """

    raw_text = input("> ")

    show_title = raw_text
    print(f"Parsed show: {show_title}")

    roku_ip = scan_roku_ip()
    if not test_connection(roku_ip):
        print("Failed to connect to Roku. Check network and IP.")
        return

    deep_link_options = get_media_deep_link_options(show_title)
    deep_link_data = next(filter(lambda option: option.get('channel_name') == 'Disney Plus',
                                 deep_link_options), None)

    if deep_link_data:
        print(f"Launching '{show_title}'")
        launch_deep_link_from_obj(roku_ip, deep_link_data)
        # launch_deep_link(roku_ip,
        #                  deep_link_data.get('channel_id'),
        #                  deep_link_data.get('content_id'),
        #                  deep_link_data.get('media_type'))
    else:
        print(f"Could not find '{show_title}' on Disney+.")


if __name__ == "__main__":
    main()
