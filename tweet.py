from tweetcapture import TweetCapture

async def taskCapture(url, port):
    tweet = TweetCapture()
    tweet.add_chrome_argument(f"--remote-debugging-port={port}")
    filename = await tweet.screenshot(url, overwrite=True)
    return filename

