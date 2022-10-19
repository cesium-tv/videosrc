from unittest import IsolatedAsyncioTestCase

from responses.registries import OrderedRegistry
from responses_server import ResponsesServer

from vidsrc.crawl.rumble import RumbleCrawler


RSP0 = '''
<!DOCTYPE html>

<html lang="en">
<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb#"><meta content="width=device-width,initial-scale=1" name="viewport"/><title>vivafrei</title><link href="https://rumble.com/user/vivafrei" rel="canonical"/><link href="https://rumble.com/user/vivafrei?page=2" rel="next"/><style>html{
	background: #f3f3f7;
	color:#333;
	font: normal 14px/1.15 sans-serif;
	-webkit-text-size-adjust: 100%;
}
body, a, button, input, textarea, select, option, h1, h2, h3, address, ul, ol { margin: 0; padding: 0; color: inherit; font-family: inherit; font-weight: inherit; font-size: inherit; text-decoration: inherit; font-style: inherit; line-height: inherit; }
button, [type=button], [type=submit] { -webkit-appearance: button; cursor: pointer; background-color: transparent; border-style: none; }
ul, ol { list-style: none; }
label { cursor: pointer; }
a:hover{ text-decoration: underline; }
button{
	white-space:nowrap;
}
.h1 {
	font-size:2rem;
	line-height: 1;
	font-weight:normal;
	margin:0 0 1rem;
 	word-wrap: break-word;
	overflow-wrap: break-word;
}
small {
	font-size: 0.9rem;
	color: #666;
}
.verification-badge-icon {
	color: #fff;
	fill: #4C8800;
}
.themable-locals-icon {
	color: #421C52;
}

/* modifiers */
.content{
	background:#fff;
	padding:1rem;
}

.container{
	box-shadow:0 0 3px rgba(0,0,0,0.1);
	border-top:1px solid #e4e4e4;
	border-bottom:1px solid #e4e4e4;
	background:#fff;
}

.flex {
	display: flex;
}

.clear{
	clear:both;
}
.round-button{
	display: inline-flex;
	padding: 0.5rem 0.7rem;
	border-radius: 10rem;
	box-shadow: 0 1px 2px rgba(0,0,0,0.2);
	font-weight: 600;
	margin-left: 0.35rem;
	margin-right: 0.35rem;
	font-size: 1rem;
	text-transform: uppercase;
	opacity: 1;
	align-items: center;
}
.round-button:hover{
	text-decoration:none;
	opacity:0.85;
}
.round-button:disabled,
.round-button:disabled:hover {
	background: #999;
	cursor: default;
}
.bg-green{
	background: #4C8800;
	color:#fff;
}
.bg-green:hover,
.bg-green:focus-visible {
	background: #407200;
	opacity: 1;
}
.bg-blue{
	background: #37c;
	color:#fff;
}
.bg-blue:hover,
.bg-blue:focus-visible {
	background: #2A62A7;
	opacity: 1;
}
.bg-red{
	background:#b70000;
	color:#fff;
}
.bg-grey{
	background:#999;
	color:#fff;
}
.bg-white{
	background:#fff;
	color:#000;
}
.select-arrow-bg{
	-moz-appearance: none;
    -webkit-appearance: none;
    appearance: none;
	background-image:  url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 34 21'%3E%3Cpath d='M16.984 12.888L4.682 1.022.984 4.589l16 15.433 16-15.433-3.698-3.567z' /%3E%3C/svg%3E");
	background-repeat: no-repeat;
	background-position:  92% center;
	background-size: 8px;
}

/* layout columns */
.thirds{
	margin-left:-1rem;
	margin-right:-1rem;
}
.two-thirds, .one-thirds{
	width:100%;
	padding: 1.5rem 0;
	box-sizing:border-box;
}
.video-processing-error {
	background: #900;
	color: white;
	padding: 10px 20px
}main{
	padding:2rem 0;
}
.constrained{
	box-sizing:border-box;
	padding-left:1rem;
	padding-right:1rem;
}#is-sidebar-open { display: none; }
.video-listing-entry:not(:first-child) { margin: 10px 0; }.subscribe-button-count { margin-left: 0.5rem; font-weight:normal; opacity: 0.85; }button.locals-button {
	background: #e73348;
	color: #fff;
	padding-top: 0.25rem;
	padding-bottom: 0.25rem;
}

.locals-button:hover {
	background: #c6172c;
	opacity: 1;
}

button.locals-button svg {
	width: 20px;
	height: 20px;
	margin-left: 0.6rem;
}.listing-header--content { line-height: 92px; position: relative; margin-top: -2rem; }
.listing-header--white-bg { position: absolute; height: 92px; background-color: white; left: 0; right: 0; }
.listing-header--thumb { display: inline-block; vertical-align: middle; border-radius: 50%; border: 2px solid #eee; width: 0; height: 0; padding: 56px 56px 0 0; background-image: url(https://sp.rmbl.ws/z0/V/u/q/b/Vuqba.asF.4-71v3-r79nct.jpeg); background-position: center; background-size: cover }
.listing-header--letter:before { display: inline-block; vertical-align: middle; border-radius: 50%; border: 2px solid #eee; width: 56px; height: 56px; text-align: center; font-size: 48px; line-height: 56px; font-weight: bold; content: "v"; background-color: #37c; color: white; text-transform: capitalize; }
.listing-header--title { margin-left: 1rem; font-weight: 300; display: inline-block; vertical-align: middle; font-size: 40px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: calc(100% - 18rem); }
.listing-header--verified {height: 32px; width: 32px; margin:0 0 -2px 10px }
.listing-header--buttons { display: flex; line-height: 1.15; position: absolute; right: 0; top: 55%; transform: translateY(-50%); }.video-item { position: relative; height: 155px; background-color: white; box-shadow: 0 2px 2px 0 #ccc; }
			.video-item:hover { background-color: #f8f8f8; }

			.video-item:hover::before { z-index: 1; position: absolute; left: 19px; bottom: 18px; content: ""; width: 0; height: 0; border-top: 12px solid transparent; border-bottom: 12px solid transparent; border-left: 20.784px solid rgba(0, 0, 0, 0.1); }
			.video-item:hover::after { z-index: 1; position: absolute; left: 20px; bottom: 20px; content: ""; width: 0; height: 0; border-top: 10px solid transparent; border-bottom: 10px solid transparent; border-left: 17.32px solid white; }

			.video-item--title {
				padding:     10px 10px 0 260px; line-height: 25px; height: 50px; font-size: 18px;
				white-space: normal; overflow: hidden; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 2;
			}

			.video-item--a { position: absolute; top: 0; left: 0; bottom: 0; right: 0; }
			.video-item--a::after { position: absolute; z-index: 1; left: 0; top: 0; right: 0; bottom: 0; content: ""; }
			.video-item--img { display: block; margin: 10px 0 0 10px; width: 240px; height: 135px; }

			.video-item--footer { position: absolute; bottom: 10px; left: 0; line-height: 20px; padding: 20px 0 0 310px; right: 0; font-size: 14px; }

			.video-item--by { position: absolute; width: 100%; bottom: 0; height: 40px; left: 0; box-sizing: border-box; padding: 0 60px 0 250px; }
			.video-item--by-a { z-index: 1; display: inline-block; max-width: 100%; position: relative; padding-left: 60px; }
			.video-item--by-a::before { position: absolute; top: 0; left: 10px; width: 40px; height: 40px; content: ""; background-repeat: no-repeat; background-size: cover; background-position: center; border-radius: 50%; text-transform: capitalize; line-height: 38px; text-align: center; color: white; font-size: 26.6667px; border: 1px solid #eee; box-sizing: border-box; }
			.video-item--by-a:hover { text-decoration: underline; }

			.video-item--by-verified {width:12px;height:12px;margin-left:4px; margin-bottom: -1px;}

			.video-item--meta:nth-child(n+4)::before { content: "•"; padding: 0 0.5em; }
			.video-item--watching-now::after { content: attr(data-value) " watching"; }
			.video-item--views::after { content: attr(data-value) " views"; }
			.video-item--plays::after { content: attr(data-value) " plays"; }
			.video-item--rumbles::after { content: attr(data-value) " rumbles"; }
			.video-item--earned::after { content: "$" attr(data-value) " earned"; color: #4C8800 }

			.video-item--duration,.video-item--live,
			.video-item--duration,.video-item--upcoming {
				position: absolute;  bottom: 7px;
				right: calc(100% + 7px);
				display: block;
			}
			.video-item--duration::after,
			.video-item--live::after,
			.video-item--upcoming::after {
				position: relative;
				left: 250px;
				display: block;
				color: white;
				font-size: 11px;
				line-height: 19px;
				padding: 0 4px;
				background: rgba(0, 0, 0, 0.5);
				content: attr(data-value);
			}
			.video-item--live::after,
			.video-item--upcoming::after{
				border-radius: 4px;
				line-height: 17px;
			}
			.video-item--live::after{
				background: #ee0000;
			}
			.video-item--upcoming::after{
				background: #ec0;
				color: #000;
			}
			.video-item--duration::after {
				-webkit-backdrop-filter: blur(4px);
				backdrop-filter: blur(4px);
				border-radius: 4px;
				overflow: hidden; /* no blur outside of radius */
			}
			.video-item--watching-now { color: #e00; }
			/* optional stuff, ellipsis on title, remember line-height & max-height! */
			.ellipsis-1 { white-space: nowrap; overflow: hidden; display: block; text-overflow: ellipsis; }
			.ellipsis-2 { white-space: normal; overflow: hidden; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 2; }.video-item--by-a--u71v3::before { background-image: url("https://sp.rmbl.ws/z0/V/u/q/b/Vuqba.asF.4-71v3-r79nct.jpeg"); }.tuner-box { display: flex; flex-direction: column; /* flex to prevent unwanted margin collapse */; font-size: 1.1rem; }
.tuner-box--section { box-shadow: 0 2px 2px 0 #ccc; background: white; margin-bottom: 1px; }
.tuner-box--section-header { color: #666; font-weight: bold; text-transform: uppercase; margin: 1rem; }
.tuner-box--ul { margin: 1rem 0 0.6rem 0; }
.tuner-box--li {}
.tuner-box--link { display: block; color: #666; padding: 0.4rem 1rem; }
a.tuner-box--link:hover { text-decoration: none; background: #eaeaea; color: #444; }
.tuner-box--link--current { background: #555; color: #eee; }.header{
	position:fixed;
	top:0;
	left:0;
	width:100%;
	color:#ddd;
	background:#fff;
	height: 4rem;
	padding:0;
	z-index:200;
}
.header-div{
	display:flex;
	color:#fff;
	height:100%;
	padding-left: 1.2rem;
	padding-right: 1.2rem;
	align-items:center;
	position:relative;
}
.main-menu-toggle{
	display: flex;
	align-items: center;
	height:2.6rem;
}
.main-menu-close,.main-menu-open{
	stroke:#555;
	stroke-width:2px
}
.main-menu-close{
	display:none;
	stroke-width:3px
}
.pop-show>.main-menu-close{display:inline-block}
.pop-show>.main-menu-open{display:none}
.header-logo{
	width:10rem;
	margin-left: 1rem;
	margin-right: 0.2rem;
	display: flex;
	flex-shrink:0;
	align-items: center;
}
.header-logo img {
	width: 100%;
	height: auto;
}
.header-upload{
	box-sizing: border-box;
	border-radius:10rem;
	padding: 0 0.35rem;
	background: #4C8800;
	height:2.6rem;
	width:2.6rem;
	margin:0 1rem;
	display: flex;
	align-items: center;
}
.header-upload svg {
	stroke: #fff;
	width: 100%;
}
.header-upload-menu {
	display: none;
	right: 0;
}
.header-upload-menu.pop-show {
	display: block;
}
main {
	display: block;
	margin-top: 4rem;
}.header-search{
	display:flex;
	margin-left: auto;
	align-items:center;
	border-radius:10rem;
	background:#eee;
}
.header-search-select, .header-search-field {
	border:0;
	height:100%;
	background-color:transparent;
	font-size:1.1rem;
	color:#000;
	outline-offset: 3px;
}
.header-search-select:not(:focus-visible),
.header-search-field:not(:focus-visible) {
	outline: none;
}
.header-search-select {
    text-indent: 0.01px;
	width: 7rem;
	flex-shrink: 0;
	padding: 0 1.5rem 0 1rem;
}
.header-search-field{
	-webkit-appearance: textfield;
	border-left:1px solid #bbb;
	width:100%;
	padding:0 0.7rem;
}
.header-search-field::-webkit-search-decoration {
	-webkit-appearance: none;
}
.header-search-field::placeholder{
	color:#555;
}
.header-search-submit{
	height:2.9rem;
	width:2.9rem;
	padding:0.6rem;
	flex-shrink:0;
}
.header-search-select,.header-search-field{display:none}
.header-search-select.pop-show,.header-search-field.pop-show{
	display:block;
}
.header-search.pop-show{
	position:absolute;
	left: 3.5rem;
	right: 1.5rem;
	z-index:100;
}
.header-search-icon{
	stroke:#000;
	fill:#000;
}svg.user-image--icon { display: inline-block; box-sizing: border-box; border: 1px solid #eee; border-radius: 50%; background:#f3f3f7; stroke:#333; }.header-user-info{display:none;}
.header-user{
	text-align:left;
}
i.header-user-img, svg.header-user-img {
	display: block;
	flex-shrink: 0;
	font-size: 2.6rem; width: 2.6rem; height: 2.6rem;
	padding:0.35rem;
}.navs{
	position:fixed;
	top:4rem;
	width:100%;
	z-index:10;
}
.hover-menu{
	position:absolute;
	color:#222;
	background:#eee;
	box-shadow:0 0 20px 0 rgba(0,0,0,0.4);
	width:16rem;
	padding: 0.5rem 0;
	font-size:1.15rem;
	box-sizing: border-box;
	max-height: calc(100vh - 4rem - (1rem + 4vh));
	overflow: hidden auto;
}
#main-menu{
	display:none;
}
#main-menu.pop-show{
	display:block;
	left: 0;
	width: auto;
	min-width: 15rem;
	max-width: 18rem;
}.main-menu-item{
	display:block;
	padding: 0.3rem 1rem 0.5rem;
	outline-offset: -3px;
	max-width: 100%;
	overflow: hidden;
	text-overflow: ellipsis;
}
.main-menu-item-important{
	color:#f99;
}
.main-menu-item:hover{
	opacity:0.7;
	text-decoration:none;
}
.main-menu-heading{
	font-size:1rem;
	font-weight:bold;
	text-transform: uppercase;
	border-top:1px solid #666;
	padding: 1.2rem 1rem 0.8rem;
	margin: 0.9rem 0 0 0;
	cursor: default;
}
:any-link > .main-menu-heading {
	cursor: pointer;
}
.main-menu-icon{
	width:1.8rem;
	height:1.8rem;
	margin:0 0.5rem -0.5rem 0;
	stroke:#000;
	stroke-width:2px;
	stroke-linejoin:round;
	stroke-linecap:round;
	fill:none;
}

.main-menu-item--active {
	background: #555;
	color: #eaeaea;
	cursor: default;
}
.main-menu-item--active .main-menu-icon {
	stroke: currentColor;
}
.main-menu-item--active:hover {
	opacity: 1;
}

.main-menu-signout {
	border-top:1px solid #666;
	padding: .8rem 0 .8rem 2.1rem;
	margin: 0.2rem 0 0;
	text-align: center;
	padding: 0.8rem 0.4rem 0.4rem;
}.footer{
	clear: both;
	background: #111;
	color:#ddd;
	padding-top: 3rem;
	padding-bottom: 3rem;
}
.footer-nav{
	display: flex;
	flex-wrap: wrap;
	margin-bottom: 2rem;
	text-transform: uppercase;
}
.footer-nav-link,
.footer-terms-link {
	margin-right: 1rem;
	margin-bottom: 0.5rem;
	display: block;
	color:#ddd;
}
.footer-nav-link:hover,
.footer-terms-link:hover {
	color: #85C742;
}
.footer-nav-link:focus-visible,
.footer-terms-link:focus-visible {
  text-decoration: underline;
  outline: none;
}
.footer-terms-copyright {
	align-items: center;
}
.footer-terms{
	display: flex;
	flex-wrap: wrap;
}
.footer-copyright {
	margin-top: 2rem;
	margin-bottom: 0;
	color: #aaa;
}.news_notification{
	position:fixed;
	top:0;
	width:100%;
	background: #85C742;
	z-index:1000;
	padding: 0.5rem 0;
	display:flex;
	align-items: center;
	justify-content: center;
	color: #061726;
}
.news_notification_a{
	width:100%;
	box-sizing:border-box;
	padding:0 2.1rem 0 0.5rem;
	text-align:center;
}
.news_close {
	cursor: pointer;
	position: absolute;
	right: 0;
	top: 0;
	bottom: 0;
	padding: 0 .7rem;
	display: flex;
	align-items: center;
}
.news_close-x {
	width: 0.8rem;
	height: 0.8rem;
	padding: 0.2rem;
	background: rgba(255,255,255,0.5);
	border-radius: 100%;
	stroke: #333;
}
.news_close:hover .news_close-x  {
	background:rgba(255,255,255,0.75);
}@media(max-width:699.95px){.desktop-only{
	display:none
}.listing-header--title { font-size: 26px; line-height: 1; position: absolute; top: 16px; max-width: calc(100% - 6rem); }
.listing-header--verified {height: 20px; margin:0 0 0 5px }
.listing-header--buttons { left: 76px; transform: none; margin-left: -0.35rem; }.video-item { height: 81px; }

			.video-item--title { padding: 4px 5px 0 149px; line-height: 16px; height: 32px; font-size: 14px; }

			.video-item--img { margin: 0; width: 144px; height: 81px; }

			.video-item--footer { bottom: 0; font-size: 11px; line-height: 1; padding: 16px 0 4px 149px; }

			.video-item--by { height: 11px; bottom: 20px; padding: 0 0 0 149px; font-size: 11px; line-height: 1; }
			.video-item--by-a { padding-left: 0; }
			.video-item--by-a::before { display: none; }

			.video-item--earned::after { content: "$" attr(data-value); }
			.video-item--duration::after,.video-item--live::after,.video-item--upcoming::after { left: 144px; }.paginator--ul { display: flex; margin: 0; padding: 0; color: #666; justify-content: center; font-size: 1rem; }
.paginator--li { display: none; }
.paginator--li--prev, .paginator--li--next { display: block; padding: 0.6rem 1rem; box-shadow: 0 2px 2px 0 #ccc; background: white; } 
.paginator--li--prev { border-top-left-radius: 2rem; border-bottom-left-radius: 2rem; }
.paginator--li--next { border-top-right-radius: 2rem; border-bottom-right-radius: 2rem; }
.paginator--li--prev .paginator--link:before { content: "« Prev" }
.paginator--li--next .paginator--link:before { content: "Next »" }
.paginator--link:hover { text-decoration: none; }
.paginator--li--next:nth-child(2) {
	border-top-left-radius: 2em;
	border-bottom-left-radius: 2em;
}
.paginator--li + .paginator--li--next:nth-child(2) {
	border-left-width: 1px;
}
.paginator--li--prev:nth-last-child(2) {
	border-top-right-radius: 2em;
	border-bottom-right-radius: 2em;
}}@media(max-width:1199.95px){.main-and-sidebar { display: block; }
.sidebar { margin: 1rem 0 0 0; }
.bottom-popup { position: fixed; left: 0; right: 0; top: 56px; bottom: 0; display: flex; flex-direction: column; z-index: 1; }
#is-sidebar-open:checked + .bottom-popup { background-color: #f3f3f7; transition: background-color 0.15s linear; } 
#is-sidebar-open:not(:checked) + .bottom-popup { display: flex; top: unset; }  
#is-sidebar-open:not(:checked) + .bottom-popup .bottom-popup--header { background-color: rgba(0, 0, 0, 0.6); }  
.bottom-popup--header { text-align: center; }
.bottom-popup--button { display: inline-block; margin: 0.5em; border-radius: 2em; background-color: black; color: white; padding: 0.5em 1.5em; text-transform: uppercase; }
.bottom-popup .bottom-popup--header-text::before { content: "Filters"; }  
#is-sidebar-open:checked + .bottom-popup .bottom-popup--header-text::before { content: "Collapse"; }  
.bottom-popup--contents { display: none; flex: 1; overflow: auto; }
@supports (-webkit-overflow-scrolling: touch) {
	 .bottom-popup--contents { overflow-y: scroll; -webkit-overflow-scrolling: touch; }
}
#is-sidebar-open:checked + .bottom-popup .bottom-popup--contents { display: flex; flex-direction: column; justify-content: center; }
.bottom-popup--sidebar { width: 100%; max-width: 336px; margin: 0 auto; min-height: 0 /* this is not a hack, but I can't explain wtf is this */; }

.bottom-popup--arrow { margin: 0 0 0.125em 1em; display: inline-block; width: 0; height: 0; border-left: 0.5em solid transparent; border-right: 0.5em solid transparent; border-bottom: 0.5em solid white; }
#is-sidebar-open:checked + .bottom-popup .bottom-popup--arrow {  border-bottom: 0; border-top: 0.5em solid white; }}@media(min-width:700px){.mobile-only{
	display:none
}.h1 {
	font-size:2.6rem;
	line-height: 1.25;
	margin:1rem 0 1.8rem;
}
.thirds{
	display: flex;
	flex-wrap: wrap;
}
.two-thirds, .one-thirds{
	display: flex;
	flex-direction: column;
	width:33.333333333%;
	padding-left: 1rem;
	padding-right: 1rem;
}
.two-thirds{
	width:66.666666667%;
}
.container{
	border-left:1px solid #e4e4e4;
	border-right:1px solid #e4e4e4;
}
.round-button{
	padding:0.85rem 1.3rem;
	margin-left: 0.5rem;
	margin-right: 0.5rem;
	font-size:1rem;
}button.locals-button svg {
	width: 24px;
	height: 24px;
}.paginator { display: flex; justify-content: center; }
.paginator--ul { display: flex; margin: 0; padding: 0; color: #666; background: white; border-radius: 2rem; box-shadow: 0 2px 2px 0 #ccc; overflow: hidden; }
.paginator--link { display: block; padding: 0.75rem 1rem; min-width: 1.5rem; text-align:center; text-decoration: none; border-right: 1px solid #eaeaea; }
.paginator--li:last-child .paginator--link { border: none; }
.paginator--link:hover { background-color: #eaeaea; text-decoration: none; }
.paginator--link--current, .paginator--link--current:hover { background-color: #555; color: #EAEAEA }
.paginator--link::before { content: attr(aria-label); }.header-upload{
	margin-left: auto;
	margin-right: 1.2rem;
}.header-search-select,.header-search-field{display:block}
.header-search,.header-search.pop-show{
	position:static;
	box-sizing: border-box;
	padding-left: 0.3rem;
	padding-right: 0.3rem;
	width: 40%;
	margin-left: 2.5rem;
	margin-right: 2.5rem;
}.header-user{
	width:9rem;
	display: flex;
	align-items: center;
}
.header-user-name,.header-user-stat{
	display:block;
	color:#555;
}
.header-user-name{
	color:#000;
	padding:0.1rem 0 0.1rem;
}
.header-user-info{
	display:inline-block;
	margin-left:0.5rem;
}.footer {
	padding-top: 2rem;
	padding-bottom: 4rem;
}
.footer-nav-link{
	margin-right: 3rem;
	margin-bottom: 0;
}
.footer-terms-link {
	margin-right: 0;
	margin-bottom: 0;
}
.footer-terms-copyright {
	display: flex;
}
.footer-terms{
	order: 2;
}
.footer-terms-link.divider::after{
	content: ' | ';
	display:inline-block;
	color: #666;
	padding-left: 10px;
	padding-right: 10px;
}
.footer-copyright {
	margin-top: 0;
	margin-right: 3rem;
}}@media(min-width:700px) and (max-width:1199.95px){.listing-header--title { font-size: 36px; }
.listing-header--verified {height: 28px; margin:0 0 -2px 10px }}@media(min-width:1200px){.constrained{
	max-width:1200px;
	width:100%;
	margin:0 auto;
}.main-and-sidebar { display: flex; }
.sidebar { margin-left: 1rem; width: 336px; }
.bottom-popup--header { display: none; }}</style><script>var $$={};var addThemeSwitcher;!function(){var c,r,s="system",i="light",h="dark",l=[h],o=[s,i,h],d=matchMedia("(prefers-color-scheme: dark)"),a=!1,m=!0,n=[],t=[];function u(){try{if(!a&&localStorage)return localStorage.getItem("themePreference")}catch(e){a=!0}}function f(){t.forEach(function(e){e(r)})}function $(){var e,t,a,n;c=c||u()||s,e=c==s?d.matches?h:i:0<=o.indexOf(c)?c:i,r!==(e=e)&&(r=e,l.indexOf(e)<0?(a=document.querySelectorAll("head .js-theme-ss"),Array.prototype.forEach.call(a,function(e){e.disabled=!0})):(t=!1,a="/c/themes/"+e+".css",n="js-theme-ss js-theme-ss--"+e,e=document.querySelectorAll(".js-theme-ss--"+e),Array.prototype.forEach.call(e,function(e){e.disabled=!1,e.dataset.themeMainStylesheet&&(t=!0)}),t||(m?document.write('<link rel=stylesheet data-theme-main-stylesheet="1" class="'+n+'" href="'+a+'" />'):((e=document.createElement("link")).rel="stylesheet",e.href=a,e.className=n,e.dataset.themeMainStylesheet="1",document.head.appendChild(e))))),f()}function y(){$$.each(n,function(){var e=this.getAttribute("data-theme")==c;$$[(e?"add":"remove")+"Class"](this,"main-menu-item--active")})}function p(e,t){(t=e.getAttribute("data-theme"))&&n.indexOf(e)<0&&(n.push(e),$$.addClick(e,function(e){return e.preventDefault(),e=t,a||localStorage.setItem("themePreference",e),c!=e&&(c=e,$(),y()),$$.query(".main-menu-toggle")[0].click(),!1}))}addThemeSwitcher=function(e,t){$$.each($$.query(e),function(){p(this)}),y(),t&&$$.each($$.query(t),function(){this.style.display="block"})},c=u()||s,$(),m=!1,d.addEventListener&&d.addEventListener("change",function(e){$()}),$$&&($$.applyThemePreference=$,$$.registerThemeCallback=function(e){t.push(e)})}();

</script><script type="application/ld+json">[{"@context":"http://schema.org","@type":"WebSite","url":"https://rumble.com/","potentialAction":{"@type":"SearchAction","target":"https://rumble.com/search/video?q={search}","query-input":"required name=search"}},{"@context":"http://schema.org","@type":"Organization","name":"Rumble","url":"https://rumble.com/","logo":"https://rumble.com/i/rumble_logo_back.png","sameAs":["https://www.facebook.com/rumblevideo/","https://twitter.com/rumblevideo"]}]</script><meta content="vivafrei's videos on Rumble.com" name="description"/><meta content="noindex" name="robots"/><meta content="155223717937973" property="fb:app_id"/><meta content="@rumblevideo" name="twitter:site"/><meta content="app-id=1518427877" name="apple-itunes-app"/><meta content="vivafrei" property="og:title"/><meta content="vivafrei's videos on Rumble.com" property="og:description"/><meta content="https://rumble.com/user/vivafrei" property="og:url"/><link href="/i/favicon-v4.png" rel="shortcut icon"/><link href="/apple-touch-icon.png" rel="apple-touch-icon"/></head> <body>
<main>
<div class="constrained">
<div style="margin-bottom: 1rem"><div class="listing-header--white-bg"></div><div class="listing-header--content"><img alt="vivafrei" class="listing-header--thumb" src="https://sp.rmbl.ws/z0/V/u/q/b/Vuqba.asF.4-71v3-r79nct.jpeg"/><h1 class="listing-header--title">vivafrei<svg class="listing-header--verified verification-badge-icon" height="24" viewbox="0 0 24 24" width="24"><circle cx="12" cy="12" r="12"></circle><path d="M5.4 11.1l5 5 8.2-8.2" fill="none" stroke="currentColor" stroke-miterlimit="10" stroke-width="2"></path></svg></h1><div class="listing-header--buttons"><button class="round-button media-subscribe bg-green" data-action="subscribe" data-slug="vivafrei" data-title="vivafrei" data-type="user"><span class="subscribe-button-label">Subscribe</span><span class="subscribe-button-count">280K</span></button><button class="round-button locals-button" data-context="channel" data-locals-community="252318154180013735">Join<svg fill="none" height="24" viewbox="0 0 95 71" width="24"><path d="M85.02 43.1a7.12 7.12 0 0 0 7.11-7.12 7.12 7.12 0 0 0-7.11-7.12 7.12 7.12 0 0 0-7.12 7.12 7.12 7.12 0 0 0 7.12 7.12z" fill="#88172B"></path><path d="M69.92 26.64v18.69h-4.8v-2a7.35 7.35 0 0 1-5.73 2.6 9.96 9.96 0 0 1-6.57-3.15 9.97 9.97 0 0 1 0-13.58 9.96 9.96 0 0 1 6.57-3.16 7.34 7.34 0 0 1 5.72 2.6v-2h4.8zm-4.8 9.34a5.13 5.13 0 0 0-3.17-4.74 5.12 5.12 0 0 0-5.58 1.11 5.13 5.13 0 0 0 3.62 8.76c1.36 0 2.66-.54 3.62-1.5a5.13 5.13 0 0 0 1.5-3.63zM41.38 39.4l2 4.3a9.7 9.7 0 0 1-6.48 2.22 9.94 9.94 0 0 1-7.3-2.76A9.95 9.95 0 0 1 26.55 36a9.96 9.96 0 0 1 3.06-7.19 9.94 9.94 0 0 1 7.3-2.76 9.64 9.64 0 0 1 6.48 2.23l-2 4.33a6.16 6.16 0 0 0-4.32-1.76 5.13 5.13 0 0 0-5.22 3.02 5.15 5.15 0 0 0 3.1 6.98 5.13 5.13 0 0 0 2.12.23 6.13 6.13 0 0 0 4.33-1.66z" fill="#fff"></path><path d="M9.93 43.1a7.12 7.12 0 0 0 7.11-7.12 7.12 7.12 0 0 0-7.11-7.12 7.12 7.12 0 0 0-7.12 7.12 7.12 7.12 0 0 0 7.12 7.12z" fill="#88172B"></path><path d="M17.93 15.53v4.8H2.03V1.6h4.72v13.93h11.18z" fill="#fff"></path><path d="M85.02 20.86A9.93 9.93 0 1 0 85 1a9.93 9.93 0 0 0 0 19.87zm-25.03-2.8a7.12 7.12 0 0 0 7.12-7.13 7.12 7.12 0 0 0-7.12-7.12 7.12 7.12 0 0 0-7.12 7.12A7.12 7.12 0 0 0 60 18.05z" fill="#88172B"></path><path d="M44.9 10.93a9.96 9.96 0 0 1-6.13 9.2A9.93 9.93 0 0 1 27.93 18a9.95 9.95 0 0 1-2.17-10.85 9.95 9.95 0 0 1 13-5.4 9.92 9.92 0 0 1 5.38 5.38c.5 1.21.75 2.5.75 3.81zm-4.83 0a5.13 5.13 0 0 0-3.16-4.74 5.12 5.12 0 0 0-5.58 1.11 5.13 5.13 0 0 0 3.62 8.76c1.36 0 2.66-.54 3.62-1.5a5.13 5.13 0 0 0 1.5-3.63zm53.37 53.42c0 3.8-3 6.63-8.2 6.63a14.33 14.33 0 0 1-8.65-2.7l1.5-4.53a10.94 10.94 0 0 0 6.63 2.63c2.22 0 3.85-.44 3.85-1.6 0-.84-.83-1.14-3.32-1.56-6.96-1.13-8.13-3.34-8.13-6.4 0-3.06 3.27-5.73 8.16-5.73 2.52.02 5 .63 7.26 1.77l-1.34 4.37a12.04 12.04 0 0 0-5.92-1.6c-1.94 0-3.34.34-3.34 1.14 0 1.13 1.95 1.32 3.94 1.66 6.34 1.06 7.56 3.55 7.56 5.92zm-25.47 1.2v4.78H52V51.7h4.91v13.84h11.07z" fill="#fff"></path><path d="M34.95 68.17a7.12 7.12 0 0 0 7.12-7.13 7.12 7.12 0 0 0-7.12-7.12 7.12 7.12 0 0 0-7.12 7.12 7.12 7.12 0 0 0 7.12 7.13zM9.92 70.98a9.93 9.93 0 1 0 0-19.86 9.93 9.93 0 0 0 0 19.86z" fill="#88172B"></path></svg></button></div></div></div>
<div class="main-and-sidebar">
<div style="flex: 1">
<ol>
<li class="video-listing-entry"><article class="video-item"><h3 class="video-item--title">Amazon Sued for Selling "Suicide Kits" and the Allegations are HORRIFYING! Viva Clips</h3><a class="video-item--a" href="/v1onhfm-amazon-sued-for-selling-suicide-kits-and-the-allegations-are-horrifying-viv.html"><img alt='Amazon Sued for Selling "Suicide Kits" and the Allegations are HORRIFYING! Viva Clips' class="video-item--img" src="https://sp.rmbl.ws/s8/6/c/q/N/e/cqNeg.oq1b.jpg"/></a><footer class="video-item--footer ellipsis-1"><address class="video-item--by"><a class="video-item--by-a video-item--by-a--u71v3" href="/user/vivafrei" rel="author"><div class="ellipsis-1">vivafrei<svg class="video-item--by-verified verification-badge-icon" height="24" viewbox="0 0 24 24" width="24"><circle cx="12" cy="12" r="12"></circle><path d="M5.4 11.1l5 5 8.2-8.2" fill="none" stroke="currentColor" stroke-miterlimit="10" stroke-width="2"></path></svg></div></a></address><span class="video-item--duration" data-value="7:35"></span><span class="video-item--meta video-item--views" data-value="137"></span><span class="video-item--meta video-item--rumbles" data-value="110"></span><time class="video-item--meta video-item--time" datetime="2022-10-18T22:17:53-04:00">Oct 19</time></footer></article></li>
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
</nav> </div>
</div>
</div>
</div>
</div>
</div>
</main>
<header class="header">
<div class="header-div constrained">
<button aria-label="main menu" class="main-menu-toggle">
<svg class="main-menu-open" height="16" width="20"><path d="M0 1h20M0 8h20M0 15h20"></path></svg> <svg class="main-menu-close" height="16" width="20"><path d="M2.5.5 l15 15 m0-15 l-15 15"></path></svg> </button>
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
<svg class="header-search-icon" viewbox="0 0 26 26"><path d="M17.6 17.6l6.3 6.3M2.2 11.2a9 9 0 1 0 18 0 9 9 0 1 0-18 0" fill="none" stroke-linecap="round" stroke-width="2"></path></svg> </button>
</form>
<button class="header-upload" title="Upload">
<svg viewbox="0 0 26 26"><path d="M4.2 17.5s-2.7-3.1-1.9-7.1C3 6.8 5.9 3.9 9.9 3.9c3.5 0 5.1 1.6 6.2 2.7 1.1 1.1 1.4 3.5 1.4 3.5s2.7-.7 4.4.7 2.4 3.8 1.8 5.6-2.6 3.1-2.6 3.1M9 17.1l4.1-3.8 4.2 3.8m-4.2 5.4v-9.2" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg> </button>
<button aria-label="sign in" class="header-user">
<svg class="user-image user-image--icon header-user-img"><path d="M8 6.8a5 5 0 1 0 10 0 5 5 0 1 0-10 0m14.8 16.7v-3.7a4 4 0 0 0-4-4H7.2a4 4 0 0 0-4 4v3.7" fill="none" stroke-linecap="round" stroke-width="2"></path></svg> <span class="header-user-info">
<span class="header-user-name">Sign In</span>
</span>
</button>
</div>
</header>
<nav class="navs">
<div class="constrained" style="position:relative">
<div class="hover-menu main-menu-nav" id="main-menu">
<a class="main-menu-item" href="/videos?date=this-week"><svg class="main-menu-icon"><path d="M5 13a8 8 0 1 0 16 0 8 8 0 1 0-16 0M2.9 8.6C4.1 6 6.2 3.9 8.7 2.8m14.5 14.7a11.5 11.5 0 0 1-5.8 5.7M13 6.9V13h4.2" fill="none"></path></svg>Latest</a> <a class="main-menu-item" href="/editor-picks"><svg class="main-menu-icon" height="27" viewbox="0 0 26 27" width="26"><path d="M4 8a6.5 7 0 1 0 13 0A6.5 7 0 1 0 4 8m15 13.5C15.6 11 1.1 13.9 1 25m13-2.4l3.9 4.4 7.1-8" fill="none"></path></svg>Editor Picks</a>
<a class="main-menu-item" href="/videos?sort=views&amp;date=today"><svg class="main-menu-icon" height="24" viewbox="0 0 24 24" width="24"><path d="m23 6-9.5 9.5-5-5L1 18M17 6h6v6"></path></svg>Trending</a>
<a class="main-menu-item" href="/license-videos"><svg class="main-menu-icon" height="26" viewbox="0 0 26 26" width="26"><path d="M19.1 20H2.3V6h11.8M24.3 20h-5.5s-.9-1.5-1.4-2c-.5-.5-1-1.3-1.9-1.7-.4-.2-2.2-1.6-2.3-2.5 0-1.7 1.1-1.4 2.3-1 1.2.5 3.6 1.6 3.6 1.6l-.9-6.7S12.9 6.2 13 5.9c.1-.3 5.8-1.9 7.2-.2s2 4.5 2.8 5.1c.8.6 1.5.6 1.5.6 M6.8,11.1a1.8,1.8 0 1,0 3.6,0a1.8,1.8 0 1,0 -3.6,0 M5.8 16.6c0-1.5 1.2-2.7 2.7-2.7s2.7 1.2 2.7 2.7" fill="none"></path></svg>License Videos</a>
<div class="js-theme-option-group" hidden="">
<h3 class="main-menu-heading">Theme</h3>
<a class="main-menu-item js-theme-option" data-theme="system" href=""><svg class="main-menu-icon" height="24" viewbox="0 0 24 24" width="24"><path d="M12 1v2m0 18v2M4.2 4.2l1.4 1.4m12.8 12.8 1.4 1.4M1 12h2m18 0h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4M16 12.36A4 4 0 1 1 11.64 8 3.12 3.12 0 0 0 16 12.36Z"></path></svg> OS Default</a>
<a class="main-menu-item js-theme-option" data-theme="dark" href=""><svg class="main-menu-icon" height="24" viewbox="0 0 24 24" width="24"><path d="M12.1 4.1c.3-.4 0-.9-.5-.8a8.5 8.5 0 1 0 9.3 12.4c.3-.4-.1-.9-.6-.7A7 7 0 0 1 12 4.2Z"></path></svg> Dark Mode</a>
<a class="main-menu-item js-theme-option" data-theme="light" href=""><svg class="main-menu-icon" height="24" viewbox="0 0 24 24" width="24"><path d="M7 12a5 5 0 1 0 10 0 5 5 0 1 0-10 0m5-11v2m0 18v2M4.2 4.2l1.4 1.4m12.8 12.8 1.4 1.4M1 12h2m18 0h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"></path></svg> Light Mode</a>
</div>
<h3 class="main-menu-heading">Featured Channels</h3><a class="main-menu-item" href="/c/Reuters">Reuters</a><a class="main-menu-item" href="/c/WildCreatures">Wild Creatures</a><a class="main-menu-item" href="/c/WayneDupreeShow">The Wayne Dupree Show</a><a class="main-menu-item" href="/c/Newsy">Newsy</a><a class="main-menu-item" href="/c/JustPlanes">JustPlanes</a><a class="main-menu-item" href="/c/DevinNunes">Devin Nunes</a><a class="main-menu-item" href="/c/MarkDice">MarkDice</a><a class="main-menu-item" href="/c/Bongino">The Dan Bongino Show</a><a class="main-menu-item" href="/c/Cioccolanti">Cioccolanti</a><a class="main-menu-item" href="/c/DineshDsouza">Dinesh Dsouza</a><a class="main-menu-item" href="/c/MLChristiansen">MLChristiansen</a><a class="main-menu-item" href="/c/RobertGouveia">RobertGrulerEsq</a><a class="main-menu-item" href="/c/BannonsWarRoom">BannonsWarRoom</a><a class="main-menu-item" href="/c/BennyJohnson">BennyJohnson</a><a class="main-menu-item" href="/c/NoreensKitchen">NoreensKitchen</a><a class="main-menu-item" href="/c/CharlieKirk">Charlie Kirk</a><a class="main-menu-item" href="/c/NewsmaxTV">NewsmaxTV</a><a class="main-menu-item" href="/c/MariaBartiromo">MariaBartiromo</a><a class="main-menu-item" href="/user/vivafrei">Viva Frei</a><a class="main-menu-item" href="/c/Fleccas">Fleccas</a><a class="main-menu-item" href="/c/Styxhexenhammer666">Styxhexenhammer666</a><a class="main-menu-item" href="/c/SeanHannity">Sean Hannity</a><a class="main-menu-item" href="/c/TrishReganShow">Trish Regan</a><a class="main-menu-item" href="/c/SamuelEarpArtist">Samuel Earp Artist</a><a class="main-menu-item" href="/c/KayaJones">KayaJones</a><a class="main-menu-item" href="/c/TheNerdRealm">The Nerd Realm</a><a class="main-menu-item" href="/c/sideserfcakes">Side Serf Cakes</a><a class="main-menu-item" href="/c/spaceXcentric">spaceXcentric</a><a class="main-menu-item" href="/c/MikhailaPeterson">Mikhaila Peterson</a><a class="main-menu-item" href="/c/NTDNews">NTDNews</a><a class="main-menu-item" href="/c/TheOfficerTatum">The Officer Tatum</a><a class="main-menu-item" href="/c/OutKickTheCoverage">OutKick</a><a class="main-menu-item" href="/c/CWLemoine">CWLemoine</a><a class="main-menu-item" href="/c/LaurenChen">Lauren Chen</a><a class="main-menu-item" href="/c/DonaldTrump">Donald Trump</a><a class="main-menu-item" href="/c/TheHistoryGuy">The History Guy</a><a class="main-menu-item" href="/c/RebelNews">RebelNews</a><a class="main-menu-item" href="/c/pintswithaquinas">pintswithaquinas</a><a class="main-menu-item" href="/c/TheBodyLanguageGuy">TheBodyLanguageGuy</a><a class="main-menu-item" href="/c/YelllowFlash">YelllowFlash</a><a class="main-menu-item" href="/c/BrightInsight">BrightInsight</a><a class="main-menu-item" href="/c/PaulandMorgan">PaulandMorgan</a><a class="main-menu-item" href="/c/AwakenWithJP">Awaken With JP</a><a class="main-menu-item" href="/c/TulsiGabbard">Tulsi Gabbard</a><a class="main-menu-item" href="/c/TheBabylonBee">The Babylon Bee</a><a class="main-menu-item" href="/c/BenShapiro">Ben Shapiro</a><a class="main-menu-item" href="/c/FactsChannel">Facts</a><a class="main-menu-item" href="/c/RandPaul">Rand Paul</a><a class="main-menu-item" href="/c/DonaldJTrumpJr">Donald Trump Jr</a><a class="main-menu-item" href="/c/EliseStefanik">Elise Stefanik</a><a class="main-menu-item" href="/c/BlacktipH">BlacktipH</a><a class="main-menu-item" href="/c/LifeStories">Life Stories</a><a class="main-menu-item" href="/c/c-647947">SCI</a><a class="main-menu-item" href="/c/StevenCrowder">Steven Crowder</a><a class="main-menu-item" href="/c/NYPost">New York Post</a><a class="main-menu-item" href="/c/PageSix">PageSix</a><a class="main-menu-item" href="/c/Decider">Decider</a><a class="main-menu-item" href="/c/JohnStossel">John Stossel</a><a class="main-menu-item" href="/c/RonPaulLibertyReport">Ron Paul Liberty Report</a><a class="main-menu-item" href="/c/ARKMedia">ARKMedia</a><a class="main-menu-item" href="/c/Locals">Locals</a><a class="main-menu-item" href="/c/Timcast">Timcast</a><a class="main-menu-item" href="/c/TimcastIRL">TimcastIRL</a><a class="main-menu-item" href="/c/Entrepreneur">Entrepreneur</a><a class="main-menu-item" href="/c/EpochTV">EpochTV</a><a class="main-menu-item" href="/c/WhitneyBjerken">WhitneyBjerken</a><a class="main-menu-item" href="/c/DrDrew">Dr Drew</a><a class="main-menu-item" href="/c/Yarnhub">Yarnhub</a><a class="main-menu-item" href="/c/RubinReport">Rubin Report</a><a class="main-menu-item" href="/c/GGreenwald">Glenn Greenwald</a><a class="main-menu-item" href="/c/MattKohrs">Matt Kohrs (Finance)</a><a class="main-menu-item" href="/c/HabibiBros">Habibi Power Hour</a><a class="main-menu-item" href="/c/Orf">Orf</a><a class="main-menu-item" href="/c/Inquire">Inquire</a><a class="main-menu-item" href="/c/phetasy">phetasy</a><a class="main-menu-item" href="/c/academyofideas">academyofideas</a><a class="main-menu-item" href="/c/JorgeMasvidal">Jorge Masvidal</a><a class="main-menu-item" href="/c/russellbrand">Russell Brand</a><a class="main-menu-item" href="/c/HonestReportingCanada">Honest Reporting</a><a class="main-menu-item" href="/c/GrantCardone">Grant Cardone</a><a class="main-menu-item" href="/c/ChrisJericho">ChrisJericho</a><a class="main-menu-item" href="/c/TheRamseyShowHighlights">TheRamseyShowHighlights</a><a class="main-menu-item" href="/c/TheRamseyShowFullEpisodes">TheRamseyShowFullEpisodes</a><a class="main-menu-item" href="/c/TheInterviewRoom">TheInterviewRoom</a><a class="main-menu-item" href="/c/MedicalMedium">MedicalMedium</a><a class="main-menu-item" href="/c/TheJimmyDoreShow">TheJimmyDoreShow</a><a class="main-menu-item" href="/c/ClayandBuck">ClayandBuck</a><a class="main-menu-item" href="/c/UprightHealth">UprightHealth</a><a class="main-menu-item" href="/c/TheRichDadChannel">TheRichDadChannel</a><a class="main-menu-item" href="/c/NaturesAlwaysRight">NaturesAlwaysRight</a><a class="main-menu-item" href="/c/ChampagneSharks">ChampagneSharks</a><a class="main-menu-item" href="/c/PetervonPanda">PetervonPanda</a><a class="main-menu-item" href="/c/AfterSkool">AfterSkool</a><a class="main-menu-item" href="/c/SmokyRibsBBQ">SmokyRibsBBQ</a><a class="main-menu-item" href="/c/MichaelLeeStrategy">MichaelLeeStrategy</a><a class="main-menu-item" href="/c/iammrbeat">iammrbeat</a><a class="main-menu-item" href="/c/WorkshopCompanion">WorkshopCompanion</a><a class="main-menu-item" href="/c/StockCurry">StockCurry</a><a class="main-menu-item" href="/c/ThePodcastoftheLotusEaters">ThePodcastoftheLotusEaters</a><a class="main-menu-item" href="/c/ArielleScarcella">ArielleScarcella</a><a class="main-menu-item" href="/c/TradersLanding">TradersLanding</a><a class="main-menu-item" href="/c/RuckaRuckaAli">Rucka Rucka Ali</a><a class="main-menu-item" href="/c/DegenerateJay">DegenerateJay</a><a class="main-menu-item" href="/c/DegeneratePlays">DegeneratePlays</a><a class="main-menu-item" href="/c/DVGPodcast">DVGPodcast</a><a class="main-menu-item" href="/c/TheDiveWithJacksonHinkle">TheDiveWithJacksonHinkle</a><a class="main-menu-item" href="/c/thatbeatgoeson">thatbeatgoeson</a><a class="main-menu-item" href="/c/Kilmeade">Kilmeade</a><a class="main-menu-item" href="/c/TheHillbillyKitchen">TheHillbillyKitchen</a><a class="main-menu-item" href="/c/NewsTalkSTL">NewsTalkSTL</a><a class="main-menu-item" href="/c/LogOffAlready">LogOffAlready</a><a class="main-menu-item" href="/c/EnterShaolin">EnterShaolin</a><a class="main-menu-item" href="/c/WillCain">WillCain</a><a class="main-menu-item" href="/c/MegynKelly">MegynKelly</a><a class="main-menu-item" href="/c/RepKevinMcCarthy">RepKevinMcCarthy</a><a class="main-menu-item" href="/c/AlisonMorrow">AlisonMorrow</a><a class="main-menu-item" href="/c/BenUyeda">BenUyeda</a><a class="main-menu-item" href="/c/MrBuildIt">MrBuildIt</a><a class="main-menu-item" href="/c/SteveScalise">SteveScalise</a><a class="main-menu-item" href="/c/TheHeritageFoundation">TheHeritageFoundation</a><a class="main-menu-item" href="/c/TheDailySignal">TheDailySignal</a><a class="main-menu-item" href="/c/GreenDreamProject">GreenDreamProject</a><a class="main-menu-item" href="/c/BlackPowerMediaChannel">BlackPowerMediaChannel</a><a class="main-menu-item" href="/c/AmericanSongwriter">AmericanSongwriter</a><a class="main-menu-item" href="/c/modernwisdompodcast">modernwisdompodcast</a><a class="main-menu-item" href="/c/IsaacArthur">IsaacArthur</a><a class="main-menu-item" href="/c/TomAntosFilms">TomAntosFilms</a><a class="main-menu-item" href="/c/ColionNoir">ColionNoir</a><a class="main-menu-item" href="/c/KimIversen">KimIversen</a><a class="main-menu-item" href="/c/Homesteadonomics">Homesteadonomics</a><a class="main-menu-item" href="/c/TheAdventureAgents">TheAdventureAgents</a><a class="main-menu-item" href="/c/NDWoodworkingArt">NDWoodworkingArt</a><a class="main-menu-item" href="/c/KenDBerryMD">KenDBerryMD</a><a class="main-menu-item" href="/c/davidpakmanshow">davidpakmanshow</a><a class="main-menu-item" href="/c/HeresyFinancial">HeresyFinancial</a><a class="main-menu-item" href="/c/RepJimBanks">RepJimBanks</a><a class="main-menu-item" href="/c/ATRestoration">ATRestoration</a><a class="main-menu-item" href="/c/ThisSouthernGirlCan">ThisSouthernGirlCan</a><a class="main-menu-item" href="/c/RockFeed">RockFeed</a><a class="main-menu-item" href="/c/CountryCast">CountryCast</a><a class="main-menu-item" href="/c/ShaunAttwood">ShaunAttwood</a><a class="main-menu-item" href="/c/TwinCoconuts">TwinCoconuts</a><a class="main-menu-item" href="/c/diywife">diywife</a><a class="main-menu-item" href="/c/RekietaLaw">RekietaLaw</a><a class="main-menu-item" href="/c/MontyFranklin">MontyFranklin</a><a class="main-menu-item" href="/c/GeeksandGamers">GeeksandGamers</a><a class="main-menu-item" href="/c/SportsWars">SportsWars</a><a class="main-menu-item" href="/c/nfldaily">nfldaily</a><a class="main-menu-item" href="/c/nbanow">nbanow</a><a class="main-menu-item" href="/c/GeeksAndGamersPlay">GamingWithGeeks</a><a class="main-menu-item" href="/c/ParkHoppin">ParkHoppin</a><a class="main-menu-item" href="/c/GeeksAndGamersClips">GeeksAndGamersClips</a><a class="main-menu-item" href="/c/chiefstv">chiefstv</a><a class="main-menu-item" href="/c/brownsreport">brownstv</a><a class="main-menu-item" href="/c/nygiantstv">giantstv</a><a class="main-menu-item" href="/c/warriorstv">warriorstv</a><a class="main-menu-item" href="/c/lakerstv">lakerstv</a><a class="main-menu-item" href="/c/DynastyFlock">DynastyFlock</a><a class="main-menu-item" href="/c/FantasyFlockNetwork">FantasyFlockNetwork</a><a class="main-menu-item" href="/c/rwmalonemd">rwmalonemd</a><a class="main-menu-item" href="/c/Chubbyemu">Chubbyemu</a><a class="main-menu-item" href="/c/AnthonyJ350">AnthonyJ350</a><a class="main-menu-item" href="/c/ReasonTV">ReasonTV</a><a class="main-menu-item" href="/c/GfinityTv">GfinityTv</a><a class="main-menu-item" href="/c/engineerman">engineerman</a><a class="main-menu-item" href="/c/Newsthink">Newsthink</a><a class="main-menu-item" href="/c/MrScientific">MrScientific</a><a class="main-menu-item" href="/c/TheS">TheS</a><a class="main-menu-item" href="/c/Debunked">Debunked</a><a class="main-menu-item" href="/c/sydneywatson">sydneywatson</a><a class="main-menu-item" href="/c/UncivilLaw">UncivilLaw</a><a class="main-menu-item" href="/c/Dannyjokes">Dannyjokes</a><a class="main-menu-item" href="/c/BitcoinMagazine">BitcoinMagazine</a><a class="main-menu-item" href="/c/SonofaTech">SonofaTech</a><a class="main-menu-item" href="/c/MysteryScoop">MysteryScoop</a><a class="main-menu-item" href="/c/SpencerCornelia">SpencerCornelia</a><a class="main-menu-item" href="/c/Multipolarista">Multipolarista</a><a class="main-menu-item" href="/c/TheLeadAttorney">TheLeadAttorney</a><a class="main-menu-item" href="/c/Monark">Monark</a><a class="main-menu-item" href="/c/ThinkBeforeYouSleep">ThinkBeforeYouSleep</a><a class="main-menu-item" href="/c/Ferrez">Ferrez</a><a class="main-menu-item" href="/c/RonDeSantisFL">RonDeSantisFL</a><a class="main-menu-item" href="/c/TheDawgfathasBBQ">TheDawgfathasBBQ</a><a class="main-menu-item" href="/c/JimBreuer">JimBreuer</a><a class="main-menu-item" href="/c/RyanLongcomedy">RyanLongcomedy</a><a class="main-menu-item" href="/c/LeeCamp">LeeCamp</a><a class="main-menu-item" href="/c/PrimitiveSurvivalTools">PrimitiveSurvivalTools</a><a class="main-menu-item" href="/c/TheChrisSalcedoShow">TheChrisSalcedoShow</a><a class="main-menu-item" href="/c/FullMag">FullMag</a><a class="main-menu-item" href="/c/BitBoyCrypto">BitBoyCrypto</a><a class="main-menu-item" href="/c/Komando">Komando</a><a class="main-menu-item" href="/c/TheMagicMatt">TheMagicMatt</a><a class="main-menu-item" href="/c/TheKevinRobertsShow">TheKevinRobertsShow</a><a class="main-menu-item" href="/c/TheInfoWarrior">TheInfoWarrior</a><a class="main-menu-item" href="/c/DirtyMoney">DirtyMoney</a><a class="main-menu-item" href="/c/UpperEchelonGamers">UpperEchelonGamers</a><a class="main-menu-item" href="/c/TripleSgames">TripleSgames</a><a class="main-menu-item" href="/c/BrainyDose">BrainyDose</a><a class="main-menu-item" href="/c/worldnomactravel">worldnomactravel</a><a class="main-menu-item" href="/c/TylerFischer">TylerFischer</a><a class="main-menu-item" href="/c/Geometryptamine">GeometryTrip</a><a class="main-menu-item" href="/c/OwnagePranks">OwnagePranks</a><a class="main-menu-item" href="/c/LockPickingLawyer">LockPickingLawyer</a><a class="main-menu-item" href="/c/HikeCampClimb">HikeCampClimb</a><a class="main-menu-item" href="/c/NickSearcy">NickSearcy</a><a class="main-menu-item" href="/c/ReviewTechUSA">ReviewTechUSA</a><a class="main-menu-item" href="/c/Rengawr">Rengawr</a><a class="main-menu-item" href="/c/lifeinthe1800s">lifeinthe1800s</a><a class="main-menu-item" href="/c/MarkandMattis">MarkandMattis</a><a class="main-menu-item" href="/c/GabePoirot">GabePoirot</a><a class="main-menu-item" href="/c/Backfire">Backfire</a><a class="main-menu-item" href="/c/realpatriotgames">realpatriotgames</a><a class="main-menu-item" href="/c/RobsAquaponics">RobsAquaponics</a><a class="main-menu-item" href="/c/tateconfidential">tateconfidential</a><a class="main-menu-item" href="/c/JoshuaPhilipp">JoshuaPhilipp</a><a class="main-menu-item" href="/c/Epimetheus">Epimetheus</a><a class="main-menu-item" href="/c/RumbleEvents">RumbleEvents</a><a class="main-menu-item" href="/c/robbraxman">robbraxman</a><a class="main-menu-item" href="/c/LofiGirl">LofiGirl</a><a class="main-menu-item" href="/c/usefulidiots">usefulidiots</a><a class="main-menu-item" href="/c/JedediahBilaLive">JedediahBilaLive</a><a class="main-menu-item" href="/c/ValuetainmentShortclips">ValuetainmentShortclips</a><a class="main-menu-item" href="/c/Valuetainment">Valuetainment</a><a class="main-menu-item" href="/c/TateSpeech">TateSpeech</a><a class="main-menu-item" href="/c/CobraTate">CobraTate</a><a class="main-menu-item" href="/c/SailingZatara">SailingZatara</a><a class="main-menu-item" href="/c/DrJohnCampbell">DrJohnCampbell</a><a class="main-menu-item" href="/c/theoriesofeverything">theoriesofeverything</a><a class="main-menu-item" href="/c/BeyondScience">BeyondScience</a><a class="main-menu-item" href="/c/RandyBooker">RandyBooker</a><a class="main-menu-item" href="/c/AIRCLIPScom">AIRCLIPScom</a><a class="main-menu-item" href="/c/ScaryInteresting">ScaryInteresting</a><a class="main-menu-item" href="/c/JasonCorey">JasonCorey</a><a class="main-menu-item" href="/c/BohoBeautiful">BohoBeautiful</a><a class="main-menu-item" href="/c/PBDPodcast">PBDPodcast</a><a class="main-menu-item" href="/c/TheCrazyChannel">TheCrazyChannel</a><a class="main-menu-item" href="/c/TheHungryHussey">TheHungryHussey</a><a class="main-menu-item" href="/c/InteractiveBiology">InteractiveBiology</a><a class="main-menu-item" href="/c/stevewilldoit">stevewilldoit</a><a class="main-menu-item" href="/c/FRIGA">FRIGA</a><a class="main-menu-item" href="/c/DreDrexler">DreDrexler</a><a class="main-menu-item" href="/c/YOUCAR">YOUCAR</a><a class="main-menu-item" href="/c/JeremyLynch">JeremyLynch</a><a class="main-menu-item" href="/c/TannerBraungardt">TannerBraungardt</a><a class="main-menu-item" href="/user/RepMattGaetz">RepMattGaetz</a><a class="main-menu-item" href="/user/Libsoftiktok">Libsoftiktok</a><a class="main-menu-item" href="/user/TreasureHuntingWithJebus">TreasureHuntingWithJebus</a><a class="main-menu-item" href="/user/TheSCraft">TheSCraft</a><a class="main-menu-item" href="/user/andyh1202">andyh1202</a><a class="main-menu-item" href="/user/HybridCalisthenics">HybridCalisthenics</a><a class="main-menu-item" href="/user/OwnagePranks">OwnagePranks</a><a class="main-menu-item" href="/user/LockPickingLawyer">LockPickingLawyer</a><a class="main-menu-item" href="/user/lifeinthe1800s">lifeinthe1800s</a><a class="main-menu-item" href="/user/HumbleMechanic1">HumbleMechanic1</a><a class="main-menu-item" href="/user/VitalyTheGoat">VitalyTheGoat</a><a class="main-menu-item" href="/user/ViralHog">Viral Hog</a> </div>
<div class="hover-menu header-upload-menu">
<a class="main-menu-item" href="/upload.php"><svg class="main-menu-icon" viewbox="0 0 26 26"><path d="M4.2 17.5s-2.7-3.1-1.9-7.1C3 6.8 5.9 3.9 9.9 3.9c3.5 0 5.1 1.6 6.2 2.7 1.1 1.1 1.4 3.5 1.4 3.5s2.7-.7 4.4.7 2.4 3.8 1.8 5.6-2.6 3.1-2.6 3.1M9 17.1l4.1-3.8 4.2 3.8m-4.2 5.4v-9.2" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg>Upload Video</a>
<a class="main-menu-item" href="/live?go-live"><svg class="main-menu-icon" viewbox="0 0 30 16" width="20"><path d="M8 4a8 8 0 0 0 0 8M4 1a14 14 0 0 0 0 14m18-3a8 8 0 0 0 0-8m4 11a14 14 0 0 0 0-14" fill="none" stroke-linecap="round" stroke-width="2"></path><circle cx="15" cy="8" fill="none" r="2" stroke-width="4"></circle></svg>Go Live</a>
</div>
</div>
</nav>
<footer class="footer">
<div class="constrained">
<nav class="footer-nav">
<a class="footer-nav-link" href="//help.rumble.com/" rel="noopener" target="_blank">Developers</a>
<a class="footer-nav-link" href="/our-apps/" rel="noopener">Our Apps</a>
<a class="footer-nav-link" href="//corp.rumble.com/" rel="noopener" target="_blank">About Us</a>
<a class="footer-nav-link" href="//corp.rumble.com/careers/" rel="noopener" target="_blank">Careers</a>
<a class="footer-nav-link" href="//ads.rumble.com/" rel="noopener" target="_blank">Advertising</a>
</nav>
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
<div class="news_notification">
<a class="news_notification_a" href="//corp.rumble.com" target="_blank">
<strong>BREAKING</strong>: Rumble is now public &amp; listed on Nasdaq as <strong>$RUM</strong>
</a>
<button class="news_close" title="Dismiss the notification" type="button">
<svg class="news_close-x" height="24" viewbox="0 0 24 24" width="24"><path d="m5 5 14 14m0-14L5 19" fill="none" stroke-width="3"></path></svg> </button>
</div>
<script>$$={query:function(e,n){return Array.isArray(e)&&(n=e[1],e=e[0]),n=n||document,"string"==typeof e?n.querySelectorAll(e):[e]},each:function(e,n){for(var t=0;t<e.length;t++)n.call(e[t])},gt:function(e){return(new Date).getTime()/(e?1e3:1)},getByClass:function(e){var n=$$.query("."+e);return 1<=n.length&&n[0]},isVisible:function(e){return 0<e.offsetWidth&&0<e.offsetHeight},addClass:function(e,n){return!e.classList.contains(n)&&(e.classList.toggle(n),!0)},removeClass:function(e,n){e.classList.remove(n)},addClick:function(e,t){var n,r=$$.query(e);if(r)for(n=0;n<r.length;n++)r[n]&&r[n].addEventListener("click",function(e){var n=t.call(this,e);return n||void 0===n||e.stopPropagation(),n})},addServiceClick:function(e,n,t,r,c){$$.addClick(e,function(e){e.preventDefault(),$$.serviceGet(n,t,r,c)})},urlQueryObject:function(){var t={};return"undefined"==typeof URLSearchParams||new URLSearchParams(location.search).forEach(function(e,n){t[n]=e}),t},urlEncodeData:function(e){var n,t="";for(n in e)e.hasOwnProperty(n)&&(t+=(t?"&":"")+encodeURIComponent(n)+"="+encodeURIComponent(e[n]));return t},include:function(e,n){var t=document.createElement("script");t.src=e,t.async=!0,n&&(t.onload=n),document.head.appendChild(t)},includeCSS:function(e){var n=document.createElement("link");n.type="text/css",n.rel="stylesheet",n.href=e,document.head.appendChild(n)}},$$.page_load_time=(new Date).getTime();

$$.injectJSLib=function(e,t){var s=document.createElement("script");return s.defer=!0,s.text=t,"code"!=e&&(s.id="js-"+e,$$.includedJSLibs[e]=s),document.getElementsByTagName("head")[0].appendChild(s),s},$$.injectCSSLib=function(e,t){var s=document.createElement("style");return s.appendChild(document.createTextNode(t)),e&&(s.id="css-"+e,$$.includedCSSLibs[e]=s),(t=document.querySelector("head .js-theme-ss"))?t.insertAdjacentElement("beforebegin",s):document.getElementsByTagName("head")[0].appendChild(s),s},$$.request=function(e,t,s,n){var i=new XMLHttpRequest;n=n||function(){},i.open(t?"POST":"GET",e,!0),i.setRequestHeader("Content-type","application/x-www-form-urlencoded"),i.responseType="json",i.onload=function(){200==i.status?s(i.response):n&&n(i.status,i.response)},i.send(t?$$.urlEncodeData(t):null)},$$.requestGet=function(e,t,s){return $$.request(e,0,t,s)},$$.requestPost=function(e,t,s,n){return $$.request(e,t,s,n)},$$.serviceGet=function(e,t,s,n){return $$.serviceLoad("get",e,t,s,n)},$$.servicePost=function(e,t,s,n){return $$.serviceLoad("post",e,t,s,n)},$$.serviceLoad=function(i,c,o,r,e){"object"==typeof i&&(c=i.name||c,o=i.data||o,r=i.success||r,e=i.fail||e,i=i.type);var t,s,n=Math.floor(1e3*Math.random()),$="__service"+((new Date).getTime()-$$.page_load_time)+"_"+n,d=[],l=[],n="/service.php?",u={};for(s in"post"==i?"object"==typeof o&&(o.get||o.post)&&(t=o.get,o=o.post):o&&(t=o),(t=$$.urlEncodeData(t))&&(n+=t+"&"),u.name=c,$$.includedJSLibs)d.push(s);for(s in 0<d.length&&(u.included_js_libs=d.join(",")),$$.includedCSSLibs)l.push(s);0<l.length&&(u.included_css_libs=l.join(","));function a(e){var t,s,n="";if(e.js_libs){for(t in e.js_libs)e.js_libs.hasOwnProperty(t)&&$$.injectJSLib(t,e.js_libs[t]);delete e.js_libs}if(e.css_libs){for(t in e.css_libs)e.css_libs.hasOwnProperty(t)&&$$.injectCSSLib(t,e.css_libs[t]);delete e.css_libs}e.html&&((s=document.createElement("div")).innerHTML=e.html,e.html=1<s.childNodes.length?s:s.firstChild),e.request={type:i,name:c,data:o},$$[$]=e,$$[$].close=function(){this.html&&this.html.remove(),this.script.remove(),delete $$[$]},e.js_code&&(n="$$."+$+".call=function(){"+e.js_code+"};$$."+$+".call();"),r&&(e.success=r,n+="$$."+$+".success();"),n&&($$[$].script=$$.injectJSLib("code",n))}n+=$$.urlEncodeData(u),"post"==i?$$.requestPost(n,o,a,e):$$.requestGet(n,a,e)};

!function(){var i=[];$$.onload=function(t){if("object"!=typeof i)return t();i.push(t)},window.addEventListener("load",function(){for(var t=i,n=i=0;n<t.length;n++)t[n]()});var e=[];$$.onDomReady=function(t){if("object"!=typeof e)return t();e.push(t)},window.addEventListener("DOMContentLoaded",function(){for(var t=e,n=e=0;n<t.length;n++)t[n]()});var o=[];$$.onScroll=function(t,n){if(void 0===n&&(n=10),0==o.length){function i(){var n=$$.ui.scrollY();$$.each(o,function(){var t=this.last-n;t<this.step&&t>-this.step||(this.last=n,this.f())})}window.addEventListener("scroll",i),setTimeout(function(){i()},25)}o.push({f:t,step:n,last:2*-n})};var c=[];$$.checkVisibility=function(t,n){n=n||0;var i=window.innerHeight||document.documentElement.clientHeight,e=t.getBoundingClientRect(),o=[-n,i+n];return e.top>=o[0]&&e.top<=o[1]||e.bottom>=o[0]&&e.bottom<=o[1]},$$.onVisible=function(t,n,i){if($$.checkVisibility(t,i))return n.call(t);if(0==c.length){$$.onScroll(function(){$$.each(c,function(){$$.checkVisibility(this.elm,this.scan_ahead)&&(c.slice(c.indexOf(this),1),this.f.call(this.elm))})},50)}c.push({elm:t,f:n,scan_ahead:i})}}();

window.rumbleErrorHandler||function(){function d(r){var n=r.match(/http[s]?:\/\/[^\/]*rumble.com(\/.*)$/);return n?n[1]:r}var u=0;window.rumbleErrorHandler=function(r){var n,e,o,t,l=r.message,i=r.filename,c=r.lineno,a=r.colno,m=d(i);i==m||l.match(/^Script error\./)||3<++u||(e=document.location+"",n=[d(e),u,l,m,c,a],r.error&&r.error.stack&&n.push(r.error.stack.split("\n").slice(1,3).join("\n")),o="/l/jserr?err="+encodeURIComponent(JSON.stringify(n)),e==n[0]&&(o="https://rumble.com"+o),(t=document.createElement("img")).src=o,t.width=t.height=1,t.onload=t.onerror=function(){t.onload=null,t.onerror=null})},window.addEventListener("error",window.rumbleErrorHandler)}();

!function(e,n,t,o,c,f,a){e.fbq||(c=e.fbq=function(){c.callMethod?c.callMethod.apply(c,arguments):c.queue.push(arguments)},e._fbq||(e._fbq=c),(c.push=c).loaded=!0,c.version="2.0",c.queue=[],(f=n.createElement(t)).async=!0,setTimeout(function(){f.src="//connect.facebook.net/en_US/fbevents.js",(a=n.getElementsByTagName(t)[0]).parentNode.insertBefore(f,a)},50))}(window,document,"script"),fbq("init","459313920860148"),fbq("track","PageView");

$$.addClick('.media-subscribe', function(){ $$.serviceGet('user.login'); });
		$$.addClick('.locals-button',function(){
			$$.serviceGet('locals.community-details', {
				community_link_id: this.dataset.localsCommunity,
				context: this.dataset.context
			});
		});
!function(){var a=[];$$.togglePopShow=function(o,s){var t,e;if((s=s||[]).length){o.stopPropagation(),o.preventDefault();var n=s[0].classList.contains("pop-show");for(t=s.length;t--;)e=s[t],n?e.classList.remove("pop-show"):(e.classList.add("pop-show"),a.indexOf(e)<0&&a.push(e))}else for(e=o.target;e instanceof HTMLElement;){if(e.classList.contains("pop-show"))return;e=e.parentNode}for(t=a.length;t--;)e=a[t],s.indexOf(e)<0&&e.classList.remove("pop-show")},$$.addClick(window,function(o){$$.togglePopShow(o)})}();

$$.addClick('.main-menu-toggle', function(e) {
	$$.togglePopShow(e, [this, $$.query('#main-menu')[0]]);
})
$$.addServiceClick('.header-upload', 'user.login', {next: "/upload.php"});
$$.addClick('.header-search-submit',function(e){
	var i=$$.getByClass('header-search-field'),
		s=$$.getByClass('header-search-select'),
		v=i.value.trim();

	e.preventDefault();
	if(!$$.isVisible(i)){
		$$.togglePopShow(e, [i,s,$$.getByClass('header-search')]);
	}else{
		if ( v == "" ) {
			i.focus();
			return false;
		}

		var type = s.value.toLowerCase(),
			submit_button = e.target;

		if ( type == 'videos' ) {
			type = 'video';
		} else if ( type == 'channels' ) {
			type = 'channel';
		} else if ( type == 'user' ){
			submit_button.setAttribute("disabled", "");
			location = location.pathname + "?q="+encodeURIComponent(v);
			return false;
		}
		submit_button.setAttribute("disabled", "");
		location = "/search/" + type + "?q="+encodeURIComponent(v);
	}
	return false;
});
$$.user={"username":false,"logged_in":false};
addThemeSwitcher( '.js-theme-option' , '.js-theme-option-group' );
$$.addServiceClick('.header-user','user.login');
window.google_analytics_uacct='UA-44331619-1';
window.dataLayer=window.dataLayer||[];
function gtag(){dataLayer.push(arguments);}

gtag("js", new Date());
gtag("config","UA-44331619-1",{custom_map:{dimension1:"server",dimension2:"user",metric1:"prebid",metric2:"loadtime"},"server":"web11","user":"Guest",'transport_type':'beacon'});
gtag("event","web11",{"event_category":"ws","event_label":"US"});

$$.include('//www.googletagmanager.com/gtag/js?id=UA-44331619-1&ext=.js');
(function(){
var notification_el = $$.getByClass('news_notification');
var header_el = $$.getByClass('header');
var navs_el = $$.getByClass('navs');
var main_el = $$.query('body > main')[0];

var close_notify = function(){
	notification_el.style.display='none';
	header_el.style.top=0;
	navs_el.style.top='4rem';
	main_el.style.paddingTop='2rem';
	document.cookie="_nnc=3;path=/;max-age=2592000;secure;samesite";
};

$$.addClick('.news_close',function(){
	close_notify();
	window.removeEventListener('resize', move_layout);
	return false;
});

var move_layout = function() {
	var notification_height = notification_el.getBoundingClientRect().height;

	header_el.style.top = notification_height + 'px';
	navs_el.style.top = 'calc(4rem + ' + notification_height + 'px)';
	main_el.style.paddingTop = 'calc(2rem + ' + notification_height + 'px)';
}

move_layout();

window.addEventListener('resize', move_layout);
}());
$$.includedJSLibs={"main":1,"web_services":1,"events":1,"error":1,"facebook_events":1,"darkmode":1,"ui_header":1};$$.includedCSSLibs=[]</script> </body>
</html>
'''
RSP1 = '''
<!DOCTYPE html>

<html lang="en">
<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb#"><meta content="width=device-width,initial-scale=1" name="viewport"/><title>Amazon Sued for Selling "Suicide Kits" and the Allegations are HORRIFYING! Viva Clips</title><link href="https://rumble.com/v1onhfm-amazon-sued-for-selling-suicide-kits-and-the-allegations-are-horrifying-viv.html" rel="canonical"/><link href="https://connect.facebook.net" rel="dns-prefetch"/><link href="https://www.facebook.com" rel="dns-prefetch"/><link href="https://imasdk.googleapis.com" rel="dns-prefetch"/><link href="https://www.google-analytics.com" rel="preconnect"/><link crossorigin="" href="https://www.googletagservices.com" rel="preconnect"/><link crossorigin="" href="https://www.googletagmanager.com" rel="preconnect"/><link href="https://sp.rmbl.ws" rel="preconnect"/><style>html{
	background: #f3f3f7;
	color:#333;
	font: normal 14px/1.15 sans-serif;
	-webkit-text-size-adjust: 100%;
}
body, a, button, input, textarea, select, option, h1, h2, h3, address, ul, ol { margin: 0; padding: 0; color: inherit; font-family: inherit; font-weight: inherit; font-size: inherit; text-decoration: inherit; font-style: inherit; line-height: inherit; }
button, [type=button], [type=submit] { -webkit-appearance: button; cursor: pointer; background-color: transparent; border-style: none; }
ul, ol { list-style: none; }
label { cursor: pointer; }
a:hover{ text-decoration: underline; }
button{
	white-space:nowrap;
}
.h1 {
	font-size:2rem;
	line-height: 1;
	font-weight:normal;
	margin:0 0 1rem;
 	word-wrap: break-word;
	overflow-wrap: break-word;
}
small {
	font-size: 0.9rem;
	color: #666;
}
.verification-badge-icon {
	color: #fff;
	fill: #4C8800;
}
.themable-locals-icon {
	color: #421C52;
}

/* modifiers */
.content{
	background:#fff;
	padding:1rem;
}

.container{
	box-shadow:0 0 3px rgba(0,0,0,0.1);
	border-top:1px solid #e4e4e4;
	border-bottom:1px solid #e4e4e4;
	background:#fff;
}

.flex {
	display: flex;
}

.clear{
	clear:both;
}
.round-button{
	display: inline-flex;
	padding: 0.5rem 0.7rem;
	border-radius: 10rem;
	box-shadow: 0 1px 2px rgba(0,0,0,0.2);
	font-weight: 600;
	margin-left: 0.35rem;
	margin-right: 0.35rem;
	font-size: 1rem;
	text-transform: uppercase;
	opacity: 1;
	align-items: center;
}
.round-button:hover{
	text-decoration:none;
	opacity:0.85;
}
.round-button:disabled,
.round-button:disabled:hover {
	background: #999;
	cursor: default;
}
.bg-green{
	background: #4C8800;
	color:#fff;
}
.bg-green:hover,
.bg-green:focus-visible {
	background: #407200;
	opacity: 1;
}
.bg-blue{
	background: #37c;
	color:#fff;
}
.bg-blue:hover,
.bg-blue:focus-visible {
	background: #2A62A7;
	opacity: 1;
}
.bg-red{
	background:#b70000;
	color:#fff;
}
.bg-grey{
	background:#999;
	color:#fff;
}
.bg-white{
	background:#fff;
	color:#000;
}
.select-arrow-bg{
	-moz-appearance: none;
    -webkit-appearance: none;
    appearance: none;
	background-image:  url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 34 21'%3E%3Cpath d='M16.984 12.888L4.682 1.022.984 4.589l16 15.433 16-15.433-3.698-3.567z' /%3E%3C/svg%3E");
	background-repeat: no-repeat;
	background-position:  92% center;
	background-size: 8px;
}

/* layout columns */
.thirds{
	margin-left:-1rem;
	margin-right:-1rem;
}
.two-thirds, .one-thirds{
	width:100%;
	padding: 1.5rem 0;
	box-sizing:border-box;
}
.video-processing-error {
	background: #900;
	color: white;
	padding: 10px 20px
}main{
	padding:2rem 0;
}
.constrained{
	box-sizing:border-box;
	padding-left:1rem;
	padding-right:1rem;
}.theatre-mode {
	overflow-x: hidden;
}
.theatre-mode .header {
	box-shadow: none;
}
.theatre-mode main{
	padding-top: 0;
}
.theatre-mode #theatreVideoPlayer {
	position: relative;
	z-index: 0;
	background: #000;
	border-top: 1px solid #333;
    margin-left: calc(50% - 50vw);
    margin-right: calc(50% - 50vw);
    height: 85vh;
    box-shadow: 0 0 25px 0 rgb(0 0 0 / 25%);
    margin-bottom: 2rem;
}
.media-under-title{
	display:flex;
	align-items:center;
	margin-bottom:1rem;
}
.mediaList-list.related{
	max-width:500px;
	margin:0 auto;
}
.media-content,.media-sidebar{
	margin:0 -1rem;
}
.play-count{
	float: right;
	margin-top: 12px;
	font-size: 12px;
	margin-left:6px;
}
#sovrn_beacon {
	position: fixed;
}

#video-comments-loading {
	text-align: center;
	margin: 3rem 0;
	color: #666;
}

.loading-spinner {
	margin: 1rem auto;
	width: 2.5rem;
	height: 2.5rem;
	border: 0.5rem solid #ccc;
	border-top-color: #74a642;
	border-radius: 50%;
	animation: loading-spin 1s linear infinite;
}

@keyframes loading-spin {
	100% { transform: rotate(360deg) }
}i.user-image--img { display: inline-block; box-sizing: border-box; border: 1px solid #eee; border-radius: 50%; background-color: white; background-position: center; background-repeat: no-repeat; background-size: cover; }i.user-image--img--id-10513a0cac051f5c1e1d44020cad3a25 { background-image: url(https://sp.rmbl.ws/z0/V/u/q/b/Vuqba.asF.4-71v3-r79nct.jpeg); }.media-user-image{
	font-size: 3.4rem; width: 3.4rem; height: 3.4rem;
	position:absolute;
	left:0;
	top:0;
}
.media-by{
	float:left;
	position:relative;
	display:flex;
	height:3rem;
	align-items: center;
	font-size:1rem;
	min-width: 50%;
}
.media-by--a:hover { text-decoration: none; }
.media-by--a:hover .media-heading-name { text-decoration: underline; }
.media-by-wrap{
	margin-left:3.8rem;
	margin-top:5px;
	min-width: 0;
}
.media-heading-name{
	font-weight: 600;
	margin:0 0 -4px;
	display:inline-block;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
	max-width: 100%;
}
.media-heading-published{
	display:block;
}
.media-heading-title,.media-earnings{
	display:none;
}
.media-heading-verified {
	height: 16px;
	width: 16px;
	margin: 0 1px -2px 5px;
}.subscribe-button-count { margin-left: 0.5rem; font-weight:normal; opacity: 0.85; }button.locals-button {
	background: #e73348;
	color: #fff;
	padding-top: 0.25rem;
	padding-bottom: 0.25rem;
}

.locals-button:hover {
	background: #c6172c;
	opacity: 1;
}

button.locals-button svg {
	width: 20px;
	height: 20px;
	margin-left: 0.6rem;
}.media-icon-share{
	margin: -5px -1px -5px 4px;
	fill: #fff;
}
.media-engage{
	margin-left:auto;
	display: flex;
	justify-content: flex-end;
	flex-wrap: wrap;
	z-index:5;
	text-transform: uppercase;
}

.media-engage button {
	margin: 0.25rem 0 0.25rem 1rem;
}.rumbles-vote{
	display:flex;
	align-items:center;
	font-size:1rem;
	color:#666;
}
.rumbles-vote-up,.rumbles-vote-down{
	float:left;
	display:inline-block;
	padding:5px 8px;
	border:1px solid #ddd;
	background:#fff;
	line-height:0;
	border-radius:1rem 0 0 1rem;
	color:#999;
}
.rumbles-vote-up:hover,.rumbles-vote-down:hover{
	opacity:0.9;
	background:#eee;
}
.rumbles-vote-up.active,.rumbles-vote-down.active{
	background:#7a4;
	color:#fff;
}
.rumbles-vote-down{
	border-radius:0 1rem 1rem 0;
	margin-right:0.7rem;
	border-left:0;
}
.icon-rumbles-up,.icon-rumbles-down{
	stroke:currentColor;
	height:100%;
	width:auto;
	width:16px;
	height: 16px;
}
.rumbles-unit{
	display:none;
}.media-video-action{
	background:#fff;
	font-weight:normal;
	align-items:center;
	display:inline-flex;
}
.media-icon-license, .media-icon-embed{
	margin:-5px -4px -5px 4px;
	stroke:#444;
	stroke-width:1.3px;
}
.media-icon-license{
	margin-left:6px;
}.video-footer-buttons{
	justify-content:space-between;
	display:flex;
	align-items:center;
	margin:1rem;
}.media-description-break{
	margin:1rem 0;
	text-align:center;
	height:90px;
	display:flex;
	justify-content:center;
	align-items:center;
}p.media-description{
	font-size:1.3rem;
	line-height:2rem;
	margin:1rem 0;
	word-wrap: break-word;
	overflow-wrap: break-word;
}
div.media-description{
	padding-top:0;
	padding-bottom:0;
}
div.media-description-locals-message {
	display: flex;
	align-items: center;
	margin: 1em 0 1em 0;
	font-size: 1.15rem;
	line-height: 1.4;
}
div.media-description-locals-message.with-separator {
	padding-bottom: 1rem;
	border-bottom: 1px solid #e4e4e4
}
.media-description :any-link {
    color: #37c;
}
.media-description :any-link:hover {
    color: #2A62A7;
}.media-related-break{
	margin-bottom:1.5rem;
	height:280px;
	display:flex;
	justify-content:center;
	align-items:center;
}.mediaList-link-more {
	display: flex;
	justify-content: center;
	margin: auto 0 -2.2rem;
	padding-top: 1rem;
}

.mediaList-link-more a {
	display: block;
	border: 1px solid #ccc;
	text-decoration: none;
	text-align: center;
	padding: 0.35rem 1.35rem;
	border-radius: 10rem;
	text-transform: lowercase;
	background: #fff;
	color: #666;
}

.mediaList-link-more a:hover {
	background: #74a642;
	border-color: #74a642;
	color: #fff;
}.singleMedia.content{
	margin-top: -3.5rem;
	padding:0;
	border-top: none;
}
.mediaList-info.singleMedia{
	padding: 1rem 0;
}.mediaList-item{
	padding: 1rem 0;
	border-bottom: 1px solid #e4e4e4;
}
.mediaList-link {
	display: flex;
	overflow: hidden;
	align-items: center;
}
.mediaList-link:hover{
	text-decoration:none;
}
.mediaList-item.first-item{
	padding-top: 0;
}
.without-show-more-link .mediaList-item.last-item{
	padding-bottom: 0;
	border-bottom: none;
}
.mediaList-link.size-large,
.mediaList-link.size-xlarge {
	flex-direction: column;
	align-items: flex-start;
}
.mediaList-image-div{
	width: 50%;
	flex-shrink: 0;
	margin-right: 10px;
	position:relative;
	line-height: 0;
}
.mediaList-image-div.size-large,
.mediaList-image-div.size-xlarge{
	width: 100%;
	margin-right: 0;
}
.mediaList-image-div.size-small{
	width:35%;
}
.mediaList-image{
	width:100%;
}
.mediaList-heading{
	font-size: 1rem;
	font-weight: 600;
	margin: 0 0 0.5rem;
	line-height: 1.1rem;
	max-height: 2.2rem;
	overflow: hidden;
}
.mediaList-heading.size-xlarge {
	font-weight: normal;
	font-size: 2rem;
	line-height: 2.2rem;
	max-height: 2.2rem;
	margin-bottom: 1.5rem;
}
.mediaList-heading.size-large {
	margin-top: 7px;
	font-size: 1.2rem;
	line-height: 1.5rem;
	max-height: 1.5rem;
}
.mediaList-heading.size-xlarge,
.mediaList-heading.size-large {
	white-space: nowrap; display: block; text-overflow: ellipsis;
}
.mediaList-heading.size-medium, .mediaList-heading.size-small {
	max-height: 2.4rem;
	white-space: normal; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 2;
}
.mediaList-by{
	position:relative;
	display: flex;
	align-items: center;
}
.mediaList-by-image{
	font-size: 2rem; width: 2rem; height: 2rem;
	left:0;
	flex-shrink: 0;
	margin-right: 7px;
}
.mediaList-by-heading{
	font-weight:normal;
	margin:0;
	font-size:0.9rem;
	color: #666;
	display: inline;
}
.mediaList-rumbles,
.mediaList-earnings,
.mediaList-liveCount {
	display: block;
	color:#587F33;
}
.mediaList-liveCount {
  color: #e00;
}
.mediaList-by.size-small .mediaList-rumbles,
.mediaList-by.size-small .mediaList-earnings,
.mediaList-by.size-small .mediaList-liveCount{
	font-size: 0.8rem;
}
.mediaList-by.size-large .mediaList-earnings,
.mediaList-by.size-xlarge .mediaList-earnings,
.mediaList-by.size-large .mediaList-liveCount,
.mediaList-by.size-xlarge .mediaList-liveCount {
	display: inline;
}
.mediaList-timestamp::before,
.mediaList-plays::before,
.mediaList-by.size-large .mediaList-earnings::before,
.mediaList-by.size-xlarge .mediaList-earnings::before,
.mediaList-by.size-large .mediaList-liveCount::before,
.mediaList-by.size-xlarge .mediaList-liveCount::before {
	content: ' • ';
    padding-left: 5px;
    padding-right: 5px;
    color: #666;
}
.mediaList-duration,.mediaList-live,.mediaList-upcoming{
	position:absolute;
	bottom:7px;
	right:7px;
	color:#ddd;
	background:rgba(0,0,0,0.5);
	padding:1px 5px;
	font-size:0.8rem;
	line-height: initial;
}
.mediaList-duration {
	-webkit-backdrop-filter: blur(4px);
	backdrop-filter: blur(4px);
	border-radius: 4px;
	overflow: hidden; /* no blur outside of radius */
}
.mediaList-live{
	color:#fff;
	background:#e00;
	border-radius: 4px;
}
.mediaList-upcoming{
	background: #ec0;
	color: #000;
	border-radius: 4px;
}
.mediaList-info { width: 100%; box-sizing: border-box; }i.user-image--img--id-dadf98c2a02afc9e736c7475ea951a5e { background-image: url(https://sp.rmbl.ws/z8/1/B/t/e/1Btea.baa.1-russellbrand-riyofh.jpeg); }i.user-image--img--id-31a00d8df4b3fae640d78fc9f462ffa0 { background-image: url(https://sp.rmbl.ws/z8/n/T/H/b/nTHba.baa.1-NickMoseder-qw0e8q.webp); }i.user-image--img--id-fe04113a4b07e4cd4f4fa603894a1ea2 { background-image: url(https://sp.rmbl.ws/z8/E/L/1/e/EL1ea.baa-ArielleScarcella-r430uw.jpeg); }i.user-image--img--id-86e56c77ea0633fcab6007dfd1789de0 { background-image: url(https://sp.rmbl.ws/z8/o/G/5/d/oG5da.baa.1-MattKohrs-qxamnz.jpeg); }i.user-image--img--id-70db634516c9313989b962a0b4f4580c { background-image: url(https://sp.rmbl.ws/z8/R/A/Z/b/RAZba.baa-Dershow-qmfgfs.jpg); }i.user-image--img--id-fa96777532f14bd6caf72b34405cfada { background-image: url(https://sp.rmbl.ws/z8/8/M/z/f/8Mzfa.baa-RekietaLaw-r7j01x.png); }i.user-image--img--id-97757b4018e18228066e546df646ae1f { background-image: url(https://sp.rmbl.ws/z8/v/Q/m/b/vQmba.baa-TheQuartering-qtissd.jpeg); }i.user-image--img--id-5dc686f428fddd5aa0d369957bfa4edd { background-image: url(https://sp.rmbl.ws/z8/L/H/f/h/LHfha.baa-BeyondScience-rhej6k.jpeg); }i.user-image--img--id-65dcf4733ab3cc83d9d968c6544859a4 { background-image: url(https://sp.rmbl.ws/z8/t/2/j/c/t2jca.baa-AwakenWithJP-r80t3j.jpeg); }i.user-image--img--id-2ba0e3c10c20da045656187e99b50b7b { background-image: url(https://sp.rmbl.ws/z8/x/S/N/f/xSNfa.baa-BitcoinMagazine-r8wnw8.jpeg); }.header{
	position:fixed;
	top:0;
	left:0;
	width:100%;
	color:#ddd;
	background:#fff;
	height: 4rem;
	padding:0;
	z-index:200;
}
.header-div{
	display:flex;
	color:#fff;
	height:100%;
	padding-left: 1.2rem;
	padding-right: 1.2rem;
	align-items:center;
	position:relative;
}
.main-menu-toggle{
	display: flex;
	align-items: center;
	height:2.6rem;
}
.main-menu-close,.main-menu-open{
	stroke:#555;
	stroke-width:2px
}
.main-menu-close{
	display:none;
	stroke-width:3px
}
.pop-show>.main-menu-close{display:inline-block}
.pop-show>.main-menu-open{display:none}
.header-logo{
	width:10rem;
	margin-left: 1rem;
	margin-right: 0.2rem;
	display: flex;
	flex-shrink:0;
	align-items: center;
}
.header-logo img {
	width: 100%;
	height: auto;
}
.header-upload{
	box-sizing: border-box;
	border-radius:10rem;
	padding: 0 0.35rem;
	background: #4C8800;
	height:2.6rem;
	width:2.6rem;
	margin:0 1rem;
	display: flex;
	align-items: center;
}
.header-upload svg {
	stroke: #fff;
	width: 100%;
}
.header-upload-menu {
	display: none;
	right: 0;
}
.header-upload-menu.pop-show {
	display: block;
}
main {
	display: block;
	margin-top: 4rem;
}.header-search{
	display:flex;
	margin-left: auto;
	align-items:center;
	border-radius:10rem;
	background:#eee;
}
.header-search-select, .header-search-field {
	border:0;
	height:100%;
	background-color:transparent;
	font-size:1.1rem;
	color:#000;
	outline-offset: 3px;
}
.header-search-select:not(:focus-visible),
.header-search-field:not(:focus-visible) {
	outline: none;
}
.header-search-select {
    text-indent: 0.01px;
	width: 7rem;
	flex-shrink: 0;
	padding: 0 1.5rem 0 1rem;
}
.header-search-field{
	-webkit-appearance: textfield;
	border-left:1px solid #bbb;
	width:100%;
	padding:0 0.7rem;
}
.header-search-field::-webkit-search-decoration {
	-webkit-appearance: none;
}
.header-search-field::placeholder{
	color:#555;
}
.header-search-submit{
	height:2.9rem;
	width:2.9rem;
	padding:0.6rem;
	flex-shrink:0;
}
.header-search-select,.header-search-field{display:none}
.header-search-select.pop-show,.header-search-field.pop-show{
	display:block;
}
.header-search.pop-show{
	position:absolute;
	left: 3.5rem;
	right: 1.5rem;
	z-index:100;
}
.header-search-icon{
	stroke:#000;
	fill:#000;
}svg.user-image--icon { display: inline-block; box-sizing: border-box; border: 1px solid #eee; border-radius: 50%; background:#f3f3f7; stroke:#333; }.header-user-info{display:none;}
.header-user{
	text-align:left;
}
i.header-user-img, svg.header-user-img {
	display: block;
	flex-shrink: 0;
	font-size: 2.6rem; width: 2.6rem; height: 2.6rem;
	padding:0.35rem;
}.navs{
	position:fixed;
	top:4rem;
	width:100%;
	z-index:10;
}
.hover-menu{
	position:absolute;
	color:#222;
	background:#eee;
	box-shadow:0 0 20px 0 rgba(0,0,0,0.4);
	width:16rem;
	padding: 0.5rem 0;
	font-size:1.15rem;
	box-sizing: border-box;
	max-height: calc(100vh - 4rem - (1rem + 4vh));
	overflow: hidden auto;
}
#main-menu{
	display:none;
}
#main-menu.pop-show{
	display:block;
	left: 0;
	width: auto;
	min-width: 15rem;
	max-width: 18rem;
}.main-menu-item{
	display:block;
	padding: 0.3rem 1rem 0.5rem;
	outline-offset: -3px;
	max-width: 100%;
	overflow: hidden;
	text-overflow: ellipsis;
}
.main-menu-item-important{
	color:#f99;
}
.main-menu-item:hover{
	opacity:0.7;
	text-decoration:none;
}
.main-menu-heading{
	font-size:1rem;
	font-weight:bold;
	text-transform: uppercase;
	border-top:1px solid #666;
	padding: 1.2rem 1rem 0.8rem;
	margin: 0.9rem 0 0 0;
	cursor: default;
}
:any-link > .main-menu-heading {
	cursor: pointer;
}
.main-menu-icon{
	width:1.8rem;
	height:1.8rem;
	margin:0 0.5rem -0.5rem 0;
	stroke:#000;
	stroke-width:2px;
	stroke-linejoin:round;
	stroke-linecap:round;
	fill:none;
}

.main-menu-item--active {
	background: #555;
	color: #eaeaea;
	cursor: default;
}
.main-menu-item--active .main-menu-icon {
	stroke: currentColor;
}
.main-menu-item--active:hover {
	opacity: 1;
}

.main-menu-signout {
	border-top:1px solid #666;
	padding: .8rem 0 .8rem 2.1rem;
	margin: 0.2rem 0 0;
	text-align: center;
	padding: 0.8rem 0.4rem 0.4rem;
}.footer{
	clear: both;
	background: #111;
	color:#ddd;
	padding-top: 3rem;
	padding-bottom: 3rem;
}
.footer-nav{
	display: flex;
	flex-wrap: wrap;
	margin-bottom: 2rem;
	text-transform: uppercase;
}
.footer-nav-link,
.footer-terms-link {
	margin-right: 1rem;
	margin-bottom: 0.5rem;
	display: block;
	color:#ddd;
}
.footer-nav-link:hover,
.footer-terms-link:hover {
	color: #85C742;
}
.footer-nav-link:focus-visible,
.footer-terms-link:focus-visible {
  text-decoration: underline;
  outline: none;
}
.footer-terms-copyright {
	align-items: center;
}
.footer-terms{
	display: flex;
	flex-wrap: wrap;
}
.footer-copyright {
	margin-top: 2rem;
	margin-bottom: 0;
	color: #aaa;
}.news_notification{
	position:fixed;
	top:0;
	width:100%;
	background: #85C742;
	z-index:1000;
	padding: 0.5rem 0;
	display:flex;
	align-items: center;
	justify-content: center;
	color: #061726;
}
.news_notification_a{
	width:100%;
	box-sizing:border-box;
	padding:0 2.1rem 0 0.5rem;
	text-align:center;
}
.news_close {
	cursor: pointer;
	position: absolute;
	right: 0;
	top: 0;
	bottom: 0;
	padding: 0 .7rem;
	display: flex;
	align-items: center;
}
.news_close-x {
	width: 0.8rem;
	height: 0.8rem;
	padding: 0.2rem;
	background: rgba(255,255,255,0.5);
	border-radius: 100%;
	stroke: #333;
}
.news_close:hover .news_close-x  {
	background:rgba(255,255,255,0.75);
}@media(max-width:699.95px){.desktop-only{
	display:none
}.mediaList-heading.size-xlarge {
	max-height: 4.4rem;
	white-space: normal; overflow: hidden; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 2;
}}@media(min-width:460px){.rumbles-unit{
	display:inline;
}}@media(min-width:700px){.mobile-only{
	display:none
}.h1 {
	font-size:2.6rem;
	line-height: 1.25;
	margin:1rem 0 1.8rem;
}
.thirds{
	display: flex;
	flex-wrap: wrap;
}
.two-thirds, .one-thirds{
	display: flex;
	flex-direction: column;
	width:33.333333333%;
	padding-left: 1rem;
	padding-right: 1rem;
}
.two-thirds{
	width:66.666666667%;
}
.container{
	border-left:1px solid #e4e4e4;
	border-right:1px solid #e4e4e4;
}
.round-button{
	padding:0.85rem 1.3rem;
	margin-left: 0.5rem;
	margin-right: 0.5rem;
	font-size:1rem;
}.media-under-title{
	margin-bottom:2rem;
}.media-user-image{
	font-size: 3.4rem; width: 3.4rem; height: 3.4rem;
}
.media-by{
	font-size:1.2rem;
	height:3.4rem;
}
.media-heading-title,.media-heading-info{
	display:inline-block;
}
.media-by-wrap{
	margin-top:0
}
.media-heading-info:before{
	content:"\00B7";
	padding:0 8px 0 2px;
	font-weight:bold;
	color:#aaa;
	display:inline-block;
}
.media-earnings{
	color:#7a4;
	font-weight:bold;
	clear:left;
	display:block;
}button.locals-button svg {
	width: 24px;
	height: 24px;
}.media-engage button {
	margin-left: 0.5rem;
	margin-right: 0.5rem;
}.media-video-action{
	font-size:1.1rem;
}.video-footer-buttons{
	margin:1rem 0;
}.media-related-break{
	margin-bottom:2rem;
}.mediaList-list.top-earners {
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	height: 100%;
}.singleMedia.content{
	margin-top: 0;
	height: 100%;
}.header-upload{
	margin-left: auto;
	margin-right: 1.2rem;
}.header-search-select,.header-search-field{display:block}
.header-search,.header-search.pop-show{
	position:static;
	box-sizing: border-box;
	padding-left: 0.3rem;
	padding-right: 0.3rem;
	width: 40%;
	margin-left: 2.5rem;
	margin-right: 2.5rem;
}.header-user{
	width:9rem;
	display: flex;
	align-items: center;
}
.header-user-name,.header-user-stat{
	display:block;
	color:#555;
}
.header-user-name{
	color:#000;
	padding:0.1rem 0 0.1rem;
}
.header-user-info{
	display:inline-block;
	margin-left:0.5rem;
}.footer {
	padding-top: 2rem;
	padding-bottom: 4rem;
}
.footer-nav-link{
	margin-right: 3rem;
	margin-bottom: 0;
}
.footer-terms-link {
	margin-right: 0;
	margin-bottom: 0;
}
.footer-terms-copyright {
	display: flex;
}
.footer-terms{
	order: 2;
}
.footer-terms-link.divider::after{
	content: ' | ';
	display:inline-block;
	color: #666;
	padding-left: 10px;
	padding-right: 10px;
}
.footer-copyright {
	margin-top: 0;
	margin-right: 3rem;
}}@media(min-width:900px){.media-content,.media-sidebar{
	float:left;
	margin:0;
}
.media-content{
	width:calc(100% - 350px);
	padding-right:14px;
}
.media-sidebar{
	width:336px;
}}@media(min-width:1200px){.constrained{
	max-width:1200px;
	width:100%;
	margin:0 auto;
}.singleMedia .mediaList-image {
	height: 28rem;
	object-fit: cover;
}}</style><script>var $$={};var addThemeSwitcher;!function(){var c,r,s="system",i="light",h="dark",l=[h],o=[s,i,h],d=matchMedia("(prefers-color-scheme: dark)"),a=!1,m=!0,n=[],t=[];function u(){try{if(!a&&localStorage)return localStorage.getItem("themePreference")}catch(e){a=!0}}function f(){t.forEach(function(e){e(r)})}function $(){var e,t,a,n;c=c||u()||s,e=c==s?d.matches?h:i:0<=o.indexOf(c)?c:i,r!==(e=e)&&(r=e,l.indexOf(e)<0?(a=document.querySelectorAll("head .js-theme-ss"),Array.prototype.forEach.call(a,function(e){e.disabled=!0})):(t=!1,a="/c/themes/"+e+".css",n="js-theme-ss js-theme-ss--"+e,e=document.querySelectorAll(".js-theme-ss--"+e),Array.prototype.forEach.call(e,function(e){e.disabled=!1,e.dataset.themeMainStylesheet&&(t=!0)}),t||(m?document.write('<link rel=stylesheet data-theme-main-stylesheet="1" class="'+n+'" href="'+a+'" />'):((e=document.createElement("link")).rel="stylesheet",e.href=a,e.className=n,e.dataset.themeMainStylesheet="1",document.head.appendChild(e))))),f()}function y(){$$.each(n,function(){var e=this.getAttribute("data-theme")==c;$$[(e?"add":"remove")+"Class"](this,"main-menu-item--active")})}function p(e,t){(t=e.getAttribute("data-theme"))&&n.indexOf(e)<0&&(n.push(e),$$.addClick(e,function(e){return e.preventDefault(),e=t,a||localStorage.setItem("themePreference",e),c!=e&&(c=e,$(),y()),$$.query(".main-menu-toggle")[0].click(),!1}))}addThemeSwitcher=function(e,t){$$.each($$.query(e),function(){p(this)}),y(),t&&$$.each($$.query(t),function(){this.style.display="block"})},c=u()||s,$(),m=!1,d.addEventListener&&d.addEventListener("change",function(e){$()}),$$&&($$.applyThemePreference=$,$$.registerThemeCallback=function(e){t.push(e)})}();

!function(s,d){function a(){return(new Date).getTime()/1e3}var t,r,o,n,i,c,l,e="Rumble",b={F:0};(d=s[e]=s[e]||function(){d._.push(arguments)})._=d._||[],b.f={},b.b={};if(!b.k){function f(o,e){return o.opts||(o.opts=[]),b.D(e,function(e,t){var r=o[t];switch(t){case"opts":o[t]=r.concat(e);break;case"ad_sys":o[t]=r?b.M(r,e):e;break;default:o[t]=e}}),o}function p(c,s,l){function u(){var e=c.v.src||c.v.currentSrc;return e=e.match(/blob:/)&&c.hls_js?c.hls_js.url||e:e}function f(){var e=u(),t=s.get();return c.current_video=s,t==e?0:t}var p;s.get=function(){return function(e,t){if(21192597==e.vid.vid)return t;var r,o=b.B(t),t=b.E(t);return e.vid.live||(r=0,e.vid.a&&(r=e.vid.a.u||0),o.u=r,o.b=0<e.bandwidth_track?1:0),t+"?"+b.C(o)}(c,s.url)};s.check=function(){return!f()},s.play=function(){l&&c.hls_js&&!p&&c.hls_js.startLoad(),p=!0},s.set=function(){if(l&&!b.I())return setTimeout(function(){s.set()},100),!1;var e,r,t,o,n,i=f(),d=0,a=0;i&&(p=!1,e=c.v,c.res=s.key,0<S&&(c.last_set_url==u()?(d=!e.paused,a=e.currentTime):0<c.video_time&&(a=c.video_time)),a&&!c.vid.live&&(c.ui.s.autoSeek=a),r=c,a=e,t=i,o=l&&Hls.isSupported(),r.hls_js&&r.hls_media_attached&&((n=r.hls_js).detachMedia(a),n.destroy(),r.hls_js=null),o?(n=r.hls_js=new Hls({capLevelToPlayerSize:!0,autoStartLoad:!1,manifestLoadingMaxRetry:6,levelLoadingMaxRetry:6}),r.j("hlsJsLoaded",n),n.on(Hls.Events.LEVEL_UPDATED,function(e,t){r.live=t.details.live}),n.loadSource(t),n.attachMedia(a),r.hls_media_attached=1):a.src=t,S++,c.last_set_url=i,e.load(),d&&(s.play(),e.play()))}}function g(e){return H.hasOwnProperty(e)?H[e]:e}function h(r,e,o){var n,t;if(!r.style&&r.length)for(t=0;t<r.length;t++)h(r[t],e,o);else b.D(e,function(e,t){n=g(t),o&&""!==r.style[n]||(r.style[n]=g(e))})}function v(){var e=G;G={},y=0,b.D(e,function(e){"function"==typeof e&&e()})}function m(e){var i,o={play:"#fff",scrubber:"#75a642",hover:"#fff",background:"#303030",hoverBackground:"#699c39"},d=this,n=-1,c=(b.D(e,function(e,t){d[t]=e}),d.hasima=1,d.hasInit=0,d.rpcl=(d.id?d.id+"-":"")+"Rumble-cls",d.rpcls="."+d.rpcl,d.bandwidth_track=0,{}),a=(d.addEvent=function(e,t,r){c[r=r||1]||(c[r]={}),c[r][e]||(c[r][e]=[]),c[r][e].indexOf(t)<0&&c[r][e].push(t);r="addEvent";e!=r&&d.j(r,e)},d.removeEvent=function(e,t,r){c[r=r||1][e]&&(r&&!t?c[r][e]=[]:(t=c[r][e].indexOf(t),c[r][e].splice(t,1)))},d.hasEventListener=function(r){return b.D(c,function(e,t){if(e[r]&&0<e[r].length)return!0})},d.j=function(r,o,n){var i,d,a=[];return b.D(c,function(e,t){if(e[r]&&(n&&n==t||!n))for(d=e[r],i=0;i<d.length;i++)"function"==typeof o&&(o=o()),a.push(d[i](o))}),a},d.triggerError=function(e,t){d.j("error",{code:e,message:t})},d.l1=function(e,t,r){},d.getSetting=function(e,t){var r=!1;return d.vid&&d.vid.player&&d.vid.player[e]&&(e=d.vid.player[e],t&&e[t]&&(r=e[t]),t||(r=e)),r=!r&&o[t]?o[t]:r},d.loadVideoStyles=function(e){var t,r,o,n="vid_"+d.vid.id;d.rpcls;d.p.id=n,d.vars.opts.title&&d.vid.title&&(i.innerHTML=d.vid.title,i.href=b.L(d.vid.l,"rumble.com"),b.w(i,{outline:0,display:"block",18:"linear-gradient(rgba(0,0,0,.7),rgba(0,0,0,0))",textShadow:"rgba(0,0,0,0.5) 0px 0px 2px",padding:"9px",fontSize:"18px",whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis",position:"absolute",top:0,left:0,right:0}),b.x(i,{textDecoration:"underline"},{textDecoration:"none"})),d.bp&&(n=d.getSetting("colors","play"),t=d.getSetting("colors","hover"),r=d.getSetting("colors","background"),o=d.getSetting("colors","hoverBackground"),b.x(d.bp,{color:t,background:o,borderColor:o},{color:n,background:r,borderColor:r},d.bp_svg),d.bp.style.opacity=1)},d.trackBandwidth=function(e){var t=d.bandwidth_track;(e=d.server.bw_tracking?e:0)!=t&&(d.bandwidth_track=e,d.current_video&&!d.m&&d.current_video.set())},d.loadVideo=function(e,t){var r,o=(e="object"!=typeof e?{id:e}:e).id;if(b.b[o]&&(d.vars.playlist||(d.vars.playlist=b.b[o]),o=b.b[o][0]),d.hasInit||(d.hasInit=1,b.c(["ui","custom_ui"],function(){for(var e=0;e<b.d.length;e++)b.d[e](d.id)})),!t)return b.e(o,function(){d.loadVideo(e,1)},{ad_count:d.ad_count||null});if(b.f[o].loaded<9){if(d.triggerError("load","Unable to load video "+o),t)throw"Unable to load video "+o;return 2}if(b.f[o].cfg=e,b.f[o].plays=0,(r=b.f[o]).restrict&&!a(r.restrict)&&(d.triggerError("restricted","Video is restricted"),b.f[o].restricted=!0,d.j("restricted",o),b.f[o].ua=0),r.id=o,d.vid=r,d.live=2==d.vid.live,d.video_list=0,d.current_video=0,n<0&&(n=(d.vars.opts.noads||d.server.bw_ourads_check&&d.vars.opts.norumbleads)&&r.a?1:0),d.trackBandwidth(r&&r.track||n?1:0),!r.restricted&&r.ua&&(d.video_list=b.G(d,r.ua),b.H(d),d.loadVideoStyles()),b.g(d),d.j("loadVideo",r),b.h(d,1),r.restricted&&t)throw"Video "+o+" is restricted"},function(e){var t,r,o,n,i=document,d=!1;if(!e||e[0]<=-3)return!0;r=e[0],o=e[1];try{t=parent!==s?i.referrer||parent.location.href:i.location.href}catch(e){}if(!t)return parent===s;if(t=t.match(/^https?\:\/\/([^\/?#]+)(?:[\/?#]|$)/i))for(t=t[1].split(".");2<=t.length&&!d;)n=t.join("."),-1<o.indexOf(n)&&(d=!0),t.shift();return r!=d}),e=d.rpcl,t="metadata";(d.vars.opts.minimal||d.vars.opts.nopreload)&&(t="none"),d.vars.quality&&(d.res=parseInt(d.vars.quality)),e=b.i('<div class="'+e+'" allowfullscreen tabindex="-1" style="outline: none;"><video muted playsinline hidefocus="hidefocus" style="width:100% !important;height:100% !important;display:block" preload="'+t+'"'+(d.vars.opts.cc?' crossorigin="anonymous"':"")+'></video><div style="display:flex;opacity:0" class="bigPlayUI ctp"><a style="display:none" target=_blank rel=noopener></a><div class="bigPlayUIInner ctp" style="display:none"></div></div></div>'),b.w(e,{2:4,9:17,10:17,18:16,color:15,clear:"both",overflow:"visible"}),b.j.c(e,"bplay","block",".bigPlayUIInner"),d.d.appendChild(d.p=e),d.v=e.firstChild,function(e){if(!b.A){var t,r="canPlayType",o='video/mp4; codecs="avc1.42E01E',n=[0,o+'"',0,o+', mp4a.40.2"',1,'video/webm; codecs="vp9, vorbis"',2,"application/vnd.apple.mpegurl"],i=[!1,!1,!1];if(!e||!e[r])return;for(t=0;t<n.length;t+=2)e[r](n[t+1])&&(i[n[t]]=!0);b.J=i[2],b.A=i}}(d.v),d.rsz=[0,0],d.bp=e.childNodes[1],d.bp_svg=d.bp.childNodes[1],d.hasStyle={},i=d.bp.childNodes[0],b.w(d.bp_svg,{fill:"currentColor",9:8,12:"14px 22px",cursor:"pointer",borderRadius:"8px"}),b.w(d.bp,{display:"flex",opacity:0,position:"absolute",top:0,left:0,width:"100%",height:"100%",cursor:"pointer",alignItems:"center",justifyContent:"center",overflow:"hidden"}),d.v.addEventListener("contextmenu",function(e){return e.preventDefault(),!1}),d.loadVideoStyles()}var _,S,y,P="https://rumble.com",e="/embedJS/u3",w=(b.l=a(),s.RumbleErrorHandler||(l=0,s.RumbleErrorHandler=function(e){var t,r=e.message,o=e.filename,n=e.lineno,i=e.colno,d=D(o);o==d||r.match(/^Script error\./)||3<++l||(o=document.location+"",r=[D(o),l,r,d,n,i],e.error&&e.error.stack&&r.push(e.error.stack.split("\n").slice(1,3).join("\n")),d="/l/jserr?err="+encodeURIComponent(JSON.stringify(r)),o==r[0]&&(d=P+d),(t=document.createElement("img")).src=d,t.width=t.height=1,t.onload=t.onerror=function(){t.onload=null,t.onerror=null})},s.addEventListener("error",s.RumbleErrorHandler)),[]),x=(b.E=function(e){return e.split("?")[0]},b.B=function(e){var e=e.split("?"),r={};return e&&e[1]&&(e=e[1],new URLSearchParams(e).forEach(function(e,t){r[t]=e})),r},b.C=function(e){var r="";return b.D(e,function(e,t){r+=(r?"&":"")+encodeURIComponent(t)+"="+encodeURIComponent(e)}),r},b.D=function(e,t){var r,o;for(o in e)if(e.hasOwnProperty(o)&&void 0!==(r=t(e[o],o)))return r},b.K=function(e,t){if("undefined"==typeof localStorageBlocked)try{localStorageBlocked="undefined"==typeof localStorage||!localStorage}catch(e){localStorageBlocked=!0}if(void 0===t){if(!localStorageBlocked)try{t=localStorage.getItem(e)}catch(e){localStorageBlocked=!0}return localStorageBlocked?w[e]:parseInt(t)==t?parseInt(t):t}if(w[e]=t,!localStorageBlocked)try{return localStorage.setItem(e,t)}catch(e){localStorageBlocked=!1}return!1},b.L=function(e,t,r,o){if(e)if(!e.match(/^(http[s]?:)?\/\/([^/]*)\//)||r)return(o?"https:":"")+"//"+t+("/"!=e[0]?"/":"")+e;return e},b.M=function(e,t){return e.filter(function(e){return-1!==t.indexOf(e)})},[2,0,1]),C=["mp4","webm","hls"],H=(b.G=function(r,e){for(var o,t,n={},i=S=0;i<x.length;i++)e[o=C[t=x[i]]]&&(b.A[t]||"hls"==o)&&b.D(e[o],function(e,t){n.hasOwnProperty(t)||(e.key=t,n[t]=e,p(r,n[t],"hls"==o))});return n},b.I=function(){return"undefined"!=typeof Hls||(b.q(["hls"]),!1)},b.H=function(e){var r,o,n,i=480;e.res&&(i=e.res),e.vid.live&&!b.J&&b.I(),b.D(e.video_list,function(e,t){n=parseInt(t),"hls"!=r&&("hls"==t&&b.J||0<n&&n<=i&&(!r||r<n)?r=t:(!o||n<o&&0<n)&&(o=t))}),(r=r||o)&&e.video_list[r].set()},b.r=function(){var d={},a={},c={b:function(e,t,r){if("object"!=typeof e){if(d[e]&&!r)return!1;if(d[e]=t=t||1,a[e])for(;o=a[e].pop();)o(e,t);return!0}for(var o in e)c.b(o,e[o],r)},a:function(e,t,r){var o,n,i;for(r=r||{},o=0;i=e[o];o++)d[i]?r[i]=d[i]:(n&&(t=function(t,r){return function(e){c.a([t],r,e)}}(n[0],n[1])),n=[i,t]);n?(a[n[0]]||(a[n[0]]=[]),a[n[0]].push(function(e,t){r[e]=t,n[1](r)})):t(r)}};return c},n=b.r(),i=document,c={},b.s=function(e,t){var r,o,n=0;c[e]||(c[e]=1,(r=i.createElement("script")).type="text/javascript",r.src=e,t&&(r.addEventListener("load",o=function(e){if(n||t())return n=1;e&&setTimeout(o,50)},!1),o(1)),i.head.appendChild(r))},b.q=function(e,t){for(var r,o=0;o<e.length;o++)if("ima3"==e[o])b.s("https://imasdk.googleapis.com/js/sdkloader/ima3.js",function(){return!("undefined"==typeof google||!google||!google.ima)&&(n.b("ima3"),!0)});else if("custom_ui"!=e[o]){r=e[o];b.s(d.s.rd+"/j/p/"+r+("hls"!=r?".r2":"")+".js?_v=330",t)}},b.c=function(e,t,r){n.a(e,t),r||b.q(e)},d.rl=function(e,t){n.b(e)&&t&&t(b)},[0,1,"position","absolute","relative","fixed","normal","none","auto","width","height","margin","padding","border","display","#FFF","#000","100%","background","opacity"]),k=(b.w=h,b.y=function(e){var r={};return b.D(e,function(e,t){r[g(t)]=g(e)}),r},b.t=function(e,t,r,o,n,i,d,a){o||(o=e,n=t);var c="0",s="0";return a&&a.viewbox_top&&(c=a.viewbox_top),a&&a.viewbox_left&&(s=a.viewbox_left),i=i?" RumbleSVG-"+i:"",d=d||"",0<r.indexOf("stroke")&&(d+="stroke:currentColor;"),[e,t,'<svg style="'+d+'" class="RumbleElm'+i+'" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="'+e+'px" height="'+t+'px" viewBox="'+s+" "+c+" "+o+" "+n+'">'+r+"</svg>"]},b.j=b.r(),b.j.c=function(t,r,o,n){b.j.a([r],function(e){n&&(t=t.querySelectorAll(n)[0]),b.z(t,e[r][2]),o&&("string"==typeof o?t.style.display=o:o.apply(t))})},'<path stroke-width="3" stroke-linejoin="round" d="M19 11L3.2 1.5v19z"/>'),B=(b.j.b({bplay:b.t(25,25,k,22,22,"bplay"),play:b.t(22,22,k,0,0,"play","height:100%;"),loader:b.t(80,10,function(){for(var e,t="<g>",r=0;r<21;r++)t+='<circle cx="'+(10*r+5)+'" cy="5" r="'+(e=(e=r-6)<1||5<e?1:e)+'" />';return t+"</g>"}(),80,10)}),s.requestAnimationFrame?1:0),G={},O=(b.a=function(e,t){if(!G[e]&&"function"==typeof t&&(G[e]=t,!y)){if(y=1,!B)return setTimeout(v,1e3/24);s.requestAnimationFrame(v)}},b.i=function(e){e=b.u("div",0,0,e);return 1<e.childNodes.length?e.childNodes:e.firstChild},b.u=function(e,t,r,o){e=document.createElement(e);return o&&(e.innerHTML=o),t&&(e.className=t),r&&(e.id=r),E(e),e},b.z=function(e,t){e.innerHTML=t,j(e)},b.y({font:"12px sans-serif",fontWeight:6,lineHeight:6,boxSizing:"content-box",webkitBoxSizing:"content-box",19:1,18:7,11:0,12:0,border:7,9:8,10:8,visibility:"visible",textSizeAdjust:8,textDecoration:7})),E=function(e){var t;(t=e.tagName)&&"path"!=(t=t.toLowerCase())&&"video"!=t&&(h(e,O,!0),"svg"==t?h(e,{fill:"currentColor"},!0):(h(e,{color:"inherit"},!0),j(e)))},j=function(e){var t,r;if(t=e.childNodes)for(r=0;r<t.length;r++)E(t[r])};b.x=function(e,t,r,o){var n="__playerHover";(o=o||e)[n]||(e.addEventListener("mouseout",function(){h(o,o[n][0])}),e.addEventListener("mouseover",function(){h(o,o[n][1])})),o[n]=[r,t],h(o,r)};b.d=[];d.s={rd:P,ru:e,ds:[],rp:P+e+"/?request=",server:{"bw_tracking":1,"bw_noads_check":1}};b.k={},d.gdpr=2,b.m=function(e,t,r,o){var n=new XMLHttpRequest;n.onreadystatechange=function(){4==n.readyState&&200==n.status&&t(JSON.parse(n.responseText))},n.open("GET",(o?"":d.s.rp)+e),n.send()},b.e=function(e,t,r){var o,n,i,d=[];for("object"!=typeof e&&(e=[e]),o=0;o<e.length;o++)n=e[o],(!b.f[n]||1<b.f[n].loaded&&b.f[n].loaded+(1==e.length?900:1800)<a())&&(b.f[n]={loaded:0,wait:[]}),0==(i=b.f[n]).loaded&&(d.push(n),i.loaded=1),t&&i.loaded<9&&i.wait.push(t);return 0<d.length?(r=r?"&ext="+encodeURIComponent(JSON.stringify(r)):"",r+="&ad_wt="+(b.K("ad_wt")||0),b.m("video&ver=2&v="+d[0]+r,function(e){var t,r,o=[],n={};for(e.loaded||!e?n[d[0]]=e:n=e,b.D(n,function(e,t){for(;r=b.f[t].wait.pop();)o.indexOf(r)<0&&o.push(r);e&&(b.f[t]=e,b.f[t].loaded=a())}),t=0;t<o.length;t++)o[t]()}),1):(t&&t(),0)},d.resize=function(){b.D(b.k,function(e){b.h(e)})},b.h=function(e,t){var r,o=!e.rsz,n=[e.p.clientWidth,e.p.clientHeight],i=s.innerHeight,d=e.vars;d.resize||(d.resize=function(){try{return s.self!==s.top}catch(e){return!0}}()?"full":"auto");(!o&&(e.rsz[0]!=n[0]||e.rsz[1]!=n[1])||n[1]>i||t)&&(t=d.resize,d.ia&&(t="ia"),e.ui&&e.ui.isFloating&&(t="auto"),r=Math.floor(n[0]/16*9),"ia"==t?screen&&screen.height<r&&(r=screen.height):"full"==t?r=0:"window"==t?r=i:("ctpauto"==t&&e.ui&&e.ui.ctp&&(d.resize="auto"),(i<r||e.ui&&e.ui.getFullScreen())&&(r=0)),"window"!=t&&"ctpauto"!=t&&"auto16:9"!=t&&"full"!=t&&(e.vid&&e.vid.a&&e.vid.a.aden&&e.vid.a.aden[2])&&r<360&&0!=r&&!d.float&&(r=360),e.rsz[0]!=n[0]&&(o=1),n[1]!=r&&(o=1,e.p.style.height=0<r?(n[1]=r)+"px":"100%")),e.rsz&&!o||(e.rsz=n),o&&(b.g(e),e.j("resize"))},b.g=function(e){if(!(!e.vid||e.ui&&e.ui.hasPlayed)){var t,r,o,n=e.vid.i,i=e.vid.t,d=-1,a=e.rsz[0],c=e.rsz[1],s=a/c;if(i)for(t=0;t<i.length;t++)o=s<(o=(r=i[t]).w/r.h)?(c-a/o)*a:(a-c*o)*c,(d<0||o<d)&&(d=o,n=r.i);e.v.poster!=n&&(e.v.poster=n)}},d.$play=function(e,t){var r,o,n=JSON.parse(JSON.stringify(d.s.ds)),i={};if((n=f(n,e)).opts&&(b.D(n.opts,function(e){i[e]=1}),n.opts=i),void 0===n.gdpr?n.gdpr=2:n.gdpr=n.gdpr?1:0,2!=n.gdpr&&(d.gdpr=n.gdpr),b.n=-1==n.analytics||n.opts.minimal?1:0,b.o=n.opts.skip_ga_load?1:0,b.p=n.opts.force_ga_load?1:0,!n.div){if(!_)throw"No div was defined for the player";n.div=_}if(_=o=n.div,!b.k[o]||(r=b.k[o]).d.parentNode||(r=0),n.macros||(n.macros={}),!r){if(!(r=document.getElementById(o))){if(2<t)throw o+" div not found";s.addEventListener("DOMContentLoaded",function(){d.$play(e,3)})}b.k[o]||b.F++,b.k[o]=r=new m({d:r,vid:0,id:o,vars:n,server:d.s.server})}r.loadVideo(n.video),b.h(r)};d.rl("custom_ui");d.$playSettings=function(e){d.s.ds=f(d.s.ds,e)},s.addEventListener("resize",function(){b.a("resize",d.resize)}),s.addEventListener("orientationchange",function(){setTimeout(function(){d.resize()},500)});var z,L,I,R=s.Rumble;for(R._=z=R._||[],z.push=function(e){var t=z.slice.call(e),r=R["$"+t.shift()];"function"==typeof r?r.apply(R,t):t.push.call(z,e)},L=-1,I=z.length;++L<I;)z.push(z.shift())}function D(e){if(!e)return e;var t=e.match(new RegExp("http[s]?://[^/]*rumble.com(/.*)$"));return t?t[1]:e}}(window);

</script><script type="application/ld+json">[{"@context":"http://schema.org","@type":"VideoObject","name":"Amazon Sued for Selling 'Suicide Kits' and the Allegations are HORRIFYING! Viva Clips","playerType":"HTML5","description":"The allegations of this lawsuit will break your heart and hurt your soul.","thumbnailUrl":"https://sp.rmbl.ws/s8/6/c/q/N/e/cqNeg.4Wpjb.jpg","uploadDate":"2022-10-19T02:17:53+00:00","duration":"PT00H07M35S","embedUrl":"https://rumble.com/embed/v1m1bmu/","url":"https://rumble.com/v1onhfm-amazon-sued-for-selling-suicide-kits-and-the-allegations-are-horrifying-viv.html","interactionStatistic":{"@type":"InteractionCounter","interactionType":{"@type":"http://schema.org/WatchAction"},"userInteractionCount":137},"width":1920,"height":1080,"videoQuality":"Full HD"},{"@context":"http://schema.org","@type":"WebSite","url":"https://rumble.com/","potentialAction":{"@type":"SearchAction","target":"https://rumble.com/search/video?q={search}","query-input":"required name=search"}},{"@context":"http://schema.org","@type":"Organization","name":"Rumble","url":"https://rumble.com/","logo":"https://rumble.com/i/rumble_logo_back.png","sameAs":["https://www.facebook.com/rumblevideo/","https://twitter.com/rumblevideo"]}]</script><meta content="The allegations of this lawsuit will break your heart and hurt your soul." name="description"/><meta content="Rumble" property="og:site_name"/><meta content="video.other" property="og:type"/><meta content='Amazon Sued for Selling "Suicide Kits" and the Allegations are HORRIFYING! Viva Clips' property="og:title"/><meta content="https://rumble.com/v1onhfm-amazon-sued-for-selling-suicide-kits-and-the-allegations-are-horrifying-viv.html" property="og:url"/><meta content="The allegations of this lawsuit will break your heart and hurt your soul." property="og:description"/><meta content="https://sp.rmbl.ws/s8/6/c/q/N/e/cqNeg.4Wpjb.jpg" property="og:image"/><meta content="summary_large_image" name="twitter:card"/><meta content="https://sp.rmbl.ws/s8/6/c/q/N/e/cqNeg.4Wpjb.jpg" name="twitter:image"/><meta content='Amazon Sued for Selling "Suicide Kits" and the Allegations are HORRIFYING! Viva Clips' name="twitter:title"/><meta content="The allegations of this lawsuit will break your heart and hurt your soul." name="twitter:description"/><meta content="155223717937973" property="fb:app_id"/><meta content="@rumblevideo" name="twitter:site"/><meta content="app-id=1518427877" name="apple-itunes-app"/><link href="/i/favicon-v4.png" rel="shortcut icon"/><link href="/apple-touch-icon.png" rel="apple-touch-icon"/></head> <body>
<main>
<div class="constrained">
<article><div id="theatreVideoPlayer"></div><h1 class="h1">Amazon Sued for Selling "Suicide Kits" and the Allegations are HORRIFYING! Viva Clips</h1><div class="media-under-title"> <div class="media-by">
<div class="media-by-wrap">
<a class="media-by--a" href="/user/vivafrei" rel="author">
<i class="user-image user-image--img user-image--img--id-10513a0cac051f5c1e1d44020cad3a25 media-user-image"></i> <span class="media-heading-name">vivafrei<svg class="verification-badge-icon media-heading-verified" height="24" viewbox="0 0 24 24" width="24"><circle cx="12" cy="12" r="12"></circle><path d="M5.4 11.1l5 5 8.2-8.2" fill="none" stroke="currentColor" stroke-miterlimit="10" stroke-width="2"></path></svg></span>
</a>
<span class="media-heading-info media-heading-published"><span class="media-heading-title">Published </span> October 18, 2022</span>
<span class="media-heading-info">137 Views</span>
</div>
</div>
<div class="media-engage">
<button class="round-button media-subscribe bg-green" data-action="subscribe" data-slug="vivafrei" data-title="vivafrei" data-type="user">
<span class="subscribe-button-label">Subscribe</span>
</button>
<button class="round-button locals-button" data-context="video" data-locals-community="252318154180013735">
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
<button class="round-button media-engage-share desktop-only bg-blue">Share<svg class="media-icon-share" height="18" viewbox="0 0 24 24" width="18"><path d="M18.7 16c-1 0-2 .5-2.7 1.2l-5-3.1c0-.4.1-.7.1-1.1 0-.4-.1-.7-.2-1.1l5-3.1c.8.7 1.7 1.2 2.8 1.2 2.1 0 3.8-1.8 3.8-4s-1.7-4-3.8-4c-2.1 0-3.8 1.8-3.8 4 0 .4.1.7.2 1.1L10 10.2C9.3 9.5 8.3 9 7.3 9c-2.1 0-3.8 1.8-3.8 4s1.7 4 3.8 4c1 0 2-.5 2.7-1.2l5 3.1c0 .4-.1.7-.1 1.1 0 2.2 1.7 4 3.8 4 2.1 0 3.8-1.8 3.8-4s-1.7-4-3.8-4zm0-12c1 0 1.9.9 1.9 2s-.9 2-1.9 2c-1 0-1.9-.9-1.9-2s.9-2 1.9-2zM7.3 15c-1 0-1.9-.9-1.9-2s.9-2 1.9-2c1 0 1.9.9 1.9 2s-.9 2-1.9 2zm11.4 7c-1 0-1.9-.9-1.9-2 0-.4.1-.7.3-1 .3-.6 1-1 1.6-1 1 0 1.9.9 1.9 2s-.9 2-1.9 2z"></path></svg></button>
</div>
</div> <div class="media-content">
<div class="video-player" id="videoPlayer" style="z-index:0;position:relative"></div><div class="video-footer-buttons"> <div class="rumbles-vote" data-id="97479462" data-type="1">
<button aria-label="Rumbles up vote" class="rumbles-vote-up" data-vote="1"><svg class="icon-rumbles-up" height="16" width="16"><path d="M1.5 8l13 0m-6.5-6.5l0 13" stroke-width="3"></path></svg></button>
<button aria-label="Rumbles down vote" class="rumbles-vote-down" data-vote="-1"><svg class="icon-rumbles-down" height="16" viewbox="0 0 16 16" width="16"><path d="M1.5 8l13 0" stroke-width="3"></path></svg></button>
<span class="rumbles-count">114</span> <span class="rumbles-unit">rumbles</span>
</div>
<div style="display: flex">
<button class="round-button media-video-action media-video-action-embed">Embed<svg class="media-icon-embed" height="20" viewbox="0 0 20 20" width="20"><path d="M16.2 7h-2c-6 0-10.9 4.6-10.9 10.3m9.1-6.3l4-4-4-3.9" fill="none"></path></svg></button>
<button class="round-button media-engage-share mobile-only bg-blue">Share<svg class="media-icon-share" height="18" viewbox="0 0 24 24" width="18"><path d="M18.7 16c-1 0-2 .5-2.7 1.2l-5-3.1c0-.4.1-.7.1-1.1 0-.4-.1-.7-.2-1.1l5-3.1c.8.7 1.7 1.2 2.8 1.2 2.1 0 3.8-1.8 3.8-4s-1.7-4-3.8-4c-2.1 0-3.8 1.8-3.8 4 0 .4.1.7.2 1.1L10 10.2C9.3 9.5 8.3 9 7.3 9c-2.1 0-3.8 1.8-3.8 4s1.7 4 3.8 4c1 0 2-.5 2.7-1.2l5 3.1c0 .4-.1.7-.1 1.1 0 2.2 1.7 4 3.8 4 2.1 0 3.8-1.8 3.8-4s-1.7-4-3.8-4zm0-12c1 0 1.9.9 1.9 2s-.9 2-1.9 2c-1 0-1.9-.9-1.9-2s.9-2 1.9-2zM7.3 15c-1 0-1.9-.9-1.9-2s.9-2 1.9-2c1 0 1.9.9 1.9 2s-.9 2-1.9 2zm11.4 7c-1 0-1.9-.9-1.9-2 0-.4.1-.7.3-1 .3-.6 1-1 1.6-1 1 0 1.9.9 1.9 2s-.9 2-1.9 2z"></path></svg></button>
</div>
</div><div class="media-description-break a-break" data-section="description"></div>
<div class="container content media-description"> <div class="media-description-locals-message with-separator">
<svg class="themable-locals-icon" style="flex: 0 0 2.5rem; width: 2.5em; height: 2.5em; margin-right: .75em" viewbox="0 0 95 71"><path d="M85.016 43.103a7.12 7.12 0 0 0 7.117-7.124 7.12 7.12 0 0 0-7.117-7.124 7.12 7.12 0 0 0-7.117 7.124 7.12 7.12 0 0 0 7.117 7.124z" fill="#E73348"></path>
<path d="M69.916 26.645V45.33h-4.803v-1.998a7.347 7.347 0 0 1-5.722 2.599 9.957 9.957 0 0 1-6.57-3.155 9.975 9.975 0 0 1 0-13.577 9.957 9.957 0 0 1 6.57-3.155 7.34 7.34 0 0 1 5.722 2.599v-1.998h4.803zm-4.803 9.334a5.13 5.13 0 0 0-3.162-4.736 5.117 5.117 0 0 0-5.581 1.11 5.127 5.127 0 0 0 3.621 8.752c1.359 0 2.661-.54 3.622-1.501a5.13 5.13 0 0 0 1.5-3.625zm-23.718 3.429 1.996 4.296a9.708 9.708 0 0 1-6.481 2.227 9.935 9.935 0 0 1-7.3-2.76 9.952 9.952 0 0 1-3.062-7.184 9.96 9.96 0 0 1 3.062-7.184 9.94 9.94 0 0 1 7.3-2.759 9.637 9.637 0 0 1 6.48 2.227l-1.995 4.331a6.16 6.16 0 0 0-4.327-1.767 5.133 5.133 0 0 0-5.217 3.029 5.148 5.148 0 0 0 3.097 6.977 5.133 5.133 0 0 0 2.12.229 6.125 6.125 0 0 0 4.327-1.662z" fill="currentColor"></path>
<path d="M9.925 43.103a7.12 7.12 0 0 0 7.117-7.124 7.12 7.12 0 0 0-7.117-7.124 7.12 7.12 0 0 0-7.117 7.124 7.12 7.12 0 0 0 7.117 7.124z" fill="#E73348"></path>
<path d="M17.925 15.526v4.808H2.031V1.596h4.715v13.93h11.179z" fill="currentColor"></path>
<path d="M85.016 20.865c5.481 0 9.925-4.448 9.925-9.935S90.497.995 85.016.995c-5.482 0-9.925 4.448-9.925 9.935s4.443 9.935 9.925 9.935zm-25.025-2.811a7.12 7.12 0 0 0 7.117-7.124 7.12 7.12 0 0 0-7.117-7.124 7.12 7.12 0 0 0-7.117 7.124 7.12 7.12 0 0 0 7.117 7.124z" fill="#E73348"></path>
<path d="M44.892 10.93a9.96 9.96 0 0 1-6.126 9.207 9.934 9.934 0 0 1-10.84-2.146 9.954 9.954 0 0 1-2.164-10.848 9.95 9.95 0 0 1 12.99-5.396 9.924 9.924 0 0 1 5.383 5.377c.5 1.207.757 2.5.757 3.806zm-4.821 0a5.13 5.13 0 0 0-3.162-4.736 5.117 5.117 0 0 0-5.581 1.111 5.128 5.128 0 0 0 3.621 8.751c1.359 0 2.661-.54 3.622-1.501a5.129 5.129 0 0 0 1.5-3.625zM93.44 64.35c0 3.801-3.003 6.63-8.195 6.63a14.33 14.33 0 0 1-8.653-2.705l1.5-4.525a10.943 10.943 0 0 0 6.624 2.634c2.225 0 3.85-.442 3.85-1.609 0-.83-.83-1.131-3.32-1.556-6.959-1.131-8.124-3.34-8.124-6.399 0-3.058 3.267-5.727 8.159-5.727 2.523.017 5.008.623 7.258 1.767l-1.342 4.367a12.035 12.035 0 0 0-5.916-1.591c-1.943 0-3.338.336-3.338 1.131 0 1.131 1.942 1.326 3.938 1.662 6.34 1.06 7.559 3.553 7.559 5.922zm-25.466 1.203v4.773H51.99V51.712h4.91v13.84h11.073z" fill="currentColor"></path>
<path d="M34.95 68.169a7.12 7.12 0 0 0 7.116-7.124 7.12 7.12 0 0 0-7.117-7.124 7.12 7.12 0 0 0-7.117 7.124 7.12 7.12 0 0 0 7.117 7.124zM9.925 70.98c5.481 0 9.925-4.448 9.925-9.935s-4.444-9.935-9.925-9.935C4.444 51.11 0 55.558 0 61.045s4.444 9.935 9.925 9.935z" fill="#E73348"></path></svg> <div>
						Enjoyed this video? Join my Locals community for exclusive content at
						<a href="https://vivabarneslaw.locals.com/track/rumble/click/video?click=description" style="text-decoration: underline" target="_blank">vivabarneslaw.locals.com</a>!
					</div>
</div>
<p class="media-description">The allegations of this lawsuit will break your heart and hurt your soul.</p>
</div> <section id="video-comments">
<div id="video-comments-loading">Loading 8 comments...
				<div class="loading-spinner"></div>
</div>
</section>
</div>
<aside class="media-sidebar">
<div class="media-related-break a-break" data-section="related"></div><ul class="mediaList-list container content related without-show-more-link"><li class="mediaList-item first-item"> <a class="mediaList-link size-medium" href="/v1okde0-stay-free-with-russell-brand-015-so-who-did-sabotage-nord-stream-plus-vanda.html">
<div class="mediaList-image-div size-medium">
<img alt="Stay Free with Russell Brand #015 - So Who DID Sabotage Nord Stream? Plus Vandana Shiva" class="mediaList-image" src="https://sp.rmbl.ws/s8/1/i/Z/d/e/iZdeg.0kob-small-Stay-Free-with-Russell-Bran.jpg"/>
<small class="mediaList-duration">1h07m10s</small>
</div>
<div class="mediaList-info first-item">
<h3 class="mediaList-heading size-medium" title="Stay Free with Russell Brand #015 - So Who DID Sabotage Nord Stream? Plus Vandana Shiva">Stay Free with Russell Brand #015 - So Who DID Sabotage Nord Stream? Plus Vandana Shiva</h3>
<section class="mediaList-by size-medium"><i class="user-image user-image--img user-image--img--id-dadf98c2a02afc9e736c7475ea951a5e mediaList-by-image"></i> <div>
<h4 class="mediaList-by-heading">Russell Brand</h4>
</div>
</section>
</div>
</a></li><li class="mediaList-item"> <a class="mediaList-link size-medium" href="/v1olssf-the-konnech-rabbit-hole-just-got-deeper.html">
<div class="mediaList-image-div size-medium">
<img alt="The Election Fraud Rabbit Hole Just Got Deeper!" class="mediaList-image" src="https://sp.rmbl.ws/s8/1/_/d/u/e/_dueg.0kob-small-The-Konnech-Rabbit-Hole-Jus.jpg"/>
<small class="mediaList-duration">1h12m42s</small>
</div>
<div class="mediaList-info">
<h3 class="mediaList-heading size-medium" title="The Election Fraud Rabbit Hole Just Got Deeper!">The Election Fraud Rabbit Hole Just Got Deeper!</h3>
<section class="mediaList-by size-medium"><i class="user-image user-image--img user-image--img--id-31a00d8df4b3fae640d78fc9f462ffa0 mediaList-by-image"></i> <div>
<h4 class="mediaList-by-heading">Nick Moseder</h4>
</div>
</section>
</div>
</a></li><li class="mediaList-item"> <a class="mediaList-link size-medium" href="/v1omt1u-trans-influencer-does-woman-face-for-ulta-beauty.html">
<div class="mediaList-image-div size-medium">
<img alt='Trans Influencer Does "Woman-Face" For Ulta Beauty' class="mediaList-image" src="https://sp.rmbl.ws/s8/6/s/I/F/e/sIFeg.0kob.1.jpg"/>
<small class="mediaList-duration">1h03m24s</small>
</div>
<div class="mediaList-info">
<h3 class="mediaList-heading size-medium" title='Trans Influencer Does "Woman-Face" For Ulta Beauty'>Trans Influencer Does "Woman-Face" For Ulta Beauty</h3>
<section class="mediaList-by size-medium"><i class="user-image user-image--img user-image--img--id-fe04113a4b07e4cd4f4fa603894a1ea2 mediaList-by-image"></i> <div>
<h4 class="mediaList-by-heading">Arielle Scarcella</h4>
</div>
</section>
</div>
</a></li><li class="mediaList-item"> <a class="mediaList-link size-medium" href="/v1om84x-government-manipulation-confirmed.html">
<div class="mediaList-image-div size-medium">
<img alt="Government Manipulation CONFIRMED!" class="mediaList-image" src="https://sp.rmbl.ws/s8/1/X/6/y/e/X6yeg.0kob-small-Government-Manipulation-CON.jpg"/>
<small class="mediaList-duration">56m00s</small>
</div>
<div class="mediaList-info">
<h3 class="mediaList-heading size-medium" title="Government Manipulation CONFIRMED!">Government Manipulation CONFIRMED!</h3>
<section class="mediaList-by size-medium"><i class="user-image user-image--img user-image--img--id-86e56c77ea0633fcab6007dfd1789de0 mediaList-by-image"></i> <div>
<h4 class="mediaList-by-heading">Matt Kohrs</h4>
</div>
</section>
</div>
</a></li><li class="mediaList-item"> <a class="mediaList-link size-medium" href="/v1olrsb-if-republican-house-impeaches-biden-i-will-oppose-it.html">
<div class="mediaList-image-div size-medium">
<img alt="If Republican house impeaches Biden I will oppose it" class="mediaList-image" src="https://sp.rmbl.ws/s8/6/R/V/t/e/RVteg.0kob.1.jpg"/>
<small class="mediaList-duration">29m09s</small>
</div>
<div class="mediaList-info">
<h3 class="mediaList-heading size-medium" title="If Republican house impeaches Biden I will oppose it">If Republican house impeaches Biden I will oppose it</h3>
<section class="mediaList-by size-medium"><i class="user-image user-image--img user-image--img--id-70db634516c9313989b962a0b4f4580c mediaList-by-image"></i> <div>
<h4 class="mediaList-by-heading">The Dershow</h4>
</div>
</section>
</div>
</a></li><li class="mediaList-item"> <a class="mediaList-link size-medium" href="/v1olbzu-darrell-brooks-trial-day-9-just-the-afternoon-though.html">
<div class="mediaList-image-div size-medium">
<img alt="Darrell Brooks Trial Day 9 (Just the Afternoon, Though)" class="mediaList-image" src="https://sp.rmbl.ws/s8/1/6/V/o/e/6Voeg.Gkob.1-small-Darrell-Brooks-Trial-Day-9-.jpg"/>
<small class="mediaList-duration">5h02m25s</small>
</div>
<div class="mediaList-info">
<h3 class="mediaList-heading size-medium" title="Darrell Brooks Trial Day 9 (Just the Afternoon, Though)">Darrell Brooks Trial Day 9 (Just the Afternoon, Though)</h3>
<section class="mediaList-by size-medium"><i class="user-image user-image--img user-image--img--id-fa96777532f14bd6caf72b34405cfada mediaList-by-image"></i> <div>
<h4 class="mediaList-by-heading">Rekieta Law</h4>
<small class="mediaList-earnings">$53.39 earned</small>
</div>
</section>
</div>
</a></li><li class="mediaList-item"> <a class="mediaList-link size-medium" href="/v1oluoc-kanye-west-buys-parler-but-should-have-invested-in-rumble.html">
<div class="mediaList-image-div size-medium">
<img alt="Kanye West Buys Parler But Should Have Invested In Rumble" class="mediaList-image" src="https://sp.rmbl.ws/s8/6/m/Q/u/e/mQueg.0kob.jpg"/>
<small class="mediaList-duration">9m40s</small>
</div>
<div class="mediaList-info">
<h3 class="mediaList-heading size-medium" title="Kanye West Buys Parler But Should Have Invested In Rumble">Kanye West Buys Parler But Should Have Invested In Rumble</h3>
<section class="mediaList-by size-medium"><i class="user-image user-image--img user-image--img--id-97757b4018e18228066e546df646ae1f mediaList-by-image"></i> <div>
<h4 class="mediaList-by-heading">The Quartering</h4>
</div>
</section>
</div>
</a></li><li class="mediaList-item"> <a class="mediaList-link size-medium" href="/v1oklz9-6-advanced-ancient-inventions-we-still-cant-figure-out.html">
<div class="mediaList-image-div size-medium">
<img alt="6 Advanced Ancient Inventions We Still Can't Figure Out" class="mediaList-image" src="https://sp.rmbl.ws/s8/1/f/H/g/e/fHgeg.Kkob-small-6-Advanced-Ancient-Inventio.jpg"/>
<small class="mediaList-duration">6m53s</small>
</div>
<div class="mediaList-info">
<h3 class="mediaList-heading size-medium" title="6 Advanced Ancient Inventions We Still Can't Figure Out">6 Advanced Ancient Inventions We Still Can't Figure Out</h3>
<section class="mediaList-by size-medium"><i class="user-image user-image--img user-image--img--id-5dc686f428fddd5aa0d369957bfa4edd mediaList-by-image"></i> <div>
<h4 class="mediaList-by-heading">Beyond Science</h4>
<small class="mediaList-earnings">$3.27 earned</small>
</div>
</section>
</div>
</a></li><li class="mediaList-item"> <a class="mediaList-link size-medium" href="/v1oh8so-tim-kennedys-firsthand-experience-in-ukraine-what-you-dont-know.html">
<div class="mediaList-image-div size-medium">
<img alt="Tim Kennedy's Firsthand Experience in Ukraine (What You Don't Know)" class="mediaList-image" src="https://sp.rmbl.ws/s8/1/i/l/G/d/ilGdg.0kob-small-Tim-Kennedys-Firsthand-Expe.jpg"/>
<small class="mediaList-duration">8m59s</small>
</div>
<div class="mediaList-info">
<h3 class="mediaList-heading size-medium" title="Tim Kennedy's Firsthand Experience in Ukraine (What You Don't Know)">Tim Kennedy's Firsthand Experience in Ukraine (What You Don't Know)</h3>
<section class="mediaList-by size-medium"><i class="user-image user-image--img user-image--img--id-65dcf4733ab3cc83d9d968c6544859a4 mediaList-by-image"></i> <div>
<h4 class="mediaList-by-heading">Awaken With JP</h4>
</div>
</section>
</div>
</a></li><li class="mediaList-item last-item"> <a class="mediaList-link size-medium" href="/v1okfwa-living-on-the-bitcoin-standard.html">
<div class="mediaList-image-div size-medium">
<img alt="Kanye West Buys Parler!" class="mediaList-image" src="https://sp.rmbl.ws/s8/1/6/L/e/e/6Leeg.0kob.1-small-Living-on-the-Bitcoin-Stand.jpg"/>
<small class="mediaList-duration">1h53m58s</small>
</div>
<div class="mediaList-info last-item">
<h3 class="mediaList-heading size-medium" title="Kanye West Buys Parler!">Kanye West Buys Parler!</h3>
<section class="mediaList-by size-medium"><i class="user-image user-image--img user-image--img--id-2ba0e3c10c20da045656187e99b50b7b mediaList-by-image"></i> <div>
<h4 class="mediaList-by-heading">Bitcoin Magazine</h4>
</div>
</section>
</div>
</a></li></ul> </aside>
<div style="height:20px;clear:both"></div>
</article> </div>
</main>
<header class="header">
<div class="header-div constrained">
<button aria-label="main menu" class="main-menu-toggle">
<svg class="main-menu-open" height="16" width="20"><path d="M0 1h20M0 8h20M0 15h20"></path></svg> <svg class="main-menu-close" height="16" width="20"><path d="M2.5.5 l15 15 m0-15 l-15 15"></path></svg> </button>
<a class="header-logo" href="/">
<img alt="Rumble" id="logo_light" src="/img/rumble-full-logo-v4.svg"/>
<img alt="Rumble" hidden="" id="logo_dark" src="/img/rumble-full-logo-v4-dark.svg"/>
</a>
<form class="header-search">
<select class="header-search-select select-arrow-bg">
<option>Videos</option>
<option>Channels</option>
</select>
<input class="header-search-field" name="query" placeholder="Search" type="search" value=""/>
<button aria-label="search Rumble" class="header-search-submit">
<svg class="header-search-icon" viewbox="0 0 26 26"><path d="M17.6 17.6l6.3 6.3M2.2 11.2a9 9 0 1 0 18 0 9 9 0 1 0-18 0" fill="none" stroke-linecap="round" stroke-width="2"></path></svg> </button>
</form>
<button class="header-upload" title="Upload">
<svg viewbox="0 0 26 26"><path d="M4.2 17.5s-2.7-3.1-1.9-7.1C3 6.8 5.9 3.9 9.9 3.9c3.5 0 5.1 1.6 6.2 2.7 1.1 1.1 1.4 3.5 1.4 3.5s2.7-.7 4.4.7 2.4 3.8 1.8 5.6-2.6 3.1-2.6 3.1M9 17.1l4.1-3.8 4.2 3.8m-4.2 5.4v-9.2" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg> </button>
<button aria-label="sign in" class="header-user">
<svg class="user-image user-image--icon header-user-img"><path d="M8 6.8a5 5 0 1 0 10 0 5 5 0 1 0-10 0m14.8 16.7v-3.7a4 4 0 0 0-4-4H7.2a4 4 0 0 0-4 4v3.7" fill="none" stroke-linecap="round" stroke-width="2"></path></svg> <span class="header-user-info">
<span class="header-user-name">Sign In</span>
</span>
</button>
</div>
</header>
<nav class="navs">
<div class="constrained" style="position:relative">
<div class="hover-menu main-menu-nav" id="main-menu">
<a class="main-menu-item" href="/videos?date=this-week"><svg class="main-menu-icon"><path d="M5 13a8 8 0 1 0 16 0 8 8 0 1 0-16 0M2.9 8.6C4.1 6 6.2 3.9 8.7 2.8m14.5 14.7a11.5 11.5 0 0 1-5.8 5.7M13 6.9V13h4.2" fill="none"></path></svg>Latest</a> <a class="main-menu-item" href="/editor-picks"><svg class="main-menu-icon" height="27" viewbox="0 0 26 27" width="26"><path d="M4 8a6.5 7 0 1 0 13 0A6.5 7 0 1 0 4 8m15 13.5C15.6 11 1.1 13.9 1 25m13-2.4l3.9 4.4 7.1-8" fill="none"></path></svg>Editor Picks</a>
<a class="main-menu-item" href="/videos?sort=views&amp;date=today"><svg class="main-menu-icon" height="24" viewbox="0 0 24 24" width="24"><path d="m23 6-9.5 9.5-5-5L1 18M17 6h6v6"></path></svg>Trending</a>
<a class="main-menu-item" href="/license-videos"><svg class="main-menu-icon" height="26" viewbox="0 0 26 26" width="26"><path d="M19.1 20H2.3V6h11.8M24.3 20h-5.5s-.9-1.5-1.4-2c-.5-.5-1-1.3-1.9-1.7-.4-.2-2.2-1.6-2.3-2.5 0-1.7 1.1-1.4 2.3-1 1.2.5 3.6 1.6 3.6 1.6l-.9-6.7S12.9 6.2 13 5.9c.1-.3 5.8-1.9 7.2-.2s2 4.5 2.8 5.1c.8.6 1.5.6 1.5.6 M6.8,11.1a1.8,1.8 0 1,0 3.6,0a1.8,1.8 0 1,0 -3.6,0 M5.8 16.6c0-1.5 1.2-2.7 2.7-2.7s2.7 1.2 2.7 2.7" fill="none"></path></svg>License Videos</a>
<div class="js-theme-option-group" hidden="">
<h3 class="main-menu-heading">Theme</h3>
<a class="main-menu-item js-theme-option" data-theme="system" href=""><svg class="main-menu-icon" height="24" viewbox="0 0 24 24" width="24"><path d="M12 1v2m0 18v2M4.2 4.2l1.4 1.4m12.8 12.8 1.4 1.4M1 12h2m18 0h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4M16 12.36A4 4 0 1 1 11.64 8 3.12 3.12 0 0 0 16 12.36Z"></path></svg> OS Default</a>
<a class="main-menu-item js-theme-option" data-theme="dark" href=""><svg class="main-menu-icon" height="24" viewbox="0 0 24 24" width="24"><path d="M12.1 4.1c.3-.4 0-.9-.5-.8a8.5 8.5 0 1 0 9.3 12.4c.3-.4-.1-.9-.6-.7A7 7 0 0 1 12 4.2Z"></path></svg> Dark Mode</a>
<a class="main-menu-item js-theme-option" data-theme="light" href=""><svg class="main-menu-icon" height="24" viewbox="0 0 24 24" width="24"><path d="M7 12a5 5 0 1 0 10 0 5 5 0 1 0-10 0m5-11v2m0 18v2M4.2 4.2l1.4 1.4m12.8 12.8 1.4 1.4M1 12h2m18 0h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"></path></svg> Light Mode</a>
</div>
<h3 class="main-menu-heading">Featured Channels</h3><a class="main-menu-item" href="/c/Reuters">Reuters</a><a class="main-menu-item" href="/c/WildCreatures">Wild Creatures</a><a class="main-menu-item" href="/c/WayneDupreeShow">The Wayne Dupree Show</a><a class="main-menu-item" href="/c/Newsy">Newsy</a><a class="main-menu-item" href="/c/JustPlanes">JustPlanes</a><a class="main-menu-item" href="/c/DevinNunes">Devin Nunes</a><a class="main-menu-item" href="/c/MarkDice">MarkDice</a><a class="main-menu-item" href="/c/Bongino">The Dan Bongino Show</a><a class="main-menu-item" href="/c/Cioccolanti">Cioccolanti</a><a class="main-menu-item" href="/c/DineshDsouza">Dinesh Dsouza</a><a class="main-menu-item" href="/c/MLChristiansen">MLChristiansen</a><a class="main-menu-item" href="/c/RobertGouveia">RobertGrulerEsq</a><a class="main-menu-item" href="/c/BannonsWarRoom">BannonsWarRoom</a><a class="main-menu-item" href="/c/BennyJohnson">BennyJohnson</a><a class="main-menu-item" href="/c/NoreensKitchen">NoreensKitchen</a><a class="main-menu-item" href="/c/CharlieKirk">Charlie Kirk</a><a class="main-menu-item" href="/c/NewsmaxTV">NewsmaxTV</a><a class="main-menu-item" href="/c/MariaBartiromo">MariaBartiromo</a><a class="main-menu-item" href="/user/vivafrei">Viva Frei</a><a class="main-menu-item" href="/c/Fleccas">Fleccas</a><a class="main-menu-item" href="/c/Styxhexenhammer666">Styxhexenhammer666</a><a class="main-menu-item" href="/c/SeanHannity">Sean Hannity</a><a class="main-menu-item" href="/c/TrishReganShow">Trish Regan</a><a class="main-menu-item" href="/c/SamuelEarpArtist">Samuel Earp Artist</a><a class="main-menu-item" href="/c/KayaJones">KayaJones</a><a class="main-menu-item" href="/c/TheNerdRealm">The Nerd Realm</a><a class="main-menu-item" href="/c/sideserfcakes">Side Serf Cakes</a><a class="main-menu-item" href="/c/spaceXcentric">spaceXcentric</a><a class="main-menu-item" href="/c/MikhailaPeterson">Mikhaila Peterson</a><a class="main-menu-item" href="/c/NTDNews">NTDNews</a><a class="main-menu-item" href="/c/TheOfficerTatum">The Officer Tatum</a><a class="main-menu-item" href="/c/OutKickTheCoverage">OutKick</a><a class="main-menu-item" href="/c/CWLemoine">CWLemoine</a><a class="main-menu-item" href="/c/LaurenChen">Lauren Chen</a><a class="main-menu-item" href="/c/DonaldTrump">Donald Trump</a><a class="main-menu-item" href="/c/TheHistoryGuy">The History Guy</a><a class="main-menu-item" href="/c/RebelNews">RebelNews</a><a class="main-menu-item" href="/c/pintswithaquinas">pintswithaquinas</a><a class="main-menu-item" href="/c/TheBodyLanguageGuy">TheBodyLanguageGuy</a><a class="main-menu-item" href="/c/YelllowFlash">YelllowFlash</a><a class="main-menu-item" href="/c/BrightInsight">BrightInsight</a><a class="main-menu-item" href="/c/PaulandMorgan">PaulandMorgan</a><a class="main-menu-item" href="/c/AwakenWithJP">Awaken With JP</a><a class="main-menu-item" href="/c/TulsiGabbard">Tulsi Gabbard</a><a class="main-menu-item" href="/c/TheBabylonBee">The Babylon Bee</a><a class="main-menu-item" href="/c/BenShapiro">Ben Shapiro</a><a class="main-menu-item" href="/c/FactsChannel">Facts</a><a class="main-menu-item" href="/c/RandPaul">Rand Paul</a><a class="main-menu-item" href="/c/DonaldJTrumpJr">Donald Trump Jr</a><a class="main-menu-item" href="/c/EliseStefanik">Elise Stefanik</a><a class="main-menu-item" href="/c/BlacktipH">BlacktipH</a><a class="main-menu-item" href="/c/LifeStories">Life Stories</a><a class="main-menu-item" href="/c/c-647947">SCI</a><a class="main-menu-item" href="/c/StevenCrowder">Steven Crowder</a><a class="main-menu-item" href="/c/NYPost">New York Post</a><a class="main-menu-item" href="/c/PageSix">PageSix</a><a class="main-menu-item" href="/c/Decider">Decider</a><a class="main-menu-item" href="/c/JohnStossel">John Stossel</a><a class="main-menu-item" href="/c/RonPaulLibertyReport">Ron Paul Liberty Report</a><a class="main-menu-item" href="/c/ARKMedia">ARKMedia</a><a class="main-menu-item" href="/c/Locals">Locals</a><a class="main-menu-item" href="/c/Timcast">Timcast</a><a class="main-menu-item" href="/c/TimcastIRL">TimcastIRL</a><a class="main-menu-item" href="/c/Entrepreneur">Entrepreneur</a><a class="main-menu-item" href="/c/EpochTV">EpochTV</a><a class="main-menu-item" href="/c/WhitneyBjerken">WhitneyBjerken</a><a class="main-menu-item" href="/c/DrDrew">Dr Drew</a><a class="main-menu-item" href="/c/Yarnhub">Yarnhub</a><a class="main-menu-item" href="/c/RubinReport">Rubin Report</a><a class="main-menu-item" href="/c/GGreenwald">Glenn Greenwald</a><a class="main-menu-item" href="/c/MattKohrs">Matt Kohrs (Finance)</a><a class="main-menu-item" href="/c/HabibiBros">Habibi Power Hour</a><a class="main-menu-item" href="/c/Orf">Orf</a><a class="main-menu-item" href="/c/Inquire">Inquire</a><a class="main-menu-item" href="/c/phetasy">phetasy</a><a class="main-menu-item" href="/c/academyofideas">academyofideas</a><a class="main-menu-item" href="/c/JorgeMasvidal">Jorge Masvidal</a><a class="main-menu-item" href="/c/russellbrand">Russell Brand</a><a class="main-menu-item" href="/c/HonestReportingCanada">Honest Reporting</a><a class="main-menu-item" href="/c/GrantCardone">Grant Cardone</a><a class="main-menu-item" href="/c/ChrisJericho">ChrisJericho</a><a class="main-menu-item" href="/c/TheRamseyShowHighlights">TheRamseyShowHighlights</a><a class="main-menu-item" href="/c/TheRamseyShowFullEpisodes">TheRamseyShowFullEpisodes</a><a class="main-menu-item" href="/c/TheInterviewRoom">TheInterviewRoom</a><a class="main-menu-item" href="/c/MedicalMedium">MedicalMedium</a><a class="main-menu-item" href="/c/TheJimmyDoreShow">TheJimmyDoreShow</a><a class="main-menu-item" href="/c/ClayandBuck">ClayandBuck</a><a class="main-menu-item" href="/c/UprightHealth">UprightHealth</a><a class="main-menu-item" href="/c/TheRichDadChannel">TheRichDadChannel</a><a class="main-menu-item" href="/c/NaturesAlwaysRight">NaturesAlwaysRight</a><a class="main-menu-item" href="/c/ChampagneSharks">ChampagneSharks</a><a class="main-menu-item" href="/c/PetervonPanda">PetervonPanda</a><a class="main-menu-item" href="/c/AfterSkool">AfterSkool</a><a class="main-menu-item" href="/c/SmokyRibsBBQ">SmokyRibsBBQ</a><a class="main-menu-item" href="/c/MichaelLeeStrategy">MichaelLeeStrategy</a><a class="main-menu-item" href="/c/iammrbeat">iammrbeat</a><a class="main-menu-item" href="/c/WorkshopCompanion">WorkshopCompanion</a><a class="main-menu-item" href="/c/StockCurry">StockCurry</a><a class="main-menu-item" href="/c/ThePodcastoftheLotusEaters">ThePodcastoftheLotusEaters</a><a class="main-menu-item" href="/c/ArielleScarcella">ArielleScarcella</a><a class="main-menu-item" href="/c/TradersLanding">TradersLanding</a><a class="main-menu-item" href="/c/RuckaRuckaAli">Rucka Rucka Ali</a><a class="main-menu-item" href="/c/DegenerateJay">DegenerateJay</a><a class="main-menu-item" href="/c/DegeneratePlays">DegeneratePlays</a><a class="main-menu-item" href="/c/DVGPodcast">DVGPodcast</a><a class="main-menu-item" href="/c/TheDiveWithJacksonHinkle">TheDiveWithJacksonHinkle</a><a class="main-menu-item" href="/c/thatbeatgoeson">thatbeatgoeson</a><a class="main-menu-item" href="/c/Kilmeade">Kilmeade</a><a class="main-menu-item" href="/c/TheHillbillyKitchen">TheHillbillyKitchen</a><a class="main-menu-item" href="/c/NewsTalkSTL">NewsTalkSTL</a><a class="main-menu-item" href="/c/LogOffAlready">LogOffAlready</a><a class="main-menu-item" href="/c/EnterShaolin">EnterShaolin</a><a class="main-menu-item" href="/c/WillCain">WillCain</a><a class="main-menu-item" href="/c/MegynKelly">MegynKelly</a><a class="main-menu-item" href="/c/RepKevinMcCarthy">RepKevinMcCarthy</a><a class="main-menu-item" href="/c/AlisonMorrow">AlisonMorrow</a><a class="main-menu-item" href="/c/BenUyeda">BenUyeda</a><a class="main-menu-item" href="/c/MrBuildIt">MrBuildIt</a><a class="main-menu-item" href="/c/SteveScalise">SteveScalise</a><a class="main-menu-item" href="/c/TheHeritageFoundation">TheHeritageFoundation</a><a class="main-menu-item" href="/c/TheDailySignal">TheDailySignal</a><a class="main-menu-item" href="/c/GreenDreamProject">GreenDreamProject</a><a class="main-menu-item" href="/c/BlackPowerMediaChannel">BlackPowerMediaChannel</a><a class="main-menu-item" href="/c/AmericanSongwriter">AmericanSongwriter</a><a class="main-menu-item" href="/c/modernwisdompodcast">modernwisdompodcast</a><a class="main-menu-item" href="/c/IsaacArthur">IsaacArthur</a><a class="main-menu-item" href="/c/TomAntosFilms">TomAntosFilms</a><a class="main-menu-item" href="/c/ColionNoir">ColionNoir</a><a class="main-menu-item" href="/c/KimIversen">KimIversen</a><a class="main-menu-item" href="/c/Homesteadonomics">Homesteadonomics</a><a class="main-menu-item" href="/c/TheAdventureAgents">TheAdventureAgents</a><a class="main-menu-item" href="/c/NDWoodworkingArt">NDWoodworkingArt</a><a class="main-menu-item" href="/c/KenDBerryMD">KenDBerryMD</a><a class="main-menu-item" href="/c/davidpakmanshow">davidpakmanshow</a><a class="main-menu-item" href="/c/HeresyFinancial">HeresyFinancial</a><a class="main-menu-item" href="/c/RepJimBanks">RepJimBanks</a><a class="main-menu-item" href="/c/ATRestoration">ATRestoration</a><a class="main-menu-item" href="/c/ThisSouthernGirlCan">ThisSouthernGirlCan</a><a class="main-menu-item" href="/c/RockFeed">RockFeed</a><a class="main-menu-item" href="/c/CountryCast">CountryCast</a><a class="main-menu-item" href="/c/ShaunAttwood">ShaunAttwood</a><a class="main-menu-item" href="/c/TwinCoconuts">TwinCoconuts</a><a class="main-menu-item" href="/c/diywife">diywife</a><a class="main-menu-item" href="/c/RekietaLaw">RekietaLaw</a><a class="main-menu-item" href="/c/MontyFranklin">MontyFranklin</a><a class="main-menu-item" href="/c/GeeksandGamers">GeeksandGamers</a><a class="main-menu-item" href="/c/SportsWars">SportsWars</a><a class="main-menu-item" href="/c/nfldaily">nfldaily</a><a class="main-menu-item" href="/c/nbanow">nbanow</a><a class="main-menu-item" href="/c/GeeksAndGamersPlay">GamingWithGeeks</a><a class="main-menu-item" href="/c/ParkHoppin">ParkHoppin</a><a class="main-menu-item" href="/c/GeeksAndGamersClips">GeeksAndGamersClips</a><a class="main-menu-item" href="/c/chiefstv">chiefstv</a><a class="main-menu-item" href="/c/brownsreport">brownstv</a><a class="main-menu-item" href="/c/nygiantstv">giantstv</a><a class="main-menu-item" href="/c/warriorstv">warriorstv</a><a class="main-menu-item" href="/c/lakerstv">lakerstv</a><a class="main-menu-item" href="/c/DynastyFlock">DynastyFlock</a><a class="main-menu-item" href="/c/FantasyFlockNetwork">FantasyFlockNetwork</a><a class="main-menu-item" href="/c/rwmalonemd">rwmalonemd</a><a class="main-menu-item" href="/c/Chubbyemu">Chubbyemu</a><a class="main-menu-item" href="/c/AnthonyJ350">AnthonyJ350</a><a class="main-menu-item" href="/c/ReasonTV">ReasonTV</a><a class="main-menu-item" href="/c/GfinityTv">GfinityTv</a><a class="main-menu-item" href="/c/engineerman">engineerman</a><a class="main-menu-item" href="/c/Newsthink">Newsthink</a><a class="main-menu-item" href="/c/MrScientific">MrScientific</a><a class="main-menu-item" href="/c/TheS">TheS</a><a class="main-menu-item" href="/c/Debunked">Debunked</a><a class="main-menu-item" href="/c/sydneywatson">sydneywatson</a><a class="main-menu-item" href="/c/UncivilLaw">UncivilLaw</a><a class="main-menu-item" href="/c/Dannyjokes">Dannyjokes</a><a class="main-menu-item" href="/c/BitcoinMagazine">BitcoinMagazine</a><a class="main-menu-item" href="/c/SonofaTech">SonofaTech</a><a class="main-menu-item" href="/c/MysteryScoop">MysteryScoop</a><a class="main-menu-item" href="/c/SpencerCornelia">SpencerCornelia</a><a class="main-menu-item" href="/c/Multipolarista">Multipolarista</a><a class="main-menu-item" href="/c/TheLeadAttorney">TheLeadAttorney</a><a class="main-menu-item" href="/c/Monark">Monark</a><a class="main-menu-item" href="/c/ThinkBeforeYouSleep">ThinkBeforeYouSleep</a><a class="main-menu-item" href="/c/Ferrez">Ferrez</a><a class="main-menu-item" href="/c/RonDeSantisFL">RonDeSantisFL</a><a class="main-menu-item" href="/c/TheDawgfathasBBQ">TheDawgfathasBBQ</a><a class="main-menu-item" href="/c/JimBreuer">JimBreuer</a><a class="main-menu-item" href="/c/RyanLongcomedy">RyanLongcomedy</a><a class="main-menu-item" href="/c/LeeCamp">LeeCamp</a><a class="main-menu-item" href="/c/PrimitiveSurvivalTools">PrimitiveSurvivalTools</a><a class="main-menu-item" href="/c/TheChrisSalcedoShow">TheChrisSalcedoShow</a><a class="main-menu-item" href="/c/FullMag">FullMag</a><a class="main-menu-item" href="/c/BitBoyCrypto">BitBoyCrypto</a><a class="main-menu-item" href="/c/Komando">Komando</a><a class="main-menu-item" href="/c/TheMagicMatt">TheMagicMatt</a><a class="main-menu-item" href="/c/TheKevinRobertsShow">TheKevinRobertsShow</a><a class="main-menu-item" href="/c/TheInfoWarrior">TheInfoWarrior</a><a class="main-menu-item" href="/c/DirtyMoney">DirtyMoney</a><a class="main-menu-item" href="/c/UpperEchelonGamers">UpperEchelonGamers</a><a class="main-menu-item" href="/c/TripleSgames">TripleSgames</a><a class="main-menu-item" href="/c/BrainyDose">BrainyDose</a><a class="main-menu-item" href="/c/worldnomactravel">worldnomactravel</a><a class="main-menu-item" href="/c/TylerFischer">TylerFischer</a><a class="main-menu-item" href="/c/Geometryptamine">GeometryTrip</a><a class="main-menu-item" href="/c/OwnagePranks">OwnagePranks</a><a class="main-menu-item" href="/c/LockPickingLawyer">LockPickingLawyer</a><a class="main-menu-item" href="/c/HikeCampClimb">HikeCampClimb</a><a class="main-menu-item" href="/c/NickSearcy">NickSearcy</a><a class="main-menu-item" href="/c/ReviewTechUSA">ReviewTechUSA</a><a class="main-menu-item" href="/c/Rengawr">Rengawr</a><a class="main-menu-item" href="/c/lifeinthe1800s">lifeinthe1800s</a><a class="main-menu-item" href="/c/MarkandMattis">MarkandMattis</a><a class="main-menu-item" href="/c/GabePoirot">GabePoirot</a><a class="main-menu-item" href="/c/Backfire">Backfire</a><a class="main-menu-item" href="/c/realpatriotgames">realpatriotgames</a><a class="main-menu-item" href="/c/RobsAquaponics">RobsAquaponics</a><a class="main-menu-item" href="/c/tateconfidential">tateconfidential</a><a class="main-menu-item" href="/c/JoshuaPhilipp">JoshuaPhilipp</a><a class="main-menu-item" href="/c/Epimetheus">Epimetheus</a><a class="main-menu-item" href="/c/RumbleEvents">RumbleEvents</a><a class="main-menu-item" href="/c/robbraxman">robbraxman</a><a class="main-menu-item" href="/c/LofiGirl">LofiGirl</a><a class="main-menu-item" href="/c/usefulidiots">usefulidiots</a><a class="main-menu-item" href="/c/JedediahBilaLive">JedediahBilaLive</a><a class="main-menu-item" href="/c/ValuetainmentShortclips">ValuetainmentShortclips</a><a class="main-menu-item" href="/c/Valuetainment">Valuetainment</a><a class="main-menu-item" href="/c/TateSpeech">TateSpeech</a><a class="main-menu-item" href="/c/CobraTate">CobraTate</a><a class="main-menu-item" href="/c/SailingZatara">SailingZatara</a><a class="main-menu-item" href="/c/DrJohnCampbell">DrJohnCampbell</a><a class="main-menu-item" href="/c/theoriesofeverything">theoriesofeverything</a><a class="main-menu-item" href="/c/BeyondScience">BeyondScience</a><a class="main-menu-item" href="/c/RandyBooker">RandyBooker</a><a class="main-menu-item" href="/c/AIRCLIPScom">AIRCLIPScom</a><a class="main-menu-item" href="/c/ScaryInteresting">ScaryInteresting</a><a class="main-menu-item" href="/c/JasonCorey">JasonCorey</a><a class="main-menu-item" href="/c/BohoBeautiful">BohoBeautiful</a><a class="main-menu-item" href="/c/PBDPodcast">PBDPodcast</a><a class="main-menu-item" href="/c/TheCrazyChannel">TheCrazyChannel</a><a class="main-menu-item" href="/c/TheHungryHussey">TheHungryHussey</a><a class="main-menu-item" href="/c/InteractiveBiology">InteractiveBiology</a><a class="main-menu-item" href="/c/stevewilldoit">stevewilldoit</a><a class="main-menu-item" href="/c/FRIGA">FRIGA</a><a class="main-menu-item" href="/c/DreDrexler">DreDrexler</a><a class="main-menu-item" href="/c/YOUCAR">YOUCAR</a><a class="main-menu-item" href="/c/JeremyLynch">JeremyLynch</a><a class="main-menu-item" href="/c/TannerBraungardt">TannerBraungardt</a><a class="main-menu-item" href="/user/RepMattGaetz">RepMattGaetz</a><a class="main-menu-item" href="/user/Libsoftiktok">Libsoftiktok</a><a class="main-menu-item" href="/user/TreasureHuntingWithJebus">TreasureHuntingWithJebus</a><a class="main-menu-item" href="/user/TheSCraft">TheSCraft</a><a class="main-menu-item" href="/user/andyh1202">andyh1202</a><a class="main-menu-item" href="/user/HybridCalisthenics">HybridCalisthenics</a><a class="main-menu-item" href="/user/OwnagePranks">OwnagePranks</a><a class="main-menu-item" href="/user/LockPickingLawyer">LockPickingLawyer</a><a class="main-menu-item" href="/user/lifeinthe1800s">lifeinthe1800s</a><a class="main-menu-item" href="/user/HumbleMechanic1">HumbleMechanic1</a><a class="main-menu-item" href="/user/VitalyTheGoat">VitalyTheGoat</a><a class="main-menu-item" href="/user/ViralHog">Viral Hog</a> </div>
<div class="hover-menu header-upload-menu">
<a class="main-menu-item" href="/upload.php"><svg class="main-menu-icon" viewbox="0 0 26 26"><path d="M4.2 17.5s-2.7-3.1-1.9-7.1C3 6.8 5.9 3.9 9.9 3.9c3.5 0 5.1 1.6 6.2 2.7 1.1 1.1 1.4 3.5 1.4 3.5s2.7-.7 4.4.7 2.4 3.8 1.8 5.6-2.6 3.1-2.6 3.1M9 17.1l4.1-3.8 4.2 3.8m-4.2 5.4v-9.2" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg>Upload Video</a>
<a class="main-menu-item" href="/live?go-live"><svg class="main-menu-icon" viewbox="0 0 30 16" width="20"><path d="M8 4a8 8 0 0 0 0 8M4 1a14 14 0 0 0 0 14m18-3a8 8 0 0 0 0-8m4 11a14 14 0 0 0 0-14" fill="none" stroke-linecap="round" stroke-width="2"></path><circle cx="15" cy="8" fill="none" r="2" stroke-width="4"></circle></svg>Go Live</a>
</div>
</div>
</nav>
<footer class="footer">
<div class="constrained">
<nav class="footer-nav">
<a class="footer-nav-link" href="//help.rumble.com/" rel="noopener" target="_blank">Developers</a>
<a class="footer-nav-link" href="/our-apps/" rel="noopener">Our Apps</a>
<a class="footer-nav-link" href="//corp.rumble.com/" rel="noopener" target="_blank">About Us</a>
<a class="footer-nav-link" href="//corp.rumble.com/careers/" rel="noopener" target="_blank">Careers</a>
<a class="footer-nav-link" href="//ads.rumble.com/" rel="noopener" target="_blank">Advertising</a>
</nav>
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
<div class="news_notification">
<a class="news_notification_a" href="//corp.rumble.com" target="_blank">
<strong>BREAKING</strong>: Rumble is now public &amp; listed on Nasdaq as <strong>$RUM</strong>
</a>
<button class="news_close" title="Dismiss the notification" type="button">
<svg class="news_close-x" height="24" viewbox="0 0 24 24" width="24"><path d="m5 5 14 14m0-14L5 19" fill="none" stroke-width="3"></path></svg> </button>
</div>
<script>$$={query:function(e,n){return Array.isArray(e)&&(n=e[1],e=e[0]),n=n||document,"string"==typeof e?n.querySelectorAll(e):[e]},each:function(e,n){for(var t=0;t<e.length;t++)n.call(e[t])},gt:function(e){return(new Date).getTime()/(e?1e3:1)},getByClass:function(e){var n=$$.query("."+e);return 1<=n.length&&n[0]},isVisible:function(e){return 0<e.offsetWidth&&0<e.offsetHeight},addClass:function(e,n){return!e.classList.contains(n)&&(e.classList.toggle(n),!0)},removeClass:function(e,n){e.classList.remove(n)},addClick:function(e,t){var n,r=$$.query(e);if(r)for(n=0;n<r.length;n++)r[n]&&r[n].addEventListener("click",function(e){var n=t.call(this,e);return n||void 0===n||e.stopPropagation(),n})},addServiceClick:function(e,n,t,r,c){$$.addClick(e,function(e){e.preventDefault(),$$.serviceGet(n,t,r,c)})},urlQueryObject:function(){var t={};return"undefined"==typeof URLSearchParams||new URLSearchParams(location.search).forEach(function(e,n){t[n]=e}),t},urlEncodeData:function(e){var n,t="";for(n in e)e.hasOwnProperty(n)&&(t+=(t?"&":"")+encodeURIComponent(n)+"="+encodeURIComponent(e[n]));return t},include:function(e,n){var t=document.createElement("script");t.src=e,t.async=!0,n&&(t.onload=n),document.head.appendChild(t)},includeCSS:function(e){var n=document.createElement("link");n.type="text/css",n.rel="stylesheet",n.href=e,document.head.appendChild(n)}},$$.page_load_time=(new Date).getTime();

$$.injectJSLib=function(e,t){var s=document.createElement("script");return s.defer=!0,s.text=t,"code"!=e&&(s.id="js-"+e,$$.includedJSLibs[e]=s),document.getElementsByTagName("head")[0].appendChild(s),s},$$.injectCSSLib=function(e,t){var s=document.createElement("style");return s.appendChild(document.createTextNode(t)),e&&(s.id="css-"+e,$$.includedCSSLibs[e]=s),(t=document.querySelector("head .js-theme-ss"))?t.insertAdjacentElement("beforebegin",s):document.getElementsByTagName("head")[0].appendChild(s),s},$$.request=function(e,t,s,n){var i=new XMLHttpRequest;n=n||function(){},i.open(t?"POST":"GET",e,!0),i.setRequestHeader("Content-type","application/x-www-form-urlencoded"),i.responseType="json",i.onload=function(){200==i.status?s(i.response):n&&n(i.status,i.response)},i.send(t?$$.urlEncodeData(t):null)},$$.requestGet=function(e,t,s){return $$.request(e,0,t,s)},$$.requestPost=function(e,t,s,n){return $$.request(e,t,s,n)},$$.serviceGet=function(e,t,s,n){return $$.serviceLoad("get",e,t,s,n)},$$.servicePost=function(e,t,s,n){return $$.serviceLoad("post",e,t,s,n)},$$.serviceLoad=function(i,c,o,r,e){"object"==typeof i&&(c=i.name||c,o=i.data||o,r=i.success||r,e=i.fail||e,i=i.type);var t,s,n=Math.floor(1e3*Math.random()),$="__service"+((new Date).getTime()-$$.page_load_time)+"_"+n,d=[],l=[],n="/service.php?",u={};for(s in"post"==i?"object"==typeof o&&(o.get||o.post)&&(t=o.get,o=o.post):o&&(t=o),(t=$$.urlEncodeData(t))&&(n+=t+"&"),u.name=c,$$.includedJSLibs)d.push(s);for(s in 0<d.length&&(u.included_js_libs=d.join(",")),$$.includedCSSLibs)l.push(s);0<l.length&&(u.included_css_libs=l.join(","));function a(e){var t,s,n="";if(e.js_libs){for(t in e.js_libs)e.js_libs.hasOwnProperty(t)&&$$.injectJSLib(t,e.js_libs[t]);delete e.js_libs}if(e.css_libs){for(t in e.css_libs)e.css_libs.hasOwnProperty(t)&&$$.injectCSSLib(t,e.css_libs[t]);delete e.css_libs}e.html&&((s=document.createElement("div")).innerHTML=e.html,e.html=1<s.childNodes.length?s:s.firstChild),e.request={type:i,name:c,data:o},$$[$]=e,$$[$].close=function(){this.html&&this.html.remove(),this.script.remove(),delete $$[$]},e.js_code&&(n="$$."+$+".call=function(){"+e.js_code+"};$$."+$+".call();"),r&&(e.success=r,n+="$$."+$+".success();"),n&&($$[$].script=$$.injectJSLib("code",n))}n+=$$.urlEncodeData(u),"post"==i?$$.requestPost(n,o,a,e):$$.requestGet(n,a,e)};

!function(){var i=[];$$.onload=function(t){if("object"!=typeof i)return t();i.push(t)},window.addEventListener("load",function(){for(var t=i,n=i=0;n<t.length;n++)t[n]()});var e=[];$$.onDomReady=function(t){if("object"!=typeof e)return t();e.push(t)},window.addEventListener("DOMContentLoaded",function(){for(var t=e,n=e=0;n<t.length;n++)t[n]()});var o=[];$$.onScroll=function(t,n){if(void 0===n&&(n=10),0==o.length){function i(){var n=$$.ui.scrollY();$$.each(o,function(){var t=this.last-n;t<this.step&&t>-this.step||(this.last=n,this.f())})}window.addEventListener("scroll",i),setTimeout(function(){i()},25)}o.push({f:t,step:n,last:2*-n})};var c=[];$$.checkVisibility=function(t,n){n=n||0;var i=window.innerHeight||document.documentElement.clientHeight,e=t.getBoundingClientRect(),o=[-n,i+n];return e.top>=o[0]&&e.top<=o[1]||e.bottom>=o[0]&&e.bottom<=o[1]},$$.onVisible=function(t,n,i){if($$.checkVisibility(t,i))return n.call(t);if(0==c.length){$$.onScroll(function(){$$.each(c,function(){$$.checkVisibility(this.elm,this.scan_ahead)&&(c.slice(c.indexOf(this),1),this.f.call(this.elm))})},50)}c.push({elm:t,f:n,scan_ahead:i})}}();

window.rumbleErrorHandler||function(){function d(r){var n=r.match(/http[s]?:\/\/[^\/]*rumble.com(\/.*)$/);return n?n[1]:r}var u=0;window.rumbleErrorHandler=function(r){var n,e,o,t,l=r.message,i=r.filename,c=r.lineno,a=r.colno,m=d(i);i==m||l.match(/^Script error\./)||3<++u||(e=document.location+"",n=[d(e),u,l,m,c,a],r.error&&r.error.stack&&n.push(r.error.stack.split("\n").slice(1,3).join("\n")),o="/l/jserr?err="+encodeURIComponent(JSON.stringify(n)),e==n[0]&&(o="https://rumble.com"+o),(t=document.createElement("img")).src=o,t.width=t.height=1,t.onload=t.onerror=function(){t.onload=null,t.onerror=null})},window.addEventListener("error",window.rumbleErrorHandler)}();

!function(e,n,t,o,c,f,a){e.fbq||(c=e.fbq=function(){c.callMethod?c.callMethod.apply(c,arguments):c.queue.push(arguments)},e._fbq||(e._fbq=c),(c.push=c).loaded=!0,c.version="2.0",c.queue=[],(f=n.createElement(t)).async=!0,setTimeout(function(){f.src="//connect.facebook.net/en_US/fbevents.js",(a=n.getElementsByTagName(t)[0]).parentNode.insertBefore(f,a)},50))}(window,document,"script"),fbq("init","459313920860148"),fbq("track","PageView");

$$.addClick('.media-subscribe', function(){ $$.serviceGet('user.login'); });
		$$.addClick('.locals-button',function(){
			$$.serviceGet('locals.community-details', {
				community_link_id: this.dataset.localsCommunity,
				context: this.dataset.context
			});
		});
Rumble("play", {"resize":"auto16:9","opts":["skip_ga_load"],"autoNext":0,"rel":11,"video":"v1m1bmu","div":"videoPlayer","api":function(api) { $$.handlePlayerApi(api) }});
(function() {
	$$.rumblesVote={
		attach:function(elm){
			var buttons = ['.rumbles-vote-up, .rumbles-vote-down', elm];
			$$.addClick(buttons, function(){
				var clicked = this;
				if (clicked.classList.contains('active')) clicked = null;

				$$.rumblesVote.updateButtons(buttons, clicked);
				$$.servicePost('user.rumbles', {
					type: elm.getAttribute('data-type'),
					id: elm.getAttribute('data-id'),
					vote: clicked ? clicked.getAttribute('data-vote') : 0
				}, function() {
				    this.data ? elm.querySelector('.rumbles-count').textContent = this.data.score_formatted : $$.removeClass(clicked, 'active');
				});
			});
		},
		updateButtons:function(buttons, clicked) {
			$$.each($$.query(buttons), function() {
				this === clicked ? $$.addClass(this, 'active') : $$.removeClass(this, 'active');
			});
		}
	};

	var parent = (this != window && typeof this.html == "object") ? this.html : null;

	$$.each($$.query('.rumbles-vote', parent), function(){
		$$.rumblesVote.attach(this);
	});
}).call(this);
$$.addClick('.media-video-action-embed',function(){
	$$.serviceGet('media.embed',{video:"1m1bmu"});
});
$$.handlePlayerApi = function(api) {
	var b=document.body, c='theatre-mode', rm=api.getResizeMode(), p = $$.query('#vid_' + api.getCurrentVideo().id)[0],
		d=$$.query('#videoPlayer')[0], dt = $$.query('#theatreVideoPlayer')[0]

	var is_theatre_mode = false;

	api.on("theaterMode", function(do_theatre_mode) {
		is_theatre_mode = do_theatre_mode;

		if ( do_theatre_mode ) {
			b.classList.add(c); dt.appendChild(p); api.setResizeMode('full');
		} else {
			b.classList.remove(c); d.appendChild(p); api.setResizeMode(rm);
		}
	});

	api.on('resize', function() {
		if( is_theatre_mode ) {
			dt.style.maxHeight = Math.floor(Math.min(window.innerHeight * 0.85, dt.clientWidth * 9 / 16)) + "px";
		}
	});
}

$$.onDomReady(function(){
	var video_comments_el = $$.query('#video-comments')[0];

	if ( !video_comments_el ) return;

	$$.serviceGet("comment.list",{video:"1m1bmu"}, function() {
		video_comments_el.textContent = "";
		video_comments_el.appendChild(this.html);
	});
});
$$.serviceGet('media.banners',{video:"1m1bmu", page_type:"Premium", ad_system:"prebid", page_layout:"Default", pub:"3", load:"float"});
$$.include('https://securepubads.g.doubleclick.net/tag/js/gpt.js');
$$.addClick('.media-engage-share', function() {
	$$.serviceGet('media.share', {video:"1m1bmu"});
});
$$.addClick('.media-video-action-write', function() {
	$$.serviceGet('media.contribution', {video:"1m1bmu"});
});
!function(){var a=[];$$.togglePopShow=function(o,s){var t,e;if((s=s||[]).length){o.stopPropagation(),o.preventDefault();var n=s[0].classList.contains("pop-show");for(t=s.length;t--;)e=s[t],n?e.classList.remove("pop-show"):(e.classList.add("pop-show"),a.indexOf(e)<0&&a.push(e))}else for(e=o.target;e instanceof HTMLElement;){if(e.classList.contains("pop-show"))return;e=e.parentNode}for(t=a.length;t--;)e=a[t],s.indexOf(e)<0&&e.classList.remove("pop-show")},$$.addClick(window,function(o){$$.togglePopShow(o)})}();

$$.addClick('.main-menu-toggle', function(e) {
	$$.togglePopShow(e, [this, $$.query('#main-menu')[0]]);
})
$$.addServiceClick('.header-upload', 'user.login', {next: "/upload.php"});
$$.addClick('.header-search-submit',function(e){
	var i=$$.getByClass('header-search-field'),
		s=$$.getByClass('header-search-select'),
		v=i.value.trim();

	e.preventDefault();
	if(!$$.isVisible(i)){
		$$.togglePopShow(e, [i,s,$$.getByClass('header-search')]);
	}else{
		if ( v == "" ) {
			i.focus();
			return false;
		}

		var type = s.value.toLowerCase(),
			submit_button = e.target;

		if ( type == 'videos' ) {
			type = 'video';
		} else if ( type == 'channels' ) {
			type = 'channel';
		} else if ( type == 'user' ){
			submit_button.setAttribute("disabled", "");
			location = location.pathname + "?q="+encodeURIComponent(v);
			return false;
		}
		submit_button.setAttribute("disabled", "");
		location = "/search/" + type + "?q="+encodeURIComponent(v);
	}
	return false;
});
$$.user={"username":false,"logged_in":false};
addThemeSwitcher( '.js-theme-option' , '.js-theme-option-group' );
$$.addServiceClick('.header-user','user.login');
window.google_analytics_uacct='UA-44331619-1';
window.dataLayer=window.dataLayer||[];
function gtag(){dataLayer.push(arguments);}

gtag("js", new Date());
gtag("config","UA-44331619-1",{custom_map:{dimension1:"server",dimension2:"user",metric1:"prebid",metric2:"loadtime"},"server":"web10","user":"Guest",'transport_type':'beacon'});
gtag("event","web10",{"event_category":"ws","event_label":"US"});

$$.include('//www.googletagmanager.com/gtag/js?id=UA-44331619-1&ext=.js');
(function(){
var notification_el = $$.getByClass('news_notification');
var header_el = $$.getByClass('header');
var navs_el = $$.getByClass('navs');
var main_el = $$.query('body > main')[0];

var close_notify = function(){
	notification_el.style.display='none';
	header_el.style.top=0;
	navs_el.style.top='4rem';
	main_el.style.paddingTop='2rem';
	document.cookie="_nnc=3;path=/;max-age=2592000;secure;samesite";
};

$$.addClick('.news_close',function(){
	close_notify();
	window.removeEventListener('resize', move_layout);
	return false;
});

var move_layout = function() {
	var notification_height = notification_el.getBoundingClientRect().height;

	header_el.style.top = notification_height + 'px';
	navs_el.style.top = 'calc(4rem + ' + notification_height + 'px)';
	main_el.style.paddingTop = 'calc(2rem + ' + notification_height + 'px)';
}

move_layout();

window.addEventListener('resize', move_layout);
}());
$$.includedJSLibs={"main":1,"web_services":1,"events":1,"error":1,"facebook_events":1,"darkmode":1,"ui_header":1};$$.includedCSSLibs=[]</script><script async="" src="//ap.lijit.com/www/sovrn_beacon_standalone/sovrn_standalone_beacon.js?iid=13427905"></script> </body>
</html>
'''
RSP2 = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Amazon Sued for Selling &quot;Suicide Kits&quot; and the Allegations are HORRIFYING! Viva Clips - Rumble</title>
	<link rel="canonical" href="https://rumble.com/v1onhfm-amazon-sued-for-selling-suicide-kits-and-the-allegations-are-horrifying-viv.html">
