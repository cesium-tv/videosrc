from unittest import IsolatedAsyncioTestCase

from responses.registries import OrderedRegistry
from responses_server import ResponsesServer

from videosrc.crawlers.timcast import TimcastCrawler


RSP0 = '''
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
    <link rel="apple-touch-icon" sizes="180x180" href="https://timcast.com/wp-content/themes/timcast/favicons/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="https://timcast.com/wp-content/themes/timcast/favicons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="https://timcast.com/wp-content/themes/timcast/favicons/favicon-16x16.png">
    <link rel="manifest" href="https://timcast.com/wp-content/themes/timcast/favicons/site.webmanifest">
    <link rel="mask-icon" href="https://timcast.com/wp-content/themes/timcast/favicons/safari-pinned-tab.svg" color="#000000">
    <meta name="msapplication-TileColor" content="#000000">
    <meta name="theme-color" content="#ffffff">
    <!-- for Facebook -->  
    <meta property="og:type" content="website" />
    <meta property="og:title" content="Seth Weathers &#038; Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK | TIMCAST" />
    <meta property="og:description" content="" />
    <meta property="og:url" content="https://timcast.com/members-area/section/timcast-irl/" />
    <meta property="og:image" content="https://timcast.com/wp-content/uploads/2022/10/640un-1024x576.png" />
    <!-- for Twitter -->          
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Seth Weathers &#038; Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK | TIMCAST" />
    <meta name="twitter:description" content="" />
    <meta name="twitter:image" content="https://timcast.com/wp-content/uploads/2022/10/640un-1024x576.png" />
    <meta property="article:published_time" content="2022-10-19T22:49:13+00:00">
    <link rel="apple-touch-icon" href="apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,300;0,400;0,600;1,300;1,400&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400&display=swap" rel="stylesheet">
    <!-- <script src="/var/www/timcast.com/html/wp-content/themes/thundercracker/assets/js/vendor/modernizr-2.8.3.min.js"></script> -->
    <meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />
    <!-- This site is optimized with the Yoast SEO plugin v18.7 - https://yoast.com/wordpress/plugins/seo/ -->
    <title>Timcast IRL Archives | TIMCAST</title>
    <link rel="canonical" href="https://timcast.com/members-area/section/timcast-irl/" />
    <link rel="next" href="https://timcast.com/members-area/section/timcast-irl/page/2/" />
    <meta property="og:locale" content="en_US" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="Timcast IRL Archives | TIMCAST" />
    <meta property="og:url" content="https://timcast.com/members-area/section/timcast-irl/" />
    <meta property="og:site_name" content="TIMCAST" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:site" content="@timcast" />
    <script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://timcast.com/#organization","name":"Timcast","url":"https://timcast.com/","sameAs":["http://www.facebook.com/timcastnews","https://www.instagram.com/timcast/","https://www.linkedin.com/in/timothy-pool-7228ba25/","http://www.youtube.com/timcast","https://en.wikipedia.org/wiki/Tim_Pool","https://twitter.com/timcast"],"logo":{"@type":"ImageObject","inLanguage":"en-US","@id":"https://timcast.com/#/schema/logo/image/","url":"https://timcast.com/wp-content/uploads/2021/01/cropped-FAVICON-1-2.jpg","contentUrl":"https://timcast.com/wp-content/uploads/2021/01/cropped-FAVICON-1-2.jpg","width":512,"height":512,"caption":"Timcast"},"image":{"@id":"https://timcast.com/#/schema/logo/image/"}},{"@type":"WebSite","@id":"https://timcast.com/#website","url":"https://timcast.com/","name":"TIMCAST","description":"timcast.com","publisher":{"@id":"https://timcast.com/#organization"},"potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://timcast.com/?s={search_term_string}"},"query-input":"required name=search_term_string"}],"inLanguage":"en-US"},{"@type":"CollectionPage","@id":"https://timcast.com/members-area/section/timcast-irl/#webpage","url":"https://timcast.com/members-area/section/timcast-irl/","name":"Timcast IRL Archives | TIMCAST","isPartOf":{"@id":"https://timcast.com/#website"},"breadcrumb":{"@id":"https://timcast.com/members-area/section/timcast-irl/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https://timcast.com/members-area/section/timcast-irl/"]}]},{"@type":"BreadcrumbList","@id":"https://timcast.com/members-area/section/timcast-irl/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://timcast.com/"},{"@type":"ListItem","position":2,"name":"Timcast IRL"}]}]}</script>
    <!-- / Yoast SEO plugin. -->
    <link rel='dns-prefetch' href='//www.google.com' />
    <link rel='dns-prefetch' href='//s.w.org' />
    <link rel="alternate" type="application/rss+xml" title="TIMCAST &raquo; Timcast IRL Section Feed" href="https://timcast.com/members-area/section/timcast-irl/feed/" />
    <link rel='stylesheet' id='mp-theme-css'  href='https://timcast.com/wp-content/plugins/memberpress/css/ui/theme.css?ver=1.9.37' type='text/css' media='all' />
    <link rel='stylesheet' id='wp-block-library-css'  href='https://timcast.com/wp-includes/css/dist/block-library/style.min.css?ver=5.9.5' type='text/css' media='all' />
    <link rel='stylesheet' id='mpp_gutenberg-css'  href='https://timcast.com/wp-content/plugins/metronet-profile-picture/dist/blocks.style.build.css?ver=2.6.0' type='text/css' media='all' />
    <style id='global-styles-inline-css' type='text/css'>
        body{--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--duotone--dark-grayscale: url('#wp-duotone-dark-grayscale');--wp--preset--duotone--grayscale: url('#wp-duotone-grayscale');--wp--preset--duotone--purple-yellow: url('#wp-duotone-purple-yellow');--wp--preset--duotone--blue-red: url('#wp-duotone-blue-red');--wp--preset--duotone--midnight: url('#wp-duotone-midnight');--wp--preset--duotone--magenta-yellow: url('#wp-duotone-magenta-yellow');--wp--preset--duotone--purple-green: url('#wp-duotone-purple-green');--wp--preset--duotone--blue-orange: url('#wp-duotone-blue-orange');--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
    </style>
    <link rel='stylesheet' id='contact-form-7-css'  href='https://timcast.com/wp-content/plugins/contact-form-7/includes/css/styles.css?ver=5.5.6' type='text/css' media='all' />
    <link rel='stylesheet' id='if-menu-site-css-css'  href='https://timcast.com/wp-content/plugins/if-menu/assets/if-menu-site.css?ver=5.9.5' type='text/css' media='all' />
    <link rel='stylesheet' id='parent-style-css'  href='https://timcast.com/wp-content/themes/timcast/style.css?ver=1665524704' type='text/css' media='all' />
    <script type='text/javascript' src='https://timcast.com/wp-includes/js/jquery/jquery.min.js?ver=3.6.0' id='jquery-core-js'></script>
    <script type='text/javascript' src='https://timcast.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.3.2' id='jquery-migrate-js'></script>
    <link rel="https://api.w.org/" href="https://timcast.com/wp-json/" />
    <link rel="alternate" type="application/json" href="https://timcast.com/wp-json/wp/v2/section/669" />
    <link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://timcast.com/xmlrpc.php?rsd" />
    <link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://timcast.com/wp-includes/wlwmanifest.xml" />
    <meta name="generator" content="WordPress 5.9.5" />
    <!-- breadcrumb Schema optimized by Schema Pro --><script type="application/ld+json">{"@context":"https:\/\/schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"item":{"@id":"https:\/\/timcast.com\/","name":"Home"}},{"@type":"ListItem","position":2,"item":{"@id":"https:\/\/timcast.com\/members-area\/section\/timcast-irl\/","name":"Timcast IRL"}}]}</script><!-- / breadcrumb Schema optimized by Schema Pro -->			
    <style id="wpsp-style-frontend"></style>
    <link rel="icon" href="https://timcast.com/wp-content/uploads/2021/11/cropped-android-chrome-512x512-1-32x32.png" sizes="32x32" />
    <link rel="icon" href="https://timcast.com/wp-content/uploads/2021/11/cropped-android-chrome-512x512-1-192x192.png" sizes="192x192" />
    <link rel="apple-touch-icon" href="https://timcast.com/wp-content/uploads/2021/11/cropped-android-chrome-512x512-1-180x180.png" />
    <meta name="msapplication-TileImage" content="https://timcast.com/wp-content/uploads/2021/11/cropped-android-chrome-512x512-1-270x270.png" />
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
        new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window,document,'script','dataLayer','GTM-KK9GLZ4');
    </script>
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
        new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window,document,'script','dataLayer','GTM-KG5GK79');
    </script>
    <!-- End Google Tag Manager -->
    <script defer src="https://users.api.jeeng.com/users/domains/3AJQ2Jdkl1/sdk/"></script>
    <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-60e766933db1abcb"></script> 
    <script src="https://script.metricode.com/wotjs/ellipsis.js?api_key=4fe7fc4c-f02b-496b-b68a-842f46bd7627"></script>
    <!-- Revcontent ad style adjustments --> 
</head>
<body style=" opacity:0"  class="t-bg:grey3  " >
    <div class="t-bg:blk">
        <!--[if lt IE 8]>
        <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->
        <header id="t-scrollnav-holder" class="t-bg:wht">
            <nav  id="t-scrollnav" >
            <div class="t-pos:cntr t-pos:rel t-bg:grey3 flex-nav">
                <div class="nav-and-search">
                    <div class="t-button-mobile-menu">
                        <div class="t-toggle-icon"></div>
                    </div>
                    <div class="btn-search">
                        <svg width="22px" height="22px" viewBox="0 0 22 22" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                        <!-- Generator: Sketch 64 (93537) - https://sketch.com -->
                        <desc>Created with Sketch.</desc>
                        <g id="Post-v2" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="01-siderail-template-v1" transform="translate(-1230.000000, -179.000000)" stroke="#FFFFFF">
                                <g id="Group-4" transform="translate(1231.000000, 180.000000)">
                                    <circle id="Oval" stroke-width="2" cx="8" cy="8" r="8"></circle>
                                    <line x1="14.5" y1="14.5" x2="18.25" y2="18.25" id="Line-2" stroke-width="3" stroke-linecap="square"></line>
                                </g>
                            </g>
                        </g>
                        </svg>
                    </div>
                </div>
                <div class="logo t-pos:cntr t-txt:cntr" >
                    <div class="t-pad:10px:lt   t-pad:5px:top t-pad:10px:bot" >
                        <a href="https://timcast.com">
                        <img src="https://timcast.com/wp-content/uploads/2022/03/logo-timcast.svg" alt="TIMCAST" class="t-hide:under:s"/>
                        <img src="https://timcast.com/wp-content/uploads/2022/03/logo-timcast.svg" alt="TIMCAST" class="t-show:under:s mobile"/>
                        </a>
                    </div>
                </div>
                <div class="t-pos:rt t-pad:25pc:rt nav-utility">
                    <ul class="t-menu t-pad:0px:top t-pad:0px:bot t-marg:0px t-pad:5px:rt   txt-light">
                        <li id="menu-item-378502" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-378502"><a href="/wp-login.php/?action=logout">Log Out</a></li>
                        <li id="menu-item-378501" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-378501"><a href="https://timcast.com/login/edit-profile/">EDIT PROFILE</a></li>
                    </ul>
                </div>
                <div class="t-nav-mobile t-bg:blk">
                    <div class="t-nav-scroller">
                        <div class="t-pad:20px:rt t-pad:20px:lt">
                        <ul class="t-menu t-marg:0px t-pad:15px:top t-pad:5px:bot  t-pad:0px:lt t-txt:lt txt-light">
                            <li id="menu-item-154775" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-154775"><a href="/">Home</a></li>
                            <li id="menu-item-154776" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-154776"><a href="/about/">About</a></li>
                            <li id="menu-item-154777" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-154777"><a target="_blank" rel="noopener" href="https://teespring.com/stores/timcast">Store</a></li>
                            <li id="menu-item-154778" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-154778"><a href="/channels/">Watch</a></li>
                            <li id="menu-item-154779" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-154779"><a href="/news/">Read</a></li>
                            <li id="menu-item-154781" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-154781"><a href="/contact/">Contact</a></li>
                            <li id="menu-item-154782" class="border-top menu-item menu-item-type-custom menu-item-object-custom menu-item-154782"><a href="/join-us/">Join Us</a></li>
                            <li id="menu-item-154783" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-154783"><a href="/members-area/">Members Only</a></li>
                        </ul>
                        <div class="non-member-alt">
                            <ul class="t-menu t-marg:0px t-pad:10px:top t-pad:5px:bot  t-pad:0px:lt t-txt:lt txt-light">
                                <li class=" menu-item menu-item-type-custom menu-item-object-custom menu-item-profil">
                                    <a href="/login/edit-profile/">My Profile</a>
                                </li>
                                <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-profil">
                                    <a href="/login/password-reset/">Reset Password</a>
                                </li>
                            </ul>
                        </div>
                        <h3 class="t-txt:clr1 u t-pad:50pc:top">Channels</h3>
                        <div class="t-fnt:1 t-pad:33pc:top channels">
                            <a href="/channel/timcast-irl" class="t-display:block t-pad:15px:bot ">
                            <span class="thumbnail">
                            <img src="https://timcast.com/wp-content/uploads/2021/07/channel_thumb_irl.jpg" alt="TimCast IRL Podcast Channel"/>
                            </span>
                            <span class="title">TimCast IRL Podcast</span></a><a href="/channel/timcast" class="t-display:block t-pad:15px:bot ">
                            <span class="thumbnail">
                            <img src="https://timcast.com/wp-content/uploads/2022/07/image-2.png" alt="Tim Pool Daily Show Channel"/>
                            </span>
                            <span class="title">Tim Pool Daily Show</span></a><a href="/channel/cast-castle" class="t-display:block t-pad:15px:bot ">
                            <span class="thumbnail">
                            <img src="https://timcast.com/wp-content/uploads/2021/12/Cast-Castle-House-no-Glow-PFP.png" alt="Cast Castle Vlog Channel"/>
                            </span>
                            <span class="title">Cast Castle Vlog</span></a><a href="/channel/tales-from-the-inverted-world" class="t-display:block t-pad:15px:bot ">
                            <span class="thumbnail">
                            <img src="https://timcast.com/wp-content/uploads/2021/12/INVERTED-WORLD-PFP-V12.png" alt="Tales from the Inverted World Channel"/>
                            </span>
                            <span class="title">Tales from the Inverted World</span></a><a href="/channel/pop-culture-crisis" class="t-display:block t-pad:15px:bot ">
                            <span class="thumbnail">
                            <img src="https://timcast.com/wp-content/uploads/2021/12/thumb-popculture.jpg" alt="Pop Culture Crisis Channel"/>
                            </span>
                            <span class="title">Pop Culture Crisis</span></a><a href="/channel/chicken-city" class="t-display:block t-pad:15px:bot ">
                            <span class="thumbnail">
                            <img src="https://timcast.com/wp-content/uploads/2022/07/channels4_profile-1.jpg" alt="Chicken-City Channel"/>
                            </span>
                            <span class="title">Chicken-City</span></a>                                        
                        </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="search-box clear t-bg:clr1">
                <div class="t-display:inline-block t-pos:cntr">
                    <div class="t-contain t-pos:cntr t-flex:valign:mid">
                        <span class="search-field">
                        <span class="shadowfield"><input type="text" id="searchfield" name="search" placeholder="Keyword..." ></span>
                        </span>
                        <div class="button:alt btn-search btn-alt">Search</div>
                    </div>
                </div>
            </div>
            </nav>
        </header>
        <div class="t-nav-spacer"></div>
        <main class="t-bg:wht">
            <div class="t-pad:75pc t-bg:clr4 t-txt:cntr t-txt:wht">
            <h1 class="t-txt:h2">Members Only: Timcast IRL</h1>
            </div>
            <div class="t-contain t-pos:cntr">
            <div class="article-links t-pad:25pc:rt t-pad:25pc:lt t-pad:0px:rt:xl t-pad:0px:lt:xl t-pad:bot">
                <div class="t-pad:25pc:top"></div>
                <div class="t-grid:s:fit:2 t-grid:m:fit:4 t-pad:25pc:top">
                    <div class="article ">
                        <div class="article-block ">
                        <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/" class="image" >
                        <img src="https://timcast.com/wp-content/uploads/2022/10/640un-300x169.png" alt="Seth Weathers & Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK" />
                        </a>
                        <div class="meta t-pad:15px:top t-pad:50pc:bot">
                            <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/">
                                <div class="summary">
                                    <h2 class=" t-txt:grey3 t-txt:h4">Seth Weathers & Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK</h2>
                                    <div class="t-txt:xs t-txt:grey1 t-fnt:1 t-pad:5px:top">
                                    10.19.22 				
                                    </div>
                                </div>
                            </a>
                        </div>
                        </div>
                    </div>
                </div>
                <div class="t-contain t-pos:cntr t-txt:cntr  t-marg:top  fnt-secondary">
                    <div class="index-nav"><span class="pgnums"><span class="pgnum"><a href="/members-area/section/timcast-irl/page/1" class="active">1</a></span><span class="pgnum"><a href="/members-area/section/timcast-irl/page/2" class="">2</a></span><span class="pgnum"><a href="/members-area/section/timcast-irl/page/3" class="">3</a></span><span class="pgnum"><a href="/members-area/section/timcast-irl/page/4" class="">4</a></span><span class="pgnum"><a href="/members-area/section/timcast-irl/page/5" class="">5</a></span></span><span class="pag-action next "><a href="/members-area/section/timcast-irl/page/2">Next</a></span></div>
                </div>
            </div>
            </div>
            <div class="t-contain t-pos:cntr">
            <div class="t-pad:50pc:rt t-pad:50pc:lt t-pad:0px:rt:xl t-pad:0px:lt:xl t-txt:lt">
                <hr class="thick " />
            </div>
            <div class="t-pad:top">
                <div class="modules bottom-modules t-contain t-pos:cntr t-pad:25pc:rt t-pad:25pc:lt t-pad:0px:rt:xl t-pad:0px:lt:xl non-member">
                    <div class="t-grid:l:70pc non-member">
                        <div class="">
                        <div class="" >
                            <div class="t-pad:25pc:bot t-marg:25pc:bot t-pad:50pc:rt:l">
                            </div>
                        </div>
                        </div>
                    </div>
                    <div class="t-grid:l:30pc listen-poll-module  t-pad:l-lt">
                        <div class="t-marg:50pc:lt:l">
                        <span class="pretty-header t-marg:50pc:bot  t-display:inline-block">
                            <h3>Popular</h3>
                        </span>
                        <div>
                            <div class="popular t-marg:25pc:top t-pad:50pc:rt:l article-links">
                                <ul class="nobull">
                                    <li>
                                    <a href="https://timcast.com/news/russian-politician-says-moscow-must-freeze-starve-ukrainians-as-winter-approaches/" >
                                        <div class="image" style="background-image:url('https://timcast.com/wp-content/uploads/2022/10/Andrey-Gurulyov.jpg')"></div>
                                        <h4 class="t-txt:sm t-fnt:3 t-fnt:med t-txt:blk"> Russian Politician Says Moscow Must Freeze, Starve...</h4>
                                    </a>
                                    </li>
                                    <li>
                                    <a href="https://timcast.com/news/republicans-submit-legislation-prohibiting-federal-funding-of-sexually-explicit-material-for-children/" >
                                        <div class="image" style="background-image:url('https://timcast.com/wp-content/uploads/2022/10/FED-Funded-Legislat.png')"></div>
                                        <h4 class="t-txt:sm t-fnt:3 t-fnt:med t-txt:blk"> Republicans Submit Legislation Prohibiting Federal...</h4>
                                    </a>
                                    </li>
                                    <li>
                                    <a href="https://timcast.com/news/bmw-to-spend-1-7-billion-on-battery-factory-electric-vehicle-production-in-south-carolina/" >
                                        <div class="image" style="background-image:url('https://timcast.com/wp-content/uploads/2022/10/BMW-Spartansburg-plant-e1666221847871.png')"></div>
                                        <h4 class="t-txt:sm t-fnt:3 t-fnt:med t-txt:blk"> BMW to Spend...</h4>
                                    </a>
                                    </li>
                                    <li>
                                    <a href="https://timcast.com/news/aoc-townhall-forum-descends-into-chaos-as-protesters-take-over-video/" >
                                        <div class="image" style="background-image:url('https://timcast.com/wp-content/uploads/2022/10/1-2.jpg')"></div>
                                        <h4 class="t-txt:sm t-fnt:3 t-fnt:med t-txt:blk"> AOC Townhall Forum Descends Into Chaos As Protesters...</h4>
                                    </a>
                                    </li>
                                    <li>
                                    <a href="https://timcast.com/news/u-k-prime-minister-resigns-after-just-44-days-in-office/" >
                                        <div class="image" style="background-image:url('https://timcast.com/wp-content/uploads/2022/10/Liz-Truss.jpg')"></div>
                                        <h4 class="t-txt:sm t-fnt:3 t-fnt:med t-txt:blk"> ...</h4>
                                    </a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
                <div class="supplimentary-content non-member-alt t-hide">
                    <div class="t-grid:l:30pc ">
                        <span class="pretty-header t-txt:cntr t-display:block t-txt:lt:l t-pad:50pc:lt t-display:block" data-size="no-size">
                        <h3>Shop</h3>
                        </span>
                        <div class="mod mod-m2 t-pad:bot t-pad:25pc:rt t-pad:25pc:lt t-contain t-pos:cntr t-pad:25pc:rt t-pad:25pc:lt show" style="">
                        <div class="  t-txt:cntr:s t-txt:cntr:xs mod-header t-pad:50pc:bot ">
                        </div>
                        <div class="slideshow shop" data-infiniteslide="1" data-dir="" data-autoslide="" data-shownum="0" data-slide="2">
                            <div class="bgimgs slide-view">
                                <ul class="slide-nav nobull">
                                    <li class="btn-prev"><em></em></li>
                                    <li class="btn-next"><em></em></li>
                                </ul>
                                <ul class="slides nobull" style="height: 350px; width: 5900px; left: -1180px; top: 0px;">
                                    <li class="slide s-0 t-img-cntr-m has-image">
                                    <div class="t-valigner">
                                        <div class="t-valign">
                                            <div class="t-contain t-pos:cntr t-pad:33pc:lt slide-content">
                                                <div class="image">
                                                <img src="https://timcast.com/wp-content/uploads/2021/12/howard-springs-2.jpg" alt="Visit Howard Springs" />
                                                </div>
                                            </div>
                                            <a href="https://timcast.creator-spring.com/listing/visit-howard-springs-poster?product=624" target="_blank"></a>
                                        </div>
                                    </div>
                                    </li>
                                    <li class="slide s-0 t-img-cntr-m has-image">
                                    <div class="t-valigner">
                                        <div class="t-valign">
                                            <div class="t-contain t-pos:cntr t-pad:33pc:lt slide-content">
                                                <div class="image">
                                                <img src="https://timcast.com/wp-content/uploads/2021/12/howard-springs-t.jpg" alt="Visit Howard Springs" />
                                                </div>
                                            </div>
                                            <a href="https://timcast.creator-spring.com/listing/visit-howard-springs?product=46" target="_blank"></a>
                                        </div>
                                    </div>
                                    </li>
                                    <li class="slide s-0 t-img-cntr-m has-image">
                                    <div class="t-valigner">
                                        <div class="t-valign">
                                            <div class="t-contain t-pos:cntr t-pad:33pc:lt slide-content">
                                                <div class="image">
                                                <img src="https://timcast.com/wp-content/uploads/2021/12/snek.jpg" alt="Step on Snek and Find Out" />
                                                </div>
                                            </div>
                                            <a href="https://timcast.creator-spring.com/listing/step-on-snek-and-find-out?product=46" target="_blank"></a>
                                        </div>
                                    </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="indicator-box  t-txt:cntr ">
                            <div class="indicator-pos">
                                <ul class="indicator"></ul>
                            </div>
                        </div>
                        </div>
                    </div>
                    <div class="t-grid:l:70pc listen-poll-module  t-pad:lt:l">
                        <div class="popular-big t-marg:25pc:top  article-links">
                        <span class="pretty-header t-marg:50pc:bot  t-display:inline-block  t-pad:15px:lt  t-pad:0px:lt:l">
                            <h3>Popular</h3>
                        </span>
                        <div class="  t-grid:m:fit:2 t-grid:l:fit:3">
                            <div class="article ">
                                <div class="article-block ">
                                    <a href="https://timcast.com/news/russian-politician-says-moscow-must-freeze-starve-ukrainians-as-winter-approaches/" class="image" >
                                    <img src="https://timcast.com/wp-content/uploads/2022/10/Andrey-Gurulyov-300x169.jpg" alt="Russian Politician Says Moscow Must Freeze, Starve Ukrainians as Winter Approaches" />
                                    </a>
                                    <div class="meta t-pad:15px:top t-pad:50pc:bot">
                                    <div class="props">
                                        <a href="/news/category/international" class="cat u b t-marg:5px:bot t-fnt:bold t-txt:u t-txt:xsm ">International</a>
                                    </div>
                                    <a href="https://timcast.com/news/russian-politician-says-moscow-must-freeze-starve-ukrainians-as-winter-approaches/">
                                        <div class="summary">
                                            <h2 class=" t-txt:grey3 t-txt:h4">Russian Politician Says Moscow Must Freeze, Starve Ukrainians as Winter Approaches</h2>
                                            <p class="t-txt:grey4 t-txt:sm ">
                                                A senior Russian politician says that Moscow should cut off electricity to Ukraine ahead of this winter,...				
                                            </p>
                                        </div>
                                    </a>
                                    </div>
                                </div>
                            </div>
                            <div class="article ">
                                <div class="article-block ">
                                    <a href="https://timcast.com/news/republicans-submit-legislation-prohibiting-federal-funding-of-sexually-explicit-material-for-children/" class="image" >
                                    <img src="https://timcast.com/wp-content/uploads/2022/10/FED-Funded-Legislat-300x170.png" alt="Republicans Submit Legislation Prohibiting Federal Funding Of Sexually Explicit Material For Children" />
                                    </a>
                                    <div class="meta t-pad:15px:top t-pad:50pc:bot">
                                    <div class="props">
                                        <a href="/news/category/legislation" class="cat u b t-marg:5px:bot t-fnt:bold t-txt:u t-txt:xsm ">Legislation</a>
                                    </div>
                                    <a href="https://timcast.com/news/republicans-submit-legislation-prohibiting-federal-funding-of-sexually-explicit-material-for-children/">
                                        <div class="summary">
                                            <h2 class=" t-txt:grey3 t-txt:h4">Republicans Submit Legislation Prohibiting Federal Funding Of Sexually Explicit Material For Children</h2>
                                            <p class="t-txt:grey4 t-txt:sm ">
                                                Thirty-three Republican members of Congress introduced a bill called Stop the Sexualization of Children Act...				
                                            </p>
                                        </div>
                                    </a>
                                    </div>
                                </div>
                            </div>
                            <div class="article ">
                                <div class="article-block ">
                                    <a href="https://timcast.com/news/bmw-to-spend-1-7-billion-on-battery-factory-electric-vehicle-production-in-south-carolina/" class="image" >
                                    <img src="https://timcast.com/wp-content/uploads/2022/10/BMW-Spartansburg-plant-300x147.png" alt="BMW to Spend $1.7 Billion on Battery Factory, Electric Vehicle Production in South Carolina" />
                                    </a>
                                    <div class="meta t-pad:15px:top t-pad:50pc:bot">
                                    <div class="props">
                                        <a href="/news/category/big-business" class="cat u b t-marg:5px:bot t-fnt:bold t-txt:u t-txt:xsm ">Big Business</a>
                                    </div>
                                    <a href="https://timcast.com/news/bmw-to-spend-1-7-billion-on-battery-factory-electric-vehicle-production-in-south-carolina/">
                                        <div class="summary">
                                            <h2 class=" t-txt:grey3 t-txt:h4">BMW to Spend $1.7 Billion on Battery Factory, Electric Vehicle Production in South Carolina</h2>
                                            <p class="t-txt:grey4 t-txt:sm ">
                                                Carmaker BMW announced plans to invest $1.7 billion in South Carolina to produce electric vehicles and...				
                                            </p>
                                        </div>
                                    </a>
                                    </div>
                                </div>
                            </div>
                            <div class="article ">
                                <div class="article-block ">
                                    <a href="https://timcast.com/news/aoc-townhall-forum-descends-into-chaos-as-protesters-take-over-video/" class="image" >
                                    <img src="https://timcast.com/wp-content/uploads/2022/10/1-2-300x167.jpg" alt="AOC Townhall Forum Descends Into Chaos As Protesters Take Over (VIDEO)" />
                                    </a>
                                    <div class="meta t-pad:15px:top t-pad:50pc:bot">
                                    <div class="props">
                                        <a href="/news/category/politics" class="cat u b t-marg:5px:bot t-fnt:bold t-txt:u t-txt:xsm ">Politics</a>
                                    </div>
                                    <a href="https://timcast.com/news/aoc-townhall-forum-descends-into-chaos-as-protesters-take-over-video/">
                                        <div class="summary">
                                            <h2 class=" t-txt:grey3 t-txt:h4">AOC Townhall Forum Descends Into Chaos As Protesters Take Over (VIDEO)</h2>
                                            <p class="t-txt:grey4 t-txt:sm ">
                                                A town hall event held by New York Rep. Alexandria Ocasio-Cortez descended into chaos when a large group of...				
                                            </p>
                                        </div>
                                    </a>
                                    </div>
                                </div>
                            </div>
                            <div class="article ">
                                <div class="article-block ">
                                    <a href="https://timcast.com/news/u-k-prime-minister-resigns-after-just-44-days-in-office/" class="image" >
                                    <img src="https://timcast.com/wp-content/uploads/2022/10/Liz-Truss-300x169.jpg" alt="U.K. Prime Minister Resigns After Just 44 Days in Office" />
                                    </a>
                                    <div class="meta t-pad:15px:top t-pad:50pc:bot">
                                    <div class="props">
                                        <a href="/news/category/world-news" class="cat u b t-marg:5px:bot t-fnt:bold t-txt:u t-txt:xsm ">World News</a>
                                    </div>
                                    <a href="https://timcast.com/news/u-k-prime-minister-resigns-after-just-44-days-in-office/">
                                        <div class="summary">
                                            <h2 class=" t-txt:grey3 t-txt:h4">U.K. Prime Minister Resigns After Just 44 Days in Office</h2>
                                            <p class="t-txt:grey4 t-txt:sm ">
                                                U.K. Prime Minister Liz Truss has announced her resignation after just 44 days in office, making her the...				
                                            </p>
                                        </div>
                                    </a>
                                    </div>
                                </div>
                            </div>
                            <div class="article ">
                                <div class="article-block ">
                                    <a href="https://timcast.com/news/ohio-supreme-court-suspends-judge-for-presiding-like-a-game-show-host/" class="image" >
                                    <img src="https://timcast.com/wp-content/uploads/2022/10/Pinkey-Carr-300x173.png" alt="Ohio Supreme Court Suspends Judge for Presiding like 'A Game Show Host'" />
                                    </a>
                                    <div class="meta t-pad:15px:top t-pad:50pc:bot">
                                    <div class="props">
                                        <a href="/news/category/legal" class="cat u b t-marg:5px:bot t-fnt:bold t-txt:u t-txt:xsm ">Legal</a>
                                    </div>
                                    <a href="https://timcast.com/news/ohio-supreme-court-suspends-judge-for-presiding-like-a-game-show-host/">
                                        <div class="summary">
                                            <h2 class=" t-txt:grey3 t-txt:h4">Ohio Supreme Court Suspends Judge for Presiding like 'A Game Show Host'</h2>
                                            <p class="t-txt:grey4 t-txt:sm ">
                                                The Supreme Court of Ohio has indefinitely suspended a municipal judge and removed her from office after...				
                                            </p>
                                        </div>
                                    </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
                <div class="t-txt:cntr t-contain t-pos:cntr">
                    <div class="t-hide:under:m">
                        <div class="banner-ad non-member t-pad:bot t-pad:50pc:bot:m">		
                        </div>
                    </div>
                    <div class="t-show:under:m">
                        <div class="banner-ad non-member t-pad:50pc:bot t-pad:50pc:bot:l ">
                        <div data-pw-mobi="leaderboard_btf"></div>
                        </div>
                    </div>
                </div>
            </div>
            </div>
            <footer class="t-pad:50pc:bot t-bg:grey3 t-pad:25pc:top:xs t-pad:50pc:top">
            <div class="  t-contain t-pos:cntr   ">
                <div class="t-grid:m:30pc ">
                    <ul class="social-links t-txt:cntr:xs social-links t-txt:cntr:m">
                        <li id="menu-item-150315"><a href="https://www.facebook.com/timcastnews/"  class="fa fa-facebook menu-item menu-item-type-custom menu-item-object-custom"><span class="txt"><strong>Facebook</strong></span></a></li>
                        <li id="menu-item-150316"><a href="https://twitter.com/timcast"  class="fa fa-twitter menu-item menu-item-type-custom menu-item-object-custom"><span class="txt"><strong>Twitter</strong></span></a></li>
                        <li id="menu-item-150317"><a href="https://www.linkedin.com/in/timothy-pool-7228ba25"  class="fa fa-linkedin menu-item menu-item-type-custom menu-item-object-custom"><span class="txt"><strong>LinkedIn</strong></span></a></li>
                        <li id="menu-item-150318"><a href="https://www.youtube.com/channel/UCG749Dj4V2fKa143f8sE60Q"  class="fa fa-youtube menu-item menu-item-type-custom menu-item-object-custom"><span class="txt"><strong>YouTube</strong></span></a></li>
                        <li id="menu-item-150319"><a href="https://www.instagram.com/timcast/"  class="fa fa-instagram menu-item menu-item-type-custom menu-item-object-custom"><span class="txt"><strong>Instagram</strong></span></a></li>
                    </ul>
                </div>
                <div class="t-show:under:m t-pad:25pc:top:xs">
                    <hr/>
                </div>
                <div class=" footer-copyright t-txt:med t-txt:wht t-pad:0px t-fnt:1 t-grid:m:70pc t-txt:rt t-pad:top:m t-pad:50pc:top:l t-marg:bot">
                    <div class="t-flex:m:valign:mid t-flex:m:align:rt  t-pad:25pc:top:xs">
                        <ul class="t-menu t-txt:clr3 t-txt:cntr:s t-txt:cntr:xs t-txt:cntr:xs  t-txt:u t-txt:med t-marg:0px:bot t-marg:25px:rt:m t-marg:50pc:rt:l">
                        <li id="menu-item-150320" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-150320"><a href="/privacy-policy/">Privacy Policy</a></li>
                        <li id="menu-item-150321" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-150321"><a href="/terms-of-service/">Terms of Service</a></li>
                        <li class="t-txt:wht">Copyright &copy; 2022 TIMCAST</li>
                        </ul>
                    </div>
                </div>
            </div>
            </footer>
        </main>
    </div>
    <script type='text/javascript' src='https://timcast.com/wp-content/plugins/metronet-profile-picture/js/mpp-frontend.js?ver=2.6.0' id='mpp_gutenberg_tabs-js'></script>
    <script type='text/javascript' src='https://timcast.com/wp-includes/js/dist/vendor/regenerator-runtime.min.js?ver=0.13.9' id='regenerator-runtime-js'></script>
    <script type='text/javascript' src='https://timcast.com/wp-includes/js/dist/vendor/wp-polyfill.min.js?ver=3.15.0' id='wp-polyfill-js'></script>
    <script type='text/javascript' id='contact-form-7-js-extra'>
        /* <![CDATA[ */
        var wpcf7 = {"api":{"root":"https:\/\/timcast.com\/wp-json\/","namespace":"contact-form-7\/v1"}};
        /* ]]> */
    </script>
    <script type='text/javascript' src='https://timcast.com/wp-content/plugins/contact-form-7/includes/js/index.js?ver=5.5.6' id='contact-form-7-js'></script>
    <script type='text/javascript' src='https://www.google.com/recaptcha/api.js?render=6Lec1_gdAAAAALY6mafp3kZgPpkAYDwil4OqMmoH&#038;ver=3.0' id='google-recaptcha-js'></script>
    <script type='text/javascript' id='wpcf7-recaptcha-js-extra'>
        /* <![CDATA[ */
        var wpcf7_recaptcha = {"sitekey":"6Lec1_gdAAAAALY6mafp3kZgPpkAYDwil4OqMmoH","actions":{"homepage":"homepage","contactform":"contactform"}};
        /* ]]> */
    </script>
    <script type='text/javascript' src='https://timcast.com/wp-content/plugins/contact-form-7/modules/recaptcha/index.js?ver=5.5.6' id='wpcf7-recaptcha-js'></script>
    <script type="text/javascript" id="wpsp-script-frontend"></script>
    <!-- ========================== End Footer / End Page Bottom   ============================= -->
    <script src="https://player.vimeo.com/api/player.js" ></script>
    <script src="https://timcast.com/wp-content/themes/timcast/scripts.js?uc=<1665524704"></script>
</body>
</html>
'''
RSP1 = '''
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
    <link rel="apple-touch-icon" sizes="180x180" href="https://timcast.com/wp-content/themes/timcast/favicons/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="https://timcast.com/wp-content/themes/timcast/favicons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="https://timcast.com/wp-content/themes/timcast/favicons/favicon-16x16.png">
    <link rel="manifest" href="https://timcast.com/wp-content/themes/timcast/favicons/site.webmanifest">
    <link rel="mask-icon" href="https://timcast.com/wp-content/themes/timcast/favicons/safari-pinned-tab.svg" color="#000000">
    <meta name="msapplication-TileColor" content="#000000">
    <meta name="theme-color" content="#ffffff">
    <!-- for Facebook -->  
    <meta property="og:type" content="website" />
    <meta property="og:title" content="Seth Weathers &#038; Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK | TIMCAST" />
    <meta property="og:description" content="" />
    <meta property="og:url" content="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/" />
    <meta property="og:image" content="https://timcast.com/wp-content/uploads/2022/10/640un-1024x576.png" />
    <!-- for Twitter -->          
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Seth Weathers &#038; Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK | TIMCAST" />
    <meta name="twitter:description" content="" />
    <meta name="twitter:image" content="https://timcast.com/wp-content/uploads/2022/10/640un-1024x576.png" />
    <meta property="article:published_time" content="2022-10-19T22:49:13+00:00">
    <link rel="apple-touch-icon" href="apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,300;0,400;0,600;1,300;1,400&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400&display=swap" rel="stylesheet">
    <!-- <script src="/var/www/timcast.com/html/wp-content/themes/thundercracker/assets/js/vendor/modernizr-2.8.3.min.js"></script> -->
    <meta name='robots' content='noindex, follow' />
    <!-- This site is optimized with the Yoast SEO plugin v18.7 - https://yoast.com/wordpress/plugins/seo/ -->
    <title>Seth Weathers &amp; Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK | TIMCAST</title>
    <meta property="og:locale" content="en_US" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="Seth Weathers &amp; Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK | TIMCAST" />
    <meta property="og:description" content="*For corrections please email corrections@timcast.com*" />
    <meta property="og:url" content="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/" />
    <meta property="og:site_name" content="TIMCAST" />
    <meta property="article:publisher" content="http://www.facebook.com/timcastnews" />
    <meta property="article:published_time" content="2022-10-20T02:49:13+00:00" />
    <meta property="og:image" content="https://timcast.com/wp-content/uploads/2022/10/640un.png" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="675" />
    <meta property="og:image:type" content="image/png" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:creator" content="@timcast" />
    <meta name="twitter:site" content="@timcast" />
    <meta name="twitter:label1" content="Written by" />
    <meta name="twitter:data1" content="Tim Pool" />
    <script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://timcast.com/#organization","name":"Timcast","url":"https://timcast.com/","sameAs":["http://www.facebook.com/timcastnews","https://www.instagram.com/timcast/","https://www.linkedin.com/in/timothy-pool-7228ba25/","http://www.youtube.com/timcast","https://en.wikipedia.org/wiki/Tim_Pool","https://twitter.com/timcast"],"logo":{"@type":"ImageObject","inLanguage":"en-US","@id":"https://timcast.com/#/schema/logo/image/","url":"https://timcast.com/wp-content/uploads/2021/01/cropped-FAVICON-1-2.jpg","contentUrl":"https://timcast.com/wp-content/uploads/2021/01/cropped-FAVICON-1-2.jpg","width":512,"height":512,"caption":"Timcast"},"image":{"@id":"https://timcast.com/#/schema/logo/image/"}},{"@type":"WebSite","@id":"https://timcast.com/#website","url":"https://timcast.com/","name":"TIMCAST","description":"timcast.com","publisher":{"@id":"https://timcast.com/#organization"},"potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://timcast.com/?s={search_term_string}"},"query-input":"required name=search_term_string"}],"inLanguage":"en-US"},{"@type":"ImageObject","inLanguage":"en-US","@id":"https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#primaryimage","url":"https://timcast.com/wp-content/uploads/2022/10/640un.png","contentUrl":"https://timcast.com/wp-content/uploads/2022/10/640un.png","width":1200,"height":675},{"@type":"WebPage","@id":"https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#webpage","url":"https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/","name":"Seth Weathers & Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK | TIMCAST","isPartOf":{"@id":"https://timcast.com/#website"},"primaryImageOfPage":{"@id":"https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#primaryimage"},"datePublished":"2022-10-20T02:49:13+00:00","dateModified":"2022-10-20T02:49:13+00:00","breadcrumb":{"@id":"https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/"]}]},{"@type":"BreadcrumbList","@id":"https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://timcast.com/"},{"@type":"ListItem","position":2,"name":"Seth Weathers &#038; Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK"}]},{"@type":"Article","@id":"https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#article","isPartOf":{"@id":"https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#webpage"},"author":{"@id":"https://timcast.com/#/schema/person/2cd6918cebea6818bf24467b043c927c"},"headline":"Seth Weathers &#038; Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK","datePublished":"2022-10-20T02:49:13+00:00","dateModified":"2022-10-20T02:49:13+00:00","mainEntityOfPage":{"@id":"https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#webpage"},"wordCount":14,"commentCount":41,"publisher":{"@id":"https://timcast.com/#organization"},"image":{"@id":"https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#primaryimage"},"thumbnailUrl":"https://timcast.com/wp-content/uploads/2022/10/640un.png","articleSection":["Members $10","Members $100","Members $1000","Members $25","Members $50","Members $500","Members Custom"],"inLanguage":"en-US","potentialAction":[{"@type":"CommentAction","name":"Comment","target":["https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#respond"]}]},{"@type":"Person","@id":"https://timcast.com/#/schema/person/2cd6918cebea6818bf24467b043c927c","name":"Tim Pool","image":{"@type":"ImageObject","inLanguage":"en-US","@id":"https://timcast.com/#/schema/person/image/","url":"https://secure.gravatar.com/avatar/2dacec5bdb1ced7c79789be015042e26?s=96&r=g","contentUrl":"https://secure.gravatar.com/avatar/2dacec5bdb1ced7c79789be015042e26?s=96&r=g","caption":"Tim Pool"}}]}</script>
    <!-- / Yoast SEO plugin. -->
    <link rel='dns-prefetch' href='//www.google.com' />
    <link rel='dns-prefetch' href='//s.w.org' />
    <link rel="alternate" type="application/rss+xml" title="TIMCAST &raquo; Seth Weathers &#038; Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK Comments Feed" href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/feed/" />
    <link rel='stylesheet' id='mp-theme-css'  href='https://timcast.com/wp-content/plugins/memberpress/css/ui/theme.css?ver=1.9.37' type='text/css' media='all' />
    <link rel='stylesheet' id='wp-block-library-css'  href='https://timcast.com/wp-includes/css/dist/block-library/style.min.css?ver=5.9.5' type='text/css' media='all' />
    <link rel='stylesheet' id='mpp_gutenberg-css'  href='https://timcast.com/wp-content/plugins/metronet-profile-picture/dist/blocks.style.build.css?ver=2.6.0' type='text/css' media='all' />
    <style id='global-styles-inline-css' type='text/css'>
        body{--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--duotone--dark-grayscale: url('#wp-duotone-dark-grayscale');--wp--preset--duotone--grayscale: url('#wp-duotone-grayscale');--wp--preset--duotone--purple-yellow: url('#wp-duotone-purple-yellow');--wp--preset--duotone--blue-red: url('#wp-duotone-blue-red');--wp--preset--duotone--midnight: url('#wp-duotone-midnight');--wp--preset--duotone--magenta-yellow: url('#wp-duotone-magenta-yellow');--wp--preset--duotone--purple-green: url('#wp-duotone-purple-green');--wp--preset--duotone--blue-orange: url('#wp-duotone-blue-orange');--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
    </style>
    <link rel='stylesheet' id='contact-form-7-css'  href='https://timcast.com/wp-content/plugins/contact-form-7/includes/css/styles.css?ver=5.5.6' type='text/css' media='all' />
    <link rel='stylesheet' id='dashicons-css'  href='https://timcast.com/wp-includes/css/dashicons.min.css?ver=5.9.5' type='text/css' media='all' />
    <link rel='stylesheet' id='if-menu-site-css-css'  href='https://timcast.com/wp-content/plugins/if-menu/assets/if-menu-site.css?ver=5.9.5' type='text/css' media='all' />
    <link rel='stylesheet' id='parent-style-css'  href='https://timcast.com/wp-content/themes/timcast/style.css?ver=1665524704' type='text/css' media='all' />
    <script type='text/javascript' src='https://timcast.com/wp-includes/js/jquery/jquery.min.js?ver=3.6.0' id='jquery-core-js'></script>
    <script type='text/javascript' src='https://timcast.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.3.2' id='jquery-migrate-js'></script>
    <link rel="https://api.w.org/" href="https://timcast.com/wp-json/" />
    <link rel="alternate" type="application/json" href="https://timcast.com/wp-json/wp/v2/posts/741122" />
    <link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://timcast.com/xmlrpc.php?rsd" />
    <link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://timcast.com/wp-includes/wlwmanifest.xml" />
    <meta name="generator" content="WordPress 5.9.5" />
    <link rel='shortlink' href='https://timcast.com/?p=741122' />
    <link rel="alternate" type="application/json+oembed" href="https://timcast.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftimcast.com%2Fmembers-area%2Fseth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak%2F" />
    <link rel="alternate" type="text/xml+oembed" href="https://timcast.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftimcast.com%2Fmembers-area%2Fseth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak%2F&#038;format=xml" />
    <!-- Schema optimized by Schema Pro --><!-- / Schema optimized by Schema Pro --><!-- breadcrumb Schema optimized by Schema Pro --><script type="application/ld+json">{"@context":"https:\/\/schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"item":{"@id":"https:\/\/timcast.com\/","name":"Home"}},{"@type":"ListItem","position":2,"item":{"@id":"https:\/\/timcast.com\/members-area\/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak\/","name":"Seth Weathers &#038; Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK"}}]}</script><!-- / breadcrumb Schema optimized by Schema Pro -->			
    <style id="wpsp-style-frontend"></style>
    <link rel="icon" href="https://timcast.com/wp-content/uploads/2021/11/cropped-android-chrome-512x512-1-32x32.png" sizes="32x32" />
    <link rel="icon" href="https://timcast.com/wp-content/uploads/2021/11/cropped-android-chrome-512x512-1-192x192.png" sizes="192x192" />
    <link rel="apple-touch-icon" href="https://timcast.com/wp-content/uploads/2021/11/cropped-android-chrome-512x512-1-180x180.png" />
    <meta name="msapplication-TileImage" content="https://timcast.com/wp-content/uploads/2021/11/cropped-android-chrome-512x512-1-270x270.png" />

    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
        new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window,document,'script','dataLayer','GTM-KK9GLZ4');
    </script>
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
        new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window,document,'script','dataLayer','GTM-KG5GK79');
    </script>
    <!-- End Google Tag Manager -->
    <script defer src="https://users.api.jeeng.com/users/domains/3AJQ2Jdkl1/sdk/"></script>
    <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-60e766933db1abcb"></script> 
    <script src="https://script.metricode.com/wotjs/ellipsis.js?api_key=4fe7fc4c-f02b-496b-b68a-842f46bd7627"></script>
    <!-- Revcontent ad style adjustments --> 
</head>
<body style=" opacity:0"  class="t-bg:grey3  " >
    <div class="t-bg:blk">
        <!--[if lt IE 8]>
        <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->
        <header id="t-scrollnav-holder" class="t-bg:wht">
            <nav  id="t-scrollnav" >
            <div class="t-pos:cntr t-pos:rel t-bg:grey3 flex-nav">
                <div class="nav-and-search">
                    <div class="t-button-mobile-menu">
                        <div class="t-toggle-icon"></div>
                    </div>
                    <div class="btn-search">
                        <svg width="22px" height="22px" viewBox="0 0 22 22" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                        <!-- Generator: Sketch 64 (93537) - https://sketch.com -->
                        <desc>Created with Sketch.</desc>
                        <g id="Post-v2" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="01-siderail-template-v1" transform="translate(-1230.000000, -179.000000)" stroke="#FFFFFF">
                                <g id="Group-4" transform="translate(1231.000000, 180.000000)">
                                    <circle id="Oval" stroke-width="2" cx="8" cy="8" r="8"></circle>
                                    <line x1="14.5" y1="14.5" x2="18.25" y2="18.25" id="Line-2" stroke-width="3" stroke-linecap="square"></line>
                                </g>
                            </g>
                        </g>
                        </svg>
                    </div>
                </div>
                <div class="logo t-pos:cntr t-txt:cntr" >
                    <div class="t-pad:10px:lt   t-pad:5px:top t-pad:10px:bot" >
                        <a href="https://timcast.com">
                        <img src="https://timcast.com/wp-content/uploads/2022/03/logo-timcast.svg" alt="TIMCAST" class="t-hide:under:s"/>
                        <img src="https://timcast.com/wp-content/uploads/2022/03/logo-timcast.svg" alt="TIMCAST" class="t-show:under:s mobile"/>
                        </a>
                    </div>
                </div>
                <div class="t-pos:rt t-pad:25pc:rt nav-utility">
                    <ul class="t-menu t-pad:0px:top t-pad:0px:bot t-marg:0px t-pad:5px:rt   txt-light">
                        <li id="menu-item-378502" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-378502"><a href="/wp-login.php/?action=logout">Log Out</a></li>
                        <li id="menu-item-378501" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-378501"><a href="https://timcast.com/login/edit-profile/">EDIT PROFILE</a></li>
                    </ul>
                </div>
                <div class="t-nav-mobile t-bg:blk">
                    <div class="t-nav-scroller">
                        <div class="t-pad:20px:rt t-pad:20px:lt">
                        <ul class="t-menu t-marg:0px t-pad:15px:top t-pad:5px:bot  t-pad:0px:lt t-txt:lt txt-light">
                            <li id="menu-item-154775" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-154775"><a href="/">Home</a></li>
                            <li id="menu-item-154776" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-154776"><a href="/about/">About</a></li>
                            <li id="menu-item-154777" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-154777"><a target="_blank" rel="noopener" href="https://teespring.com/stores/timcast">Store</a></li>
                            <li id="menu-item-154778" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-154778"><a href="/channels/">Watch</a></li>
                            <li id="menu-item-154779" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-154779"><a href="/news/">Read</a></li>
                            <li id="menu-item-154781" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-154781"><a href="/contact/">Contact</a></li>
                            <li id="menu-item-154782" class="border-top menu-item menu-item-type-custom menu-item-object-custom menu-item-154782"><a href="/join-us/">Join Us</a></li>
                            <li id="menu-item-154783" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-154783"><a href="/members-area/">Members Only</a></li>
                        </ul>
                        <div class="non-member-alt">
                            <ul class="t-menu t-marg:0px t-pad:10px:top t-pad:5px:bot  t-pad:0px:lt t-txt:lt txt-light">
                                <li class=" menu-item menu-item-type-custom menu-item-object-custom menu-item-profil">
                                    <a href="/login/edit-profile/">My Profile</a>
                                </li>
                                <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-profil">
                                    <a href="/login/password-reset/">Reset Password</a>
                                </li>
                            </ul>
                        </div>
                        <h3 class="t-txt:clr1 u t-pad:50pc:top">Channels</h3>
                        <div class="t-fnt:1 t-pad:33pc:top channels">
                            <a href="/channel/timcast-irl" class="t-display:block t-pad:15px:bot ">
                            <span class="thumbnail">
                            <img src="https://timcast.com/wp-content/uploads/2021/07/channel_thumb_irl.jpg" alt="TimCast IRL Podcast Channel"/>
                            </span>
                            <span class="title">TimCast IRL Podcast</span></a><a href="/channel/timcast" class="t-display:block t-pad:15px:bot ">
                            <span class="thumbnail">
                            <img src="https://timcast.com/wp-content/uploads/2022/07/image-2.png" alt="Tim Pool Daily Show Channel"/>
                            </span>
                            <span class="title">Tim Pool Daily Show</span></a><a href="/channel/cast-castle" class="t-display:block t-pad:15px:bot ">
                            <span class="thumbnail">
                            <img src="https://timcast.com/wp-content/uploads/2021/12/Cast-Castle-House-no-Glow-PFP.png" alt="Cast Castle Vlog Channel"/>
                            </span>
                            <span class="title">Cast Castle Vlog</span></a><a href="/channel/tales-from-the-inverted-world" class="t-display:block t-pad:15px:bot ">
                            <span class="thumbnail">
                            <img src="https://timcast.com/wp-content/uploads/2021/12/INVERTED-WORLD-PFP-V12.png" alt="Tales from the Inverted World Channel"/>
                            </span>
                            <span class="title">Tales from the Inverted World</span></a><a href="/channel/pop-culture-crisis" class="t-display:block t-pad:15px:bot ">
                            <span class="thumbnail">
                            <img src="https://timcast.com/wp-content/uploads/2021/12/thumb-popculture.jpg" alt="Pop Culture Crisis Channel"/>
                            </span>
                            <span class="title">Pop Culture Crisis</span></a><a href="/channel/chicken-city" class="t-display:block t-pad:15px:bot ">
                            <span class="thumbnail">
                            <img src="https://timcast.com/wp-content/uploads/2022/07/channels4_profile-1.jpg" alt="Chicken-City Channel"/>
                            </span>
                            <span class="title">Chicken-City</span></a>                                        
                        </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="search-box clear t-bg:clr1">
                <div class="t-display:inline-block t-pos:cntr">
                    <div class="t-contain t-pos:cntr t-flex:valign:mid">
                        <span class="search-field">
                        <span class="shadowfield"><input type="text" id="searchfield" name="search" placeholder="Keyword..." ></span>
                        </span>
                        <div class="button:alt btn-search btn-alt">Search</div>
                    </div>
                </div>
            </div>
            </nav>
        </header>
        <div class="t-nav-spacer"></div>
        <main class="t-bg:wht">
            <div class="bg:pattern t-txt:wht" >
            <div class="t-contain t-pos:cntr">
                <div class="t-txt:cntr t-contain t-pos:cntr t-pad:top">
                    <div class="banner-ad non-member t-pad:bot">
                        <a href="https://amzn.to/3AZ8puK" target="_blank"><img src="https://timcast.com/wp-content/uploads/2022/02/TIMCAST-Ad-2.png"></a>
                        <!--- <div id="rc-widget-914547" data-rc-widget data-widget-host="habitat" data-endpoint="//trends.revcontent.com" data-widget-id="267304"></div>
                        <script type="text/javascript" src="https://assets.revcontent.com/master/delivery.js" defer="defer"></script> -->
                    </div>
                </div>
                <div class="columns t-pad:10px:lt:xs t-pad:10px:rt:xs t-pad:25pc:lt t-pad:25pc:rt ">
                    <div class="t-grid:l:70pc ">
                        <article>
                        <div class="article-header t-pad:33pc:bot">
                            <h1 class="t-pad:25pc:top t-fnt:1">Seth Weathers & Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK</h1>
                            <hr class="thick t-marg:15px:top " />
                            <div class="article-meta ">
                                <div class="t-txt:sm t-txt:u t-display:inline-block">Published: October 19, 2022</div>
                                <div class="t-display:inline-block t-txt:sm t-txt:u ">&nbsp; | &nbsp; By <a href="/author/timcast" class="auth-link">Tim Pool</a></div>
                            </div>
                        </div>
                        <div class="article-container">
                            <div class="article-img t-img:cntr:m   t-marg:50pc:bot"  style="
                                ">
                                <div>
                                </div>
                            </div>
                            <div class="article-content t-pad:50pc:top">
                                <div class="t-grid:m:fit:1 non-member">
                                    <div>
                                    <p><iframe loading="lazy" class="rumble" width="640" height="360" src="%%URL%%" frameborder="0" allowfullscreen></iframe></p>
                                    <div class='code-block code-block-1' style='margin: 8px 0; clear: both;'>
                                        <i>*For corrections please email <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="eb888499998e889f82848598ab9f8286888a989fc5888486">[email&#160;protected]</a>*</i>
                                    </div>
                                    <!-- AI CONTENT END 1 -->
                                    </div>
                                    <div class="t-pad:bot t-pad:top t-pad:0px:top:m t-pad:0px:top:l t-marg:bot">
                                    </div>
                                </div>
                                <div class="non-member-alt">
                                    <div>
                                    <iframe class="rumble" width="640" height="360" src="%%URL%%" frameborder="0" allowfullscreen></iframe>                   
                                    </div>
                                </div>
                                <div class="banner-ad non-member  t-pad:50pc:top ">
                                    <a href="https://amzn.to/3AZ8puK" target="_blank"><img src="https://timcast.com/wp-content/uploads/2022/02/TIMCAST-Ad-1.png"></a>
                                    <!-- <div id="rc-widget-98ddff" data-rc-widget data-widget-host="habitat" data-endpoint="//trends.revcontent.com" data-widget-id="267303"></div>
                                    <script type="text/javascript" src="https://assets.revcontent.com/master/delivery.js" defer="defer"></script>-->
                                </div>
                                <div class="sharelinks t-marg:top t-marg:50pc:top">
                                    <hr class="no-size no-marg"/>
                                    <div class=" alignshare t-marg:25pc:top">
                                    <span class="t-txt:h4  txt-share t-fnt:1 t-txt:u t-marg:10px:rt">Share<span></span></span>
                                    <!-- Go to www.addthis.com/dashboard to customize your tools --> 
                                    <div class="addthis_inline_share_toolbox addthis-links"  data-url="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/" data-title="Seth Weathers & Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK" data-description="" data-media="https://timcast.com/wp-content/uploads/2022/10/640un.png"></div>
                                    </div>
                                    <hr class="no-size no-marg"/>
                                </div>
                                <div class="next-article t-flex:s:valign:topm t-pad:50pc:bot">
                                    <div class="next-txt colon-red t-txt:h4 t-pad:10px:bot t-pad:10px:rt t-fnt:1">Next<span></span></div>
                                    <div class="">
                                    <div class="article ">
                                        <div class="article-block ">
                                            <a href="https://timcast.com/members-area/ammon-bundy-uncensored-show-ammon-tells-insane-story-of-fbi-corruption-and-government-attempt-to-steal-land-and-destroy-lives/" class="image" >
                                            <img src="https://timcast.com/wp-content/uploads/2022/10/639un-300x169.png" alt="Ammon Bundy Uncensored Show: Ammon Tells INSANE Story Of FBI Corruption And Government Attempt To Steal Land And Destroy Lives" />
                                            </a>
                                            <div class="meta t-pad:15px:top t-pad:50pc:bot">
                                                <a href="https://timcast.com/members-area/ammon-bundy-uncensored-show-ammon-tells-insane-story-of-fbi-corruption-and-government-attempt-to-steal-land-and-destroy-lives/">
                                                <div class="summary">
                                                    <h2 class=" t-txt:grey3 t-txt:h4">Ammon Bundy Uncensored Show: Ammon Tells INSANE Story Of FBI Corruption And Government Attempt To Steal Land And Destroy Lives</h2>
                                                    <div class="t-txt:xs t-txt:grey1 t-fnt:1 t-pad:5px:top">
                                                        10.18.22 					<span class=" auth">  | Tim Pool</span> 
                                                    </div>
                                                </div>
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                    </div>
                                    <hr class="no-size no-marg"/>
                                </div>
                                <div class="comments t-marg:50pc:bot">
                                    <!-- You can start editing here. -->
                                    <h3 id="comments">
                                    41 responses to &#8220;Seth Weathers &#038; Megan Hansen Uncensored Show: Crew Talks Nutrition And Plastics Making Men WEAK&#8221;	
                                    </h3>
                                    <div class="navigation">
                                    <div class="alignleft"></div>
                                    <div class="alignright"></div>
                                    </div>
                                    <ol class="commentlist">
                                    <li class="comment byuser comment-author-jo_momma69 even thread-even depth-1" id="comment-49677">
                                        <div id="div-comment-49677" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/591e580ae40487123abc7a09ab24396b?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/591e580ae40487123abc7a09ab24396b?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Reilly Cassel</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49677">October 20, 2022 at 9:58 am</a>		
                                            </div>
                                            <p>Smoke cigarettes. Drink lots of non fluoride water out of glass jars. Fast twice a week. No meat on fridays. Cut out sugar and processed foods. Work a manual labor job. </p>
                                            <p>I lost 40 lbs in a month and started sleeping way better. I feel better and have way more energy</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-ford42 odd alt thread-odd thread-alt depth-1" id="comment-49676">
                                        <div id="div-comment-49676" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/ab71812af4e2ef31d3c3bd4ecd4ebfe9?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/ab71812af4e2ef31d3c3bd4ecd4ebfe9?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Ford42</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49676">October 20, 2022 at 9:36 am</a>		
                                            </div>
                                            <p>Ian: &#8220;Necks, tho.&#8221; 🙄</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-freighttrain172002gmail-com even thread-even depth-1" id="comment-49675">
                                        <div id="div-comment-49675" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/d07c47f876c1f187829396231ed1a014?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/d07c47f876c1f187829396231ed1a014?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn"><a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="1d7b6f78747a7569696f7c74732c2a2f2d2d2f5d7a707c7471337e7270">[email&#160;protected]</a></cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49675">October 20, 2022 at 9:27 am</a>		
                                            </div>
                                            <p>Why wasn’t she on the main show? 😍🥰</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-strangerthanyouthink odd alt thread-odd thread-alt depth-1" id="comment-49674">
                                        <div id="div-comment-49674" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/8fcb11bbc3c29bd49ee0f44195d3e22b?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/8fcb11bbc3c29bd49ee0f44195d3e22b?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Strangerthanyouthink</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49674">October 20, 2022 at 9:19 am</a>		
                                            </div>
                                            <p>This felt like a fake opinionated nutrition discussion</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-boganlarker even thread-even depth-1" id="comment-49673">
                                        <div id="div-comment-49673" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/29eb2e51114c793fcb375fadc1a99bdf?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/29eb2e51114c793fcb375fadc1a99bdf?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Logan Barker</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49673">October 20, 2022 at 8:51 am</a>		
                                            </div>
                                            <p>Tim regarding the red meat making you sick, have you been bitten by any ticks lately? Some ticks carry the alpha gal disease that causes you to become allergic to red meats.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-louis odd alt thread-odd thread-alt depth-1" id="comment-49672">
                                        <div id="div-comment-49672" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/92859ce6357a45fb12ad09ab0a44d6e0?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/92859ce6357a45fb12ad09ab0a44d6e0?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Louis</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49672">October 20, 2022 at 8:41 am</a>		
                                            </div>
                                            <p>I&#8217;ve studied Nutrition, and that was the lowest IQ discussion on &#8220;health&#8221; that I&#8217;ve ever heard. Wow, just wow. The pseudoscience and quackery was real. Stop seed oils and you won&#8217;t need sunscreen and getting 150g of protein from one meal? My God, what utter foolishness.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-freewitch even thread-even depth-1" id="comment-49671">
                                        <div id="div-comment-49671" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/b4dfeca087c3232d8f83153f52254dbc?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/b4dfeca087c3232d8f83153f52254dbc?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">freewitch</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49671">October 20, 2022 at 8:18 am</a>		
                                            </div>
                                            <p>I&#8217;ve cut out seed oils, leafy greens &amp; sugars/grains since Oct 2021. Before then, I had such bad autoimmune brain fog, that I was about to file for disability because my cognitive abilities were so impaired that I couldn&#8217;t perform simple tasks. Within 2 months I was literally cured. I was able to work again, many other additional issues I had vanished as well. Also I can confirm that I do not get sunburn anymore either. Seed oil is actually legit poison.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-yourmom6969 odd alt thread-odd thread-alt depth-1" id="comment-49669">
                                        <div id="div-comment-49669" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/9c3f3cc4a9b6cefd1736a40157664962?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/9c3f3cc4a9b6cefd1736a40157664962?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Your Mom</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49669">October 20, 2022 at 7:46 am</a>		
                                            </div>
                                            <p>@BigJoe77<br />
                                                No. Cannibalism is not vegan. To be a cannibal, you have to eat people, and vegans are not people. HOWEVER eating a diet that consists of vegans (not to be confused with a vegan diet), you are saving the lives of chickens, cows, fish, and once the Great Reset happens, bugs. Every vegan that is harvested for food means less innocent plants are killed in order to feed them, and the same goes for the wildlife that would otherwise be killed in the harvesting of their food. Also, eating vegans means that less fossil fuels are burned in the harvesting of their hippie food. So not only is eating vegans morally superior to a vegan diet, it is also more sustainable, environmentally friendly, and is cruelty-free! #SaveAChickenEatAVegan
                                            </p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-ficocgsx even thread-even depth-1" id="comment-49665">
                                        <div id="div-comment-49665" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/20327017d60d56be7c7e8de99e2dcd39?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/20327017d60d56be7c7e8de99e2dcd39?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">ficocgsx</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49665">October 20, 2022 at 6:22 am</a>		
                                            </div>
                                            <p>Such a nice conversation ! Good vibes&#8230;</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-sweetbabyray3_16 odd alt thread-odd thread-alt depth-1" id="comment-49664">
                                        <div id="div-comment-49664" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/4d5e5663b087bb0eeb3b76e8a0c2c600?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/4d5e5663b087bb0eeb3b76e8a0c2c600?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">SweetBabyRay3_16</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49664">October 20, 2022 at 6:16 am</a>		
                                            </div>
                                            <p>🔨👇</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-tomrat247 even thread-even depth-1" id="comment-49663">
                                        <div id="div-comment-49663" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/782f8c95401542bcfb2f433bf7d41971?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/782f8c95401542bcfb2f433bf7d41971?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">tomrat247</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49663">October 20, 2022 at 6:12 am</a>		
                                            </div>
                                            <p>If Tim wanted to use his Tim Pool-Money for good it would be to create seed-capital for expanding businesses like Nash bars so they get better market penetration.</p>
                                            <p>That would make an awesome channel in itself &#8211; kind of a long-form Dragons Den type of idea, where it&#8217;s part discussion, part documentary on the process currently, with a discussion on what he negotiates for his money.</p>
                                            <p>I&#8217;d watch it; and he could set up Pool-inc investment vehicles for his fans to invest in that&#8217;d behave like Kickstarter.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-tomrat247 odd alt thread-odd thread-alt depth-1" id="comment-49662">
                                        <div id="div-comment-49662" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/782f8c95401542bcfb2f433bf7d41971?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/782f8c95401542bcfb2f433bf7d41971?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">tomrat247</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49662">October 20, 2022 at 6:08 am</a>		
                                            </div>
                                            <p>Keep firing assholes!</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-stmyles2 even thread-even depth-1" id="comment-49660">
                                        <div id="div-comment-49660" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/5a698867333ca3e9f6dda776bf63cb78?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/5a698867333ca3e9f6dda776bf63cb78?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">StMyles2</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49660">October 20, 2022 at 5:08 am</a>		
                                            </div>
                                            <p>😂…. It was funny to watch Tim go all Alpha Male…. Luke is like “Tim can I have some”. Tim says “No F’k You I’m hungry”.  I was waiting for Tim to crouch down like a caveman and start growling…. Fun After show tonight.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-ians_hallucination odd alt thread-odd thread-alt depth-1" id="comment-49659">
                                        <div id="div-comment-49659" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/a33f659ae18c1193db11d37ac8d81a34?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/a33f659ae18c1193db11d37ac8d81a34?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Ians_hallucination</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49659">October 20, 2022 at 4:48 am</a>		
                                            </div>
                                            <p>AND im 37 and drive a semi truck all damn day</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-ians_hallucination even thread-even depth-1" id="comment-49658">
                                        <div id="div-comment-49658" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/a33f659ae18c1193db11d37ac8d81a34?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/a33f659ae18c1193db11d37ac8d81a34?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Ians_hallucination</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49658">October 20, 2022 at 4:47 am</a>		
                                            </div>
                                            <p>Luke, i eat all the shit you say not to and i guarantee im in better shape and have more muscle than you. Quit being a pussy, fat boy</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-seeseanj odd alt thread-odd thread-alt depth-1" id="comment-49657">
                                        <div id="div-comment-49657" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/cbd6ed62cf22cd158622e8882f476c43?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/cbd6ed62cf22cd158622e8882f476c43?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Carl Calderone</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49657">October 20, 2022 at 4:32 am</a>		
                                            </div>
                                            <p>Nope, uncensored not loading again even after logging out and back in again.<br />
                                                Where&#8217;s Lydia, this only started after she left 😮‍💨
                                            </p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-seeseanj even thread-even depth-1" id="comment-49656">
                                        <div id="div-comment-49656" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/cbd6ed62cf22cd158622e8882f476c43?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/cbd6ed62cf22cd158622e8882f476c43?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Carl Calderone</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49656">October 20, 2022 at 4:29 am</a>		
                                            </div>
                                            <p>Uncensored not loading again, last time it did load after I commented, seeing if it works again this time.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-bigx5murf odd alt thread-odd thread-alt depth-1" id="comment-49651">
                                        <div id="div-comment-49651" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/6eb45c838ae32f73589f1399db1e89db?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/6eb45c838ae32f73589f1399db1e89db?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Bigx5murf</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49651">October 20, 2022 at 3:02 am</a>		
                                            </div>
                                            <p>Checkout the YouTube channel &#8220;Vegan deterioration&#8221;. Long term vegans do not have young looking skin.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-tvan even thread-even depth-1" id="comment-49650">
                                        <div id="div-comment-49650" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/b2329e987c19744fb36d7335cef8dcd3?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/b2329e987c19744fb36d7335cef8dcd3?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Tria V</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49650">October 20, 2022 at 3:02 am</a>		
                                            </div>
                                            <p>It&#8217;s entertaining to see Ian explain himself into deeper confusion.  </p>
                                            <p>My brother does the same thing alot because of his unwillingness to give up his pride.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-lillyd odd alt thread-odd thread-alt depth-1" id="comment-49649">
                                        <div id="div-comment-49649" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/78d6b346fbd718cc607669215c90927e?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/78d6b346fbd718cc607669215c90927e?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Michelle Donahue</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49649">October 20, 2022 at 2:12 am</a>		
                                            </div>
                                            <p>It makes me sad how you younger people care so little about marriage. You never go into a marriage thinking well how are we going to split everything when we get divorced. You are dooming yourself before you even get started. When you find the right person, your soul mate, you’ll want to spend the rest of your life with them. Doesn’t mean you have to get married but you’ll definitely know you want to grow old with that person. But it’s nothing to be scared of or shy away from. But most definitely you don’t want to start talking about what’s going to happen when you break up before you even get in the marriage.  I’m sorry Ian but you have it wrong about trump. No one is out there looking for a father figure in him. People are definitely messed up from the war they fought but they are even more upset about all the lies they were told. Especially our vets that were put in war because of those lies. He is the only president, in my lifetime anyway, that calls out all the BS!! He is the only one that has gone against the grain and said nope I’m not like the rest of you. If you look back at the last presidents they all lied about so much and trump just tells you straight up how it is. He tells you hey they are not after me, they are after you, I’m just in the way. And that’s the truth, they are after all of us. If it wasn’t for trump none of the stuff that was revealed would have been. The news lying, congress hiding stuff, the jacked up elections, the corrupt agencies, pharma, all the child trafficking, I could go on and on but I’m sure you get the point. He is taking all the shit just to show the whole world how corrupt our government is. And the whole world is watching and seeing it. I’m not in the military but I’m pretty sure it’s not about a father figure at all, it’s about him actually giving a shit about this great nation!! But your missing the bigger picture of what trump has done and continues to do. He has woke up millions of people so no one is waiting for him to come rescue us, we are doing it now. We the people are awake now and we are actually out there making a difference in our communities. School boards, local offices, state reps, even governors are out there making a change now. He made and started a path for us and we are making the change now, well most of us anyway. You still have some that are too scared to stand up or speak out but that’s ok. They’ll get off their knees eventually.  Change is happening and most do thank trump for making that path for us, IMO.  If your community isn’t better then why, why aren’t you out there making a change and making this country better for the future of our children?  If not you then who? Thank you Tim, as always, for everything. Again your billboard needs to say ‘WE ARE THE NEWS’ (because for some you are their news now)</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-mickzero even thread-even depth-1" id="comment-49648">
                                        <div id="div-comment-49648" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/0b33a64c85f8b759c71d95550ebfef47?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/0b33a64c85f8b759c71d95550ebfef47?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Orlando Wynn</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49648">October 20, 2022 at 2:04 am</a>		
                                            </div>
                                            <p>The stomach and heart and brain are connected through the vegus nerve</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-wolv256 odd alt thread-odd thread-alt depth-1" id="comment-49643">
                                        <div id="div-comment-49643" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/5b9a02d3ba0593b14c49b5038b2cfa96?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/5b9a02d3ba0593b14c49b5038b2cfa96?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Wolv256</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49643">October 20, 2022 at 1:31 am</a>		
                                            </div>
                                            <p>Tim, aim for about 1 gram of protein per day per pound of body weight you have.  So if you weigh 170 lbs, eat about 170 grams of protein per day.  What will happen?  You’ll get biceps.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-wolv256 even thread-even depth-1" id="comment-49642">
                                        <div id="div-comment-49642" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/5b9a02d3ba0593b14c49b5038b2cfa96?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/5b9a02d3ba0593b14c49b5038b2cfa96?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Wolv256</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49642">October 20, 2022 at 1:25 am</a>		
                                            </div>
                                            <p>For your thyroid health, take iodine.  Alex Jones is right, as always</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-roflo1804 odd alt thread-odd thread-alt depth-1" id="comment-49639">
                                        <div id="div-comment-49639" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/ef8ce0ce631a6893a186908dbda2ec48?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/ef8ce0ce631a6893a186908dbda2ec48?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">roflo1804</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49639">October 20, 2022 at 1:15 am</a>		
                                            </div>
                                            <p>NINJAGRIPS makes a good point. Ian, don&#8217;t spout off over stupid, cringey shit. Think before you open you mouth, Ian. Your constant crnge takes need to stop. Just accept that you&#8217;re an average IQ guy who&#8217;s put too many illicit drugs in your system over the years. Also, let the guests talk without your asinine interruptions!</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-leedyn22 even thread-even depth-1" id="comment-49638">
                                        <div id="div-comment-49638" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/828fb4d232e70837073d6c1ac4a93d97?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/828fb4d232e70837073d6c1ac4a93d97?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Leedyn22</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49638">October 20, 2022 at 12:59 am</a>		
                                            </div>
                                            <p>Stomach, congestion and heart&#8230;. Three words I never thought I would here in a serious sentence</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-gertpacu odd alt thread-odd thread-alt depth-1" id="comment-49637">
                                        <div id="div-comment-49637" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/01183e464a49b363c813b2d53c93564b?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/01183e464a49b363c813b2d53c93564b?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Gary Pucci</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49637">October 20, 2022 at 12:54 am</a>		
                                            </div>
                                            <p>Good lord Ian&#8230; Stop with your new age crap that you know nothing about already.. You are flipping insane and the crap you say is so incorrect and stupid.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-lilyanne even thread-even depth-1" id="comment-49636">
                                        <div id="div-comment-49636" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/c4140cd6e16766f331c50d98a1d39e9e?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/c4140cd6e16766f331c50d98a1d39e9e?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">LilyAnne</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49636">October 20, 2022 at 12:45 am</a>		
                                            </div>
                                            <p>So I went to my doctor and talked to them about changing my diet. As a 32 Woman that has had 4 kids it was hard to go pre baby weight. But I dropped all sugar went to Munk Fruit. And went to meat, vegetables and some fruit. And started using bio trust. Dropped 30 lbs in from July till now. And feel so much better.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-sc0rp10n odd alt thread-odd thread-alt depth-1" id="comment-49634">
                                        <div id="div-comment-49634" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/1b56f4ba67f7bfd031be7dfae3e605e9?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/1b56f4ba67f7bfd031be7dfae3e605e9?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Sc0rp10N</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49634">October 20, 2022 at 12:26 am</a>		
                                            </div>
                                            <p>Tim&#8217;s al mmmffmmfmfmfmmmffmm</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-backtracker101 even thread-even depth-1" id="comment-49633">
                                        <div id="div-comment-49633" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/374aed674d16da0f0ee5de495e233e3a?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/374aed674d16da0f0ee5de495e233e3a?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Robert Wortz</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49633">October 20, 2022 at 12:19 am</a>		
                                            </div>
                                            <p>Something tells me that Nash Bar Co is going to get a shit load of orders after this&#8230;. Thanks Seth &amp; Megan</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-philm odd alt thread-odd thread-alt depth-1" id="comment-49632">
                                        <div id="div-comment-49632" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/c3e1300e145f49490da794cf9f14cb0b?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/c3e1300e145f49490da794cf9f14cb0b?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">PhilM</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49632">October 20, 2022 at 12:11 am</a>		
                                            </div>
                                            <p>Personally, I only drink spring water or mineral water since they have like little to no phthalates but still have that plastic.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-ninjagrips even thread-even depth-1" id="comment-49631">
                                        <div id="div-comment-49631" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/d3e30cb4e48135168563c4eccce81a37?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/d3e30cb4e48135168563c4eccce81a37?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">ninjagrips</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49631">October 20, 2022 at 12:02 am</a>		
                                            </div>
                                            <p>I&#8217;m SO SICK of Ian&#8217;s dumb crap comments and theories. At least someone was there who was knowledgeable enough to shut him down, for once. Ian, before you open your mouth, make sure you truly know what it is you&#8217;re talking about.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-keklordgrey odd alt thread-odd thread-alt depth-1" id="comment-49630">
                                        <div id="div-comment-49630" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/091867a747cf8494cd8d786c58e9d4e5?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/091867a747cf8494cd8d786c58e9d4e5?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">KekLordGrey</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49630">October 19, 2022 at 11:58 pm</a>		
                                            </div>
                                            <p>VEGANS !!! just run your tongue across your teeth&#8230; YOU ARE NOT !!! you&#8230; are an OMINIVORE&#8230; just sayin&#8217;</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-rachelgrabow even thread-even depth-1" id="comment-49628">
                                        <div id="div-comment-49628" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/5401a04291a12560fe46984f95e1c7dd?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/5401a04291a12560fe46984f95e1c7dd?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">rachelgrabow</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49628">October 19, 2022 at 11:44 pm</a>		
                                            </div>
                                            <p>Hilarious and informative after show!</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-taurusbrit odd alt thread-odd thread-alt depth-1" id="comment-49627">
                                        <div id="div-comment-49627" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/525695b62cb0e9cf0d27ef827393378b?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/525695b62cb0e9cf0d27ef827393378b?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Britnee Tippins</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49627">October 19, 2022 at 11:41 pm</a>		
                                            </div>
                                            <p>Been meaning to say something&#8230;Luke appears to have ridiculous side burns with those headphones&#8230;🤣😂&#8230;just saying.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-bigjoe77 even thread-even depth-1" id="comment-49626">
                                        <div id="div-comment-49626" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/e6db142fc89c79fe8d9f8ba782118ec8?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/e6db142fc89c79fe8d9f8ba782118ec8?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">BigJoe77</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49626">October 19, 2022 at 11:34 pm</a>		
                                            </div>
                                            <p>Is cannibalism vegan?</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-messymav odd alt thread-odd thread-alt depth-1" id="comment-49625">
                                        <div id="div-comment-49625" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/11b3eaee3da6aa518c6e4c2be5558244?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/11b3eaee3da6aa518c6e4c2be5558244?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Messymav</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49625">October 19, 2022 at 11:30 pm</a>		
                                            </div>
                                            <p>So can anyone confirm if it&#8217;s seeds in general to avoid or just the seed oils??</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-ave even thread-even depth-1" id="comment-49624">
                                        <div id="div-comment-49624" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/4f77fe3df915bd028cf598af151c34b1?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/4f77fe3df915bd028cf598af151c34b1?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Andrew Vernon</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49624">October 19, 2022 at 11:27 pm</a>		
                                            </div>
                                            <p>omg ian lol</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-jrhaile odd alt thread-odd thread-alt depth-1" id="comment-49623">
                                        <div id="div-comment-49623" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/d04983c16401286fbc5f8743259c162a?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/d04983c16401286fbc5f8743259c162a?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">jrhaile</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49623">October 19, 2022 at 11:24 pm</a>		
                                            </div>
                                            <p>Just had a son and his balls are friggin&#8217; huge for a 3 month old!</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-yobuyahouse even thread-even depth-1" id="comment-49622">
                                        <div id="div-comment-49622" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/5f688281902dcac07ae4ca0054f9bcde?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/5f688281902dcac07ae4ca0054f9bcde?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Yobuyahouse</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49622">October 19, 2022 at 11:24 pm</a>		
                                            </div>
                                            <p>Ian quiet let Megan talk about health. Even deer eat bugs. Holy shit the part about sun burns and vegetable oils no freaking way I used to do tons of seed oil and i would burn like hell!</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-smactn odd alt thread-odd thread-alt depth-1" id="comment-49620">
                                        <div id="div-comment-49620" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/d2d6615cc8e67d4c1344bb8fb087c722?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/d2d6615cc8e67d4c1344bb8fb087c722?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">Steve McCullough</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49620">October 19, 2022 at 11:09 pm</a>		
                                            </div>
                                            <p>The Crystal Geyser website says that their bottles contain no bhp&#8217;s. Take that for what it&#8217;s worth. I drink their water and my balls are huge.</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    <li class="comment byuser comment-author-cevdrummer even thread-even depth-1" id="comment-49619">
                                        <div id="div-comment-49619" class="comment-body">
                                            <div class="comment-author vcard">
                                                <img alt='' src='https://secure.gravatar.com/avatar/2403b1bc669aa89a7f77cb52226afec6?s=32&#038;r=g' srcset='https://secure.gravatar.com/avatar/2403b1bc669aa89a7f77cb52226afec6?s=64&#038;r=g 2x' class='avatar avatar-32 photo' height='32' width='32' loading='lazy'/>			<cite class="fn">cevdrummer</cite> <span class="says">says:</span>		
                                            </div>
                                            <div class="comment-meta commentmetadata">
                                                <a href="https://timcast.com/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/#comment-49619">October 19, 2022 at 11:05 pm</a>		
                                            </div>
                                            <p>try eating a steak for breakfast to see if it&#8217;s a fat overload</p>
                                        </div>
                                    </li>
                                    <!-- #comment-## -->
                                    </ol>
                                    <div class="navigation">
                                    <div class="alignleft"></div>
                                    <div class="alignright"></div>
                                    </div>
                                    <div id="respond" class="comment-respond">
                                    <h3 id="reply-title" class="comment-reply-title">Leave a Reply</h3>
                                    <form action="https://timcast.com/wp-comments-post.php" method="post" id="commentform" class="comment-form">
                                        <p class="logged-in-as"><a href="https://timcast.com/wp-admin/profile.php" aria-label="Logged in as btimby. Edit your profile.">Logged in as btimby</a>. <a href="https://timcast.com/wp-login.php?action=logout&amp;redirect_to=https%3A%2F%2Ftimcast.com%2Fmembers-area%2Fseth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak%2F&amp;_wpnonce=2e5a2db0e9">Log out?</a> <span class="required-field-message" aria-hidden="true">Required fields are marked <span class="required" aria-hidden="true">*</span></span></p>
                                        <p class="comment-form-comment"><label for="comment">Comment <span class="required" aria-hidden="true">*</span></label> <textarea id="comment" name="comment" cols="45" rows="8" maxlength="65525" required="required"></textarea></p>
                                        <p class="form-submit"><input name="submit" type="submit" id="submit" class="submit" value="Post Comment" /> <input type='hidden' name='comment_post_ID' value='741122' id='comment_post_ID' />
                                            <input type='hidden' name='comment_parent' id='comment_parent' value='0' />
                                        </p>
                                        <p style="display: none;"><input type="hidden" id="akismet_comment_nonce" name="akismet_comment_nonce" value="7965336c35" /></p>
                                        <p style="display: none !important;">
                                            <label>&#916;<textarea name="ak_hp_textarea" cols="45" rows="8" maxlength="100"></textarea></label><input type="hidden" id="ak_js_1" name="ak_js" value="227"/><script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script>document.getElementById( "ak_js_1" ).setAttribute( "value", ( new Date() ).getTime() );</script>
                                        </p>
                                    </form>
                                    </div>
                                    <!-- #respond -->
                                </div>
                            </div>
                            <!-- End Article Content -->
                        </div>
                        <!-- End Article Container -->
                        </article>
                    </div>
                    <!-- End Column -->
                    <div class="t-grid:l:30pc t-pad:0px:lt:xs t-pad:0px:top:xs   t-pad:0px:top:m  t-pad:50pc:top:l t-pad:lt:l  t-pad:50pc:top:xl">
                        <div class="t-hide:under:s side-rail ">
                        <span class="pretty-header t-marg:5px:bot  t-display:inline-block">
                            <h3>Popular</h3>
                        </span>
                        <hr class="thick t-marg:15px:top " />
                        <div class="popular t-marg:25pc:top t-pad:50pc:rt:l article-links">
                            <ul class="nobull">
                                <li>
                                    <a href="https://timcast.com/news/republicans-submit-legislation-prohibiting-federal-funding-of-sexually-explicit-material-for-children/" >
                                    <div class="image" style="background-image:url('https://timcast.com/wp-content/uploads/2022/10/FED-Funded-Legislat.png')"></div>
                                    <h4 class="t-txt:sm t-fnt:3 t-fnt:med t-txt:blk"> Republicans Submit Legislation Prohibiting Federal...</h4>
                                    </a>
                                </li>
                                <li>
                                    <a href="https://timcast.com/news/bmw-to-spend-1-7-billion-on-battery-factory-electric-vehicle-production-in-south-carolina/" >
                                    <div class="image" style="background-image:url('https://timcast.com/wp-content/uploads/2022/10/BMW-Spartansburg-plant-e1666221847871.png')"></div>
                                    <h4 class="t-txt:sm t-fnt:3 t-fnt:med t-txt:blk"> BMW to Spend...</h4>
                                    </a>
                                </li>
                                <li>
                                    <a href="https://timcast.com/news/aoc-townhall-forum-descends-into-chaos-as-protesters-take-over-video/" >
                                    <div class="image" style="background-image:url('https://timcast.com/wp-content/uploads/2022/10/1-2.jpg')"></div>
                                    <h4 class="t-txt:sm t-fnt:3 t-fnt:med t-txt:blk"> AOC Townhall Forum Descends Into Chaos As Protesters...</h4>
                                    </a>
                                </li>
                                <li>
                                    <a href="https://timcast.com/news/arizona-will-not-move-shipping-containers-until-biden-administration-closes-gaps-in-border-wall/" >
                                    <div class="image" style="background-image:url('https://timcast.com/wp-content/uploads/2022/10/AZ-border-wall-shipping-containers-e1666278874334.png')"></div>
                                    <h4 class="t-txt:sm t-fnt:3 t-fnt:med t-txt:blk"> Arizona Will Not Move Shipping Containers Until Biden...</h4>
                                    </a>
                                </li>
                                <li>
                                    <a href="https://timcast.com/news/u-k-prime-minister-resigns-after-just-44-days-in-office/" >
                                    <div class="image" style="background-image:url('https://timcast.com/wp-content/uploads/2022/10/Liz-Truss.jpg')"></div>
                                    <h4 class="t-txt:sm t-fnt:3 t-fnt:med t-txt:blk"> ...</h4>
                                    </a>
                                </li>
                            </ul>
                        </div>
                        <div class="pin-holder t-pad:50pc:top:l">
                            <div class="pinned t-pad:50pc:top:xs t-pad:50pc:top:m " data-bottom-threshold="350">
                                <div class="banner-ad non-member no-borders-bot t-pad:50pc:top">
                                    <a href="https://amzn.to/3AZ8puK" target="_blank"><img src="https://timcast.com/wp-content/uploads/2022/02/TIMCAST-Ad-1.png"></a><br>
                                    <!-- <div id="rc-widget-5de5d4" data-rc-widget data-widget-host="habitat" data-endpoint="//trends.revcontent.com" data-widget-id="267305"></div>
                                    <script type="text/javascript" src="https://assets.revcontent.com/master/delivery.js" defer="defer"></script> -->
                                </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
                <!-- End Columns -->
                <div class="t-txt:cntr t-contain t-pos:cntr t-pad:top">
                    <div class="banner-ad non-member t-pad:bot">		
                    </div>
                </div>
            </div>
            </div>
            <footer class="t-pad:50pc:bot t-bg:grey3 t-pad:25pc:top:xs t-pad:50pc:top">
            <div class="  t-contain t-pos:cntr   ">
                <div class="t-grid:m:30pc ">
                    <ul class="social-links t-txt:cntr:xs social-links t-txt:cntr:m">
                        <li id="menu-item-150315"><a href="https://www.facebook.com/timcastnews/"  class="fa fa-facebook menu-item menu-item-type-custom menu-item-object-custom"><span class="txt"><strong>Facebook</strong></span></a></li>
                        <li id="menu-item-150316"><a href="https://twitter.com/timcast"  class="fa fa-twitter menu-item menu-item-type-custom menu-item-object-custom"><span class="txt"><strong>Twitter</strong></span></a></li>
                        <li id="menu-item-150317"><a href="https://www.linkedin.com/in/timothy-pool-7228ba25"  class="fa fa-linkedin menu-item menu-item-type-custom menu-item-object-custom"><span class="txt"><strong>LinkedIn</strong></span></a></li>
                        <li id="menu-item-150318"><a href="https://www.youtube.com/channel/UCG749Dj4V2fKa143f8sE60Q"  class="fa fa-youtube menu-item menu-item-type-custom menu-item-object-custom"><span class="txt"><strong>YouTube</strong></span></a></li>
                        <li id="menu-item-150319"><a href="https://www.instagram.com/timcast/"  class="fa fa-instagram menu-item menu-item-type-custom menu-item-object-custom"><span class="txt"><strong>Instagram</strong></span></a></li>
                    </ul>
                </div>
                <div class="t-show:under:m t-pad:25pc:top:xs">
                    <hr/>
                </div>
                <div class=" footer-copyright t-txt:med t-txt:wht t-pad:0px t-fnt:1 t-grid:m:70pc t-txt:rt t-pad:top:m t-pad:50pc:top:l t-marg:bot">
                    <div class="t-flex:m:valign:mid t-flex:m:align:rt  t-pad:25pc:top:xs">
                        <ul class="t-menu t-txt:clr3 t-txt:cntr:s t-txt:cntr:xs t-txt:cntr:xs  t-txt:u t-txt:med t-marg:0px:bot t-marg:25px:rt:m t-marg:50pc:rt:l">
                        <li id="menu-item-150320" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-150320"><a href="/privacy-policy/">Privacy Policy</a></li>
                        <li id="menu-item-150321" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-150321"><a href="/terms-of-service/">Terms of Service</a></li>
                        <li class="t-txt:wht">Copyright &copy; 2022 TIMCAST</li>
                        </ul>
                    </div>
                </div>
            </div>
            </footer>
        </main>
    </div>
    <script type='text/javascript' src='https://timcast.com/wp-content/plugins/metronet-profile-picture/js/mpp-frontend.js?ver=2.6.0' id='mpp_gutenberg_tabs-js'></script>
    <script type='text/javascript' src='https://timcast.com/wp-includes/js/dist/vendor/regenerator-runtime.min.js?ver=0.13.9' id='regenerator-runtime-js'></script>
    <script type='text/javascript' src='https://timcast.com/wp-includes/js/dist/vendor/wp-polyfill.min.js?ver=3.15.0' id='wp-polyfill-js'></script>
    <script type='text/javascript' id='contact-form-7-js-extra'>
        /* <![CDATA[ */
        var wpcf7 = {"api":{"root":"https:\/\/timcast.com\/wp-json\/","namespace":"contact-form-7\/v1"}};
        /* ]]> */
    </script>
    <script type='text/javascript' src='https://timcast.com/wp-content/plugins/contact-form-7/includes/js/index.js?ver=5.5.6' id='contact-form-7-js'></script>
    <script type='text/javascript' src='https://www.google.com/recaptcha/api.js?render=6Lec1_gdAAAAALY6mafp3kZgPpkAYDwil4OqMmoH&#038;ver=3.0' id='google-recaptcha-js'></script>
    <script type='text/javascript' id='wpcf7-recaptcha-js-extra'>
        /* <![CDATA[ */
        var wpcf7_recaptcha = {"sitekey":"6Lec1_gdAAAAALY6mafp3kZgPpkAYDwil4OqMmoH","actions":{"homepage":"homepage","contactform":"contactform"}};
        /* ]]> */
    </script>
    <script type='text/javascript' src='https://timcast.com/wp-content/plugins/contact-form-7/modules/recaptcha/index.js?ver=5.5.6' id='wpcf7-recaptcha-js'></script>
    <script type="text/javascript" id="wpsp-script-frontend"></script>
    <!-- ========================== End Footer / End Page Bottom   ============================= -->
    <script src="https://player.vimeo.com/api/player.js" ></script>
    <script src="https://timcast.com/wp-content/themes/timcast/scripts.js?uc=<1665524704"></script>
</body>
</html>
'''
RSP2 = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<title>seth and megan hansen member show 2022 - Rumble</title>
	<meta name=robots content=noindex>
	<link rel="canonical" href="https://rumble.com/v1otqmk-seth-and-megan-hansen-member-show-2022.html">
