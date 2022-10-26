from unittest import IsolatedAsyncioTestCase

from responses.registries import OrderedRegistry
from responses_server import ResponsesServer

from videosrc.crawlers.rumble import RumbleCrawler


RSP0 = '''
<!DOCTYPE html>
<html lang="en">
   <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb#">
      <meta content="width=device-width,initial-scale=1" name="viewport"/>
      <title>vivafrei</title>
      <link href="https://rumble.com/user/vivafrei" rel="canonical"/>
      <link href="https://rumble.com/user/vivafrei?page=2" rel="next"/>
      <meta content="vivafrei's videos on Rumble.com" name="description"/>
      <meta content="noindex" name="robots"/>
      <meta content="155223717937973" property="fb:app_id"/>
      <meta content="@rumblevideo" name="twitter:site"/>
      <meta content="app-id=1518427877" name="apple-itunes-app"/>
      <meta content="vivafrei" property="og:title"/>
      <meta content="vivafrei's videos on Rumble.com" property="og:description"/>
      <meta content="https://rumble.com/user/vivafrei" property="og:url"/>
      <link href="/i/favicon-v4.png" rel="shortcut icon"/>
      <link href="/apple-touch-icon.png" rel="apple-touch-icon"/>
   </head>
   <body>
      <main>
         <div class="constrained">
            <div style="margin-bottom: 1rem">
               <div class="listing-header--white-bg"></div>
               <div class="listing-header--content">
                  <img alt="vivafrei" class="listing-header--thumb" src="https://sp.rmbl.ws/z0/V/u/q/b/Vuqba.asF.4-71v3-r79nct.jpeg"/>
                  <h1 class="listing-header--title">
                     vivafrei
                     <svg class="listing-header--verified verification-badge-icon" height="24" viewbox="0 0 24 24" width="24">
                        <circle cx="12" cy="12" r="12"></circle>
                        <path d="M5.4 11.1l5 5 8.2-8.2" fill="none" stroke="currentColor" stroke-miterlimit="10" stroke-width="2"></path>
                     </svg>
                  </h1>
                  <div class="listing-header--buttons">
                     <button class="round-button media-subscribe bg-green" data-action="subscribe" data-slug="vivafrei" data-title="vivafrei" data-type="user"><span class="subscribe-button-label">Subscribe</span><span class="subscribe-button-count">280K</span></button>
                     <button class="round-button locals-button" data-context="channel" data-locals-community="252318154180013735">
                        Join
                        <svg fill="none" height="24" viewbox="0 0 95 71" width="24">
                           <path d="M85.02 43.1a7.12 7.12 0 0 0 7.11-7.12 7.12 7.12 0 0 0-7.11-7.12 7.12 7.12 0 0 0-7.12 7.12 7.12 7.12 0 0 0 7.12 7.12z" fill="#88172B"></path>
                           <path d="M69.92 26.64v18.69h-4.8v-2a7.35 7.35 0 0 1-5.73 2.6 9.96 9.96 0 0 1-6.57-3.15 9.97 9.97 0 0 1 0-13.58 9.96 9.96 0 0 1 6.57-3.16 7.34 7.34 0 0 1 5.72 2.6v-2h4.8zm-4.8 9.34a5.13 5.13 0 0 0-3.17-4.74 5.12 5.12 0 0 0-5.58 1.11 5.13 5.13 0 0 0 3.62 8.76c1.36 0 2.66-.54 3.62-1.5a5.13 5.13 0 0 0 1.5-3.63zM41.38 39.4l2 4.3a9.7 9.7 0 0 1-6.48 2.22 9.94 9.94 0 0 1-7.3-2.76A9.95 9.95 0 0 1 26.55 36a9.96 9.96 0 0 1 3.06-7.19 9.94 9.94 0 0 1 7.3-2.76 9.64 9.64 0 0 1 6.48 2.23l-2 4.33a6.16 6.16 0 0 0-4.32-1.76 5.13 5.13 0 0 0-5.22 3.02 5.15 5.15 0 0 0 3.1 6.98 5.13 5.13 0 0 0 2.12.23 6.13 6.13 0 0 0 4.33-1.66z" fill="#fff"></path>
                           <path d="M9.93 43.1a7.12 7.12 0 0 0 7.11-7.12 7.12 7.12 0 0 0-7.11-7.12 7.12 7.12 0 0 0-7.12 7.12 7.12 7.12 0 0 0 7.12 7.12z" fill="#88172B"></path>
                           <path d="M17.93 15.53v4.8H2.03V1.6h4.72v13.93h11.18z" fill="#fff"></path>
                           <path d="M85.02 20.86A9.93 9.93 0 1 0 85 1a9.93 9.93 0 0 0 0 19.87zm-25.03-2.8a7.12 7.12 0 0 0 7.12-7.13 7.12 7.12 0 0 0-7.12-7.12 7.12 7.12 0 0 0-7.12 7.12A7.12 7.12 0 0 0 60 18.05z" fill="#88172B"></path>
                           <path d="M44.9 10.93a9.96 9.96 0 0 1-6.13 9.2A9.93 9.93 0 0 1 27.93 18a9.95 9.95 0 0 1-2.17-10.85 9.95 9.95 0 0 1 13-5.4 9.92 9.92 0 0 1 5.38 5.38c.5 1.21.75 2.5.75 3.81zm-4.83 0a5.13 5.13 0 0 0-3.16-4.74 5.12 5.12 0 0 0-5.58 1.11 5.13 5.13 0 0 0 3.62 8.76c1.36 0 2.66-.54 3.62-1.5a5.13 5.13 0 0 0 1.5-3.63zm53.37 53.42c0 3.8-3 6.63-8.2 6.63a14.33 14.33 0 0 1-8.65-2.7l1.5-4.53a10.94 10.94 0 0 0 6.63 2.63c2.22 0 3.85-.44 3.85-1.6 0-.84-.83-1.14-3.32-1.56-6.96-1.13-8.13-3.34-8.13-6.4 0-3.06 3.27-5.73 8.16-5.73 2.52.02 5 .63 7.26 1.77l-1.34 4.37a12.04 12.04 0 0 0-5.92-1.6c-1.94 0-3.34.34-3.34 1.14 0 1.13 1.95 1.32 3.94 1.66 6.34 1.06 7.56 3.55 7.56 5.92zm-25.47 1.2v4.78H52V51.7h4.91v13.84h11.07z" fill="#fff"></path>
                           <path d="M34.95 68.17a7.12 7.12 0 0 0 7.12-7.13 7.12 7.12 0 0 0-7.12-7.12 7.12 7.12 0 0 0-7.12 7.12 7.12 7.12 0 0 0 7.12 7.13zM9.92 70.98a9.93 9.93 0 1 0 0-19.86 9.93 9.93 0 0 0 0 19.86z" fill="#88172B"></path>
                        </svg>
                     </button>
                  </div>
               </div>
            </div>
            <div class="main-and-sidebar">
               <div style="flex: 1">
                  <ol>
                     <li class="video-listing-entry">
                        <article class="video-item">
                           <h3 class="video-item--title">Amazon Sued for Selling "Suicide Kits" and the Allegations are HORRIFYING! Viva Clips</h3>
                           <a class="video-item--a" href="/v1onhfm-amazon-sued-for-selling-suicide-kits-and-the-allegations-are-horrifying-viv.html"><img alt='Amazon Sued for Selling "Suicide Kits" and the Allegations are HORRIFYING! Viva Clips' class="video-item--img" src="https://sp.rmbl.ws/s8/6/c/q/N/e/cqNeg.oq1b.jpg"/></a>
                           <footer class="video-item--footer ellipsis-1">
                              <address class="video-item--by">
                                 <a class="video-item--by-a video-item--by-a--u71v3" href="/user/vivafrei" rel="author">
                                    <div class="ellipsis-1">
                                       vivafrei
                                       <svg class="video-item--by-verified verification-badge-icon" height="24" viewbox="0 0 24 24" width="24">
                                          <circle cx="12" cy="12" r="12"></circle>
                                          <path d="M5.4 11.1l5 5 8.2-8.2" fill="none" stroke="currentColor" stroke-miterlimit="10" stroke-width="2"></path>
                                       </svg>
                                    </div>
                                 </a>
                              </address>
                              <span class="video-item--duration" data-value="7:35"></span><span class="video-item--meta video-item--views" data-value="137"></span><span class="video-item--meta video-item--rumbles" data-value="110"></span><time class="video-item--meta video-item--time" datetime="2022-10-18T22:17:53-04:00">Oct 19</time>
                           </footer>
                        </article>
                     </li>
                  </ol>
                  <div style="margin: 1em 0">
                     <nav class="paginator">
                        <ul class="paginator--ul">
                           <li class="paginator--li">
                              <span aria-label="1" class="paginator--link paginator--link--current"></span>
                           </li>
                           <li class="paginator--li paginator--li--next">
                              <a aria-label="2" class="paginator--link" href="/user/vivafrei?page=2"></a>
                           </li>
                           <li class="paginator--li">
                              <a aria-label="3" class="paginator--link" href="/user/vivafrei?page=3"></a>
                           </li>
                           <li class="paginator--li">
                              <a aria-label="4" class="paginator--link" href="/user/vivafrei?page=4"></a>
                           </li>
                           <li class="paginator--li">
                              <a aria-label="»" class="paginator--link" href="/user/vivafrei?page=5"></a>
                           </li>
                        </ul>
                     </nav>
                  </div>
               </div>
               <div class="sidebar">
                  <input id="is-sidebar-open" type="checkbox"/>
                  <div class="bottom-popup" data-is-open="">
                     <label class="bottom-popup--header" for="is-sidebar-open">
                     <span class="bottom-popup--button">
                     <span class="bottom-popup--header-text"></span>
                     <span class="bottom-popup--arrow"></span>
                     </span>
                     </label>
                     <div class="bottom-popup--contents">
                        <div class="bottom-popup--sidebar">
                           <nav class="tuner-box">
                              <div class="tuner-box--section">
                                 <div class="tuner-box--section-header">Sort by</div>
                                 <ul class="tuner-box--ul">
                                    <li>
                                       <span class="tuner-box--link tuner-box--link--current">Most recent</span>
                                    </li>
                                    <li>
                                       <a class="tuner-box--link" href="/user/vivafrei?sort=views">Views</a>
                                    </li>
                                 </ul>
                              </div>
                              <div class="tuner-box--section">
                                 <div class="tuner-box--section-header">Date</div>
                                 <ul class="tuner-box--ul">
                                    <li>
                                       <a class="tuner-box--link" href="/user/vivafrei?date=today">Today</a>
                                    </li>
                                    <li>
                                       <a class="tuner-box--link" href="/user/vivafrei?date=this-week">Last week</a>
                                    </li>
                                    <li>
                                       <a class="tuner-box--link" href="/user/vivafrei?date=this-month">Last month</a>
                                    </li>
                                    <li>
                                       <a class="tuner-box--link" href="/user/vivafrei?date=this-year">Last year</a>
                                    </li>
                                    <li>
                                       <span class="tuner-box--link tuner-box--link--current">All Time</span>
                                    </li>
                                 </ul>
                              </div>
                              <div class="tuner-box--section">
                                 <div class="tuner-box--section-header">Duration</div>
                                 <ul class="tuner-box--ul">
                                    <li>
                                       <span class="tuner-box--link tuner-box--link--current">Any</span>
                                    </li>
                                    <li>
                                       <a class="tuner-box--link" href="/user/vivafrei?duration=short">Short</a>
                                    </li>
                                    <li>
                                       <a class="tuner-box--link" href="/user/vivafrei?duration=long">Long</a>
                                    </li>
                                 </ul>
                              </div>
                           </nav>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </main>
      <header class="header">
         <div class="header-div constrained">
            <button aria-label="main menu" class="main-menu-toggle">
               <svg class="main-menu-open" height="16" width="20">
                  <path d="M0 1h20M0 8h20M0 15h20"></path>
               </svg>
               <svg class="main-menu-close" height="16" width="20">
                  <path d="M2.5.5 l15 15 m0-15 l-15 15"></path>
               </svg>
            </button>
            <a class="header-logo" href="/">
            <img alt="Rumble" id="logo_light" src="/img/rumble-full-logo-v4.svg"/>
            <img alt="Rumble" hidden="" id="logo_dark" src="/img/rumble-full-logo-v4-dark.svg"/>
            </a>
            <form class="header-search">
               <select class="header-search-select select-arrow-bg">
                  <option>Videos</option>
                  <option>Channels</option>
                  <option selected="" value="user">vivafrei</option>
               </select>
               <input class="header-search-field" name="query" placeholder="Search" type="search" value=""/>
               <button aria-label="search Rumble" class="header-search-submit">
                  <svg class="header-search-icon" viewbox="0 0 26 26">
                     <path d="M17.6 17.6l6.3 6.3M2.2 11.2a9 9 0 1 0 18 0 9 9 0 1 0-18 0" fill="none" stroke-linecap="round" stroke-width="2"></path>
                  </svg>
               </button>
            </form>
            <button class="header-upload" title="Upload">
               <svg viewbox="0 0 26 26">
                  <path d="M4.2 17.5s-2.7-3.1-1.9-7.1C3 6.8 5.9 3.9 9.9 3.9c3.5 0 5.1 1.6 6.2 2.7 1.1 1.1 1.4 3.5 1.4 3.5s2.7-.7 4.4.7 2.4 3.8 1.8 5.6-2.6 3.1-2.6 3.1M9 17.1l4.1-3.8 4.2 3.8m-4.2 5.4v-9.2" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path>
               </svg>
            </button>
            <button aria-label="sign in" class="header-user">
               <svg class="user-image user-image--icon header-user-img">
                  <path d="M8 6.8a5 5 0 1 0 10 0 5 5 0 1 0-10 0m14.8 16.7v-3.7a4 4 0 0 0-4-4H7.2a4 4 0 0 0-4 4v3.7" fill="none" stroke-linecap="round" stroke-width="2"></path>
               </svg>
               <span class="header-user-info">
               <span class="header-user-name">Sign In</span>
               </span>
            </button>
         </div>
      </header>
      <nav class="navs">
         <div class="constrained" style="position:relative">
            <div class="hover-menu main-menu-nav" id="main-menu">
               <a class="main-menu-item" href="/videos?date=this-week">
                  <svg class="main-menu-icon">
                     <path d="M5 13a8 8 0 1 0 16 0 8 8 0 1 0-16 0M2.9 8.6C4.1 6 6.2 3.9 8.7 2.8m14.5 14.7a11.5 11.5 0 0 1-5.8 5.7M13 6.9V13h4.2" fill="none"></path>
                  </svg>
                  Latest
               </a>
               <a class="main-menu-item" href="/editor-picks">
                  <svg class="main-menu-icon" height="27" viewbox="0 0 26 27" width="26">
                     <path d="M4 8a6.5 7 0 1 0 13 0A6.5 7 0 1 0 4 8m15 13.5C15.6 11 1.1 13.9 1 25m13-2.4l3.9 4.4 7.1-8" fill="none"></path>
                  </svg>
                  Editor Picks
               </a>
               <a class="main-menu-item" href="/videos?sort=views&amp;date=today">
                  <svg class="main-menu-icon" height="24" viewbox="0 0 24 24" width="24">
                     <path d="m23 6-9.5 9.5-5-5L1 18M17 6h6v6"></path>
                  </svg>
                  Trending
               </a>
               <a class="main-menu-item" href="/license-videos">
                  <svg class="main-menu-icon" height="26" viewbox="0 0 26 26" width="26">
                     <path d="M19.1 20H2.3V6h11.8M24.3 20h-5.5s-.9-1.5-1.4-2c-.5-.5-1-1.3-1.9-1.7-.4-.2-2.2-1.6-2.3-2.5 0-1.7 1.1-1.4 2.3-1 1.2.5 3.6 1.6 3.6 1.6l-.9-6.7S12.9 6.2 13 5.9c.1-.3 5.8-1.9 7.2-.2s2 4.5 2.8 5.1c.8.6 1.5.6 1.5.6 M6.8,11.1a1.8,1.8 0 1,0 3.6,0a1.8,1.8 0 1,0 -3.6,0 M5.8 16.6c0-1.5 1.2-2.7 2.7-2.7s2.7 1.2 2.7 2.7" fill="none"></path>
                  </svg>
                  License Videos
               </a>
               <div class="js-theme-option-group" hidden="">
                  <h3 class="main-menu-heading">Theme</h3>
                  <a class="main-menu-item js-theme-option" data-theme="system" href="">
                     <svg class="main-menu-icon" height="24" viewbox="0 0 24 24" width="24">
                        <path d="M12 1v2m0 18v2M4.2 4.2l1.4 1.4m12.8 12.8 1.4 1.4M1 12h2m18 0h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4M16 12.36A4 4 0 1 1 11.64 8 3.12 3.12 0 0 0 16 12.36Z"></path>
                     </svg>
                     OS Default
                  </a>
                  <a class="main-menu-item js-theme-option" data-theme="dark" href="">
                     <svg class="main-menu-icon" height="24" viewbox="0 0 24 24" width="24">
                        <path d="M12.1 4.1c.3-.4 0-.9-.5-.8a8.5 8.5 0 1 0 9.3 12.4c.3-.4-.1-.9-.6-.7A7 7 0 0 1 12 4.2Z"></path>
                     </svg>
                     Dark Mode
                  </a>
                  <a class="main-menu-item js-theme-option" data-theme="light" href="">
                     <svg class="main-menu-icon" height="24" viewbox="0 0 24 24" width="24">
                        <path d="M7 12a5 5 0 1 0 10 0 5 5 0 1 0-10 0m5-11v2m0 18v2M4.2 4.2l1.4 1.4m12.8 12.8 1.4 1.4M1 12h2m18 0h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"></path>
                     </svg>
                     Light Mode
                  </a>
               </div>
               <h3 class="main-menu-heading">Featured Channels</h3>
               <a class="main-menu-item" href="/c/Reuters">Reuters</a><a class="main-menu-item" href="/c/WildCreatures">Wild Creatures</a><a class="main-menu-item" href="/c/WayneDupreeShow">The Wayne Dupree Show</a><a class="main-menu-item" href="/c/Newsy">Newsy</a><a class="main-menu-item" href="/c/JustPlanes">JustPlanes</a><a class="main-menu-item" href="/c/DevinNunes">Devin Nunes</a><a class="main-menu-item" href="/c/MarkDice">MarkDice</a><a class="main-menu-item" href="/c/Bongino">The Dan Bongino Show</a><a class="main-menu-item" href="/c/Cioccolanti">Cioccolanti</a><a class="main-menu-item" href="/c/DineshDsouza">Dinesh Dsouza</a><a class="main-menu-item" href="/c/MLChristiansen">MLChristiansen</a><a class="main-menu-item" href="/c/RobertGouveia">RobertGrulerEsq</a><a class="main-menu-item" href="/c/BannonsWarRoom">BannonsWarRoom</a><a class="main-menu-item" href="/c/BennyJohnson">BennyJohnson</a><a class="main-menu-item" href="/c/NoreensKitchen">NoreensKitchen</a><a class="main-menu-item" href="/c/CharlieKirk">Charlie Kirk</a><a class="main-menu-item" href="/c/NewsmaxTV">NewsmaxTV</a><a class="main-menu-item" href="/c/MariaBartiromo">MariaBartiromo</a><a class="main-menu-item" href="/user/vivafrei">Viva Frei</a><a class="main-menu-item" href="/c/Fleccas">Fleccas</a><a class="main-menu-item" href="/c/Styxhexenhammer666">Styxhexenhammer666</a><a class="main-menu-item" href="/c/SeanHannity">Sean Hannity</a><a class="main-menu-item" href="/c/TrishReganShow">Trish Regan</a><a class="main-menu-item" href="/c/SamuelEarpArtist">Samuel Earp Artist</a><a class="main-menu-item" href="/c/KayaJones">KayaJones</a><a class="main-menu-item" href="/c/TheNerdRealm">The Nerd Realm</a><a class="main-menu-item" href="/c/sideserfcakes">Side Serf Cakes</a><a class="main-menu-item" href="/c/spaceXcentric">spaceXcentric</a><a class="main-menu-item" href="/c/MikhailaPeterson">Mikhaila Peterson</a><a class="main-menu-item" href="/c/NTDNews">NTDNews</a><a class="main-menu-item" href="/c/TheOfficerTatum">The Officer Tatum</a><a class="main-menu-item" href="/c/OutKickTheCoverage">OutKick</a><a class="main-menu-item" href="/c/CWLemoine">CWLemoine</a><a class="main-menu-item" href="/c/LaurenChen">Lauren Chen</a><a class="main-menu-item" href="/c/DonaldTrump">Donald Trump</a><a class="main-menu-item" href="/c/TheHistoryGuy">The History Guy</a><a class="main-menu-item" href="/c/RebelNews">RebelNews</a><a class="main-menu-item" href="/c/pintswithaquinas">pintswithaquinas</a><a class="main-menu-item" href="/c/TheBodyLanguageGuy">TheBodyLanguageGuy</a><a class="main-menu-item" href="/c/YelllowFlash">YelllowFlash</a><a class="main-menu-item" href="/c/BrightInsight">BrightInsight</a><a class="main-menu-item" href="/c/PaulandMorgan">PaulandMorgan</a><a class="main-menu-item" href="/c/AwakenWithJP">Awaken With JP</a><a class="main-menu-item" href="/c/TulsiGabbard">Tulsi Gabbard</a><a class="main-menu-item" href="/c/TheBabylonBee">The Babylon Bee</a><a class="main-menu-item" href="/c/BenShapiro">Ben Shapiro</a><a class="main-menu-item" href="/c/FactsChannel">Facts</a><a class="main-menu-item" href="/c/RandPaul">Rand Paul</a><a class="main-menu-item" href="/c/DonaldJTrumpJr">Donald Trump Jr</a><a class="main-menu-item" href="/c/EliseStefanik">Elise Stefanik</a><a class="main-menu-item" href="/c/BlacktipH">BlacktipH</a><a class="main-menu-item" href="/c/LifeStories">Life Stories</a><a class="main-menu-item" href="/c/c-647947">SCI</a><a class="main-menu-item" href="/c/StevenCrowder">Steven Crowder</a><a class="main-menu-item" href="/c/NYPost">New York Post</a><a class="main-menu-item" href="/c/PageSix">PageSix</a><a class="main-menu-item" href="/c/Decider">Decider</a><a class="main-menu-item" href="/c/JohnStossel">John Stossel</a><a class="main-menu-item" href="/c/RonPaulLibertyReport">Ron Paul Liberty Report</a><a class="main-menu-item" href="/c/ARKMedia">ARKMedia</a><a class="main-menu-item" href="/c/Locals">Locals</a><a class="main-menu-item" href="/c/Timcast">Timcast</a><a class="main-menu-item" href="/c/TimcastIRL">TimcastIRL</a><a class="main-menu-item" href="/c/Entrepreneur">Entrepreneur</a><a class="main-menu-item" href="/c/EpochTV">EpochTV</a><a class="main-menu-item" href="/c/WhitneyBjerken">WhitneyBjerken</a><a class="main-menu-item" href="/c/DrDrew">Dr Drew</a><a class="main-menu-item" href="/c/Yarnhub">Yarnhub</a><a class="main-menu-item" href="/c/RubinReport">Rubin Report</a><a class="main-menu-item" href="/c/GGreenwald">Glenn Greenwald</a><a class="main-menu-item" href="/c/MattKohrs">Matt Kohrs (Finance)</a><a class="main-menu-item" href="/c/HabibiBros">Habibi Power Hour</a><a class="main-menu-item" href="/c/Orf">Orf</a><a class="main-menu-item" href="/c/Inquire">Inquire</a><a class="main-menu-item" href="/c/phetasy">phetasy</a><a class="main-menu-item" href="/c/academyofideas">academyofideas</a><a class="main-menu-item" href="/c/JorgeMasvidal">Jorge Masvidal</a><a class="main-menu-item" href="/c/russellbrand">Russell Brand</a><a class="main-menu-item" href="/c/HonestReportingCanada">Honest Reporting</a><a class="main-menu-item" href="/c/GrantCardone">Grant Cardone</a><a class="main-menu-item" href="/c/ChrisJericho">ChrisJericho</a><a class="main-menu-item" href="/c/TheRamseyShowHighlights">TheRamseyShowHighlights</a><a class="main-menu-item" href="/c/TheRamseyShowFullEpisodes">TheRamseyShowFullEpisodes</a><a class="main-menu-item" href="/c/TheInterviewRoom">TheInterviewRoom</a><a class="main-menu-item" href="/c/MedicalMedium">MedicalMedium</a><a class="main-menu-item" href="/c/TheJimmyDoreShow">TheJimmyDoreShow</a><a class="main-menu-item" href="/c/ClayandBuck">ClayandBuck</a><a class="main-menu-item" href="/c/UprightHealth">UprightHealth</a><a class="main-menu-item" href="/c/TheRichDadChannel">TheRichDadChannel</a><a class="main-menu-item" href="/c/NaturesAlwaysRight">NaturesAlwaysRight</a><a class="main-menu-item" href="/c/ChampagneSharks">ChampagneSharks</a><a class="main-menu-item" href="/c/PetervonPanda">PetervonPanda</a><a class="main-menu-item" href="/c/AfterSkool">AfterSkool</a><a class="main-menu-item" href="/c/SmokyRibsBBQ">SmokyRibsBBQ</a><a class="main-menu-item" href="/c/MichaelLeeStrategy">MichaelLeeStrategy</a><a class="main-menu-item" href="/c/iammrbeat">iammrbeat</a><a class="main-menu-item" href="/c/WorkshopCompanion">WorkshopCompanion</a><a class="main-menu-item" href="/c/StockCurry">StockCurry</a><a class="main-menu-item" href="/c/ThePodcastoftheLotusEaters">ThePodcastoftheLotusEaters</a><a class="main-menu-item" href="/c/ArielleScarcella">ArielleScarcella</a><a class="main-menu-item" href="/c/TradersLanding">TradersLanding</a><a class="main-menu-item" href="/c/RuckaRuckaAli">Rucka Rucka Ali</a><a class="main-menu-item" href="/c/DegenerateJay">DegenerateJay</a><a class="main-menu-item" href="/c/DegeneratePlays">DegeneratePlays</a><a class="main-menu-item" href="/c/DVGPodcast">DVGPodcast</a><a class="main-menu-item" href="/c/TheDiveWithJacksonHinkle">TheDiveWithJacksonHinkle</a><a class="main-menu-item" href="/c/thatbeatgoeson">thatbeatgoeson</a><a class="main-menu-item" href="/c/Kilmeade">Kilmeade</a><a class="main-menu-item" href="/c/TheHillbillyKitchen">TheHillbillyKitchen</a><a class="main-menu-item" href="/c/NewsTalkSTL">NewsTalkSTL</a><a class="main-menu-item" href="/c/LogOffAlready">LogOffAlready</a><a class="main-menu-item" href="/c/EnterShaolin">EnterShaolin</a><a class="main-menu-item" href="/c/WillCain">WillCain</a><a class="main-menu-item" href="/c/MegynKelly">MegynKelly</a><a class="main-menu-item" href="/c/RepKevinMcCarthy">RepKevinMcCarthy</a><a class="main-menu-item" href="/c/AlisonMorrow">AlisonMorrow</a><a class="main-menu-item" href="/c/BenUyeda">BenUyeda</a><a class="main-menu-item" href="/c/MrBuildIt">MrBuildIt</a><a class="main-menu-item" href="/c/SteveScalise">SteveScalise</a><a class="main-menu-item" href="/c/TheHeritageFoundation">TheHeritageFoundation</a><a class="main-menu-item" href="/c/TheDailySignal">TheDailySignal</a><a class="main-menu-item" href="/c/GreenDreamProject">GreenDreamProject</a><a class="main-menu-item" href="/c/BlackPowerMediaChannel">BlackPowerMediaChannel</a><a class="main-menu-item" href="/c/AmericanSongwriter">AmericanSongwriter</a><a class="main-menu-item" href="/c/modernwisdompodcast">modernwisdompodcast</a><a class="main-menu-item" href="/c/IsaacArthur">IsaacArthur</a><a class="main-menu-item" href="/c/TomAntosFilms">TomAntosFilms</a><a class="main-menu-item" href="/c/ColionNoir">ColionNoir</a><a class="main-menu-item" href="/c/KimIversen">KimIversen</a><a class="main-menu-item" href="/c/Homesteadonomics">Homesteadonomics</a><a class="main-menu-item" href="/c/TheAdventureAgents">TheAdventureAgents</a><a class="main-menu-item" href="/c/NDWoodworkingArt">NDWoodworkingArt</a><a class="main-menu-item" href="/c/KenDBerryMD">KenDBerryMD</a><a class="main-menu-item" href="/c/davidpakmanshow">davidpakmanshow</a><a class="main-menu-item" href="/c/HeresyFinancial">HeresyFinancial</a><a class="main-menu-item" href="/c/RepJimBanks">RepJimBanks</a><a class="main-menu-item" href="/c/ATRestoration">ATRestoration</a><a class="main-menu-item" href="/c/ThisSouthernGirlCan">ThisSouthernGirlCan</a><a class="main-menu-item" href="/c/RockFeed">RockFeed</a><a class="main-menu-item" href="/c/CountryCast">CountryCast</a><a class="main-menu-item" href="/c/ShaunAttwood">ShaunAttwood</a><a class="main-menu-item" href="/c/TwinCoconuts">TwinCoconuts</a><a class="main-menu-item" href="/c/diywife">diywife</a><a class="main-menu-item" href="/c/RekietaLaw">RekietaLaw</a><a class="main-menu-item" href="/c/MontyFranklin">MontyFranklin</a><a class="main-menu-item" href="/c/GeeksandGamers">GeeksandGamers</a><a class="main-menu-item" href="/c/SportsWars">SportsWars</a><a class="main-menu-item" href="/c/nfldaily">nfldaily</a><a class="main-menu-item" href="/c/nbanow">nbanow</a><a class="main-menu-item" href="/c/GeeksAndGamersPlay">GamingWithGeeks</a><a class="main-menu-item" href="/c/ParkHoppin">ParkHoppin</a><a class="main-menu-item" href="/c/GeeksAndGamersClips">GeeksAndGamersClips</a><a class="main-menu-item" href="/c/chiefstv">chiefstv</a><a class="main-menu-item" href="/c/brownsreport">brownstv</a><a class="main-menu-item" href="/c/nygiantstv">giantstv</a><a class="main-menu-item" href="/c/warriorstv">warriorstv</a><a class="main-menu-item" href="/c/lakerstv">lakerstv</a><a class="main-menu-item" href="/c/DynastyFlock">DynastyFlock</a><a class="main-menu-item" href="/c/FantasyFlockNetwork">FantasyFlockNetwork</a><a class="main-menu-item" href="/c/rwmalonemd">rwmalonemd</a><a class="main-menu-item" href="/c/Chubbyemu">Chubbyemu</a><a class="main-menu-item" href="/c/AnthonyJ350">AnthonyJ350</a><a class="main-menu-item" href="/c/ReasonTV">ReasonTV</a><a class="main-menu-item" href="/c/GfinityTv">GfinityTv</a><a class="main-menu-item" href="/c/engineerman">engineerman</a><a class="main-menu-item" href="/c/Newsthink">Newsthink</a><a class="main-menu-item" href="/c/MrScientific">MrScientific</a><a class="main-menu-item" href="/c/TheS">TheS</a><a class="main-menu-item" href="/c/Debunked">Debunked</a><a class="main-menu-item" href="/c/sydneywatson">sydneywatson</a><a class="main-menu-item" href="/c/UncivilLaw">UncivilLaw</a><a class="main-menu-item" href="/c/Dannyjokes">Dannyjokes</a><a class="main-menu-item" href="/c/BitcoinMagazine">BitcoinMagazine</a><a class="main-menu-item" href="/c/SonofaTech">SonofaTech</a><a class="main-menu-item" href="/c/MysteryScoop">MysteryScoop</a><a class="main-menu-item" href="/c/SpencerCornelia">SpencerCornelia</a><a class="main-menu-item" href="/c/Multipolarista">Multipolarista</a><a class="main-menu-item" href="/c/TheLeadAttorney">TheLeadAttorney</a><a class="main-menu-item" href="/c/Monark">Monark</a><a class="main-menu-item" href="/c/ThinkBeforeYouSleep">ThinkBeforeYouSleep</a><a class="main-menu-item" href="/c/Ferrez">Ferrez</a><a class="main-menu-item" href="/c/RonDeSantisFL">RonDeSantisFL</a><a class="main-menu-item" href="/c/TheDawgfathasBBQ">TheDawgfathasBBQ</a><a class="main-menu-item" href="/c/JimBreuer">JimBreuer</a><a class="main-menu-item" href="/c/RyanLongcomedy">RyanLongcomedy</a><a class="main-menu-item" href="/c/LeeCamp">LeeCamp</a><a class="main-menu-item" href="/c/PrimitiveSurvivalTools">PrimitiveSurvivalTools</a><a class="main-menu-item" href="/c/TheChrisSalcedoShow">TheChrisSalcedoShow</a><a class="main-menu-item" href="/c/FullMag">FullMag</a><a class="main-menu-item" href="/c/BitBoyCrypto">BitBoyCrypto</a><a class="main-menu-item" href="/c/Komando">Komando</a><a class="main-menu-item" href="/c/TheMagicMatt">TheMagicMatt</a><a class="main-menu-item" href="/c/TheKevinRobertsShow">TheKevinRobertsShow</a><a class="main-menu-item" href="/c/TheInfoWarrior">TheInfoWarrior</a><a class="main-menu-item" href="/c/DirtyMoney">DirtyMoney</a><a class="main-menu-item" href="/c/UpperEchelonGamers">UpperEchelonGamers</a><a class="main-menu-item" href="/c/TripleSgames">TripleSgames</a><a class="main-menu-item" href="/c/BrainyDose">BrainyDose</a><a class="main-menu-item" href="/c/worldnomactravel">worldnomactravel</a><a class="main-menu-item" href="/c/TylerFischer">TylerFischer</a><a class="main-menu-item" href="/c/Geometryptamine">GeometryTrip</a><a class="main-menu-item" href="/c/OwnagePranks">OwnagePranks</a><a class="main-menu-item" href="/c/LockPickingLawyer">LockPickingLawyer</a><a class="main-menu-item" href="/c/HikeCampClimb">HikeCampClimb</a><a class="main-menu-item" href="/c/NickSearcy">NickSearcy</a><a class="main-menu-item" href="/c/ReviewTechUSA">ReviewTechUSA</a><a class="main-menu-item" href="/c/Rengawr">Rengawr</a><a class="main-menu-item" href="/c/lifeinthe1800s">lifeinthe1800s</a><a class="main-menu-item" href="/c/MarkandMattis">MarkandMattis</a><a class="main-menu-item" href="/c/GabePoirot">GabePoirot</a><a class="main-menu-item" href="/c/Backfire">Backfire</a><a class="main-menu-item" href="/c/realpatriotgames">realpatriotgames</a><a class="main-menu-item" href="/c/RobsAquaponics">RobsAquaponics</a><a class="main-menu-item" href="/c/tateconfidential">tateconfidential</a><a class="main-menu-item" href="/c/JoshuaPhilipp">JoshuaPhilipp</a><a class="main-menu-item" href="/c/Epimetheus">Epimetheus</a><a class="main-menu-item" href="/c/RumbleEvents">RumbleEvents</a><a class="main-menu-item" href="/c/robbraxman">robbraxman</a><a class="main-menu-item" href="/c/LofiGirl">LofiGirl</a><a class="main-menu-item" href="/c/usefulidiots">usefulidiots</a><a class="main-menu-item" href="/c/JedediahBilaLive">JedediahBilaLive</a><a class="main-menu-item" href="/c/ValuetainmentShortclips">ValuetainmentShortclips</a><a class="main-menu-item" href="/c/Valuetainment">Valuetainment</a><a class="main-menu-item" href="/c/TateSpeech">TateSpeech</a><a class="main-menu-item" href="/c/CobraTate">CobraTate</a><a class="main-menu-item" href="/c/SailingZatara">SailingZatara</a><a class="main-menu-item" href="/c/DrJohnCampbell">DrJohnCampbell</a><a class="main-menu-item" href="/c/theoriesofeverything">theoriesofeverything</a><a class="main-menu-item" href="/c/BeyondScience">BeyondScience</a><a class="main-menu-item" href="/c/RandyBooker">RandyBooker</a><a class="main-menu-item" href="/c/AIRCLIPScom">AIRCLIPScom</a><a class="main-menu-item" href="/c/ScaryInteresting">ScaryInteresting</a><a class="main-menu-item" href="/c/JasonCorey">JasonCorey</a><a class="main-menu-item" href="/c/BohoBeautiful">BohoBeautiful</a><a class="main-menu-item" href="/c/PBDPodcast">PBDPodcast</a><a class="main-menu-item" href="/c/TheCrazyChannel">TheCrazyChannel</a><a class="main-menu-item" href="/c/TheHungryHussey">TheHungryHussey</a><a class="main-menu-item" href="/c/InteractiveBiology">InteractiveBiology</a><a class="main-menu-item" href="/c/stevewilldoit">stevewilldoit</a><a class="main-menu-item" href="/c/FRIGA">FRIGA</a><a class="main-menu-item" href="/c/DreDrexler">DreDrexler</a><a class="main-menu-item" href="/c/YOUCAR">YOUCAR</a><a class="main-menu-item" href="/c/JeremyLynch">JeremyLynch</a><a class="main-menu-item" href="/c/TannerBraungardt">TannerBraungardt</a><a class="main-menu-item" href="/user/RepMattGaetz">RepMattGaetz</a><a class="main-menu-item" href="/user/Libsoftiktok">Libsoftiktok</a><a class="main-menu-item" href="/user/TreasureHuntingWithJebus">TreasureHuntingWithJebus</a><a class="main-menu-item" href="/user/TheSCraft">TheSCraft</a><a class="main-menu-item" href="/user/andyh1202">andyh1202</a><a class="main-menu-item" href="/user/HybridCalisthenics">HybridCalisthenics</a><a class="main-menu-item" href="/user/OwnagePranks">OwnagePranks</a><a class="main-menu-item" href="/user/LockPickingLawyer">LockPickingLawyer</a><a class="main-menu-item" href="/user/lifeinthe1800s">lifeinthe1800s</a><a class="main-menu-item" href="/user/HumbleMechanic1">HumbleMechanic1</a><a class="main-menu-item" href="/user/VitalyTheGoat">VitalyTheGoat</a><a class="main-menu-item" href="/user/ViralHog">Viral Hog</a> 
            </div>
            <div class="hover-menu header-upload-menu">
               <a class="main-menu-item" href="/upload.php">
                  <svg class="main-menu-icon" viewbox="0 0 26 26">
                     <path d="M4.2 17.5s-2.7-3.1-1.9-7.1C3 6.8 5.9 3.9 9.9 3.9c3.5 0 5.1 1.6 6.2 2.7 1.1 1.1 1.4 3.5 1.4 3.5s2.7-.7 4.4.7 2.4 3.8 1.8 5.6-2.6 3.1-2.6 3.1M9 17.1l4.1-3.8 4.2 3.8m-4.2 5.4v-9.2" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path>
                  </svg>
                  Upload Video
               </a>
               <a class="main-menu-item" href="/live?go-live">
                  <svg class="main-menu-icon" viewbox="0 0 30 16" width="20">
                     <path d="M8 4a8 8 0 0 0 0 8M4 1a14 14 0 0 0 0 14m18-3a8 8 0 0 0 0-8m4 11a14 14 0 0 0 0-14" fill="none" stroke-linecap="round" stroke-width="2"></path>
                     <circle cx="15" cy="8" fill="none" r="2" stroke-width="4"></circle>
                  </svg>
                  Go Live
               </a>
            </div>
         </div>
      </nav>
      <footer class="footer">
         <div class="constrained">
            <nav class="footer-nav"></nav>
            <div class="footer-terms-copyright">
               <nav class="footer-terms">
                  <a class="footer-terms-link divider" href="/s/terms" rel="nofollow">Terms &amp; Conditions</a>
                  <a class="footer-terms-link divider" href="/s/privacy" rel="nofollow">Privacy Policy</a>
                  <a class="footer-terms-link" href="/s/dmca" rel="nofollow">Copyright / DMCA</a>
               </nav>
               <p class="footer-copyright">Copyright © 2022 Rumble. All Rights Reserved.</p>
            </div>
         </div>
      </footer>
   </body>
</html>
'''
RSP1 = '''
<!DOCTYPE html>
<html lang="en">
   <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb#">
      <meta content="width=device-width,initial-scale=1" name="viewport"/>
      <title>Amazon Sued for Selling "Suicide Kits" and the Allegations are HORRIFYING! Viva Clips</title>
      <link href="https://rumble.com/v1onhfm-amazon-sued-for-selling-suicide-kits-and-the-allegations-are-horrifying-viv.html" rel="canonical"/>
      <link href="https://connect.facebook.net" rel="dns-prefetch"/>
      <link href="https://www.facebook.com" rel="dns-prefetch"/>
      <link href="https://imasdk.googleapis.com" rel="dns-prefetch"/>
      <link href="https://www.google-analytics.com" rel="preconnect"/>
      <link crossorigin="" href="https://www.googletagservices.com" rel="preconnect"/>
      <link crossorigin="" href="https://www.googletagmanager.com" rel="preconnect"/>
      <link href="https://sp.rmbl.ws" rel="preconnect"/>
      <script>var $$={};var addThemeSwitcher;!function(){var c,r,s="system",i="light",h="dark",l=[h],o=[s,i,h],d=matchMedia("(prefers-color-scheme: dark)"),a=!1,m=!0,n=[],t=[];function u(){try{if(!a&&localStorage)return localStorage.getItem("themePreference")}catch(e){a=!0}}function f(){t.forEach(function(e){e(r)})}function $(){var e,t,a,n;c=c||u()||s,e=c==s?d.matches?h:i:0<=o.indexOf(c)?c:i,r!==(e=e)&&(r=e,l.indexOf(e)<0?(a=document.querySelectorAll("head .js-theme-ss"),Array.prototype.forEach.call(a,function(e){e.disabled=!0})):(t=!1,a="/c/themes/"+e+".css",n="js-theme-ss js-theme-ss--"+e,e=document.querySelectorAll(".js-theme-ss--"+e),Array.prototype.forEach.call(e,function(e){e.disabled=!1,e.dataset.themeMainStylesheet&&(t=!0)}),t||(m?document.write('<link rel=stylesheet data-theme-main-stylesheet="1" class="'+n+'" href="'+a+'" />'):((e=document.createElement("link")).rel="stylesheet",e.href=a,e.className=n,e.dataset.themeMainStylesheet="1",document.head.appendChild(e))))),f()}function y(){$$.each(n,function(){var e=this.getAttribute("data-theme")==c;$$[(e?"add":"remove")+"Class"](this,"main-menu-item--active")})}function p(e,t){(t=e.getAttribute("data-theme"))&&n.indexOf(e)<0&&(n.push(e),$$.addClick(e,function(e){return e.preventDefault(),e=t,a||localStorage.setItem("themePreference",e),c!=e&&(c=e,$(),y()),$$.query(".main-menu-toggle")[0].click(),!1}))}addThemeSwitcher=function(e,t){$$.each($$.query(e),function(){p(this)}),y(),t&&$$.each($$.query(t),function(){this.style.display="block"})},c=u()||s,$(),m=!1,d.addEventListener&&d.addEventListener("change",function(e){$()}),$$&&($$.applyThemePreference=$,$$.registerThemeCallback=function(e){t.push(e)})}();
         !function(s,d){function a(){return(new Date).getTime()/1e3}var t,r,o,n,i,c,l,e="Rumble",b={F:0};(d=s[e]=s[e]||function(){d._.push(arguments)})._=d._||[],b.f={},b.b={};if(!b.k){function f(o,e){return o.opts||(o.opts=[]),b.D(e,function(e,t){var r=o[t];switch(t){case"opts":o[t]=r.concat(e);break;case"ad_sys":o[t]=r?b.M(r,e):e;break;default:o[t]=e}}),o}function p(c,s,l){function u(){var e=c.v.src||c.v.currentSrc;return e=e.match(/blob:/)&&c.hls_js?c.hls_js.url||e:e}function f(){var e=u(),t=s.get();return c.current_video=s,t==e?0:t}var p;s.get=function(){return function(e,t){if(21192597==e.vid.vid)return t;var r,o=b.B(t),t=b.E(t);return e.vid.live||(r=0,e.vid.a&&(r=e.vid.a.u||0),o.u=r,o.b=0<e.bandwidth_track?1:0),t+"?"+b.C(o)}(c,s.url)};s.check=function(){return!f()},s.play=function(){l&&c.hls_js&&!p&&c.hls_js.startLoad(),p=!0},s.set=function(){if(l&&!b.I())return setTimeout(function(){s.set()},100),!1;var e,r,t,o,n,i=f(),d=0,a=0;i&&(p=!1,e=c.v,c.res=s.key,0<S&&(c.last_set_url==u()?(d=!e.paused,a=e.currentTime):0<c.video_time&&(a=c.video_time)),a&&!c.vid.live&&(c.ui.s.autoSeek=a),r=c,a=e,t=i,o=l&&Hls.isSupported(),r.hls_js&&r.hls_media_attached&&((n=r.hls_js).detachMedia(a),n.destroy(),r.hls_js=null),o?(n=r.hls_js=new Hls({capLevelToPlayerSize:!0,autoStartLoad:!1,manifestLoadingMaxRetry:6,levelLoadingMaxRetry:6}),r.j("hlsJsLoaded",n),n.on(Hls.Events.LEVEL_UPDATED,function(e,t){r.live=t.details.live}),n.loadSource(t),n.attachMedia(a),r.hls_media_attached=1):a.src=t,S++,c.last_set_url=i,e.load(),d&&(s.play(),e.play()))}}function g(e){return H.hasOwnProperty(e)?H[e]:e}function h(r,e,o){var n,t;if(!r.style&&r.length)for(t=0;t<r.length;t++)h(r[t],e,o);else b.D(e,function(e,t){n=g(t),o&&""!==r.style[n]||(r.style[n]=g(e))})}function v(){var e=G;G={},y=0,b.D(e,function(e){"function"==typeof e&&e()})}function m(e){var i,o={play:"#fff",scrubber:"#75a642",hover:"#fff",background:"#303030",hoverBackground:"#699c39"},d=this,n=-1,c=(b.D(e,function(e,t){d[t]=e}),d.hasima=1,d.hasInit=0,d.rpcl=(d.id?d.id+"-":"")+"Rumble-cls",d.rpcls="."+d.rpcl,d.bandwidth_track=0,{}),a=(d.addEvent=function(e,t,r){c[r=r||1]||(c[r]={}),c[r][e]||(c[r][e]=[]),c[r][e].indexOf(t)<0&&c[r][e].push(t);r="addEvent";e!=r&&d.j(r,e)},d.removeEvent=function(e,t,r){c[r=r||1][e]&&(r&&!t?c[r][e]=[]:(t=c[r][e].indexOf(t),c[r][e].splice(t,1)))},d.hasEventListener=function(r){return b.D(c,function(e,t){if(e[r]&&0<e[r].length)return!0})},d.j=function(r,o,n){var i,d,a=[];return b.D(c,function(e,t){if(e[r]&&(n&&n==t||!n))for(d=e[r],i=0;i<d.length;i++)"function"==typeof o&&(o=o()),a.push(d[i](o))}),a},d.triggerError=function(e,t){d.j("error",{code:e,message:t})},d.l1=function(e,t,r){},d.getSetting=function(e,t){var r=!1;return d.vid&&d.vid.player&&d.vid.player[e]&&(e=d.vid.player[e],t&&e[t]&&(r=e[t]),t||(r=e)),r=!r&&o[t]?o[t]:r},d.loadVideoStyles=function(e){var t,r,o,n="vid_"+d.vid.id;d.rpcls;d.p.id=n,d.vars.opts.title&&d.vid.title&&(i.innerHTML=d.vid.title,i.href=b.L(d.vid.l,"rumble.com"),b.w(i,{outline:0,display:"block",18:"linear-gradient(rgba(0,0,0,.7),rgba(0,0,0,0))",textShadow:"rgba(0,0,0,0.5) 0px 0px 2px",padding:"9px",fontSize:"18px",whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis",position:"absolute",top:0,left:0,right:0}),b.x(i,{textDecoration:"underline"},{textDecoration:"none"})),d.bp&&(n=d.getSetting("colors","play"),t=d.getSetting("colors","hover"),r=d.getSetting("colors","background"),o=d.getSetting("colors","hoverBackground"),b.x(d.bp,{color:t,background:o,borderColor:o},{color:n,background:r,borderColor:r},d.bp_svg),d.bp.style.opacity=1)},d.trackBandwidth=function(e){var t=d.bandwidth_track;(e=d.server.bw_tracking?e:0)!=t&&(d.bandwidth_track=e,d.current_video&&!d.m&&d.current_video.set())},d.loadVideo=function(e,t){var r,o=(e="object"!=typeof e?{id:e}:e).id;if(b.b[o]&&(d.vars.playlist||(d.vars.playlist=b.b[o]),o=b.b[o][0]),d.hasInit||(d.hasInit=1,b.c(["ui","custom_ui"],function(){for(var e=0;e<b.d.length;e++)b.d[e](d.id)})),!t)return b.e(o,function(){d.loadVideo(e,1)},{ad_count:d.ad_count||null});if(b.f[o].loaded<9){if(d.triggerError("load","Unable to load video "+o),t)throw"Unable to load video "+o;return 2}if(b.f[o].cfg=e,b.f[o].plays=0,(r=b.f[o]).restrict&&!a(r.restrict)&&(d.triggerError("restricted","Video is restricted"),b.f[o].restricted=!0,d.j("restricted",o),b.f[o].ua=0),r.id=o,d.vid=r,d.live=2==d.vid.live,d.video_list=0,d.current_video=0,n<0&&(n=(d.vars.opts.noads||d.server.bw_ourads_check&&d.vars.opts.norumbleads)&&r.a?1:0),d.trackBandwidth(r&&r.track||n?1:0),!r.restricted&&r.ua&&(d.video_list=b.G(d,r.ua),b.H(d),d.loadVideoStyles()),b.g(d),d.j("loadVideo",r),b.h(d,1),r.restricted&&t)throw"Video "+o+" is restricted"},function(e){var t,r,o,n,i=document,d=!1;if(!e||e[0]<=-3)return!0;r=e[0],o=e[1];try{t=parent!==s?i.referrer||parent.location.href:i.location.href}catch(e){}if(!t)return parent===s;if(t=t.match(/^https?\:\/\/([^\/?#]+)(?:[\/?#]|$)/i))for(t=t[1].split(".");2<=t.length&&!d;)n=t.join("."),-1<o.indexOf(n)&&(d=!0),t.shift();return r!=d}),e=d.rpcl,t="metadata";(d.vars.opts.minimal||d.vars.opts.nopreload)&&(t="none"),d.vars.quality&&(d.res=parseInt(d.vars.quality)),e=b.i('<div class="'+e+'" allowfullscreen tabindex="-1" style="outline: none;"><video muted playsinline hidefocus="hidefocus" style="width:100% !important;height:100% !important;display:block" preload="'+t+'"'+(d.vars.opts.cc?' crossorigin="anonymous"':"")+'></video><div style="display:flex;opacity:0" class="bigPlayUI ctp"><a style="display:none" target=_blank rel=noopener></a><div class="bigPlayUIInner ctp" style="display:none"></div></div></div>'),b.w(e,{2:4,9:17,10:17,18:16,color:15,clear:"both",overflow:"visible"}),b.j.c(e,"bplay","block",".bigPlayUIInner"),d.d.appendChild(d.p=e),d.v=e.firstChild,function(e){if(!b.A){var t,r="canPlayType",o='video/mp4; codecs="avc1.42E01E',n=[0,o+'"',0,o+', mp4a.40.2"',1,'video/webm; codecs="vp9, vorbis"',2,"application/vnd.apple.mpegurl"],i=[!1,!1,!1];if(!e||!e[r])return;for(t=0;t<n.length;t+=2)e[r](n[t+1])&&(i[n[t]]=!0);b.J=i[2],b.A=i}}(d.v),d.rsz=[0,0],d.bp=e.childNodes[1],d.bp_svg=d.bp.childNodes[1],d.hasStyle={},i=d.bp.childNodes[0],b.w(d.bp_svg,{fill:"currentColor",9:8,12:"14px 22px",cursor:"pointer",borderRadius:"8px"}),b.w(d.bp,{display:"flex",opacity:0,position:"absolute",top:0,left:0,width:"100%",height:"100%",cursor:"pointer",alignItems:"center",justifyContent:"center",overflow:"hidden"}),d.v.addEventListener("contextmenu",function(e){return e.preventDefault(),!1}),d.loadVideoStyles()}var _,S,y,P="https://rumble.com",e="/embedJS/u3",w=(b.l=a(),s.RumbleErrorHandler||(l=0,s.RumbleErrorHandler=function(e){var t,r=e.message,o=e.filename,n=e.lineno,i=e.colno,d=D(o);o==d||r.match(/^Script error\./)||3<++l||(o=document.location+"",r=[D(o),l,r,d,n,i],e.error&&e.error.stack&&r.push(e.error.stack.split("\n").slice(1,3).join("\n")),d="/l/jserr?err="+encodeURIComponent(JSON.stringify(r)),o==r[0]&&(d=P+d),(t=document.createElement("img")).src=d,t.width=t.height=1,t.onload=t.onerror=function(){t.onload=null,t.onerror=null})},s.addEventListener("error",s.RumbleErrorHandler)),[]),x=(b.E=function(e){return e.split("?")[0]},b.B=function(e){var e=e.split("?"),r={};return e&&e[1]&&(e=e[1],new URLSearchParams(e).forEach(function(e,t){r[t]=e})),r},b.C=function(e){var r="";return b.D(e,function(e,t){r+=(r?"&":"")+encodeURIComponent(t)+"="+encodeURIComponent(e)}),r},b.D=function(e,t){var r,o;for(o in e)if(e.hasOwnProperty(o)&&void 0!==(r=t(e[o],o)))return r},b.K=function(e,t){if("undefined"==typeof localStorageBlocked)try{localStorageBlocked="undefined"==typeof localStorage||!localStorage}catch(e){localStorageBlocked=!0}if(void 0===t){if(!localStorageBlocked)try{t=localStorage.getItem(e)}catch(e){localStorageBlocked=!0}return localStorageBlocked?w[e]:parseInt(t)==t?parseInt(t):t}if(w[e]=t,!localStorageBlocked)try{return localStorage.setItem(e,t)}catch(e){localStorageBlocked=!1}return!1},b.L=function(e,t,r,o){if(e)if(!e.match(/^(http[s]?:)?\/\/([^/]*)\//)||r)return(o?"https:":"")+"//"+t+("/"!=e[0]?"/":"")+e;return e},b.M=function(e,t){return e.filter(function(e){return-1!==t.indexOf(e)})},[2,0,1]),C=["mp4","webm","hls"],H=(b.G=function(r,e){for(var o,t,n={},i=S=0;i<x.length;i++)e[o=C[t=x[i]]]&&(b.A[t]||"hls"==o)&&b.D(e[o],function(e,t){n.hasOwnProperty(t)||(e.key=t,n[t]=e,p(r,n[t],"hls"==o))});return n},b.I=function(){return"undefined"!=typeof Hls||(b.q(["hls"]),!1)},b.H=function(e){var r,o,n,i=480;e.res&&(i=e.res),e.vid.live&&!b.J&&b.I(),b.D(e.video_list,function(e,t){n=parseInt(t),"hls"!=r&&("hls"==t&&b.J||0<n&&n<=i&&(!r||r<n)?r=t:(!o||n<o&&0<n)&&(o=t))}),(r=r||o)&&e.video_list[r].set()},b.r=function(){var d={},a={},c={b:function(e,t,r){if("object"!=typeof e){if(d[e]&&!r)return!1;if(d[e]=t=t||1,a[e])for(;o=a[e].pop();)o(e,t);return!0}for(var o in e)c.b(o,e[o],r)},a:function(e,t,r){var o,n,i;for(r=r||{},o=0;i=e[o];o++)d[i]?r[i]=d[i]:(n&&(t=function(t,r){return function(e){c.a([t],r,e)}}(n[0],n[1])),n=[i,t]);n?(a[n[0]]||(a[n[0]]=[]),a[n[0]].push(function(e,t){r[e]=t,n[1](r)})):t(r)}};return c},n=b.r(),i=document,c={},b.s=function(e,t){var r,o,n=0;c[e]||(c[e]=1,(r=i.createElement("script")).type="text/javascript",r.src=e,t&&(r.addEventListener("load",o=function(e){if(n||t())return n=1;e&&setTimeout(o,50)},!1),o(1)),i.head.appendChild(r))},b.q=function(e,t){for(var r,o=0;o<e.length;o++)if("ima3"==e[o])b.s("https://imasdk.googleapis.com/js/sdkloader/ima3.js",function(){return!("undefined"==typeof google||!google||!google.ima)&&(n.b("ima3"),!0)});else if("custom_ui"!=e[o]){r=e[o];b.s(d.s.rd+"/j/p/"+r+("hls"!=r?".r2":"")+".js?_v=330",t)}},b.c=function(e,t,r){n.a(e,t),r||b.q(e)},d.rl=function(e,t){n.b(e)&&t&&t(b)},[0,1,"position","absolute","relative","fixed","normal","none","auto","width","height","margin","padding","border","display","#FFF","#000","100%","background","opacity"]),k=(b.w=h,b.y=function(e){var r={};return b.D(e,function(e,t){r[g(t)]=g(e)}),r},b.t=function(e,t,r,o,n,i,d,a){o||(o=e,n=t);var c="0",s="0";return a&&a.viewbox_top&&(c=a.viewbox_top),a&&a.viewbox_left&&(s=a.viewbox_left),i=i?" RumbleSVG-"+i:"",d=d||"",0<r.indexOf("stroke")&&(d+="stroke:currentColor;"),[e,t,'<svg style="'+d+'" class="RumbleElm'+i+'" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="'+e+'px" height="'+t+'px" viewBox="'+s+" "+c+" "+o+" "+n+'">'+r+"</svg>"]},b.j=b.r(),b.j.c=function(t,r,o,n){b.j.a([r],function(e){n&&(t=t.querySelectorAll(n)[0]),b.z(t,e[r][2]),o&&("string"==typeof o?t.style.display=o:o.apply(t))})},'<path stroke-width="3" stroke-linejoin="round" d="M19 11L3.2 1.5v19z"/>'),B=(b.j.b({bplay:b.t(25,25,k,22,22,"bplay"),play:b.t(22,22,k,0,0,"play","height:100%;"),loader:b.t(80,10,function(){for(var e,t="<g>",r=0;r<21;r++)t+='<circle cx="'+(10*r+5)+'" cy="5" r="'+(e=(e=r-6)<1||5<e?1:e)+'" />';return t+"</g>"}(),80,10)}),s.requestAnimationFrame?1:0),G={},O=(b.a=function(e,t){if(!G[e]&&"function"==typeof t&&(G[e]=t,!y)){if(y=1,!B)return setTimeout(v,1e3/24);s.requestAnimationFrame(v)}},b.i=function(e){e=b.u("div",0,0,e);return 1<e.childNodes.length?e.childNodes:e.firstChild},b.u=function(e,t,r,o){e=document.createElement(e);return o&&(e.innerHTML=o),t&&(e.className=t),r&&(e.id=r),E(e),e},b.z=function(e,t){e.innerHTML=t,j(e)},b.y({font:"12px sans-serif",fontWeight:6,lineHeight:6,boxSizing:"content-box",webkitBoxSizing:"content-box",19:1,18:7,11:0,12:0,border:7,9:8,10:8,visibility:"visible",textSizeAdjust:8,textDecoration:7})),E=function(e){var t;(t=e.tagName)&&"path"!=(t=t.toLowerCase())&&"video"!=t&&(h(e,O,!0),"svg"==t?h(e,{fill:"currentColor"},!0):(h(e,{color:"inherit"},!0),j(e)))},j=function(e){var t,r;if(t=e.childNodes)for(r=0;r<t.length;r++)E(t[r])};b.x=function(e,t,r,o){var n="__playerHover";(o=o||e)[n]||(e.addEventListener("mouseout",function(){h(o,o[n][0])}),e.addEventListener("mouseover",function(){h(o,o[n][1])})),o[n]=[r,t],h(o,r)};b.d=[];d.s={rd:P,ru:e,ds:[],rp:P+e+"/?request=",server:{"bw_tracking":1,"bw_noads_check":1}};b.k={},d.gdpr=2,b.m=function(e,t,r,o){var n=new XMLHttpRequest;n.onreadystatechange=function(){4==n.readyState&&200==n.status&&t(JSON.parse(n.responseText))},n.open("GET",(o?"":d.s.rp)+e),n.send()},b.e=function(e,t,r){var o,n,i,d=[];for("object"!=typeof e&&(e=[e]),o=0;o<e.length;o++)n=e[o],(!b.f[n]||1<b.f[n].loaded&&b.f[n].loaded+(1==e.length?900:1800)<a())&&(b.f[n]={loaded:0,wait:[]}),0==(i=b.f[n]).loaded&&(d.push(n),i.loaded=1),t&&i.loaded<9&&i.wait.push(t);return 0<d.length?(r=r?"&ext="+encodeURIComponent(JSON.stringify(r)):"",r+="&ad_wt="+(b.K("ad_wt")||0),b.m("video&ver=2&v="+d[0]+r,function(e){var t,r,o=[],n={};for(e.loaded||!e?n[d[0]]=e:n=e,b.D(n,function(e,t){for(;r=b.f[t].wait.pop();)o.indexOf(r)<0&&o.push(r);e&&(b.f[t]=e,b.f[t].loaded=a())}),t=0;t<o.length;t++)o[t]()}),1):(t&&t(),0)},d.resize=function(){b.D(b.k,function(e){b.h(e)})},b.h=function(e,t){var r,o=!e.rsz,n=[e.p.clientWidth,e.p.clientHeight],i=s.innerHeight,d=e.vars;d.resize||(d.resize=function(){try{return s.self!==s.top}catch(e){return!0}}()?"full":"auto");(!o&&(e.rsz[0]!=n[0]||e.rsz[1]!=n[1])||n[1]>i||t)&&(t=d.resize,d.ia&&(t="ia"),e.ui&&e.ui.isFloating&&(t="auto"),r=Math.floor(n[0]/16*9),"ia"==t?screen&&screen.height<r&&(r=screen.height):"full"==t?r=0:"window"==t?r=i:("ctpauto"==t&&e.ui&&e.ui.ctp&&(d.resize="auto"),(i<r||e.ui&&e.ui.getFullScreen())&&(r=0)),"window"!=t&&"ctpauto"!=t&&"auto16:9"!=t&&"full"!=t&&(e.vid&&e.vid.a&&e.vid.a.aden&&e.vid.a.aden[2])&&r<360&&0!=r&&!d.float&&(r=360),e.rsz[0]!=n[0]&&(o=1),n[1]!=r&&(o=1,e.p.style.height=0<r?(n[1]=r)+"px":"100%")),e.rsz&&!o||(e.rsz=n),o&&(b.g(e),e.j("resize"))},b.g=function(e){if(!(!e.vid||e.ui&&e.ui.hasPlayed)){var t,r,o,n=e.vid.i,i=e.vid.t,d=-1,a=e.rsz[0],c=e.rsz[1],s=a/c;if(i)for(t=0;t<i.length;t++)o=s<(o=(r=i[t]).w/r.h)?(c-a/o)*a:(a-c*o)*c,(d<0||o<d)&&(d=o,n=r.i);e.v.poster!=n&&(e.v.poster=n)}},d.$play=function(e,t){var r,o,n=JSON.parse(JSON.stringify(d.s.ds)),i={};if((n=f(n,e)).opts&&(b.D(n.opts,function(e){i[e]=1}),n.opts=i),void 0===n.gdpr?n.gdpr=2:n.gdpr=n.gdpr?1:0,2!=n.gdpr&&(d.gdpr=n.gdpr),b.n=-1==n.analytics||n.opts.minimal?1:0,b.o=n.opts.skip_ga_load?1:0,b.p=n.opts.force_ga_load?1:0,!n.div){if(!_)throw"No div was defined for the player";n.div=_}if(_=o=n.div,!b.k[o]||(r=b.k[o]).d.parentNode||(r=0),n.macros||(n.macros={}),!r){if(!(r=document.getElementById(o))){if(2<t)throw o+" div not found";s.addEventListener("DOMContentLoaded",function(){d.$play(e,3)})}b.k[o]||b.F++,b.k[o]=r=new m({d:r,vid:0,id:o,vars:n,server:d.s.server})}r.loadVideo(n.video),b.h(r)};d.rl("custom_ui");d.$playSettings=function(e){d.s.ds=f(d.s.ds,e)},s.addEventListener("resize",function(){b.a("resize",d.resize)}),s.addEventListener("orientationchange",function(){setTimeout(function(){d.resize()},500)});var z,L,I,R=s.Rumble;for(R._=z=R._||[],z.push=function(e){var t=z.slice.call(e),r=R["$"+t.shift()];"function"==typeof r?r.apply(R,t):t.push.call(z,e)},L=-1,I=z.length;++L<I;)z.push(z.shift())}function D(e){if(!e)return e;var t=e.match(new RegExp("http[s]?://[^/]*rumble.com(/.*)$"));return t?t[1]:e}}(window);
         
      </script><script type="application/ld+json">[{"@context":"http://schema.org","@type":"VideoObject","name":"Amazon Sued for Selling 'Suicide Kits' and the Allegations are HORRIFYING! Viva Clips","playerType":"HTML5","description":"The allegations of this lawsuit will break your heart and hurt your soul.","thumbnailUrl":"https://sp.rmbl.ws/s8/6/c/q/N/e/cqNeg.4Wpjb.jpg","uploadDate":"2022-10-19T02:17:53+00:00","duration":"PT00H07M35S","embedUrl":"https://rumble.com/embed/v1m1bmu/","url":"https://rumble.com/v1onhfm-amazon-sued-for-selling-suicide-kits-and-the-allegations-are-horrifying-viv.html","interactionStatistic":{"@type":"InteractionCounter","interactionType":{"@type":"http://schema.org/WatchAction"},"userInteractionCount":137},"width":1920,"height":1080,"videoQuality":"Full HD"},{"@context":"http://schema.org","@type":"WebSite","url":"https://rumble.com/","potentialAction":{"@type":"SearchAction","target":"https://rumble.com/search/video?q={search}","query-input":"required name=search"}},{"@context":"http://schema.org","@type":"Organization","name":"Rumble","url":"https://rumble.com/","logo":"https://rumble.com/i/rumble_logo_back.png","sameAs":["https://www.facebook.com/rumblevideo/","https://twitter.com/rumblevideo"]}]</script>
      <meta content="The allegations of this lawsuit will break your heart and hurt your soul." name="description"/>
      <meta content="Rumble" property="og:site_name"/>
      <meta content="video.other" property="og:type"/>
      <meta content='Amazon Sued for Selling "Suicide Kits" and the Allegations are HORRIFYING! Viva Clips' property="og:title"/>
      <meta content="https://rumble.com/v1onhfm-amazon-sued-for-selling-suicide-kits-and-the-allegations-are-horrifying-viv.html" property="og:url"/>
      <meta content="The allegations of this lawsuit will break your heart and hurt your soul." property="og:description"/>
      <meta content="https://sp.rmbl.ws/s8/6/c/q/N/e/cqNeg.4Wpjb.jpg" property="og:image"/>
      <meta content="summary_large_image" name="twitter:card"/>
      <meta content="https://sp.rmbl.ws/s8/6/c/q/N/e/cqNeg.4Wpjb.jpg" name="twitter:image"/>
      <meta content='Amazon Sued for Selling "Suicide Kits" and the Allegations are HORRIFYING! Viva Clips' name="twitter:title"/>
      <meta content="The allegations of this lawsuit will break your heart and hurt your soul." name="twitter:description"/>
      <meta content="155223717937973" property="fb:app_id"/>
      <meta content="@rumblevideo" name="twitter:site"/>
      <meta content="app-id=1518427877" name="apple-itunes-app"/>
      <link href="/i/favicon-v4.png" rel="shortcut icon"/>
      <link href="/apple-touch-icon.png" rel="apple-touch-icon"/>
   </head>
   <body></body>
</html>
'''
RSP2 = '''
<!DOCTYPE html>
<html lang="en">
   <head>
      <title>Amazon Sued for Selling &quot;Suicide Kits&quot; and the Allegations are HORRIFYING! Viva Clips - Rumble</title>
      <link rel="canonical" href="https://rumble.com/v1onhfm-amazon-sued-for-selling-suicide-kits-and-the-allegations-are-horrifying-viv.html">
      <link rel="alternate" href="https://rumble.com/api/Media/oembed.json?url=https%3A%2F%2Frumble.com%2Fembed%2Fv1m1bmu%2F" type="application/json+oembed" title="Amazon Sued for Selling &quot;Suicide Kits&quot; and the Allegations are HORRIFYING! Viva Clips">
      <link rel="alternate" href="https://rumble.com/api/Media/oembed.xml?url=https%3A%2F%2Frumble.com%2Fembed%2Fv1m1bmu%2F" type="text/xml+oembed" title="Amazon Sued for Selling &quot;Suicide Kits&quot; and the Allegations are HORRIFYING! Viva Clips">
      <meta name="viewport" content="width=device-width,initial-scale=1" />
      <link rel="dns-prefetch" href="https://sp.rmbl.ws">
      <link rel="dns-prefetch" href="//imasdk.googleapis.com/">
   </head>
   <body style="margin:0;padding:0">
      <div id="player" style="width:100%;height:100%;overflow:hidden;position:absolute"></div>
      <script type="text/javascript">!function(s,d){function a(){return(new Date).getTime()/1e3}var t,r,o,n,i,c,l,e="Rumble",b={F:0};(d=s[e]=s[e]||function(){d._.push(arguments)})._=d._||[],b.f={},b.b={};b.f["v1m1bmu"]={"fps":23.98,"w":1920,"h":1080,"u":{"mp4":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/c\/q\/N\/e\/cqNeg.caa.mp4","meta":{"bitrate":813,"size":46340113,"w":854,"h":480}},"webm":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/c\/q\/N\/e\/cqNeg.daa.webm","meta":{"bitrate":808,"size":46045321,"w":854,"h":480}}},"ua":{"mp4":{"360":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/c\/q\/N\/e\/cqNeg.baa.mp4","meta":{"bitrate":633,"size":36076638,"w":640,"h":360}},"480":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/c\/q\/N\/e\/cqNeg.caa.mp4","meta":{"bitrate":813,"size":46340113,"w":854,"h":480}},"720":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/c\/q\/N\/e\/cqNeg.gaa.mp4","meta":{"bitrate":1965,"size":111946468,"w":1280,"h":720}},"1080":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/c\/q\/N\/e\/cqNeg.haa.mp4","meta":{"bitrate":2698,"size":153655690,"w":1920,"h":1080}}},"webm":{"480":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/c\/q\/N\/e\/cqNeg.daa.webm","meta":{"bitrate":808,"size":46045321,"w":854,"h":480}}}},"i":"https:\/\/sp.rmbl.ws\/s8\/6\/c\/q\/N\/e\/cqNeg.OvCc.jpg","evt":{"v":"\/l\/view...1m1bmu.9xskxr","e":"\/l\/pte...1m1bmu.1e976ro","wt":0,"t":"\/l\/timeline...1m1bmu.cn.158mwt1"},"cc":[],"l":"\/v1onhfm-amazon-sued-for-selling-suicide-kits-and-the-allegations-are-horrifying-viv.html","r":1,"title":"Amazon Sued for Selling &quot;Suicide Kits&quot; and the Allegations are HORRIFYING! Viva Clips","author":{"name":"vivafrei","url":"https:\/\/rumble.com\/user\/vivafrei"},"player":false,"duration":455,"pubDate":"2022-10-19T02:17:53+00:00","loaded":1,"vid":97479462,"timeline":[0,0],"own":false,"mod":[],"restrict":[-3,0],"autoplay":0,"track":0,"live":0,"live_placeholder":false,"livestream_has_dvr":null,"a":{"timeout":-1,"u":"4","aden":[1,0,0],"ov":false,"ads":[],"a":".4.71v3.1m1bmu..qm.wl8gah","ae":".4.71v3.1m1bmu..qm.5hvpfw","ap":[false,0],"loop":[]},loaded:a()};if(!b.k){function f(o,e){return o.opts||(o.opts=[]),b.D(e,function(e,t){var r=o[t];switch(t){case"opts":o[t]=r.concat(e);break;case"ad_sys":o[t]=r?b.M(r,e):e;break;default:o[t]=e}}),o}function p(c,s,l){function u(){var e=c.v.src||c.v.currentSrc;return e=e.match(/blob:/)&&c.hls_js?c.hls_js.url||e:e}function f(){var e=u(),t=s.get();return c.current_video=s,t==e?0:t}var p;s.get=function(){return function(e,t){if(21192597==e.vid.vid)return t;var r,o=b.B(t),t=b.E(t);return e.vid.live||(r=0,e.vid.a&&(r=e.vid.a.u||0),o.u=r,o.b=0<e.bandwidth_track?1:0),t+"?"+b.C(o)}(c,s.url)};s.check=function(){return!f()},s.play=function(){l&&c.hls_js&&!p&&c.hls_js.startLoad(),p=!0},s.set=function(){if(l&&!b.I())return setTimeout(function(){s.set()},100),!1;var e,r,t,o,n,i=f(),d=0,a=0;i&&(p=!1,e=c.v,c.res=s.key,0<S&&(c.last_set_url==u()?(d=!e.paused,a=e.currentTime):0<c.video_time&&(a=c.video_time)),a&&!c.vid.live&&(c.ui.s.autoSeek=a),r=c,a=e,t=i,o=l&&Hls.isSupported(),r.hls_js&&r.hls_media_attached&&((n=r.hls_js).detachMedia(a),n.destroy(),r.hls_js=null),o?(n=r.hls_js=new Hls({capLevelToPlayerSize:!0,autoStartLoad:!1,manifestLoadingMaxRetry:6,levelLoadingMaxRetry:6}),r.j("hlsJsLoaded",n),n.on(Hls.Events.LEVEL_UPDATED,function(e,t){r.live=t.details.live}),n.loadSource(t),n.attachMedia(a),r.hls_media_attached=1):a.src=t,S++,c.last_set_url=i,e.load(),d&&(s.play(),e.play()))}}function g(e){return H.hasOwnProperty(e)?H[e]:e}function h(r,e,o){var n,t;if(!r.style&&r.length)for(t=0;t<r.length;t++)h(r[t],e,o);else b.D(e,function(e,t){n=g(t),o&&""!==r.style[n]||(r.style[n]=g(e))})}function v(){var e=G;G={},y=0,b.D(e,function(e){"function"==typeof e&&e()})}function m(e){var i,o={play:"#fff",scrubber:"#75a642",hover:"#fff",background:"#303030",hoverBackground:"#699c39"},d=this,n=-1,c=(b.D(e,function(e,t){d[t]=e}),d.hasima=1,d.hasInit=0,d.rpcl=(d.id?d.id+"-":"")+"Rumble-cls",d.rpcls="."+d.rpcl,d.bandwidth_track=0,{}),a=(d.addEvent=function(e,t,r){c[r=r||1]||(c[r]={}),c[r][e]||(c[r][e]=[]),c[r][e].indexOf(t)<0&&c[r][e].push(t);r="addEvent";e!=r&&d.j(r,e)},d.removeEvent=function(e,t,r){c[r=r||1][e]&&(r&&!t?c[r][e]=[]:(t=c[r][e].indexOf(t),c[r][e].splice(t,1)))},d.hasEventListener=function(r){return b.D(c,function(e,t){if(e[r]&&0<e[r].length)return!0})},d.j=function(r,o,n){var i,d,a=[];return b.D(c,function(e,t){if(e[r]&&(n&&n==t||!n))for(d=e[r],i=0;i<d.length;i++)"function"==typeof o&&(o=o()),a.push(d[i](o))}),a},d.triggerError=function(e,t){d.j("error",{code:e,message:t})},d.l1=function(e,t,r){},d.getSetting=function(e,t){var r=!1;return d.vid&&d.vid.player&&d.vid.player[e]&&(e=d.vid.player[e],t&&e[t]&&(r=e[t]),t||(r=e)),r=!r&&o[t]?o[t]:r},d.loadVideoStyles=function(e){var t,r,o,n="vid_"+d.vid.id;d.rpcls;d.p.id=n,d.vars.opts.title&&d.vid.title&&(i.innerHTML=d.vid.title,i.href=b.L(d.vid.l,"rumble.com"),b.w(i,{outline:0,display:"block",18:"linear-gradient(rgba(0,0,0,.7),rgba(0,0,0,0))",textShadow:"rgba(0,0,0,0.5) 0px 0px 2px",padding:"9px",fontSize:"18px",whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis",position:"absolute",top:0,left:0,right:0}),b.x(i,{textDecoration:"underline"},{textDecoration:"none"})),d.bp&&(n=d.getSetting("colors","play"),t=d.getSetting("colors","hover"),r=d.getSetting("colors","background"),o=d.getSetting("colors","hoverBackground"),b.x(d.bp,{color:t,background:o,borderColor:o},{color:n,background:r,borderColor:r},d.bp_svg),d.bp.style.opacity=1)},d.trackBandwidth=function(e){var t=d.bandwidth_track;(e=d.server.bw_tracking?e:0)!=t&&(d.bandwidth_track=e,d.current_video&&!d.m&&d.current_video.set())},d.loadVideo=function(e,t){var r,o=(e="object"!=typeof e?{id:e}:e).id;if(b.b[o]&&(d.vars.playlist||(d.vars.playlist=b.b[o]),o=b.b[o][0]),d.hasInit||(d.hasInit=1,b.c(["ui","custom_ui"],function(){for(var e=0;e<b.d.length;e++)b.d[e](d.id)})),!t)return b.e(o,function(){d.loadVideo(e,1)},{ad_count:d.ad_count||null});if(b.f[o].loaded<9){if(d.triggerError("load","Unable to load video "+o),t)throw"Unable to load video "+o;return 2}if(b.f[o].cfg=e,b.f[o].plays=0,(r=b.f[o]).restrict&&!a(r.restrict)&&(d.triggerError("restricted","Video is restricted"),b.f[o].restricted=!0,d.j("restricted",o),b.f[o].ua=0),r.id=o,d.vid=r,d.live=2==d.vid.live,d.video_list=0,d.current_video=0,n<0&&(n=(d.vars.opts.noads||d.server.bw_ourads_check&&d.vars.opts.norumbleads)&&r.a?1:0),d.trackBandwidth(r&&r.track||n?1:0),!r.restricted&&r.ua&&(d.video_list=b.G(d,r.ua),b.H(d),d.loadVideoStyles()),b.g(d),d.j("loadVideo",r),b.h(d,1),r.restricted&&t)throw"Video "+o+" is restricted"},function(e){var t,r,o,n,i=document,d=!1;if(!e||e[0]<=-3)return!0;r=e[0],o=e[1];try{t=parent!==s?i.referrer||parent.location.href:i.location.href}catch(e){}if(!t)return parent===s;if(t=t.match(/^https?\:\/\/([^\/?#]+)(?:[\/?#]|$)/i))for(t=t[1].split(".");2<=t.length&&!d;)n=t.join("."),-1<o.indexOf(n)&&(d=!0),t.shift();return r!=d}),e=d.rpcl,t="metadata";(d.vars.opts.minimal||d.vars.opts.nopreload)&&(t="none"),d.vars.quality&&(d.res=parseInt(d.vars.quality)),e=b.i('<div class="'+e+'" allowfullscreen tabindex="-1" style="outline: none;"><video muted playsinline hidefocus="hidefocus" style="width:100% !important;height:100% !important;display:block" preload="'+t+'"'+(d.vars.opts.cc?' crossorigin="anonymous"':"")+'></video><div style="display:flex;opacity:0" class="bigPlayUI ctp"><a style="display:none" target=_blank rel=noopener></a><div class="bigPlayUIInner ctp" style="display:none"></div></div></div>'),b.w(e,{2:4,9:17,10:17,18:16,color:15,clear:"both",overflow:"visible"}),b.j.c(e,"bplay","block",".bigPlayUIInner"),d.d.appendChild(d.p=e),d.v=e.firstChild,function(e){if(!b.A){var t,r="canPlayType",o='video/mp4; codecs="avc1.42E01E',n=[0,o+'"',0,o+', mp4a.40.2"',1,'video/webm; codecs="vp9, vorbis"',2,"application/vnd.apple.mpegurl"],i=[!1,!1,!1];if(!e||!e[r])return;for(t=0;t<n.length;t+=2)e[r](n[t+1])&&(i[n[t]]=!0);b.J=i[2],b.A=i}}(d.v),d.rsz=[0,0],d.bp=e.childNodes[1],d.bp_svg=d.bp.childNodes[1],d.hasStyle={},i=d.bp.childNodes[0],b.w(d.bp_svg,{fill:"currentColor",9:8,12:"14px 22px",cursor:"pointer",borderRadius:"8px"}),b.w(d.bp,{display:"flex",opacity:0,position:"absolute",top:0,left:0,width:"100%",height:"100%",cursor:"pointer",alignItems:"center",justifyContent:"center",overflow:"hidden"}),d.v.addEventListener("contextmenu",function(e){return e.preventDefault(),!1}),d.loadVideoStyles()}var _,S,y,P="https://rumble.com",e="/embedJS/u4",w=(b.l=a(),s.RumbleErrorHandler||(l=0,s.RumbleErrorHandler=function(e){var t,r=e.message,o=e.filename,n=e.lineno,i=e.colno,d=D(o);o==d||r.match(/^Script error\./)||3<++l||(o=document.location+"",r=[D(o),l,r,d,n,i],e.error&&e.error.stack&&r.push(e.error.stack.split("\n").slice(1,3).join("\n")),d="/l/jserr?err="+encodeURIComponent(JSON.stringify(r)),o==r[0]&&(d=P+d),(t=document.createElement("img")).src=d,t.width=t.height=1,t.onload=t.onerror=function(){t.onload=null,t.onerror=null})},s.addEventListener("error",s.RumbleErrorHandler)),[]),x=(b.E=function(e){return e.split("?")[0]},b.B=function(e){var e=e.split("?"),r={};return e&&e[1]&&(e=e[1],new URLSearchParams(e).forEach(function(e,t){r[t]=e})),r},b.C=function(e){var r="";return b.D(e,function(e,t){r+=(r?"&":"")+encodeURIComponent(t)+"="+encodeURIComponent(e)}),r},b.D=function(e,t){var r,o;for(o in e)if(e.hasOwnProperty(o)&&void 0!==(r=t(e[o],o)))return r},b.K=function(e,t){if("undefined"==typeof localStorageBlocked)try{localStorageBlocked="undefined"==typeof localStorage||!localStorage}catch(e){localStorageBlocked=!0}if(void 0===t){if(!localStorageBlocked)try{t=localStorage.getItem(e)}catch(e){localStorageBlocked=!0}return localStorageBlocked?w[e]:parseInt(t)==t?parseInt(t):t}if(w[e]=t,!localStorageBlocked)try{return localStorage.setItem(e,t)}catch(e){localStorageBlocked=!1}return!1},b.L=function(e,t,r,o){if(e)if(!e.match(/^(http[s]?:)?\/\/([^/]*)\//)||r)return(o?"https:":"")+"//"+t+("/"!=e[0]?"/":"")+e;return e},b.M=function(e,t){return e.filter(function(e){return-1!==t.indexOf(e)})},[2,0,1]),C=["mp4","webm","hls"],H=(b.G=function(r,e){for(var o,t,n={},i=S=0;i<x.length;i++)e[o=C[t=x[i]]]&&(b.A[t]||"hls"==o)&&b.D(e[o],function(e,t){n.hasOwnProperty(t)||(e.key=t,n[t]=e,p(r,n[t],"hls"==o))});return n},b.I=function(){return"undefined"!=typeof Hls||(b.q(["hls"]),!1)},b.H=function(e){var r,o,n,i=480;e.res&&(i=e.res),e.vid.live&&!b.J&&b.I(),b.D(e.video_list,function(e,t){n=parseInt(t),"hls"!=r&&("hls"==t&&b.J||0<n&&n<=i&&(!r||r<n)?r=t:(!o||n<o&&0<n)&&(o=t))}),(r=r||o)&&e.video_list[r].set()},b.r=function(){var d={},a={},c={b:function(e,t,r){if("object"!=typeof e){if(d[e]&&!r)return!1;if(d[e]=t=t||1,a[e])for(;o=a[e].pop();)o(e,t);return!0}for(var o in e)c.b(o,e[o],r)},a:function(e,t,r){var o,n,i;for(r=r||{},o=0;i=e[o];o++)d[i]?r[i]=d[i]:(n&&(t=function(t,r){return function(e){c.a([t],r,e)}}(n[0],n[1])),n=[i,t]);n?(a[n[0]]||(a[n[0]]=[]),a[n[0]].push(function(e,t){r[e]=t,n[1](r)})):t(r)}};return c},n=b.r(),i=document,c={},b.s=function(e,t){var r,o,n=0;c[e]||(c[e]=1,(r=i.createElement("script")).type="text/javascript",r.src=e,t&&(r.addEventListener("load",o=function(e){if(n||t())return n=1;e&&setTimeout(o,50)},!1),o(1)),i.head.appendChild(r))},b.q=function(e,t){for(var r,o=0;o<e.length;o++)if("ima3"==e[o])b.s("https://imasdk.googleapis.com/js/sdkloader/ima3.js",function(){return!("undefined"==typeof google||!google||!google.ima)&&(n.b("ima3"),!0)});else if("custom_ui"!=e[o]){r=e[o];b.s(d.s.rd+"/j/p/"+r+("hls"!=r?".r2":"")+".js?_v=330",t)}},b.c=function(e,t,r){n.a(e,t),r||b.q(e)},d.rl=function(e,t){n.b(e)&&t&&t(b)},[0,1,"position","absolute","relative","fixed","normal","none","auto","width","height","margin","padding","border","display","#FFF","#000","100%","background","opacity"]),k=(b.w=h,b.y=function(e){var r={};return b.D(e,function(e,t){r[g(t)]=g(e)}),r},b.t=function(e,t,r,o,n,i,d,a){o||(o=e,n=t);var c="0",s="0";return a&&a.viewbox_top&&(c=a.viewbox_top),a&&a.viewbox_left&&(s=a.viewbox_left),i=i?" RumbleSVG-"+i:"",d=d||"",0<r.indexOf("stroke")&&(d+="stroke:currentColor;"),[e,t,'<svg style="'+d+'" class="RumbleElm'+i+'" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="'+e+'px" height="'+t+'px" viewBox="'+s+" "+c+" "+o+" "+n+'">'+r+"</svg>"]},b.j=b.r(),b.j.c=function(t,r,o,n){b.j.a([r],function(e){n&&(t=t.querySelectorAll(n)[0]),b.z(t,e[r][2]),o&&("string"==typeof o?t.style.display=o:o.apply(t))})},'<path stroke-width="3" stroke-linejoin="round" d="M19 11L3.2 1.5v19z"/>'),B=(b.j.b({bplay:b.t(25,25,k,22,22,"bplay"),play:b.t(22,22,k,0,0,"play","height:100%;"),loader:b.t(80,10,function(){for(var e,t="<g>",r=0;r<21;r++)t+='<circle cx="'+(10*r+5)+'" cy="5" r="'+(e=(e=r-6)<1||5<e?1:e)+'" />';return t+"</g>"}(),80,10)}),s.requestAnimationFrame?1:0),G={},O=(b.a=function(e,t){if(!G[e]&&"function"==typeof t&&(G[e]=t,!y)){if(y=1,!B)return setTimeout(v,1e3/24);s.requestAnimationFrame(v)}},b.i=function(e){e=b.u("div",0,0,e);return 1<e.childNodes.length?e.childNodes:e.firstChild},b.u=function(e,t,r,o){e=document.createElement(e);return o&&(e.innerHTML=o),t&&(e.className=t),r&&(e.id=r),E(e),e},b.z=function(e,t){e.innerHTML=t,j(e)},b.y({font:"12px sans-serif",fontWeight:6,lineHeight:6,boxSizing:"content-box",webkitBoxSizing:"content-box",19:1,18:7,11:0,12:0,border:7,9:8,10:8,visibility:"visible",textSizeAdjust:8,textDecoration:7})),E=function(e){var t;(t=e.tagName)&&"path"!=(t=t.toLowerCase())&&"video"!=t&&(h(e,O,!0),"svg"==t?h(e,{fill:"currentColor"},!0):(h(e,{color:"inherit"},!0),j(e)))},j=function(e){var t,r;if(t=e.childNodes)for(r=0;r<t.length;r++)E(t[r])};b.x=function(e,t,r,o){var n="__playerHover";(o=o||e)[n]||(e.addEventListener("mouseout",function(){h(o,o[n][0])}),e.addEventListener("mouseover",function(){h(o,o[n][1])})),o[n]=[r,t],h(o,r)};b.d=[];d.s={rd:P,ru:e,ds:f({opts:["title"]},[]),rp:P+e+"/?request=",server:{"bw_tracking":1,"bw_noads_check":1}};b.k={},d.gdpr=2,b.m=function(e,t,r,o){var n=new XMLHttpRequest;n.onreadystatechange=function(){4==n.readyState&&200==n.status&&t(JSON.parse(n.responseText))},n.open("GET",(o?"":d.s.rp)+e),n.send()},b.e=function(e,t,r){var o,n,i,d=[];for("object"!=typeof e&&(e=[e]),o=0;o<e.length;o++)n=e[o],(!b.f[n]||1<b.f[n].loaded&&b.f[n].loaded+(1==e.length?900:1800)<a())&&(b.f[n]={loaded:0,wait:[]}),0==(i=b.f[n]).loaded&&(d.push(n),i.loaded=1),t&&i.loaded<9&&i.wait.push(t);return 0<d.length?(r=r?"&ext="+encodeURIComponent(JSON.stringify(r)):"",r+="&ad_wt="+(b.K("ad_wt")||0),b.m("video&ver=2&v="+d[0]+r,function(e){var t,r,o=[],n={};for(e.loaded||!e?n[d[0]]=e:n=e,b.D(n,function(e,t){for(;r=b.f[t].wait.pop();)o.indexOf(r)<0&&o.push(r);e&&(b.f[t]=e,b.f[t].loaded=a())}),t=0;t<o.length;t++)o[t]()}),1):(t&&t(),0)},d.resize=function(){b.D(b.k,function(e){b.h(e)})},b.h=function(e,t){var r,o=!e.rsz,n=[e.p.clientWidth,e.p.clientHeight],i=s.innerHeight,d=e.vars;d.resize||(d.resize=function(){try{return s.self!==s.top}catch(e){return!0}}()?"full":"auto");(!o&&(e.rsz[0]!=n[0]||e.rsz[1]!=n[1])||n[1]>i||t)&&(t=d.resize,d.ia&&(t="ia"),e.ui&&e.ui.isFloating&&(t="auto"),r=Math.floor(n[0]/16*9),"ia"==t?screen&&screen.height<r&&(r=screen.height):"full"==t?r=0:"window"==t?r=i:("ctpauto"==t&&e.ui&&e.ui.ctp&&(d.resize="auto"),(i<r||e.ui&&e.ui.getFullScreen())&&(r=0)),"window"!=t&&"ctpauto"!=t&&"auto16:9"!=t&&"full"!=t&&(e.vid&&e.vid.a&&e.vid.a.aden&&e.vid.a.aden[2])&&r<360&&0!=r&&!d.float&&(r=360),e.rsz[0]!=n[0]&&(o=1),n[1]!=r&&(o=1,e.p.style.height=0<r?(n[1]=r)+"px":"100%")),e.rsz&&!o||(e.rsz=n),o&&(b.g(e),e.j("resize"))},b.g=function(e){if(!(!e.vid||e.ui&&e.ui.hasPlayed)){var t,r,o,n=e.vid.i,i=e.vid.t,d=-1,a=e.rsz[0],c=e.rsz[1],s=a/c;if(i)for(t=0;t<i.length;t++)o=s<(o=(r=i[t]).w/r.h)?(c-a/o)*a:(a-c*o)*c,(d<0||o<d)&&(d=o,n=r.i);e.v.poster!=n&&(e.v.poster=n)}},d.$play=function(e,t){var r,o,n=JSON.parse(JSON.stringify(d.s.ds)),i={};if((n=f(n,e)).opts&&(b.D(n.opts,function(e){i[e]=1}),n.opts=i),void 0===n.gdpr?n.gdpr=2:n.gdpr=n.gdpr?1:0,2!=n.gdpr&&(d.gdpr=n.gdpr),b.n=-1==n.analytics||n.opts.minimal?1:0,b.o=n.opts.skip_ga_load?1:0,b.p=n.opts.force_ga_load?1:0,!n.div){if(!_)throw"No div was defined for the player";n.div=_}if(_=o=n.div,!b.k[o]||(r=b.k[o]).d.parentNode||(r=0),n.macros||(n.macros={}),!r){if(!(r=document.getElementById(o))){if(2<t)throw o+" div not found";s.addEventListener("DOMContentLoaded",function(){d.$play(e,3)})}b.k[o]||b.F++,b.k[o]=r=new m({d:r,vid:0,id:o,vars:n,server:d.s.server})}r.loadVideo(n.video),b.h(r)};d.rl("custom_ui");d.$playSettings=function(e){d.s.ds=f(d.s.ds,e)},s.addEventListener("resize",function(){b.a("resize",d.resize)}),s.addEventListener("orientationchange",function(){setTimeout(function(){d.resize()},500)});var z,L,I,R=s.Rumble;for(R._=z=R._||[],z.push=function(e){var t=z.slice.call(e),r=R["$"+t.shift()];"function"==typeof r?r.apply(R,t):t.push.call(z,e)},L=-1,I=z.length;++L<I;)z.push(z.shift())}function D(e){if(!e)return e;var t=e.match(new RegExp("http[s]?://[^/]*rumble.com(/.*)$"));return t?t[1]:e}}(window);
         Rumble("play", {"video":{"id":"v1m1bmu"},"div":"player","resize":"full","opts":["force_ga_load"]});
      </script>
   </body>
</html>
'''

class RumbleTestCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.server = ResponsesServer(
            responses_kwargs={'registry': OrderedRegistry})
        self.server.start()
        self.server.get(
            self.server.url('/user/vivafrei/'),
            headers={'Content-Type': 'text/html'},
            body=RSP0)
        self.server.get(
            self.server.url('/v1onhfm-amazon-sued-for-selling-suicide-kits-and-the-allegations-are-horrifying-viv.html'),
            headers={'Content-Type': 'text/html'},
            body=RSP1.replace(
                'https://rumble.com/embed/v1m1bmu/',
                self.server.url('/embed/v1m1bmu/')
            ))
        self.server.get(
            self.server.url('/embed/v1m1bmu/'),
            headers={'Content-Type': 'text/html'},
            body=RSP2)
        self.crawler = RumbleCrawler()

    def tearDown(self):
        self.server.stop()

    async def test_login(self):
        await self.crawler.login()

    async def test_crawl(self):
        channel, videos = await self.crawler.crawl(
            self.server.url('/user/vivafrei/'))
        videos = [v async for v, s in videos]
        self.assertEqual('vivafrei', channel.name)
        self.assertEqual(1, len(videos))
        self.assertEqual(4, len(videos[0].sources))
