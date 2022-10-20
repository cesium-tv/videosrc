import re
import time
from pprint import pprint
from urllib.parse import urlparse
from pprint import pprint
from datetime import datetime

from aiohttp.hdrs import METH_POST
from aiohttp_scraper import ScraperSession

from videosrc.models import Channel, Video, VideoSource


API_URL = 'https://api.na-backend.odysee.com/api/v1/proxy'


class OdyseeCrawler:
    def __init__(self, state=None, ChannelModel=Channel, VideoModel=Video,
                 VideoSourceModel=VideoSource, api_url=API_URL):
        self.auth = None
        self.state = state
        self.ChannelModel = ChannelModel
        self.VideoModel = VideoModel
        self.VideoSourceModel = VideoSourceModel
        self.api_url = api_url
        self.auth_token = None

    @staticmethod
    def check_url(url):
        urlp = urlparse(url)
        return urlp.netloc.endswith('odysee.com')

    async def _make_request(self, method, params):
        ts = int(time.time())
        async with ScraperSession() as s:
            r = await s.request(
                    METH_POST,
                self.api_url,
                params={'m': method},
                json={
                    "jsonrpc": "2.0",
                    "method": method,
                    "params": params,
                    "id": ts,
                })
        return (await r.json())['result']

    async def login(self):
        async with ScraperSession() as s:
            r = await s._request(
                METH_POST,
                'https://api.odysee.com/user/new',
                data={
                    'auth_token': '',
                    'language': 'en',
                    'app_id': 'odyseecom692EAWhtoqDuAfQ6KHMXxFxt8tkhmt7sfprEMHWKjy5hf6PwZcHDV542V',
            })
        self.auth = (await r.json())['auth_token']

    # {
    #     "address": "bMyDG3xgFUK4fao4dU8jq1THhEGhJr5z55",
    #     "amount": "0.002",
    #     "canonical_url": "lbry://@timcast#c/elon-musk-nuked-ukrainian-gov-from-orbit#5",
    #     "claim_id": "5c02f6632888b2462c60fc3e608721b3c45cb402",
    #     "claim_op": "create",
    #     "confirmations": 23,
    #     "height": 1242068,
    #     "is_channel_signature_valid": true,
    #     "meta": {
    #         "activation_height": 1242068,
    #         "creation_height": 1242068,
    #         "creation_timestamp": 1665779521,
    #         "effective_amount": "0.002",
    #         "expiration_height": 3344468,
    #         "is_controlling": true,
    #         "reposted": 0,
    #         "support_amount": "0.0",
    #         "take_over_height": 1242068
    #     },
    #     "name": "elon-musk-nuked-ukrainian-gov-from-orbit",
    #     "normalized_name": "elon-musk-nuked-ukrainian-gov-from-orbit",
    #     "nout": 0,
    #     "permanent_url": "lbry://elon-musk-nuked-ukrainian-gov-from-orbit#5c02f6632888b2462c60fc3e608721b3c45cb402",
    #     "short_url": "lbry://elon-musk-nuked-ukrainian-gov-from-orbit#5",
    #     "signing_channel": {
    #         "address": "bMyDG3xgFUK4fao4dU8jq1THhEGhJr5z55",
    #         "amount": "0.005",
    #         "canonical_url": "lbry://@timcast#c",
    #         "claim_id": "c9da929d12afe6066acc89eb044b552f0d63782a",
    #         "claim_op": "update",
    #         "confirmations": 475110,
    #         "has_signing_key": false,
    #         "height": 766981,
    #         "meta": {
    #         "activation_height": 766981,
    #         "claims_in_channel": 2091,
    #         "creation_height": 303200,
    #         "creation_timestamp": 1515621908,
    #         "effective_amount": "77718.4454",
    #         "expiration_height": 2869381,
    #         "is_controlling": true,
    #         "reposted": 1,
    #         "support_amount": "77718.4404",
    #         "take_over_height": 307232
    #         },
    #         "name": "@timcast",
    #         "normalized_name": "@timcast",
    #         "nout": 0,
    #         "permanent_url": "lbry://@timcast#c9da929d12afe6066acc89eb044b552f0d63782a",
    #         "short_url": "lbry://@timcast#c",
    #         "timestamp": 1589902980,
    #         "txid": "94f2374d50b5b645a05b2bc6fc405d7cbd9f940509d4695f81b68bc18866ceeb",
    #         "type": "claim",
    #         "value": {
    #         "cover": {
    #             "url": "https://thumbnails.lbry.com/banner-UCG749Dj4V2fKa143f8sE60Q"
    #         },
    #         "description": "Tim Pool brings you breaking news from around the world and commentary on top news topics in Politics and Cultural issues\naround the world.\n\nStay tuned for live news, livestreams, breaking stories, everyday and a new podcast episode of \"The Culture War\" every Sunday at 4pm.\n\nUse the email below for any business inquiries.",
    #         "locations": [
    #             {
    #             "country": "US"
    #             }
    #         ],
    #         "public_key": "029da7c3648c9b9f9e46e6c15eaa91a1a502baa389bc8fea07c0fe35be99c5bc47",
    #         "public_key_id": "bPCWHNqyteXatNEHJR73UeZdpC13CsJMRs",
    #         "tags": [
    #             "news",
    #             "technology"
    #         ],
    #         "thumbnail": {
    #             "url": "https://thumbnails.lbry.com/UCG749Dj4V2fKa143f8sE60Q"
    #         },
    #         "title": "Tim Pool"
    #         },
    #         "value_type": "channel"
    #     },
    #     "timestamp": 1665779521,
    #     "txid": "782e0c0566843c399e95684eea4532b26cc4bc9441e4a3ae1dd9cedb895be214",
    #     "type": "claim",
    #     "value": {
    #         "description": "Elon Musk NUKED Ukrainian Gov FROM ORBIT SHUTTERING Starlink After They Told Him To F OFF. After Elon Musk proposed peace Ukrainian Government officials insulted him, now the tech billionaire is saying he won't pay for Starlink anymore in Ukraine.\n\nAlready reports have surfaced that elon shuttered the use of starlink in Crimea and one person accused Elon of having spoken to Putin about it. Elon Musk denies this however.\n\nBut one thing is clear, Ukraine should be grateful that Elon Musk was assisting in the ukraine war effort and if they want his support they should apologize.\n\nAt any rate it seems that Biden and the Democrats do not have a plan for how to win and the end result will simply be world war three\n\n#starlink \n#elonmusk \n#ukraine \n\nBecome A Member And Protect Our Work at http://www.timcast.com\n\nMy Second Channel - https://www.youtube.com/timcastnews\nPodcast Channel - https://www.youtube.com/TimcastIRL\n\nMerch - http://teespring.com/timcast\n\nMake sure to subscribe for more travel, news, opinion, and documentary with Tim Pool everyday.\n...\nhttps://www.youtube.com/watch?v=gxOz3q0jrEY",
    #         "languages": [
    #             "en"
    #         ],
    #         "license": "Copyrighted (contact publisher)",
    #         "release_time": "1665777612",
    #         "source": {
    #             "hash": "f360f8a33fd12fb633a21bc67f56aef2a68f9423c1c2c33557a53321dc2921c0ba7df2df5de3fb40f98c24a88db4c2c8",
    #             "media_type": "video/mp4",
    #             "name": "elon-musk-nuked-ukrainian-gov.mp4",
    #             "sd_hash": "bf39ccb675f0d041b938c7d31e04de45224ecd0a9d74241fc39c035e763e5d92d64feb8d3e56b2b592667a6d4236f570",
    #             "size": "194873679"
    #         },
    #         "stream_type": "video",
    #         "tags": [
    #             "news",
    #             "technology",
    #             "biden",
    #             "elon musk",
    #             "elon starlink",
    #             "intellectual dark web",
    #             "starlink crimea",
    #             "tim pool",
    #             "timcast",
    #             "ukraine",
    #             "ukraine starlink",
    #             "ukraine war",
    #             "world war three"
    #         ],
    #         "thumbnail": {
    #             "url": "https://thumbnails.lbry.com/gxOz3q0jrEY"
    #         },
    #         "title": "Elon Musk NUKED Ukrainian Gov FROM ORBIT SHUTTERING Starlink After They Told Him To F OFF",
    #         "video": {
    #             "duration": 1948,
    #             "height": 1080,
    #             "width": 1920
    #         }
    #     },
    #     "value_type": "stream"
    # },
    async def _iter_videos(self, channel_id, state):
        page_number = 1
        release_time = f"<{self.state}"
        if state:
            release_time = [release_time, f'>{state}']
        while True:
            result = await self._make_request('claim_search', {
                "page_size": 2,
                "page": page_number,
                "claim_type": ["stream","repost"],
                "no_totals": True,
                "not_tags": ["porn","porno","nsfw","mature","xxx","sex","creampie","blowjob","handjob","vagina","boobs","big boobs","big dick","pussy","cumshot","anal","hard fucking","ass","fuck","hentai"],
                "order_by": ["release_time"],
                "has_source": True,
                "channel_ids": [channel_id],
                "release_time": release_time,
            })
            items = result['items']
            for item in items:
                published = datetime.fromtimestamp(
                    int(item['value']['release_time']))
                stream = await self._make_request('get', { 'uri': item['short_url'] })
                source = self.VideoSourceModel(
                    url=stream['streaming_url'],
                    size=item['value']['source']['size'],
                    width=item['value']['video']['width'],
                    height=item['value']['video']['height'],
                    original=item,
                )
                video = self.VideoModel(
                    title=item['value']['title'],
                    description=item['value']['description'],
                    extern_id=item['claim_id'],
                    poster=item['value']['thumbnail']['url'],
                    duration=item['value']['video']['duration'],
                    tags=item['value']['tags'],
                    published=published,
                    sources=[source],
                    original=item,
                )
                yield video, self.state
            if len(items) + 1 < int(result['page_size']):
                break
            break
            page_number += 1

    async def crawl(self, url, options=None):
        # https://odysee.com/@timcast:c
        state, self.state = self.state, int(time.time())
        urlp = urlparse(url)
        channel_name = re.match('/@(\w+):c', urlp.path).group(1)
        lbry_url = f'lbry://@{channel_name}#c'
        result = await self._make_request('resolve', {
            'urls': [
                lbry_url,
            ],
            'include_purchase_receipt': True,
            'include_is_my_output': True,
        })
        result = result[lbry_url]
        value = result['value']
        channel = self.ChannelModel(
            name=channel_name,
            url=url,
            title=value['title'],
            description=value['description'],
            poster=value['cover']['url'],
        )
        channel_id = result['claim_id']
        return channel, self._iter_videos(channel_id, state)
