import requests, pickle, os
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote, parse_qs
import pandas as pd
import json
from re import search

ayristir = lambda berisi, gerisi, yazi : search(f'{berisi}(.*){gerisi}', yazi).group(1)

class FacebookError(Exception):
    pass


class FacebookPostsScraper:
    def __init__(self, email, password, post_url_text="Full Story"):
        self.email = email
        self.password = password
        self.headers = {
            "User-Agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
        }
        self.session = requests.session()
        self.cookies_path = (
            "session_facebook.cki"
        )

        # - English: 'Full Story'
        # - Spanish: 'Historia completa'
        self.post_url_text = post_url_text

        if self.new_session():
            self.login()

        self.posts = []

    def new_session(self):
        if not os.path.exists(self.cookies_path):
            return True

        f = open(self.cookies_path, "rb")
        cookies = pickle.load(f)
        self.session.cookies = cookies
        return False

    def make_request(self, url, method="GET", data=None, is_soup=True):
        if len(url) == 0:
            raise FacebookError(f"Empty Url")

        if method == "GET":
            resp = self.session.get(url, headers=self.headers)
        elif method == "POST":
            resp = self.session.post(url, headers=self.headers, data=data)
        else:
            raise FacebookError(f"Method [{method}] Not Supported")

        if resp.status_code != 200:
            raise FacebookError(f"Error [{resp.status_code}] > {url}")

        if is_soup:
            return BeautifulSoup(resp.text, "lxml")
        return resp

    def login(self):
        url_home = "https://m.facebook.com/"
        soup = self.make_request(url_home)
        if soup is None:
            raise FacebookError("Couldn't load the Login Page")

        soup = self.make_request(
            url     = "https://m.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fm.facebook.com%2F&lwv=100&refid=8",
            method  = "POST",
            data    = {
                "lsd": soup.find("input", {"name": "lsd"}).get("value"),
                "jazoest": soup.find("input", {"name": "jazoest"}).get("value"),
                "m_ts": soup.find("input", {"name": "m_ts"}).get("value"),
                "li": soup.find("input", {"name": "li"}).get("value"),
                "try_number": soup.find("input", {"name": "try_number"}).get("value"),
                "unrecognized_tries": soup.find("input", {"name": "unrecognized_tries"}).get("value"),
                "email": self.email,
                "pass": self.password,
                "login": "Iniciar sesión",
                "prefill_contact_point": "",
                "prefill_source": "",
                "prefill_type": "",
                "first_prefill_source": "",
                "first_prefill_type": "",
                "had_cp_prefilled": "false",
                "had_password_prefilled": "false",
                "is_smart_lock": "false",
                "_fb_noscript": "true",
            },
            is_soup = True
        )
        if soup is None:
            raise FacebookError(f"The login request couldn't be made: login_url")

        redirect = soup.select_one("a")
        if not redirect:
            raise FacebookError("Please log in desktop/mobile Facebook and change your password")

        url_redirect = redirect.get("href", "")
        resp = self.make_request(url_redirect)
        if resp is None:
            raise FacebookError(f"The login request couldn't be made: {url_redirect}")

        cookies = self.session.cookies
        f = open(self.cookies_path, "wb")
        pickle.dump(cookies, f)

        return {"code": 200}

    def get_posts_from_list(self, profiles):
        data = []

        for say, profil in enumerate(profiles, start=1):
            print(f"{say}/{len(profiles)} | {profil}")

            posts = self.get_posts_from_profile(profil)
            data.append(posts)

        return data

    def get_posts_from_profile(self, url_profile):
        if "www." in url_profile:
            url_profile = url_profile.replace("www.", "m.")
        if "v=timeline" not in url_profile:
            if "?" in url_profile:
                url_profile = f"{url_profile}&v=timeline"
            else:
                url_profile = f"{url_profile}?v=timeline"

        is_group = "/groups/" in url_profile

        soup = self.make_request(url_profile)
        if soup is None:
            print(f"Couldn't load the Page: {url_profile}")
            return []

        css_profile = ".storyStream > div"
        css_page = "#recent > div > div > div"
        css_group = "#m_group_stories_container > div > div"
        raw_data = soup.select(f"{css_profile} , {css_page} , {css_group}")

        for item in raw_data:
            published = item.select_one("abbr")
            description = item.select("p")
            images = item.select("a > img")
            _external_links = item.select("p a")
            post_url = item.find("a", text=self.post_url_text)
            like_url = item.find("a", text="Beğen")

            if published is not None:
                published = published.get_text()
            else:
                published = ""

            if len(description) > 0:
                description = "\n".join([d.get_text() for d in description])
            else:
                description = ""

            images = [image.get("src", "") for image in images]

            if post_url is not None:
                post_url = post_url.get("href", "")
                if len(post_url) > 0:
                    post_url = f"https://www.facebook.com{post_url}"
                    p_url = urlparse(post_url)
                    qs = parse_qs(p_url.query)
                    # print(qs)
                    if not is_group:
                        post_url = f'{p_url.scheme}://{p_url.hostname}{p_url.path}?story_fbid={qs["story_fbid"][0]}&id={qs["id"][0]}'
                    else:
                        post_url = f'{url_profile.split("?")[0].replace("m.", "")}/permalink/{ayristir("top_level_post_id.", ":tl_objid", qs["_ft_"][0])}'
            else:
                post_url = ""

            if like_url is not None:
                like_url = like_url.get("href", "")
                if len(like_url) > 0:
                    like_url = f"https://m.facebook.com{like_url}"
            else:
                like_url = ""

            external_links = []
            for link in _external_links:
                link = link.get("href", "")
                try:
                    a = link.index("u=") + 2
                    z = link.index("&h=")
                    link = unquote(link[a:z])
                    link = link.split("?fbclid=")[0]
                    external_links.append(link)
                except ValueError:
                    continue

            self.posts.append({
                "paylasim": published,
                "metin": description,
                # "images": images,
                "link": post_url,
                # "external_links": external_links,
                # "like_url": like_url,
            })

        return self.posts