<link rel="alternate" href="https://rumble.com/api/Media/oembed.json?url=https%3A%2F%2Frumble.com%2Fembed%2Fv1m7kuc%2F%3Fpub%3Dlf6yv" type="application/json+oembed" title="seth and megan hansen member show 2022"><link rel="alternate" href="https://rumble.com/api/Media/oembed.xml?url=https%3A%2F%2Frumble.com%2Fembed%2Fv1m7kuc%2F%3Fpub%3Dlf6yv" type="text/xml+oembed" title="seth and megan hansen member show 2022">
	<meta name="viewport" content="width=device-width,initial-scale=1" />
	<link rel="dns-prefetch" href="https://sp.rmbl.ws"><link rel="dns-prefetch" href="//imasdk.googleapis.com/"></head><body style="margin:0;padding:0">
<div id="player" style="width:100%;height:100%;overflow:hidden;position:absolute"></div>
<script type="text/javascript">!function(s,d){function a(){return(new Date).getTime()/1e3}var t,r,o,n,i,c,l,e="Rumble",b={F:0};(d=s[e]=s[e]||function(){d._.push(arguments)})._=d._||[],b.f={},b.b={};b.f["v1m7kuc"]={"fps":30,"w":1920,"h":1080,"u":{"mp4":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/m\/G\/U\/f\/mGUfg.caa.mp4","meta":{"bitrate":816,"size":201860220,"w":854,"h":480}},"webm":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/m\/G\/U\/f\/mGUfg.daa.webm","meta":{"bitrate":814,"size":201395199,"w":854,"h":480}}},"ua":{"mp4":{"360":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/m\/G\/U\/f\/mGUfg.baa.mp4","meta":{"bitrate":636,"size":157266626,"w":640,"h":360}},"480":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/m\/G\/U\/f\/mGUfg.caa.mp4","meta":{"bitrate":816,"size":201860220,"w":854,"h":480}},"720":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/m\/G\/U\/f\/mGUfg.gaa.mp4","meta":{"bitrate":1968,"size":486561040,"w":1280,"h":720}},"1080":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/m\/G\/U\/f\/mGUfg.haa.mp4","meta":{"bitrate":2700,"size":667430434,"w":1920,"h":1080}},"240":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/m\/G\/U\/f\/mGUfg.oaa.mp4","meta":{"bitrate":203,"size":50324051,"w":640,"h":360}}},"webm":{"480":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/m\/G\/U\/f\/mGUfg.daa.webm","meta":{"bitrate":814,"size":201395199,"w":854,"h":480}}}},"i":"https:\/\/sp.rmbl.ws\/s8\/6\/m\/G\/U\/f\/mGUfg.OvCc.jpg","evt":{"v":"\/l\/view.830r7..1m7kuc.wv9461","e":"\/l\/pte.830r7..1m7kuc.f5zn5m","wt":1,"t":"\/l\/timeline.830r7..1m7kuc.1ix.edrxv3"},"cc":[],"l":"\/v1otqmk-seth-and-megan-hansen-member-show-2022.html","r":1,"title":"seth and megan hansen member show 2022","author":{"name":"ATimcastIRL","url":"https:\/\/rumble.com\/c\/ATimcastIRL"},"player":{"logo":{"tw":75,"th":22,"path":"<style type=\"text\/css\"> .st0{fill:#ffffff;} <\/style><path class=\"st0\" d=\"M51.8,55.9c-2.5,0-4.8,0-7.2,0c0-17.7,0-35.4,0-53.2c3.8,0,7.7,0,11.6,0c2,12.1,4,24.3,6,36.4 c0.1,0,0.2,0,0.3,0c1.8-12.1,3.7-24.3,5.5-36.5c3.9,0,7.7,0,11.6,0c0,17.7,0,35.4,0,53.1c-2.6,0-5.1,0-7.7,0c0-12.1,0-24.3,0-36.4 c-0.1,0-0.2,0-0.3,0c-1.8,12.1-3.7,24.3-5.6,36.5c-2.7,0-5.3,0-8,0c-2-12-4-23.9-6-35.9c-0.1,0-0.2,0-0.3,0 C51.8,31.9,51.8,43.9,51.8,55.9z\"\/><path class=\"st0\" d=\"M122,46.4c-0.5,3.2-1,6.3-1.4,9.4c-2.5,0-5.1,0-7.7,0c2.8-17.7,5.7-35.4,8.5-53.1c4.1,0,8.2,0,12.4,0 c2.8,17.7,5.7,35.4,8.5,53.1c-2.9,0-5.6,0-8.5,0c-0.5-3.1-1-6.2-1.4-9.4C128.8,46.4,125.4,46.4,122,46.4z M127.2,13.3 c-0.1,0-0.2,0-0.3,0c-1.3,8.5-2.5,17.1-3.8,25.7c2.7,0,5.3,0,8,0C129.7,30.4,128.4,21.9,127.2,13.3z\"\/><path class=\"st0\" d=\"M102.1,20.6c0-1.5,0-3,0-4.5c0-0.9,0-1.8-0.2-2.7c-0.4-2.6-1.8-3.7-4.2-3.7c-2.4,0-3.7,1.1-4.1,3.6 c-0.1,0.7-0.2,1.4-0.2,2.2c0,9.2,0,18.4,0,27.6c0,0.7,0,1.4,0.1,2c0.4,2.6,1.8,3.8,4.3,3.7c2.4,0,3.8-1.2,4.1-3.8 c0.1-0.8,0.1-1.5,0.1-2.3c0-2.2,0-4.3,0-6.6c2.6,0,5.2,0,8.1,0c-0.2,3.9-0.2,7.9-0.8,11.7c-0.9,5-4.5,8-9.6,8.5 c-1.7,0.2-3.4,0.2-5-0.1c-5.5-0.8-8.9-4.4-9.6-9.9C85,45.3,85,44.1,85,42.9c0-9.3,0-18.7,0-28c0-1.7,0.3-3.5,0.8-5.2 c1.1-3.6,3.5-6.1,7.2-7.1c3.2-0.9,6.4-0.9,9.5,0.1c4.9,1.6,6.9,5.6,7.4,10.4c0.2,2.4,0,4.9,0,7.4C107.3,20.6,104.7,20.6,102.1,20.6z \"\/><path class=\"st0\" d=\"M169.5,17.1c-2.5,0-5,0-7.6,0c-0.1-1.2-0.1-2.4-0.2-3.6c-0.2-2.4-1.6-3.7-3.9-3.7c-2.6-0.1-4,1.2-4.3,3.8 c-0.5,4.1,1.3,7.3,4.1,10.1c2.2,2.2,4.6,4.3,6.7,6.5c4.9,4.9,6.5,10.9,5,17.6c-1,4.8-4,7.8-8.8,8.6c-3.7,0.6-7.4,0.5-10.7-1.7 c-3.2-2.1-4.4-5.3-4.8-8.9c-0.2-1.9,0-3.8,0-5.8c2.6,0,5.1,0,7.8,0c0,1.6-0.1,3.1,0,4.6c0.2,3,1.8,4.4,4.7,4.2 c2-0.1,3.3-1.1,3.7-3.1c0.7-3.3-0.2-6.3-2.3-8.7c-2.2-2.5-4.7-4.8-7.1-7.1c-5.7-5.4-8-11.8-6.1-19.6c1.2-4.8,4.6-7.7,9.5-8.2 c1.7-0.1,3.4-0.2,5,0.1c5.5,0.9,8.8,4.5,9.4,10.2C169.6,13.9,169.5,15.4,169.5,17.1z\"\/><path class=\"st0\" d=\"M26.4,2.8c0,2.5,0,4.9,0,7.5c-2.9,0-5.7,0-8.7,0c0,15.3,0,30.4,0,45.6c-2.9,0-5.5,0-8.4,0c0-15.2,0-30.3,0-45.6 c-3,0-5.8,0-8.7,0c0-2.6,0-5,0-7.5C9.2,2.8,17.7,2.8,26.4,2.8z\"\/><path class=\"st0\" d=\"M181,10.3c-3,0-5.8,0-8.7,0c0-2.5,0-5,0-7.5c8.6,0,17.1,0,25.7,0c0,2.5,0,4.9,0,7.5c-2.8,0-5.7,0-8.6,0 c0,15.3,0,30.4,0,45.7c-2.9,0-5.5,0-8.4,0C181,40.7,181,25.6,181,10.3z\"\/><path class=\"st0\" d=\"M38.4,55.9c-2.8,0-5.4,0-8.2,0c0-17.7,0-35.4,0-53.1c2.7,0,5.4,0,8.2,0C38.4,20.4,38.4,38.1,38.4,55.9z\"\/>","w":"200","h":"58","link":"\/\/rumble.com\/c\/ATimcastIRL","allow":true},"timestamp":1620930686,"colors":{"play":"#FFFFFF","scrubber":"#4CC0E0","hover":"#FFFFFF","background":"#4CC0E0","hoverBackground":"#303030"}},"duration":1977,"pubDate":"2022-10-20T02:48:40+00:00","loaded":1,"vid":97771332,"timeline":[0,0],"own":true,"mod":[],"restrict":[0,["timcast.com"]],"autoplay":1,"track":1,"live":0,"live_placeholder":false,"livestream_has_dvr":null,"a":{"timeout":-1,"u":"lf6yv","aden":[1,0,1],"ov":1,"ads":[],"a":"830r7.lf6yv.lf6yv.1m7kuc..ob.1wsdj2y","ae":"830r7.lf6yv.lf6yv.1m7kuc..ob.44u9qh","ap":[false,0],"loop":[]},loaded:a()};if(!b.k){function f(o,e){return o.opts||(o.opts=[]),b.D(e,function(e,t){var r=o[t];switch(t){case"opts":o[t]=r.concat(e);break;case"ad_sys":o[t]=r?b.M(r,e):e;break;default:o[t]=e}}),o}function p(c,s,l){function u(){var e=c.v.src||c.v.currentSrc;return e=e.match(/blob:/)&&c.hls_js?c.hls_js.url||e:e}function f(){var e=u(),t=s.get();return c.current_video=s,t==e?0:t}var p;s.get=function(){return function(e,t){if(21192597==e.vid.vid)return t;var r,o=b.B(t),t=b.E(t);return e.vid.live||(r=0,e.vid.a&&(r=e.vid.a.u||0),o.u=r,o.b=0<e.bandwidth_track?1:0),t+"?"+b.C(o)}(c,s.url)};s.check=function(){return!f()},s.play=function(){l&&c.hls_js&&!p&&c.hls_js.startLoad(),p=!0},s.set=function(){if(l&&!b.I())return setTimeout(function(){s.set()},100),!1;var e,r,t,o,n,i=f(),d=0,a=0;i&&(p=!1,e=c.v,c.res=s.key,0<S&&(c.last_set_url==u()?(d=!e.paused,a=e.currentTime):0<c.video_time&&(a=c.video_time)),a&&!c.vid.live&&(c.ui.s.autoSeek=a),r=c,a=e,t=i,o=l&&Hls.isSupported(),r.hls_js&&r.hls_media_attached&&((n=r.hls_js).detachMedia(a),n.destroy(),r.hls_js=null),o?(n=r.hls_js=new Hls({capLevelToPlayerSize:!0,autoStartLoad:!1,manifestLoadingMaxRetry:6,levelLoadingMaxRetry:6}),r.j("hlsJsLoaded",n),n.on(Hls.Events.LEVEL_UPDATED,function(e,t){r.live=t.details.live}),n.loadSource(t),n.attachMedia(a),r.hls_media_attached=1):a.src=t,S++,c.last_set_url=i,e.load(),d&&(s.play(),e.play()))}}function g(e){return H.hasOwnProperty(e)?H[e]:e}function h(r,e,o){var n,t;if(!r.style&&r.length)for(t=0;t<r.length;t++)h(r[t],e,o);else b.D(e,function(e,t){n=g(t),o&&""!==r.style[n]||(r.style[n]=g(e))})}function v(){var e=G;G={},y=0,b.D(e,function(e){"function"==typeof e&&e()})}function m(e){var i,o={play:"#fff",scrubber:"#75a642",hover:"#fff",background:"#303030",hoverBackground:"#699c39"},d=this,n=-1,c=(b.D(e,function(e,t){d[t]=e}),d.hasima=1,d.hasInit=0,d.rpcl=(d.id?d.id+"-":"")+"Rumble-cls",d.rpcls="."+d.rpcl,d.bandwidth_track=0,{}),a=(d.addEvent=function(e,t,r){c[r=r||1]||(c[r]={}),c[r][e]||(c[r][e]=[]),c[r][e].indexOf(t)<0&&c[r][e].push(t);r="addEvent";e!=r&&d.j(r,e)},d.removeEvent=function(e,t,r){c[r=r||1][e]&&(r&&!t?c[r][e]=[]:(t=c[r][e].indexOf(t),c[r][e].splice(t,1)))},d.hasEventListener=function(r){return b.D(c,function(e,t){if(e[r]&&0<e[r].length)return!0})},d.j=function(r,o,n){var i,d,a=[];return b.D(c,function(e,t){if(e[r]&&(n&&n==t||!n))for(d=e[r],i=0;i<d.length;i++)"function"==typeof o&&(o=o()),a.push(d[i](o))}),a},d.triggerError=function(e,t){d.j("error",{code:e,message:t})},d.l1=function(e,t,r){},d.getSetting=function(e,t){var r=!1;return d.vid&&d.vid.player&&d.vid.player[e]&&(e=d.vid.player[e],t&&e[t]&&(r=e[t]),t||(r=e)),r=!r&&o[t]?o[t]:r},d.loadVideoStyles=function(e){var t,r,o,n="vid_"+d.vid.id;d.rpcls;d.p.id=n,d.vars.opts.title&&d.vid.title&&(i.innerHTML=d.vid.title,i.href=b.L(d.vid.l,"rumble.com"),b.w(i,{outline:0,display:"block",18:"linear-gradient(rgba(0,0,0,.7),rgba(0,0,0,0))",textShadow:"rgba(0,0,0,0.5) 0px 0px 2px",padding:"9px",fontSize:"18px",whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis",position:"absolute",top:0,left:0,right:0}),b.x(i,{textDecoration:"underline"},{textDecoration:"none"})),d.bp&&(n=d.getSetting("colors","play"),t=d.getSetting("colors","hover"),r=d.getSetting("colors","background"),o=d.getSetting("colors","hoverBackground"),b.x(d.bp,{color:t,background:o,borderColor:o},{color:n,background:r,borderColor:r},d.bp_svg),d.bp.style.opacity=1)},d.trackBandwidth=function(e){var t=d.bandwidth_track;(e=d.server.bw_tracking?e:0)!=t&&(d.bandwidth_track=e,d.current_video&&!d.m&&d.current_video.set())},d.loadVideo=function(e,t){var r,o=(e="object"!=typeof e?{id:e}:e).id;if(b.b[o]&&(d.vars.playlist||(d.vars.playlist=b.b[o]),o=b.b[o][0]),d.hasInit||(d.hasInit=1,b.c(["ui","custom_ui"],function(){for(var e=0;e<b.d.length;e++)b.d[e](d.id)})),!t)return b.e(o,function(){d.loadVideo(e,1)},{ad_count:d.ad_count||null});if(b.f[o].loaded<9){if(d.triggerError("load","Unable to load video "+o),t)throw"Unable to load video "+o;return 2}if(b.f[o].cfg=e,b.f[o].plays=0,(r=b.f[o]).restrict&&!a(r.restrict)&&(d.triggerError("restricted","Video is restricted"),b.f[o].restricted=!0,d.j("restricted",o),b.f[o].ua=0),r.id=o,d.vid=r,d.live=2==d.vid.live,d.video_list=0,d.current_video=0,n<0&&(n=(d.vars.opts.noads||d.server.bw_ourads_check&&d.vars.opts.norumbleads)&&r.a?1:0),d.trackBandwidth(r&&r.track||n?1:0),!r.restricted&&r.ua&&(d.video_list=b.G(d,r.ua),b.H(d),d.loadVideoStyles()),b.g(d),d.j("loadVideo",r),b.h(d,1),r.restricted&&t)throw"Video "+o+" is restricted"},function(e){var t,r,o,n,i=document,d=!1;if(!e||e[0]<=-3)return!0;r=e[0],o=e[1];try{t=parent!==s?i.referrer||parent.location.href:i.location.href}catch(e){}if(!t)return parent===s;if(t=t.match(/^https?\:\/\/([^\/?#]+)(?:[\/?#]|$)/i))for(t=t[1].split(".");2<=t.length&&!d;)n=t.join("."),-1<o.indexOf(n)&&(d=!0),t.shift();return r!=d}),e=d.rpcl,t="metadata";(d.vars.opts.minimal||d.vars.opts.nopreload)&&(t="none"),d.vars.quality&&(d.res=parseInt(d.vars.quality)),e=b.i('<div class="'+e+'" allowfullscreen tabindex="-1" style="outline: none;"><video muted playsinline hidefocus="hidefocus" style="width:100% !important;height:100% !important;display:block" preload="'+t+'"'+(d.vars.opts.cc?' crossorigin="anonymous"':"")+'></video><div style="display:flex;opacity:0" class="bigPlayUI ctp"><a style="display:none" target=_blank rel=noopener></a><div class="bigPlayUIInner ctp" style="display:none"></div></div></div>'),b.w(e,{2:4,9:17,10:17,18:16,color:15,clear:"both",overflow:"visible"}),b.j.c(e,"bplay","block",".bigPlayUIInner"),d.d.appendChild(d.p=e),d.v=e.firstChild,function(e){if(!b.A){var t,r="canPlayType",o='video/mp4; codecs="avc1.42E01E',n=[0,o+'"',0,o+', mp4a.40.2"',1,'video/webm; codecs="vp9, vorbis"',2,"application/vnd.apple.mpegurl"],i=[!1,!1,!1];if(!e||!e[r])return;for(t=0;t<n.length;t+=2)e[r](n[t+1])&&(i[n[t]]=!0);b.J=i[2],b.A=i}}(d.v),d.rsz=[0,0],d.bp=e.childNodes[1],d.bp_svg=d.bp.childNodes[1],d.hasStyle={},i=d.bp.childNodes[0],b.w(d.bp_svg,{fill:"currentColor",9:8,12:"14px 22px",cursor:"pointer",borderRadius:"8px"}),b.w(d.bp,{display:"flex",opacity:0,position:"absolute",top:0,left:0,width:"100%",height:"100%",cursor:"pointer",alignItems:"center",justifyContent:"center",overflow:"hidden"}),d.v.addEventListener("contextmenu",function(e){return e.preventDefault(),!1}),d.loadVideoStyles()}var _,S,y,P="https://rumble.com",e="/embedJS/ulf6yv",w=(b.l=a(),s.RumbleErrorHandler||(l=0,s.RumbleErrorHandler=function(e){var t,r=e.message,o=e.filename,n=e.lineno,i=e.colno,d=D(o);o==d||r.match(/^Script error\./)||3<++l||(o=document.location+"",r=[D(o),l,r,d,n,i],e.error&&e.error.stack&&r.push(e.error.stack.split("\n").slice(1,3).join("\n")),d="/l/jserr?err="+encodeURIComponent(JSON.stringify(r)),o==r[0]&&(d=P+d),(t=document.createElement("img")).src=d,t.width=t.height=1,t.onload=t.onerror=function(){t.onload=null,t.onerror=null})},s.addEventListener("error",s.RumbleErrorHandler)),[]),x=(b.E=function(e){return e.split("?")[0]},b.B=function(e){var e=e.split("?"),r={};return e&&e[1]&&(e=e[1],new URLSearchParams(e).forEach(function(e,t){r[t]=e})),r},b.C=function(e){var r="";return b.D(e,function(e,t){r+=(r?"&":"")+encodeURIComponent(t)+"="+encodeURIComponent(e)}),r},b.D=function(e,t){var r,o;for(o in e)if(e.hasOwnProperty(o)&&void 0!==(r=t(e[o],o)))return r},b.K=function(e,t){if("undefined"==typeof localStorageBlocked)try{localStorageBlocked="undefined"==typeof localStorage||!localStorage}catch(e){localStorageBlocked=!0}if(void 0===t){if(!localStorageBlocked)try{t=localStorage.getItem(e)}catch(e){localStorageBlocked=!0}return localStorageBlocked?w[e]:parseInt(t)==t?parseInt(t):t}if(w[e]=t,!localStorageBlocked)try{return localStorage.setItem(e,t)}catch(e){localStorageBlocked=!1}return!1},b.L=function(e,t,r,o){if(e)if(!e.match(/^(http[s]?:)?\/\/([^/]*)\//)||r)return(o?"https:":"")+"//"+t+("/"!=e[0]?"/":"")+e;return e},b.M=function(e,t){return e.filter(function(e){return-1!==t.indexOf(e)})},[2,0,1]),C=["mp4","webm","hls"],H=(b.G=function(r,e){for(var o,t,n={},i=S=0;i<x.length;i++)e[o=C[t=x[i]]]&&(b.A[t]||"hls"==o)&&b.D(e[o],function(e,t){n.hasOwnProperty(t)||(e.key=t,n[t]=e,p(r,n[t],"hls"==o))});return n},b.I=function(){return"undefined"!=typeof Hls||(b.q(["hls"]),!1)},b.H=function(e){var r,o,n,i=480;e.res&&(i=e.res),e.vid.live&&!b.J&&b.I(),b.D(e.video_list,function(e,t){n=parseInt(t),"hls"!=r&&("hls"==t&&b.J||0<n&&n<=i&&(!r||r<n)?r=t:(!o||n<o&&0<n)&&(o=t))}),(r=r||o)&&e.video_list[r].set()},b.r=function(){var d={},a={},c={b:function(e,t,r){if("object"!=typeof e){if(d[e]&&!r)return!1;if(d[e]=t=t||1,a[e])for(;o=a[e].pop();)o(e,t);return!0}for(var o in e)c.b(o,e[o],r)},a:function(e,t,r){var o,n,i;for(r=r||{},o=0;i=e[o];o++)d[i]?r[i]=d[i]:(n&&(t=function(t,r){return function(e){c.a([t],r,e)}}(n[0],n[1])),n=[i,t]);n?(a[n[0]]||(a[n[0]]=[]),a[n[0]].push(function(e,t){r[e]=t,n[1](r)})):t(r)}};return c},n=b.r(),i=document,c={},b.s=function(e,t){var r,o,n=0;c[e]||(c[e]=1,(r=i.createElement("script")).type="text/javascript",r.src=e,t&&(r.addEventListener("load",o=function(e){if(n||t())return n=1;e&&setTimeout(o,50)},!1),o(1)),i.head.appendChild(r))},b.q=function(e,t){for(var r,o=0;o<e.length;o++)if("ima3"==e[o])b.s("https://imasdk.googleapis.com/js/sdkloader/ima3.js",function(){return!("undefined"==typeof google||!google||!google.ima)&&(n.b("ima3"),!0)});else if("custom_ui"!=e[o]){r=e[o];b.s(d.s.rd+"/j/p/"+r+("hls"!=r?".r2":"")+".js?_v=330",t)}},b.c=function(e,t,r){n.a(e,t),r||b.q(e)},d.rl=function(e,t){n.b(e)&&t&&t(b)},[0,1,"position","absolute","relative","fixed","normal","none","auto","width","height","margin","padding","border","display","#FFF","#000","100%","background","opacity"]),k=(b.w=h,b.y=function(e){var r={};return b.D(e,function(e,t){r[g(t)]=g(e)}),r},b.t=function(e,t,r,o,n,i,d,a){o||(o=e,n=t);var c="0",s="0";return a&&a.viewbox_top&&(c=a.viewbox_top),a&&a.viewbox_left&&(s=a.viewbox_left),i=i?" RumbleSVG-"+i:"",d=d||"",0<r.indexOf("stroke")&&(d+="stroke:currentColor;"),[e,t,'<svg style="'+d+'" class="RumbleElm'+i+'" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="'+e+'px" height="'+t+'px" viewBox="'+s+" "+c+" "+o+" "+n+'">'+r+"</svg>"]},b.j=b.r(),b.j.c=function(t,r,o,n){b.j.a([r],function(e){n&&(t=t.querySelectorAll(n)[0]),b.z(t,e[r][2]),o&&("string"==typeof o?t.style.display=o:o.apply(t))})},'<path stroke-width="3" stroke-linejoin="round" d="M19 11L3.2 1.5v19z"/>'),B=(b.j.b({bplay:b.t(25,25,k,22,22,"bplay"),play:b.t(22,22,k,0,0,"play","height:100%;"),loader:b.t(80,10,function(){for(var e,t="<g>",r=0;r<21;r++)t+='<circle cx="'+(10*r+5)+'" cy="5" r="'+(e=(e=r-6)<1||5<e?1:e)+'" />';return t+"</g>"}(),80,10)}),s.requestAnimationFrame?1:0),G={},O=(b.a=function(e,t){if(!G[e]&&"function"==typeof t&&(G[e]=t,!y)){if(y=1,!B)return setTimeout(v,1e3/24);s.requestAnimationFrame(v)}},b.i=function(e){e=b.u("div",0,0,e);return 1<e.childNodes.length?e.childNodes:e.firstChild},b.u=function(e,t,r,o){e=document.createElement(e);return o&&(e.innerHTML=o),t&&(e.className=t),r&&(e.id=r),E(e),e},b.z=function(e,t){e.innerHTML=t,j(e)},b.y({font:"12px sans-serif",fontWeight:6,lineHeight:6,boxSizing:"content-box",webkitBoxSizing:"content-box",19:1,18:7,11:0,12:0,border:7,9:8,10:8,visibility:"visible",textSizeAdjust:8,textDecoration:7})),E=function(e){var t;(t=e.tagName)&&"path"!=(t=t.toLowerCase())&&"video"!=t&&(h(e,O,!0),"svg"==t?h(e,{fill:"currentColor"},!0):(h(e,{color:"inherit"},!0),j(e)))},j=function(e){var t,r;if(t=e.childNodes)for(r=0;r<t.length;r++)E(t[r])};b.x=function(e,t,r,o){var n="__playerHover";(o=o||e)[n]||(e.addEventListener("mouseout",function(){h(o,o[n][0])}),e.addEventListener("mouseover",function(){h(o,o[n][1])})),o[n]=[r,t],h(o,r)};b.d=[];d.s={rd:P,ru:e,ds:{"opts":["norumbleads"]},rp:P+e+"/?request=",server:{"bw_tracking":1,"bw_noads_check":1,"bw_ourads_check":0}};b.k={},d.gdpr=2,b.m=function(e,t,r,o){var n=new XMLHttpRequest;n.onreadystatechange=function(){4==n.readyState&&200==n.status&&t(JSON.parse(n.responseText))},n.open("GET",(o?"":d.s.rp)+e),n.send()},b.e=function(e,t,r){var o,n,i,d=[];for("object"!=typeof e&&(e=[e]),o=0;o<e.length;o++)n=e[o],(!b.f[n]||1<b.f[n].loaded&&b.f[n].loaded+(1==e.length?900:1800)<a())&&(b.f[n]={loaded:0,wait:[]}),0==(i=b.f[n]).loaded&&(d.push(n),i.loaded=1),t&&i.loaded<9&&i.wait.push(t);return 0<d.length?(r=r?"&ext="+encodeURIComponent(JSON.stringify(r)):"",r+="&ad_wt="+(b.K("ad_wt")||0),b.m("video&ver=2&v="+d[0]+r,function(e){var t,r,o=[],n={};for(e.loaded||!e?n[d[0]]=e:n=e,b.D(n,function(e,t){for(;r=b.f[t].wait.pop();)o.indexOf(r)<0&&o.push(r);e&&(b.f[t]=e,b.f[t].loaded=a())}),t=0;t<o.length;t++)o[t]()}),1):(t&&t(),0)},d.resize=function(){b.D(b.k,function(e){b.h(e)})},b.h=function(e,t){var r,o=!e.rsz,n=[e.p.clientWidth,e.p.clientHeight],i=s.innerHeight,d=e.vars;d.resize||(d.resize=function(){try{return s.self!==s.top}catch(e){return!0}}()?"full":"auto");(!o&&(e.rsz[0]!=n[0]||e.rsz[1]!=n[1])||n[1]>i||t)&&(t=d.resize,d.ia&&(t="ia"),e.ui&&e.ui.isFloating&&(t="auto"),r=Math.floor(n[0]/16*9),"ia"==t?screen&&screen.height<r&&(r=screen.height):"full"==t?r=0:"window"==t?r=i:("ctpauto"==t&&e.ui&&e.ui.ctp&&(d.resize="auto"),(i<r||e.ui&&e.ui.getFullScreen())&&(r=0)),"window"!=t&&"ctpauto"!=t&&"auto16:9"!=t&&"full"!=t&&(e.vid&&e.vid.a&&e.vid.a.aden&&e.vid.a.aden[2])&&r<360&&0!=r&&!d.float&&(r=360),e.rsz[0]!=n[0]&&(o=1),n[1]!=r&&(o=1,e.p.style.height=0<r?(n[1]=r)+"px":"100%")),e.rsz&&!o||(e.rsz=n),o&&(b.g(e),e.j("resize"))},b.g=function(e){if(!(!e.vid||e.ui&&e.ui.hasPlayed)){var t,r,o,n=e.vid.i,i=e.vid.t,d=-1,a=e.rsz[0],c=e.rsz[1],s=a/c;if(i)for(t=0;t<i.length;t++)o=s<(o=(r=i[t]).w/r.h)?(c-a/o)*a:(a-c*o)*c,(d<0||o<d)&&(d=o,n=r.i);e.v.poster!=n&&(e.v.poster=n)}},d.$play=function(e,t){var r,o,n=JSON.parse(JSON.stringify(d.s.ds)),i={};if((n=f(n,e)).opts&&(b.D(n.opts,function(e){i[e]=1}),n.opts=i),void 0===n.gdpr?n.gdpr=2:n.gdpr=n.gdpr?1:0,2!=n.gdpr&&(d.gdpr=n.gdpr),b.n=-1==n.analytics||n.opts.minimal?1:0,b.o=n.opts.skip_ga_load?1:0,b.p=n.opts.force_ga_load?1:0,!n.div){if(!_)throw"No div was defined for the player";n.div=_}if(_=o=n.div,!b.k[o]||(r=b.k[o]).d.parentNode||(r=0),n.macros||(n.macros={}),!r){if(!(r=document.getElementById(o))){if(2<t)throw o+" div not found";s.addEventListener("DOMContentLoaded",function(){d.$play(e,3)})}b.k[o]||b.F++,b.k[o]=r=new m({d:r,vid:0,id:o,vars:n,server:d.s.server})}r.loadVideo(n.video),b.h(r)};d.rl("custom_ui");d.$playSettings=function(e){d.s.ds=f(d.s.ds,e)},s.addEventListener("resize",function(){b.a("resize",d.resize)}),s.addEventListener("orientationchange",function(){setTimeout(function(){d.resize()},500)});var z,L,I,R=s.Rumble;for(R._=z=R._||[],z.push=function(e){var t=z.slice.call(e),r=R["$"+t.shift()];"function"==typeof r?r.apply(R,t):t.push.call(z,e)},L=-1,I=z.length;++L<I;)z.push(z.shift())}function D(e){if(!e)return e;var t=e.match(new RegExp("http[s]?://[^/]*rumble.com(/.*)$"));return t?t[1]:e}}(window);
Rumble("play", {"video":{"id":"v1m7kuc"},"div":"player","resize":"full","opts":["force_ga_load"]});</script>
</body></html>
'''


class TimcastTestCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.server = ResponsesServer(
            responses_kwargs={'registry': OrderedRegistry})
        self.server.start()
        self.crawler = TimcastCrawler()
        self.server.get(
            self.server.url(),
            headers={'Content-Type': 'text/html'},
            body=RSP0)
        iframe_url = self.server.url('/embed/v1m7kuc/')
        self.server.get(
            self.server.url('/members-area/seth-weathers-megan-hansen-uncensored-show-crew-talks-nutrition-and-plastics-making-men-weak/'),
            headers={'Content-Type': 'text/html'},
            body=RSP1.replace('%%URL%%', iframe_url))
        self.server.get(iframe_url,
            headers={'Content-Type': 'text/html'},
            body=RSP2)

    def tearDown(self):
        self.server.stop()

    async def test_crawl(self):
        channel, videos = await self.crawler.crawl(self.server.url())
        videos = [v async for v, s in videos]
        self.assertEqual('Members Only: Timcast IRL', channel.name)
        self.assertEqual(1, len(videos))
        self.assertEqual(5, len(videos[0].sources))
