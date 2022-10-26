from unittest import IsolatedAsyncioTestCase

from responses.registries import OrderedRegistry
from responses_server import ResponsesServer

from videosrc.crawlers.odysee import OdyseeCrawler


RSP0 = {'id': 0,
 'jsonrpc': '2.0',
 'result': {'lbry://@timcast#c': {'address': 'bMyDG3xgFUK4fao4dU8jq1THhEGhJr5z55',
                                  'amount': '0.005',
                                  'canonical_url': 'lbry://@timcast#c',
                                  'claim_id': 'c9da929d12afe6066acc89eb044b552f0d63782a',
                                  'claim_op': 'update',
                                  'confirmations': 475239,
                                  'has_signing_key': False,
                                  'height': 766981,
                                  'is_my_output': False,
                                  'meta': {'activation_height': 766981,
                                           'claims_in_channel': 2091,
                                           'creation_height': 303200,
                                           'creation_timestamp': 1515621908,
                                           'effective_amount': '77718.4454',
                                           'expiration_height': 2869381,
                                           'is_controlling': True,
                                           'reposted': 1,
                                           'support_amount': '77718.4404',
                                           'take_over_height': 307232},
                                  'name': '@timcast',
                                  'normalized_name': '@timcast',
                                  'nout': 0,
                                  'permanent_url': 'lbry://@timcast#c9da929d12afe6066acc89eb044b552f0d63782a',
                                  'short_url': 'lbry://@timcast#c',
                                  'timestamp': 1589902980,
                                  'txid': '94f2374d50b5b645a05b2bc6fc405d7cbd9f940509d4695f81b68bc18866ceeb',
                                  'type': 'claim',
                                  'value': {'cover': {'url': 'https://thumbnails.lbry.com/banner-UCG749Dj4V2fKa143f8sE60Q'},
                                            'description': 'Tim Pool brings '
                                                           'you breaking news '
                                                           'from around the '
                                                           'world and '
                                                           'commentary on top '
                                                           'news topics in '
                                                           'Politics and '
                                                           'Cultural issues\n'
                                                           'around the world.\n'
                                                           '\n'
                                                           'Stay tuned for '
                                                           'live news, '
                                                           'livestreams, '
                                                           'breaking stories, '
                                                           'everyday and a new '
                                                           'podcast episode of '
                                                           '"The Culture War" '
                                                           'every Sunday at '
                                                           '4pm.\n'
                                                           '\n'
                                                           'Use the email '
                                                           'below for any '
                                                           'business '
                                                           'inquiries.',
                                            'locations': [{'country': 'US'}],
                                            'public_key': '029da7c3648c9b9f9e46e6c15eaa91a1a502baa389bc8fea07c0fe35be99c5bc47',
                                            'public_key_id': 'bPCWHNqyteXatNEHJR73UeZdpC13CsJMRs',
                                            'tags': ['news', 'technology'],
                                            'thumbnail': {'url': 'https://thumbnails.lbry.com/UCG749Dj4V2fKa143f8sE60Q'},
                                            'title': 'Tim Pool'},
                                  'value_type': 'channel'}}}
