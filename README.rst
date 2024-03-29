********
videosrc
********
Web crawler to extract video data from HTML, MRSS and more.

This library primarily extracts the source attributes / tags from the HTML5
`<video/>` element.

Each crawler accepts an opaque `state` value which allows it to resume a crawl
at a later time. In addition, each crawler accepts an argument `save_state`
which should be a callback that receives this opaque state value. A caller's
job is to store that state for future use.

Motivation
##########
I needed to be able to enumerate videos from multiple different websites and formats.

Backends
########
A given URL is handled by a specific backend which knows how to interpret the HTML.

HTML
****
Meant to read from a static HTML page or index page generated by a webserver when viewing a directory full of video files. Looks for videos in `<video/>` and `<a/>` tags.

MRSS
****
Media RSS is a syndication format for media. As such we don't really need to crawl the given URL but simply parse it and return the listed videos.

Peertube
********
Utilizes the PeerTube REST API to fetch video information.

Odysee
******
Utilizes the Odysee REST API to fetch video information.

Rumble
******
Uses web scraping to fetch video information. Utilizes Chromium to allow Javascript execution.

Timcast
*******
Uses pyppeteer to login then uses the authentication cookie with aiohttp_scraper to scrape video urls, then fetches video data from Rumble.

Twitter
*******
Uses snscrape to scrape media from a user's tweets.
