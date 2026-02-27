import yt_dlp

def get_transcript(video_url):
    try:
        ydl_opts = {
            "skip_download": True,
            "quiet": True,
            "writesubtitles": True,
            "writeautomaticsub": True,
            "subtitleslangs": ["en", "hi", "auto"],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)

            subtitles = info.get("subtitles") or info.get("automatic_captions")

            if not subtitles:
                return None

            # Try English first
            for lang in ["en", "hi"]:
                if lang in subtitles:
                    url = subtitles[lang][0]["url"]

                    import requests
                    response = requests.get(url)
                    return response.text

            # If no en/hi, take first available
            first_lang = list(subtitles.keys())[0]
            url = subtitles[first_lang][0]["url"]

            import requests
            response = requests.get(url)
            return response.text

    except Exception as e:
        print("Transcript error:", e)
        return None
