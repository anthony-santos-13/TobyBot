import os
from bets import Bookie
from typing import List
import utils

class Polls():
    def __init__(self):
        pass

    def initialize(self):
        cwd = os.getcwd()
        self.file_base_path = cwd + "\\packages\\TobyBot\\files\\"
        self.poll_dict = self._read_poll_dict(self.file_base_path)

    def _read_poll_dict(self, file_base_path):
        file = 'polls.yml'
        try:
            dict = utils.get_dict_from_yaml(file_base_path + file)
        except:
            dict = {}
        return dict

    def add_new_poll(self, poll_label: str, option_one: str, option_two: str):
        new_poll_dict = {poll_label: {option_one : [], 
                                      option_two: []}}
        self.poll_dict.update(new_poll_dict)
        self._announce_poll()

    def _announce_poll(self):
        # announce options

        # update poll_dict with message id
        pass

    def close_poll(self, poll_label):
        self._read_poll_response(poll_label)

        poll_result = 'test1'
        winner_list = self._identify_poll_winners(poll_label, poll_result)
        return winner_list

    def _read_poll_response(self, poll_label):
        # get votes from announce_poll message id
        # update poll dict option value lists with emote response
        pass

    def _identify_poll_winners(self, poll_label: str, poll_result: str):
        winner_list = self.poll_dict.get(poll_label).get(poll_result)
        print('and the winners are ' + str(winner_list))
        return winner_list