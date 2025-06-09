import requests
import json

def get_media_deep_link_options(query: str):
    try:
        # Step 1: Search Roku API for the query
        search_url = f"https://www.roku.com/api/v1/sow/search?series=1&query={requests.utils.quote(query)}"
        search_response = requests.get(search_url)
        search_response.raise_for_status()
        search_data = search_response.json()

        # Step 2: Get the first media ID from search results
        media_id = None
        media_type = None
        for item in search_data.get("view", []):
            meta = item.get("content", {}).get("meta", {})
            media_id = meta.get("id")
            media_type = meta.get("mediaType")
            if media_id:
                break

        if not media_id:
            return None  # No media ID found

        # Step 3: Request content details using media ID
        content_url = f"https://www.roku.com/api/v1/sow/content/v1/roku/{media_id}"
        content_response = requests.get(content_url)
        content_response.raise_for_status()
        content_data = content_response.json()

        raw_options = content_data.get("view", {}).get("viewOptions", [])
        options = []

        for option in raw_options:
            options.append({
                "channel_id": option.get('channelId'),
                "channel_name": option.get('channelName'),
                "media_type": media_type,
                "content_id": option.get('playId')
            })

        return options
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


def get_disney_plus_play_id(query):
    """
    Searches Roku for a given query and returns the Disney Plus playId for the first matching result.

    :param query: The search term (e.g., "Shark Tank")
    :return: playId as a string, or None if not found
    """
    try:
        # Step 1: Search Roku API for the query
        search_url = f"https://www.roku.com/api/v1/sow/search?series=1&query={requests.utils.quote(query)}"
        search_response = requests.get(search_url)
        search_response.raise_for_status()
        search_data = search_response.json()

        # Step 2: Get the first media ID from search results
        media_id = None
        for item in search_data.get("view", []):
            meta = item.get("content", {}).get("meta", {})
            media_id = meta.get("id")
            if media_id:
                break

        if not media_id:
            return None  # No media ID found

        # Step 3: Request content details using media ID
        content_url = f"https://www.roku.com/api/v1/sow/content/v1/roku/{media_id}1"
        content_response = requests.get(content_url)
        content_response.raise_for_status()
        content_data = content_response.json()

        # Step 4: Search for Disney Plus playId
        for option in content_data.get("view", {}).get("viewOptions", []):
            if option.get("channelName") == "Disney Plus":
                return option.get("playId")

        return None  # Disney Plus playId not found

    except requests.RequestException as e:
        print(f"Network error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    deep_link_options = get_media_deep_link_options("adventure time")
    print(json.dumps(deep_link_options, indent=2))
