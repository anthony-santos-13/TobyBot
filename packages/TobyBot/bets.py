from typing import Dict, List
import utils
import os


class Bookie():
    def __init__(self):
        pass

    """Bookie maintains, processes, and organizes the betting within the channel."""

    def initialize(self):
        cwd = os.getcwd()
        self.file_base_path = cwd + "\\packages\\TobyBot\\files\\"
        self.bank_dict = self._read_bank_dict(self.file_base_path)

        print('hello')
        pass

    def _read_bank_dict(self, file_base_path: str) -> Dict:
        # check if file exists - if not, make it
        file = 'bank.yml'
        dict = utils.get_dict_from_yaml(file_base_path + file)
        return dict

    def _write_bank_dict(self):
        file = 'bank.yml'
        utils.write_dict_to_yaml(self.file_base_path + file, self.bank_dict)

    def _read_bets_dict(yaml_path):
        pass

    def update_member_funds(self, name: str, fund_update: int):
        current_fund = self.bank_dict.get(name)
        if not current_fund:
            current_fund = 0
        new_fund = current_fund + fund_update
        self.bank_dict.update({name: new_fund})

        # write to bank yml
        self._write_bank_dict()

    def check_member_funds_exist(self, name, welcome_fund):
        if name not in [k for k in self.bank_dict]:
            self._grant_welcome_funds(name, welcome_fund)


    def _grant_welcome_funds(self, name, welcome_fund):
        self.update_member_funds(name, welcome_fund)

    def read_incoming_bet():
        pass

    def _check_bet_valid():
        pass

    def reward_winners(self, winner_list: List, reward):
        for winner in winner_list:
            self._update_member_funds(winner, reward)

    def get_member_funds(self, name):
        self._read_bank_dict
        current_fund = self.bank_dict.get(name)
        return current_fund