RSP1 = {'id': 0,
 'jsonrpc': '2.0',
 'result': {'blocked': {'channels': [], 'total': 0},
            'items': [{'address': 'bMyDG3xgFUK4fao4dU8jq1THhEGhJr5z55',
                       'amount': '0.002',
                       'canonical_url': 'lbry://@timcast#c/elon-musk-nuked-ukrainian-gov-from-orbit#5',
                       'claim_id': '5c02f6632888b2462c60fc3e608721b3c45cb402',
                       'claim_op': 'create',
                       'confirmations': 152,
                       'height': 1242068,
                       'is_channel_signature_valid': True,
                       'meta': {'activation_height': 1242068,
                                'creation_height': 1242068,
                                'creation_timestamp': 1665779521,
                                'effective_amount': '0.002',
                                'expiration_height': 3344468,
                                'is_controlling': True,
                                'reposted': 0,
                                'support_amount': '0.0',
                                'take_over_height': 1242068},
                       'name': 'elon-musk-nuked-ukrainian-gov-from-orbit',
                       'normalized_name': 'elon-musk-nuked-ukrainian-gov-from-orbit',
                       'nout': 0,
                       'permanent_url': 'lbry://elon-musk-nuked-ukrainian-gov-from-orbit#5c02f6632888b2462c60fc3e608721b3c45cb402',
                       'short_url': 'lbry://elon-musk-nuked-ukrainian-gov-from-orbit#5',
                       'signing_channel': {'address': 'bMyDG3xgFUK4fao4dU8jq1THhEGhJr5z55',
                                           'amount': '0.005',
                                           'canonical_url': 'lbry://@timcast#c',
                                           'claim_id': 'c9da929d12afe6066acc89eb044b552f0d63782a',
                                           'claim_op': 'update',
                                           'confirmations': 475239,
                                           'has_signing_key': False,
                                           'height': 766981,
                                           'meta': {'activation_height': 766981,
                                                    'claims_in_channel': 2091,
                                                    'creation_height': 303200,
                                                    'creation_timestamp': 1515621908,
                                                    'effective_amount': '77718.4454',
                                                    'expiration_height': 2869381,
                                                    'is_controlling': True,
                                                    'reposted': 1,
                                                    'support_amount': '77718.4404',
                                                    'take_over_height': 307232},
                                           'name': '@timcast',
                                           'normalized_name': '@timcast',
                                           'nout': 0,
                                           'permanent_url': 'lbry://@timcast#c9da929d12afe6066acc89eb044b552f0d63782a',
                                           'short_url': 'lbry://@timcast#c',
                                           'timestamp': 1589902980,
                                           'txid': '94f2374d50b5b645a05b2bc6fc405d7cbd9f940509d4695f81b68bc18866ceeb',
                                           'type': 'claim',
                                           'value': {'cover': {'url': 'https://thumbnails.lbry.com/banner-UCG749Dj4V2fKa143f8sE60Q'},
                                                     'description': 'Tim Pool '
                                                                    'brings '
                                                                    'you '
                                                                    'breaking '
                                                                    'news from '
                                                                    'around '
                                                                    'the world '
                                                                    'and '
                                                                    'commentary '
                                                                    'on top '
                                                                    'news '
                                                                    'topics in '
                                                                    'Politics '
                                                                    'and '
                                                                    'Cultural '
                                                                    'issues\n'
                                                                    'around '
                                                                    'the '
                                                                    'world.\n'
                                                                    '\n'
                                                                    'Stay '
                                                                    'tuned for '
                                                                    'live '
                                                                    'news, '
                                                                    'livestreams, '
                                                                    'breaking '
                                                                    'stories, '
                                                                    'everyday '
                                                                    'and a new '
                                                                    'podcast '
                                                                    'episode '
                                                                    'of "The '
                                                                    'Culture '
                                                                    'War" '
                                                                    'every '
                                                                    'Sunday at '
                                                                    '4pm.\n'
                                                                    '\n'
                                                                    'Use the '
                                                                    'email '
                                                                    'below for '
                                                                    'any '
                                                                    'business '
                                                                    'inquiries.',
                                                     'locations': [{'country': 'US'}],
                                                     'public_key': '029da7c3648c9b9f9e46e6c15eaa91a1a502baa389bc8fea07c0fe35be99c5bc47',
                                                     'public_key_id': 'bPCWHNqyteXatNEHJR73UeZdpC13CsJMRs',
                                                     'tags': ['news',
                                                              'technology'],
                                                     'thumbnail': {'url': 'https://thumbnails.lbry.com/UCG749Dj4V2fKa143f8sE60Q'},
                                                     'title': 'Tim Pool'},
                                           'value_type': 'channel'},
                       'timestamp': 1665779521,
                       'txid': '782e0c0566843c399e95684eea4532b26cc4bc9441e4a3ae1dd9cedb895be214',
                       'type': 'claim',
                       'value': {'description': 'Elon Musk NUKED Ukrainian Gov '
                                                'FROM ORBIT SHUTTERING '
                                                'Starlink After They Told Him '
                                                'To F OFF. After Elon Musk '
                                                'proposed peace Ukrainian '
                                                'Government officials insulted '
                                                'him, now the tech billionaire '
                                                "is saying he won't pay for "
                                                'Starlink anymore in Ukraine.\n'
                                                '\n'
                                                'Already reports have surfaced '
                                                'that elon shuttered the use '
                                                'of starlink in Crimea and one '
                                                'person accused Elon of having '
                                                'spoken to Putin about it. '
                                                'Elon Musk denies this '
                                                'however.\n'
                                                '\n'
                                                'But one thing is clear, '
                                                'Ukraine should be grateful '
                                                'that Elon Musk was assisting '
                                                'in the ukraine war effort and '
                                                'if they want his support they '
                                                'should apologize.\n'
                                                '\n'
                                                'At any rate it seems that '
                                                'Biden and the Democrats do '
                                                'not have a plan for how to '
                                                'win and the end result will '
                                                'simply be world war three\n'
                                                '\n'
                                                '#starlink \n'
                                                '#elonmusk \n'
                                                '#ukraine \n'
                                                '\n'
                                                'Become A Member And Protect '
                                                'Our Work at '
                                                'http://www.timcast.com\n'
                                                '\n'
                                                'My Second Channel - '
                                                'https://www.youtube.com/timcastnews\n'
                                                'Podcast Channel - '
                                                'https://www.youtube.com/TimcastIRL\n'
                                                '\n'
                                                'Merch - '
                                                'http://teespring.com/timcast\n'
                                                '\n'
                                                'Make sure to subscribe for '
                                                'more travel, news, opinion, '
                                                'and documentary with Tim Pool '
                                                'everyday.\n'
                                                '...\n'
                                                'https://www.youtube.com/watch?v=gxOz3q0jrEY',
                                 'languages': ['en'],
                                 'license': 'Copyrighted (contact publisher)',
                                 'release_time': '1665777612',
                                 'source': {'hash': 'f360f8a33fd12fb633a21bc67f56aef2a68f9423c1c2c33557a53321dc2921c0ba7df2df5de3fb40f98c24a88db4c2c8',
                                            'media_type': 'video/mp4',
                                            'name': 'elon-musk-nuked-ukrainian-gov.mp4',
                                            'sd_hash': 'bf39ccb675f0d041b938c7d31e04de45224ecd0a9d74241fc39c035e763e5d92d64feb8d3e56b2b592667a6d4236f570',
                                            'size': '194873679'},
                                 'stream_type': 'video',
                                 'tags': ['news',
                                          'technology',
                                          'biden',
                                          'elon musk',
                                          'elon starlink',
                                          'intellectual dark web',
                                          'starlink crimea',
                                          'tim pool',
                                          'timcast',
                                          'ukraine',
                                          'ukraine starlink',
                                          'ukraine war',
                                          'world war three'],
                                 'thumbnail': {'url': 'https://thumbnails.lbry.com/gxOz3q0jrEY'},
                                 'title': 'Elon Musk NUKED Ukrainian Gov FROM '
                                          'ORBIT SHUTTERING Starlink After '
                                          'They Told Him To F OFF',
                                 'video': {'duration': 1948,
                                           'height': 1080,
                                           'width': 1920}},
                       'value_type': 'stream'},
                      {'address': 'bMyDG3xgFUK4fao4dU8jq1THhEGhJr5z55',
                       'amount': '0.002',
                       'canonical_url': 'lbry://@timcast#c/biden-caught-in-quid-pro-quo,-democrats#a',
                       'claim_id': 'aaa507ff12f7d0d296e9707fe8e5aa9a6e37dfc9',
                       'claim_op': 'create',
                       'confirmations': 695,
                       'height': 1241525,
                       'is_channel_signature_valid': True,
                       'meta': {'activation_height': 1241525,
                                'creation_height': 1241525,
                                'creation_timestamp': 1665692097,
                                'effective_amount': '6.002',
                                'expiration_height': 3343925,
                                'is_controlling': True,
                                'reposted': 0,
                                'support_amount': '6.0',
                                'take_over_height': 1241525},
                       'name': 'biden-caught-in-quid-pro-quo,-democrats',
                       'normalized_name': 'biden-caught-in-quid-pro-quo,-democrats',
                       'nout': 0,
                       'permanent_url': 'lbry://biden-caught-in-quid-pro-quo,-democrats#aaa507ff12f7d0d296e9707fe8e5aa9a6e37dfc9',
                       'short_url': 'lbry://biden-caught-in-quid-pro-quo,-democrats#a',
                       'signing_channel': {'address': 'bMyDG3xgFUK4fao4dU8jq1THhEGhJr5z55',
                                           'amount': '0.005',
                                           'canonical_url': 'lbry://@timcast#c',
                                           'claim_id': 'c9da929d12afe6066acc89eb044b552f0d63782a',
                                           'claim_op': 'update',
                                           'confirmations': 475239,
                                           'has_signing_key': False,
                                           'height': 766981,
                                           'meta': {'activation_height': 766981,
                                                    'claims_in_channel': 2091,
                                                    'creation_height': 303200,
                                                    'creation_timestamp': 1515621908,
                                                    'effective_amount': '77718.4454',
                                                    'expiration_height': 2869381,
                                                    'is_controlling': True,
                                                    'reposted': 1,
                                                    'support_amount': '77718.4404',
                                                    'take_over_height': 307232},
                                           'name': '@timcast',
                                           'normalized_name': '@timcast',
                                           'nout': 0,
                                           'permanent_url': 'lbry://@timcast#c9da929d12afe6066acc89eb044b552f0d63782a',
                                           'short_url': 'lbry://@timcast#c',
                                           'timestamp': 1589902980,
                                           'txid': '94f2374d50b5b645a05b2bc6fc405d7cbd9f940509d4695f81b68bc18866ceeb',
                                           'type': 'claim',
                                           'value': {'cover': {'url': 'https://thumbnails.lbry.com/banner-UCG749Dj4V2fKa143f8sE60Q'},
                                                     'description': 'Tim Pool '
                                                                    'brings '
                                                                    'you '
                                                                    'breaking '
                                                                    'news from '
                                                                    'around '
                                                                    'the world '
                                                                    'and '
                                                                    'commentary '
                                                                    'on top '
                                                                    'news '
                                                                    'topics in '
                                                                    'Politics '
                                                                    'and '
                                                                    'Cultural '
                                                                    'issues\n'
                                                                    'around '
                                                                    'the '
                                                                    'world.\n'
                                                                    '\n'
                                                                    'Stay '
                                                                    'tuned for '
                                                                    'live '
                                                                    'news, '
                                                                    'livestreams, '
                                                                    'breaking '
                                                                    'stories, '
                                                                    'everyday '
                                                                    'and a new '
                                                                    'podcast '
                                                                    'episode '
                                                                    'of "The '
                                                                    'Culture '
                                                                    'War" '
                                                                    'every '
                                                                    'Sunday at '
                                                                    '4pm.\n'
                                                                    '\n'
                                                                    'Use the '
                                                                    'email '
                                                                    'below for '
                                                                    'any '
                                                                    'business '
                                                                    'inquiries.',
                                                     'locations': [{'country': 'US'}],
                                                     'public_key': '029da7c3648c9b9f9e46e6c15eaa91a1a502baa389bc8fea07c0fe35be99c5bc47',
                                                     'public_key_id': 'bPCWHNqyteXatNEHJR73UeZdpC13CsJMRs',
                                                     'tags': ['news',
                                                              'technology'],
                                                     'thumbnail': {'url': 'https://thumbnails.lbry.com/UCG749Dj4V2fKa143f8sE60Q'},
                                                     'title': 'Tim Pool'},
                                           'value_type': 'channel'},
                       'timestamp': 1665692097,
                       'txid': '746285c53c7bcdc9335110dcb75d36510f667b6bb0f78e9ac158ff77d761417c',
                       'type': 'claim',
                       'value': {'description': 'Biden CAUGHT In Quid Pro Quo, '
                                                'Democrats DEMAND Saudi Arabia '
                                                'HELP Them Win Midterms, '
                                                'THREATEN Allies. Democrats '
                                                'wanted OPEC+ to postpone oil '
                                                'reduction only until after '
                                                'the midterms which would have '
                                                'done nothing for Americans in '
                                                'the long run but would have '
                                                'helped Democrats win '
                                                'political victories.\n'
                                                '\n'
                                                'This quid pro quo is beyond '
                                                'anything Trump was accused of '
                                                "and in the case of Trump's "
                                                'impeachment Ukraine denied '
                                                'there being any quid pro '
                                                'quo.\n'
                                                '\n'
                                                'Saudi Arabia is now outright '
                                                'stating the US tried to get '
                                                'them to do this.\n'
                                                '\n'
                                                'Republicans must impeach joe '
                                                'biden upon winning the '
                                                'midterms\n'
                                                '\n'
                                                '#democrats \n'
                                                '#biden \n'
                                                '#republicans \n'
                                                '\n'
                                                'Become A Member And Protect '
                                                'Our Work at '
                                                'http://www.timcast.com\n'
                                                '\n'
                                                'My Second Channel - '
                                                'https://www.youtube.com/timcastnews\n'
                                                'Podcast Channel - '
                                                'https://www.youtube.com/TimcastIRL\n'
                                                '\n'
                                                'Merch - '
                                                'http://teespring.com/timcast\n'
                                                '\n'
                                                'Make sure to subscribe for '
                                                'more travel, news, opinion, '
                                                'and documentary with Tim Pool '
                                                'everyday.\n'
                                                '...\n'
                                                'https://www.youtube.com/watch?v=W0K4cYa5PK4',
                                 'languages': ['en'],
                                 'license': 'Copyrighted (contact publisher)',
                                 'release_time': '1665691217',
                                 'source': {'hash': '76d7655a1a8a0b2d9ed1a59317bb1e457b6a54d01e1e8114a1bfef5915ba6f5c414ff8ff29f739032f319f2c3153847f',
                                            'media_type': 'video/mp4',
                                            'name': 'biden-caught-in-quid-pro-quo.mp4',
                                            'sd_hash': 'd16ae0bd4395b48fae24a55c067160469809605a47b5b4c5ec345e8132198fd596d74fd26db4becbefdadcff374a5c0f',
                                            'size': '212307786'},
                                 'stream_type': 'video',
                                 'tags': ['news',
                                          'technology',
                                          'biden',
                                          'biden caught',
                                          'biden exposed',
                                          'biden quid pro quo',
                                          'democrats',
                                          'impeach joe biden',
                                          'intellectual dark web',
                                          'midterms',
                                          'open',
                                          'republicans',
                                          'saudi arabia',
                                          'tim pool',
                                          'timcast',
                                          'trump'],
                                 'thumbnail': {'url': 'https://thumbnails.lbry.com/W0K4cYa5PK4'},
                                 'title': 'Biden CAUGHT In Quid Pro Quo, '
                                          'Democrats DEMAND Saudi Arabia HELP '
                                          'Them Win Midterms, THREATEN Allies',
                                 'video': {'duration': 1980,
                                           'height': 1080,
                                           'width': 1920}},
                       'value_type': 'stream'}],
            'page': 1,
            'page_size': 2}}
