
tools = [{
    "type": "function",
    "function": {
        "name": "launch_media",
        "description": "Launches a show, movie, etc based on the media's name and the name of the Roku channel that it is hosted on.",
        "parameters": {
            "type": "object",
            "properties": {
                "media_name": {
                    "type": "string",
                    "description": "The name of the media to be launched. E.g \"Shark Tank\""
                },
                "channel_name": {
                    "type": "string",
                    "description": "The name of the channel to launch the media from, in all caps. E.g \"DISNEY PLUS\""
                }
            },
            "required": ["media_name", "channel_name"],
            "additionalProperties": False
        },
        "strict": True
    }
}]

system_prompt = {
    "role": "system",
    "content": "You are a smart media-launching assistant. When the user asks you to play, launch, or open a movie, show, or other media, you must extract the title and the Roku channel name and return **only** a JSON function call to `launch_media` with the exact `media_name` and `channel_name` (in ALL CAPS) parameters. Do not return any additional text or explanation. If the user’s request does not pertain to launching media, answer normally as a helpful assistant."
}
