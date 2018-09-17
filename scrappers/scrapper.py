import logging
import requests
import networkx
import time
import collections
import json


logger = logging.getLogger(__name__)


class Scrapper(object):
    def __init__(self, skip_objects=None):
        self.skip_objects = skip_objects

    def get_friends_ids(self,user_id):
        friends_url = 'https://api.vk.com/method/friends.get?user_id={}&v=5.74&access_token=ac2900b3ac2900b3ac2900b3a4ac1d5169aac29ac2900b3f7a3a6bbd3410c4eabaa13f5&fields=bdate,last_name,city,sex,country'
        # также вы можете добавить access_token в запрос, получив его через OAuth 2.0
        json_response = requests.get(friends_url.format(user_id)).json()
        if json_response.get('error'):
            logger.info(json_response.get('error'))
            return list()

        with open('data.txt','w', encoding='utf-8') as file:
            json.dump(json_response[u'response'],file,ensure_ascii=False)
        return json_response[u'response']
    def scrap_process(self, storage):
        user_id = 5117073
        friend_ids = self.get_friends_ids(user_id)
        logger.info(friend_ids)
        for friend_id in friend_ids:
            logger.info(friend_id)