RSP2 = {'id': 1665803360,
 'jsonrpc': '2.0',
 'result': {'streaming_url': 'https://player.odycdn.com/api/v4/streams/free/elon-musk-nuked-ukrainian-gov-from-orbit/5c02f6632888b2462c60fc3e608721b3c45cb402/bf39cc'}}
RSP3 = {'id': 1665803361,
 'jsonrpc': '2.0',
 'result': {'streaming_url': 'https://player.odycdn.com/api/v4/streams/free/biden-caught-in-quid-pro-quo,-democrats/aaa507ff12f7d0d296e9707fe8e5aa9a6e37dfc9/d16ae0'}}


class OdyseeTestCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.server = ResponsesServer(
            responses_kwargs={'registry': OrderedRegistry})
        self.server.start()
        self.crawler = OdyseeCrawler(api_url=self.server.url())
        self.server.post(self.server.url(), json=RSP0)
        self.server.post(self.server.url(), json=RSP1)
        self.server.post(self.server.url(), json=RSP2)
        self.server.post(self.server.url(), json=RSP3)

    def tearDown(self):
        self.server.stop()

    async def test_login(self):
        pass #  await self.crawler.login()

    async def test_crawl(self):
        channel, videos = await self.crawler.crawl('https://odysee.com/@timcast:c')
        videos = [v async for v, s in videos]
        self.assertEqual('timcast', channel.name)
        self.assertEqual(2, len(videos))
        self.assertEqual(
            'Elon Musk NUKED Ukrainian Gov FROM ORBIT SHUTTERING Starlink After They Told Him To F OFF',
            videos[0].title)
        self.assertEqual(1, len(videos[0].sources))
        self.assertEqual(
            'https://player.odycdn.com/api/v4/streams/free/elon-musk-nuked-ukrainian-gov-from-orbit/5c02f6632888b2462c60fc3e608721b3c45cb402/bf39cc',
            videos[0].sources[0].url)
