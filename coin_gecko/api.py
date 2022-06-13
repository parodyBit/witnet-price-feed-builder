import json
import os
from typing import Any

import requests
from datetime import datetime

from coin_gecko.models.coin import Coin
from coin_gecko.util import save_json_file
from dataclasses import dataclass

gecko_base_url: str = 'https://api.coingecko.com/api/v3'


def _gecko_request(method: str):
    return requests.get(f'{gecko_base_url}/{method}')


def asset_platforms(save_to_json: bool = True) -> Any:
    """
    :param save_to_json:
    :return:
    """
    response = _gecko_request("asset_platforms")
    data = json.loads(response.text)
    if save_to_json:
        date = datetime.today().strftime('%Y-%m-%d')
        save_json_file(data=data, file_name=f'data/gecko/asset_platforms_{date}.json')
    return data


def coin_list(by_symbol=False) -> dict:
    url = _gecko_request("coins/list?include_platform=true")
    text = url.text
    data = json.loads(url.text)
    # print(text)
    date = datetime.today().strftime('%Y-%m-%d')
    save_json_file(data=data, file_name=f'data/coin_gecko/coin_list_{date}.json')
    data_by_symbol = {}
    for coin in data:
        symbol = coin['symbol']
        if symbol in data_by_symbol:
            data_by_symbol[symbol].append(coin)
        else:
            data_by_symbol[symbol] = [coin]

        # print(coin['id'])

    # print(data[0].keys())

    if by_symbol:
        return data_by_symbol
    else:
        return data


def coin_data(coin_id: str):
    url = _gecko_request(f"coins/{coin_id}")
    text = url.text

    data = json.loads(url.text)

    # make coin directory
    parent_dir = 'data/gecko/coins'
    path = os.path.join(parent_dir, f"{coin_id[0]}/{coin_id}")

    if not os.path.isdir(path):
        os.makedirs(path)

    # save coin data to json
    coin = Coin.from_dict(data)
    save_json_file(data=coin.to_dict(), file_name=f'{path}/{coin_id}.json')

    if 'tickers' in data:
        tickers = data['tickers']
        print_tickers = False
        if print_tickers:
            t_str = ''
            for t in tickers:
                dat = f'{t["market"]["name"]} {t["base"]} {t["target"]}'

                print(dat)
    # print(data)
    # print(data.keys())

    return data


def save_image(url, local_file):
    import urllib.request
    urllib.request.urlretrieve(url=url, filename=local_file)
