from tweetcapture import TweetCapture

async def taskcapture(url, port):
    tweet = TweetCapture()
    tweet.add_chrome_arguments(f"--remote-debugging-port={port}")
    filename = await tweet.screen_capture(url, overwrite=True)
    filename = await tweet.screenshot(
    "https://twitter.com/jack/status/20", "mode3.png", mode=3, night_mode=2)
    return filename

def main():
    print(taskcapture("https://twitter.com/barnabus__s/status/1744808339106627651", 9222))