<link rel="alternate" href="https://rumble.com/api/Media/oembed.json?url=https%3A%2F%2Frumble.com%2Fembed%2Fv1m1bmu%2F" type="application/json+oembed" title="Amazon Sued for Selling &quot;Suicide Kits&quot; and the Allegations are HORRIFYING! Viva Clips"><link rel="alternate" href="https://rumble.com/api/Media/oembed.xml?url=https%3A%2F%2Frumble.com%2Fembed%2Fv1m1bmu%2F" type="text/xml+oembed" title="Amazon Sued for Selling &quot;Suicide Kits&quot; and the Allegations are HORRIFYING! Viva Clips">
	<meta name="viewport" content="width=device-width,initial-scale=1" />
	<link rel="dns-prefetch" href="https://sp.rmbl.ws"><link rel="dns-prefetch" href="//imasdk.googleapis.com/"></head><body style="margin:0;padding:0">
<div id="player" style="width:100%;height:100%;overflow:hidden;position:absolute"></div>
<script type="text/javascript">!function(s,d){function a(){return(new Date).getTime()/1e3}var t,r,o,n,i,c,l,e="Rumble",b={F:0};(d=s[e]=s[e]||function(){d._.push(arguments)})._=d._||[],b.f={},b.b={};b.f["v1m1bmu"]={"fps":23.98,"w":1920,"h":1080,"u":{"mp4":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/c\/q\/N\/e\/cqNeg.caa.mp4","meta":{"bitrate":813,"size":46340113,"w":854,"h":480}},"webm":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/c\/q\/N\/e\/cqNeg.daa.webm","meta":{"bitrate":808,"size":46045321,"w":854,"h":480}}},"ua":{"mp4":{"360":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/c\/q\/N\/e\/cqNeg.baa.mp4","meta":{"bitrate":633,"size":36076638,"w":640,"h":360}},"480":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/c\/q\/N\/e\/cqNeg.caa.mp4","meta":{"bitrate":813,"size":46340113,"w":854,"h":480}},"720":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/c\/q\/N\/e\/cqNeg.gaa.mp4","meta":{"bitrate":1965,"size":111946468,"w":1280,"h":720}},"1080":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/c\/q\/N\/e\/cqNeg.haa.mp4","meta":{"bitrate":2698,"size":153655690,"w":1920,"h":1080}}},"webm":{"480":{"url":"https:\/\/sp.rmbl.ws\/s8\/2\/c\/q\/N\/e\/cqNeg.daa.webm","meta":{"bitrate":808,"size":46045321,"w":854,"h":480}}}},"i":"https:\/\/sp.rmbl.ws\/s8\/6\/c\/q\/N\/e\/cqNeg.OvCc.jpg","evt":{"v":"\/l\/view...1m1bmu.9xskxr","e":"\/l\/pte...1m1bmu.1e976ro","wt":0,"t":"\/l\/timeline...1m1bmu.cn.158mwt1"},"cc":[],"l":"\/v1onhfm-amazon-sued-for-selling-suicide-kits-and-the-allegations-are-horrifying-viv.html","r":1,"title":"Amazon Sued for Selling &quot;Suicide Kits&quot; and the Allegations are HORRIFYING! Viva Clips","author":{"name":"vivafrei","url":"https:\/\/rumble.com\/user\/vivafrei"},"player":false,"duration":455,"pubDate":"2022-10-19T02:17:53+00:00","loaded":1,"vid":97479462,"timeline":[0,0],"own":false,"mod":[],"restrict":[-3,0],"autoplay":0,"track":0,"live":0,"live_placeholder":false,"livestream_has_dvr":null,"a":{"timeout":-1,"u":"4","aden":[1,0,0],"ov":false,"ads":[],"a":".4.71v3.1m1bmu..qm.wl8gah","ae":".4.71v3.1m1bmu..qm.5hvpfw","ap":[false,0],"loop":[]},loaded:a()};if(!b.k){function f(o,e){return o.opts||(o.opts=[]),b.D(e,function(e,t){var r=o[t];switch(t){case"opts":o[t]=r.concat(e);break;case"ad_sys":o[t]=r?b.M(r,e):e;break;default:o[t]=e}}),o}function p(c,s,l){function u(){var e=c.v.src||c.v.currentSrc;return e=e.match(/blob:/)&&c.hls_js?c.hls_js.url||e:e}function f(){var e=u(),t=s.get();return c.current_video=s,t==e?0:t}var p;s.get=function(){return function(e,t){if(21192597==e.vid.vid)return t;var r,o=b.B(t),t=b.E(t);return e.vid.live||(r=0,e.vid.a&&(r=e.vid.a.u||0),o.u=r,o.b=0<e.bandwidth_track?1:0),t+"?"+b.C(o)}(c,s.url)};s.check=function(){return!f()},s.play=function(){l&&c.hls_js&&!p&&c.hls_js.startLoad(),p=!0},s.set=function(){if(l&&!b.I())return setTimeout(function(){s.set()},100),!1;var e,r,t,o,n,i=f(),d=0,a=0;i&&(p=!1,e=c.v,c.res=s.key,0<S&&(c.last_set_url==u()?(d=!e.paused,a=e.currentTime):0<c.video_time&&(a=c.video_time)),a&&!c.vid.live&&(c.ui.s.autoSeek=a),r=c,a=e,t=i,o=l&&Hls.isSupported(),r.hls_js&&r.hls_media_attached&&((n=r.hls_js).detachMedia(a),n.destroy(),r.hls_js=null),o?(n=r.hls_js=new Hls({capLevelToPlayerSize:!0,autoStartLoad:!1,manifestLoadingMaxRetry:6,levelLoadingMaxRetry:6}),r.j("hlsJsLoaded",n),n.on(Hls.Events.LEVEL_UPDATED,function(e,t){r.live=t.details.live}),n.loadSource(t),n.attachMedia(a),r.hls_media_attached=1):a.src=t,S++,c.last_set_url=i,e.load(),d&&(s.play(),e.play()))}}function g(e){return H.hasOwnProperty(e)?H[e]:e}function h(r,e,o){var n,t;if(!r.style&&r.length)for(t=0;t<r.length;t++)h(r[t],e,o);else b.D(e,function(e,t){n=g(t),o&&""!==r.style[n]||(r.style[n]=g(e))})}function v(){var e=G;G={},y=0,b.D(e,function(e){"function"==typeof e&&e()})}function m(e){var i,o={play:"#fff",scrubber:"#75a642",hover:"#fff",background:"#303030",hoverBackground:"#699c39"},d=this,n=-1,c=(b.D(e,function(e,t){d[t]=e}),d.hasima=1,d.hasInit=0,d.rpcl=(d.id?d.id+"-":"")+"Rumble-cls",d.rpcls="."+d.rpcl,d.bandwidth_track=0,{}),a=(d.addEvent=function(e,t,r){c[r=r||1]||(c[r]={}),c[r][e]||(c[r][e]=[]),c[r][e].indexOf(t)<0&&c[r][e].push(t);r="addEvent";e!=r&&d.j(r,e)},d.removeEvent=function(e,t,r){c[r=r||1][e]&&(r&&!t?c[r][e]=[]:(t=c[r][e].indexOf(t),c[r][e].splice(t,1)))},d.hasEventListener=function(r){return b.D(c,function(e,t){if(e[r]&&0<e[r].length)return!0})},d.j=function(r,o,n){var i,d,a=[];return b.D(c,function(e,t){if(e[r]&&(n&&n==t||!n))for(d=e[r],i=0;i<d.length;i++)"function"==typeof o&&(o=o()),a.push(d[i](o))}),a},d.triggerError=function(e,t){d.j("error",{code:e,message:t})},d.l1=function(e,t,r){},d.getSetting=function(e,t){var r=!1;return d.vid&&d.vid.player&&d.vid.player[e]&&(e=d.vid.player[e],t&&e[t]&&(r=e[t]),t||(r=e)),r=!r&&o[t]?o[t]:r},d.loadVideoStyles=function(e){var t,r,o,n="vid_"+d.vid.id;d.rpcls;d.p.id=n,d.vars.opts.title&&d.vid.title&&(i.innerHTML=d.vid.title,i.href=b.L(d.vid.l,"rumble.com"),b.w(i,{outline:0,display:"block",18:"linear-gradient(rgba(0,0,0,.7),rgba(0,0,0,0))",textShadow:"rgba(0,0,0,0.5) 0px 0px 2px",padding:"9px",fontSize:"18px",whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis",position:"absolute",top:0,left:0,right:0}),b.x(i,{textDecoration:"underline"},{textDecoration:"none"})),d.bp&&(n=d.getSetting("colors","play"),t=d.getSetting("colors","hover"),r=d.getSetting("colors","background"),o=d.getSetting("colors","hoverBackground"),b.x(d.bp,{color:t,background:o,borderColor:o},{color:n,background:r,borderColor:r},d.bp_svg),d.bp.style.opacity=1)},d.trackBandwidth=function(e){var t=d.bandwidth_track;(e=d.server.bw_tracking?e:0)!=t&&(d.bandwidth_track=e,d.current_video&&!d.m&&d.current_video.set())},d.loadVideo=function(e,t){var r,o=(e="object"!=typeof e?{id:e}:e).id;if(b.b[o]&&(d.vars.playlist||(d.vars.playlist=b.b[o]),o=b.b[o][0]),d.hasInit||(d.hasInit=1,b.c(["ui","custom_ui"],function(){for(var e=0;e<b.d.length;e++)b.d[e](d.id)})),!t)return b.e(o,function(){d.loadVideo(e,1)},{ad_count:d.ad_count||null});if(b.f[o].loaded<9){if(d.triggerError("load","Unable to load video "+o),t)throw"Unable to load video "+o;return 2}if(b.f[o].cfg=e,b.f[o].plays=0,(r=b.f[o]).restrict&&!a(r.restrict)&&(d.triggerError("restricted","Video is restricted"),b.f[o].restricted=!0,d.j("restricted",o),b.f[o].ua=0),r.id=o,d.vid=r,d.live=2==d.vid.live,d.video_list=0,d.current_video=0,n<0&&(n=(d.vars.opts.noads||d.server.bw_ourads_check&&d.vars.opts.norumbleads)&&r.a?1:0),d.trackBandwidth(r&&r.track||n?1:0),!r.restricted&&r.ua&&(d.video_list=b.G(d,r.ua),b.H(d),d.loadVideoStyles()),b.g(d),d.j("loadVideo",r),b.h(d,1),r.restricted&&t)throw"Video "+o+" is restricted"},function(e){var t,r,o,n,i=document,d=!1;if(!e||e[0]<=-3)return!0;r=e[0],o=e[1];try{t=parent!==s?i.referrer||parent.location.href:i.location.href}catch(e){}if(!t)return parent===s;if(t=t.match(/^https?\:\/\/([^\/?#]+)(?:[\/?#]|$)/i))for(t=t[1].split(".");2<=t.length&&!d;)n=t.join("."),-1<o.indexOf(n)&&(d=!0),t.shift();return r!=d}),e=d.rpcl,t="metadata";(d.vars.opts.minimal||d.vars.opts.nopreload)&&(t="none"),d.vars.quality&&(d.res=parseInt(d.vars.quality)),e=b.i('<div class="'+e+'" allowfullscreen tabindex="-1" style="outline: none;"><video muted playsinline hidefocus="hidefocus" style="width:100% !important;height:100% !important;display:block" preload="'+t+'"'+(d.vars.opts.cc?' crossorigin="anonymous"':"")+'></video><div style="display:flex;opacity:0" class="bigPlayUI ctp"><a style="display:none" target=_blank rel=noopener></a><div class="bigPlayUIInner ctp" style="display:none"></div></div></div>'),b.w(e,{2:4,9:17,10:17,18:16,color:15,clear:"both",overflow:"visible"}),b.j.c(e,"bplay","block",".bigPlayUIInner"),d.d.appendChild(d.p=e),d.v=e.firstChild,function(e){if(!b.A){var t,r="canPlayType",o='video/mp4; codecs="avc1.42E01E',n=[0,o+'"',0,o+', mp4a.40.2"',1,'video/webm; codecs="vp9, vorbis"',2,"application/vnd.apple.mpegurl"],i=[!1,!1,!1];if(!e||!e[r])return;for(t=0;t<n.length;t+=2)e[r](n[t+1])&&(i[n[t]]=!0);b.J=i[2],b.A=i}}(d.v),d.rsz=[0,0],d.bp=e.childNodes[1],d.bp_svg=d.bp.childNodes[1],d.hasStyle={},i=d.bp.childNodes[0],b.w(d.bp_svg,{fill:"currentColor",9:8,12:"14px 22px",cursor:"pointer",borderRadius:"8px"}),b.w(d.bp,{display:"flex",opacity:0,position:"absolute",top:0,left:0,width:"100%",height:"100%",cursor:"pointer",alignItems:"center",justifyContent:"center",overflow:"hidden"}),d.v.addEventListener("contextmenu",function(e){return e.preventDefault(),!1}),d.loadVideoStyles()}var _,S,y,P="https://rumble.com",e="/embedJS/u4",w=(b.l=a(),s.RumbleErrorHandler||(l=0,s.RumbleErrorHandler=function(e){var t,r=e.message,o=e.filename,n=e.lineno,i=e.colno,d=D(o);o==d||r.match(/^Script error\./)||3<++l||(o=document.location+"",r=[D(o),l,r,d,n,i],e.error&&e.error.stack&&r.push(e.error.stack.split("\n").slice(1,3).join("\n")),d="/l/jserr?err="+encodeURIComponent(JSON.stringify(r)),o==r[0]&&(d=P+d),(t=document.createElement("img")).src=d,t.width=t.height=1,t.onload=t.onerror=function(){t.onload=null,t.onerror=null})},s.addEventListener("error",s.RumbleErrorHandler)),[]),x=(b.E=function(e){return e.split("?")[0]},b.B=function(e){var e=e.split("?"),r={};return e&&e[1]&&(e=e[1],new URLSearchParams(e).forEach(function(e,t){r[t]=e})),r},b.C=function(e){var r="";return b.D(e,function(e,t){r+=(r?"&":"")+encodeURIComponent(t)+"="+encodeURIComponent(e)}),r},b.D=function(e,t){var r,o;for(o in e)if(e.hasOwnProperty(o)&&void 0!==(r=t(e[o],o)))return r},b.K=function(e,t){if("undefined"==typeof localStorageBlocked)try{localStorageBlocked="undefined"==typeof localStorage||!localStorage}catch(e){localStorageBlocked=!0}if(void 0===t){if(!localStorageBlocked)try{t=localStorage.getItem(e)}catch(e){localStorageBlocked=!0}return localStorageBlocked?w[e]:parseInt(t)==t?parseInt(t):t}if(w[e]=t,!localStorageBlocked)try{return localStorage.setItem(e,t)}catch(e){localStorageBlocked=!1}return!1},b.L=function(e,t,r,o){if(e)if(!e.match(/^(http[s]?:)?\/\/([^/]*)\//)||r)return(o?"https:":"")+"//"+t+("/"!=e[0]?"/":"")+e;return e},b.M=function(e,t){return e.filter(function(e){return-1!==t.indexOf(e)})},[2,0,1]),C=["mp4","webm","hls"],H=(b.G=function(r,e){for(var o,t,n={},i=S=0;i<x.length;i++)e[o=C[t=x[i]]]&&(b.A[t]||"hls"==o)&&b.D(e[o],function(e,t){n.hasOwnProperty(t)||(e.key=t,n[t]=e,p(r,n[t],"hls"==o))});return n},b.I=function(){return"undefined"!=typeof Hls||(b.q(["hls"]),!1)},b.H=function(e){var r,o,n,i=480;e.res&&(i=e.res),e.vid.live&&!b.J&&b.I(),b.D(e.video_list,function(e,t){n=parseInt(t),"hls"!=r&&("hls"==t&&b.J||0<n&&n<=i&&(!r||r<n)?r=t:(!o||n<o&&0<n)&&(o=t))}),(r=r||o)&&e.video_list[r].set()},b.r=function(){var d={},a={},c={b:function(e,t,r){if("object"!=typeof e){if(d[e]&&!r)return!1;if(d[e]=t=t||1,a[e])for(;o=a[e].pop();)o(e,t);return!0}for(var o in e)c.b(o,e[o],r)},a:function(e,t,r){var o,n,i;for(r=r||{},o=0;i=e[o];o++)d[i]?r[i]=d[i]:(n&&(t=function(t,r){return function(e){c.a([t],r,e)}}(n[0],n[1])),n=[i,t]);n?(a[n[0]]||(a[n[0]]=[]),a[n[0]].push(function(e,t){r[e]=t,n[1](r)})):t(r)}};return c},n=b.r(),i=document,c={},b.s=function(e,t){var r,o,n=0;c[e]||(c[e]=1,(r=i.createElement("script")).type="text/javascript",r.src=e,t&&(r.addEventListener("load",o=function(e){if(n||t())return n=1;e&&setTimeout(o,50)},!1),o(1)),i.head.appendChild(r))},b.q=function(e,t){for(var r,o=0;o<e.length;o++)if("ima3"==e[o])b.s("https://imasdk.googleapis.com/js/sdkloader/ima3.js",function(){return!("undefined"==typeof google||!google||!google.ima)&&(n.b("ima3"),!0)});else if("custom_ui"!=e[o]){r=e[o];b.s(d.s.rd+"/j/p/"+r+("hls"!=r?".r2":"")+".js?_v=330",t)}},b.c=function(e,t,r){n.a(e,t),r||b.q(e)},d.rl=function(e,t){n.b(e)&&t&&t(b)},[0,1,"position","absolute","relative","fixed","normal","none","auto","width","height","margin","padding","border","display","#FFF","#000","100%","background","opacity"]),k=(b.w=h,b.y=function(e){var r={};return b.D(e,function(e,t){r[g(t)]=g(e)}),r},b.t=function(e,t,r,o,n,i,d,a){o||(o=e,n=t);var c="0",s="0";return a&&a.viewbox_top&&(c=a.viewbox_top),a&&a.viewbox_left&&(s=a.viewbox_left),i=i?" RumbleSVG-"+i:"",d=d||"",0<r.indexOf("stroke")&&(d+="stroke:currentColor;"),[e,t,'<svg style="'+d+'" class="RumbleElm'+i+'" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="'+e+'px" height="'+t+'px" viewBox="'+s+" "+c+" "+o+" "+n+'">'+r+"</svg>"]},b.j=b.r(),b.j.c=function(t,r,o,n){b.j.a([r],function(e){n&&(t=t.querySelectorAll(n)[0]),b.z(t,e[r][2]),o&&("string"==typeof o?t.style.display=o:o.apply(t))})},'<path stroke-width="3" stroke-linejoin="round" d="M19 11L3.2 1.5v19z"/>'),B=(b.j.b({bplay:b.t(25,25,k,22,22,"bplay"),play:b.t(22,22,k,0,0,"play","height:100%;"),loader:b.t(80,10,function(){for(var e,t="<g>",r=0;r<21;r++)t+='<circle cx="'+(10*r+5)+'" cy="5" r="'+(e=(e=r-6)<1||5<e?1:e)+'" />';return t+"</g>"}(),80,10)}),s.requestAnimationFrame?1:0),G={},O=(b.a=function(e,t){if(!G[e]&&"function"==typeof t&&(G[e]=t,!y)){if(y=1,!B)return setTimeout(v,1e3/24);s.requestAnimationFrame(v)}},b.i=function(e){e=b.u("div",0,0,e);return 1<e.childNodes.length?e.childNodes:e.firstChild},b.u=function(e,t,r,o){e=document.createElement(e);return o&&(e.innerHTML=o),t&&(e.className=t),r&&(e.id=r),E(e),e},b.z=function(e,t){e.innerHTML=t,j(e)},b.y({font:"12px sans-serif",fontWeight:6,lineHeight:6,boxSizing:"content-box",webkitBoxSizing:"content-box",19:1,18:7,11:0,12:0,border:7,9:8,10:8,visibility:"visible",textSizeAdjust:8,textDecoration:7})),E=function(e){var t;(t=e.tagName)&&"path"!=(t=t.toLowerCase())&&"video"!=t&&(h(e,O,!0),"svg"==t?h(e,{fill:"currentColor"},!0):(h(e,{color:"inherit"},!0),j(e)))},j=function(e){var t,r;if(t=e.childNodes)for(r=0;r<t.length;r++)E(t[r])};b.x=function(e,t,r,o){var n="__playerHover";(o=o||e)[n]||(e.addEventListener("mouseout",function(){h(o,o[n][0])}),e.addEventListener("mouseover",function(){h(o,o[n][1])})),o[n]=[r,t],h(o,r)};b.d=[];d.s={rd:P,ru:e,ds:f({opts:["title"]},[]),rp:P+e+"/?request=",server:{"bw_tracking":1,"bw_noads_check":1}};b.k={},d.gdpr=2,b.m=function(e,t,r,o){var n=new XMLHttpRequest;n.onreadystatechange=function(){4==n.readyState&&200==n.status&&t(JSON.parse(n.responseText))},n.open("GET",(o?"":d.s.rp)+e),n.send()},b.e=function(e,t,r){var o,n,i,d=[];for("object"!=typeof e&&(e=[e]),o=0;o<e.length;o++)n=e[o],(!b.f[n]||1<b.f[n].loaded&&b.f[n].loaded+(1==e.length?900:1800)<a())&&(b.f[n]={loaded:0,wait:[]}),0==(i=b.f[n]).loaded&&(d.push(n),i.loaded=1),t&&i.loaded<9&&i.wait.push(t);return 0<d.length?(r=r?"&ext="+encodeURIComponent(JSON.stringify(r)):"",r+="&ad_wt="+(b.K("ad_wt")||0),b.m("video&ver=2&v="+d[0]+r,function(e){var t,r,o=[],n={};for(e.loaded||!e?n[d[0]]=e:n=e,b.D(n,function(e,t){for(;r=b.f[t].wait.pop();)o.indexOf(r)<0&&o.push(r);e&&(b.f[t]=e,b.f[t].loaded=a())}),t=0;t<o.length;t++)o[t]()}),1):(t&&t(),0)},d.resize=function(){b.D(b.k,function(e){b.h(e)})},b.h=function(e,t){var r,o=!e.rsz,n=[e.p.clientWidth,e.p.clientHeight],i=s.innerHeight,d=e.vars;d.resize||(d.resize=function(){try{return s.self!==s.top}catch(e){return!0}}()?"full":"auto");(!o&&(e.rsz[0]!=n[0]||e.rsz[1]!=n[1])||n[1]>i||t)&&(t=d.resize,d.ia&&(t="ia"),e.ui&&e.ui.isFloating&&(t="auto"),r=Math.floor(n[0]/16*9),"ia"==t?screen&&screen.height<r&&(r=screen.height):"full"==t?r=0:"window"==t?r=i:("ctpauto"==t&&e.ui&&e.ui.ctp&&(d.resize="auto"),(i<r||e.ui&&e.ui.getFullScreen())&&(r=0)),"window"!=t&&"ctpauto"!=t&&"auto16:9"!=t&&"full"!=t&&(e.vid&&e.vid.a&&e.vid.a.aden&&e.vid.a.aden[2])&&r<360&&0!=r&&!d.float&&(r=360),e.rsz[0]!=n[0]&&(o=1),n[1]!=r&&(o=1,e.p.style.height=0<r?(n[1]=r)+"px":"100%")),e.rsz&&!o||(e.rsz=n),o&&(b.g(e),e.j("resize"))},b.g=function(e){if(!(!e.vid||e.ui&&e.ui.hasPlayed)){var t,r,o,n=e.vid.i,i=e.vid.t,d=-1,a=e.rsz[0],c=e.rsz[1],s=a/c;if(i)for(t=0;t<i.length;t++)o=s<(o=(r=i[t]).w/r.h)?(c-a/o)*a:(a-c*o)*c,(d<0||o<d)&&(d=o,n=r.i);e.v.poster!=n&&(e.v.poster=n)}},d.$play=function(e,t){var r,o,n=JSON.parse(JSON.stringify(d.s.ds)),i={};if((n=f(n,e)).opts&&(b.D(n.opts,function(e){i[e]=1}),n.opts=i),void 0===n.gdpr?n.gdpr=2:n.gdpr=n.gdpr?1:0,2!=n.gdpr&&(d.gdpr=n.gdpr),b.n=-1==n.analytics||n.opts.minimal?1:0,b.o=n.opts.skip_ga_load?1:0,b.p=n.opts.force_ga_load?1:0,!n.div){if(!_)throw"No div was defined for the player";n.div=_}if(_=o=n.div,!b.k[o]||(r=b.k[o]).d.parentNode||(r=0),n.macros||(n.macros={}),!r){if(!(r=document.getElementById(o))){if(2<t)throw o+" div not found";s.addEventListener("DOMContentLoaded",function(){d.$play(e,3)})}b.k[o]||b.F++,b.k[o]=r=new m({d:r,vid:0,id:o,vars:n,server:d.s.server})}r.loadVideo(n.video),b.h(r)};d.rl("custom_ui");d.$playSettings=function(e){d.s.ds=f(d.s.ds,e)},s.addEventListener("resize",function(){b.a("resize",d.resize)}),s.addEventListener("orientationchange",function(){setTimeout(function(){d.resize()},500)});var z,L,I,R=s.Rumble;for(R._=z=R._||[],z.push=function(e){var t=z.slice.call(e),r=R["$"+t.shift()];"function"==typeof r?r.apply(R,t):t.push.call(z,e)},L=-1,I=z.length;++L<I;)z.push(z.shift())}function D(e){if(!e)return e;var t=e.match(new RegExp("http[s]?://[^/]*rumble.com(/.*)$"));return t?t[1]:e}}(window);
Rumble("play", {"video":{"id":"v1m1bmu"},"div":"player","resize":"full","opts":["force_ga_load"]});</script>
</body></html>
'''

class RumbleTestCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.server = ResponsesServer(
            responses_kwargs={'registry': OrderedRegistry})
        self.server.start()
        self.server.get(
            self.server.url(),
            headers={'Content-Type': 'text/html'},
            body=RSP0)
        self.server.get(
            self.server.url('/v1onhfm-amazon-sued-for-selling-suicide-kits-and-the-allegations-are-horrifying-viv.html'),
            headers={'Content-Type': 'text/html'},
            body=RSP1)
        self.server.get(
            self.server.url('/embed/v1m1bmu/'),
            headers={'Content-Type': 'text/html'},
            body=RSP2)
        self.crawler = RumbleCrawler()

    def tearDown(self):
        self.server.stop()

    async def test_crawl(self):
        channel, videos = await self.crawler.crawl(self.server.url())
        videos = [v async for v in videos]