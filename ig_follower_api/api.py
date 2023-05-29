import requests

class IgAPIClient(object):

    ROOT_URL = 'https://www.instagram.com/api/v1'
    
    def __init__(self, cookie:str, x_asbd_id:str, x_csrftoken:str, x_ig_app_id:str, x_ig_www_claim:str, session=None) -> None:
        
        self._session = session if session else requests.Session()
        
        self.cookie = cookie
        self.x_asbd_id = x_asbd_id
        self.x_csrftoken = x_csrftoken
        self.x_ig_app_id = x_ig_app_id
        self.x_ig_www_claim = x_ig_www_claim
        
        self.headers = {
            'cookie': fr'{cookie}',
            # 'referer': 'https://www.instagram.com/{username}/{action}/',
            'sec-ch-ua': '"Brave";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'x-asbd-id': x_asbd_id,
            'x-csrftoken': x_csrftoken,
            'x-ig-app-id': x_ig_app_id,
            'x-ig-www-claim': x_ig_www_claim,
            'x-requested-with': 'XMLHttpRequest',
        }

    def user_data(self, username:str) -> requests.Response:
        path = f'/users/web_profile_info/?username={username}'
        return self._request(path)
    
    def user_id(self, username: str) -> int:
        user_data = self.user_data(username)
        user_id = user_data['data']['user']['id']
        return user_id
        
    def followers(self, user_id:str, count:int = 12) -> requests.Response:
        '''Only owner of account can see all followers
        
        ## TODO
        - Page parsing
        '''
        path = f'/friendships/{user_id}/followers/?count={count}&page_size=10&search_surface=follow_list_page'
        return self._request(path)
    
    def following(self, user_id:str, count:int = 12) -> requests.Response:
        path = f'/friendships/{user_id}/following/?count={count}'
        return self._request(path)

    def _request(self, path:str) -> requests.Response:
        url = self.ROOT_URL + path
        return self._session.get(url=url, headers=self.headers)
