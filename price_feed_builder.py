import operator

import time
from typing import Any, TypeVar, Type, cast

from builder.javascript_builder import build_dr_js
from coin_gecko.api import coin_list, coin_data
from coin_gecko.util import load_csv_file
from coin_gecko import exchange_sources as exchanges

from menu.gui import fixed_length_text, blue_text, green_text, red_text, yellow_text

VERSION = '0.0.1'
DEFAULT_PAUSE = 0.05

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


legacy_currencies = {'usd': {'name': 'United States Dollar'}, 'euro': {'name': 'Euro'}}


def load_legacy_currencies():
    currency_rows = load_csv_file('data/legacy_currencies.csv')
    row_index = 0
    # data by currency code

    for row in currency_rows:
        # skip header
        if row_index > 1:
            print(row)
        row_index += 1
    return currency_rows


def check_if_legacy_currency(symbol):
    if symbol == '':
        ...

    currencies = load_legacy_currencies()

    for currency in currencies:
        print(currency[3])


def check_symbol(symbol: str):
    if symbol == '':
        ...


def check_pair(coin_list_dict: dict, symbol_0: str, symbol_1: str):

    menu_width = 64
    print(f'{fixed_length_text("   ├", width=menu_width, fill="─")}┐', )

    pre_print = '   ├'

    def _check_symbol(symbol):
        print(f"{fixed_length_text(f'   │ Checking for {symbol}...', width=menu_width)}│")
        time.sleep(.1)
        _coin = {}
        time.sleep(DEFAULT_PAUSE)
        if symbol in legacy_currencies:
            print(f"{fixed_length_text(f'   │ Warning: {symbol} is a legacy currency.', width=menu_width)}│")

            time.sleep(DEFAULT_PAUSE)
            print(f"{fixed_length_text(f'   │  (Euro, United States Dollar, etc...)', width=menu_width)}│")

            _coin = legacy_currencies[symbol]
        elif symbol in coin_list_dict:
            if len(coin_list_dict[symbol]) > 1:
                time.sleep(DEFAULT_PAUSE)
                print(f"{fixed_length_text(f'   │ Multiple Coins/Tokens with symbol {symbol}', width=menu_width)}│")

                time.sleep(DEFAULT_PAUSE)
                coin_index = 0
                for coin in coin_list_dict[symbol]:
                    _line = f'{pre_print} [{coin_index}] {coin["name"]}'

                    print(f"{fixed_length_text(f'{_line}', width=menu_width)}│")
                    coin_index += 1
                print(f'{fixed_length_text("   ├", width=menu_width, fill="─")}┘', )
                selected = input(f'{pre_print}─ witnet:$» ')
                print(f'{fixed_length_text("   ├", width=menu_width, fill="─")}┐', )
                _coin = coin_list_dict[symbol][int(selected)]
                _line = f'{pre_print} {_coin["name"]} selected.'
                print(f"{fixed_length_text(f'{_line}', width=menu_width)}│")
            if len(coin_list_dict[symbol]) == 1:
                coin_name = coin_list_dict[symbol][0]["name"]
                time.sleep(DEFAULT_PAUSE)
                print(f"{fixed_length_text(f'{pre_print} Found {coin_name}', width=menu_width)}│")
                time.sleep(DEFAULT_PAUSE * 2)
                time.sleep(DEFAULT_PAUSE * 2)
                _coin = coin_list_dict[symbol][0]

        return _coin

    coin_0 = _check_symbol(symbol_0)
    coin_1 = _check_symbol(symbol_1)
    time.sleep(DEFAULT_PAUSE)
    line = f'   │ Contiue with {coin_0["name"]} / {coin_1["name"]}? [y/n]'
    print(f"{fixed_length_text(f'{line}', width=menu_width)}│")
    print(f'{fixed_length_text("   ├", width=menu_width, fill="─")}┘', )
    confirmed = input(f'   ├─ {green_text("witnet")}:$» ')
    _yes = ['y', 'yes', ]
    if confirmed.lower() in _yes:
        print(f'{fixed_length_text("   ├", width=menu_width, fill="─")}┐', )

        _coin_data = coin_data(coin_0["id"])
        markets = []
        tickers = {}
        for ticker in _coin_data['tickers']:
            # if ticker['target'].lower() == symbol_1:
            markets.append(ticker)

        for market in markets:
            if market['market']['identifier'] in exchanges:
                tickers[market['market']['identifier']] = market

        ticker_by_volume = {}
        for ticker in tickers:
            ticker_by_volume[ticker] = tickers[ticker]['volume']

        ticker_by_volume = sorted(ticker_by_volume.items(), key=operator.itemgetter(1), reverse=True)

        m_idx = 0
        line = f'{pre_print}───  {symbol_0}/{symbol_1} Markets sorted by Volume ──'
        print(f"{fixed_length_text(f'{line}', width=menu_width)}│")
        for t in ticker_by_volume:
            print(f"{fixed_length_text(f'{pre_print} [{m_idx}] {t} ', width=menu_width)}│")

            m_idx += 1
        local_markets = {}

        for t in markets:
            _pair = f'{t["base"]}/{t["target"]}'
            if _pair in local_markets:
                local_markets[_pair].append(t["market"]["name"])
            else:
                local_markets[_pair] = [t["market"]["name"]]

            _str = f'{t["base"]}/{t["target"]} {t["market"]["name"]}'

        print(f"{fixed_length_text(f'{pre_print} multiple seperated by commas, e.g. 1,2,3', width=menu_width)}│")

        print(f'{fixed_length_text("   ├", width=menu_width, fill="─")}┘', )
        chosen_markets = input(f'{pre_print} Enter Sources:$» ')

        chosen_market_indexes = [int(x) for x in chosen_markets.strip(' ').split(',')]

        sources = []
        for x in chosen_market_indexes:
            idx = ticker_by_volume[x]

            if idx[0] in exchanges:
                sources.append(exchanges[idx[0]])
            else:
                ...
        build_dr_js(sources, symbol_0, symbol_1)


def new_price_feed():
    # menu_width = 64
    sub_width = 37
    print(f'{fixed_length_text("   ├", width=sub_width, fill="─")}┐', )
    time.sleep(DEFAULT_PAUSE)
    print(f'{fixed_length_text("   │ Enter Price Pair (e.g. BTC/USD)", width=sub_width)}│', )
    time.sleep(DEFAULT_PAUSE)
    print(f'{fixed_length_text("   ├", width=sub_width, fill="─")}┘', )

    price_pair = input('   ├─ witnet:$» ')
    if '/' in price_pair:
        token_0, token_1 = price_pair.split('/')
        _coin_list = coin_list(by_symbol=True)
        check_pair(_coin_list, token_0, token_1)

    else:
        print('invalid input. exiting...')


def coin_snapshot():

    print('Total Coins:')
    coins = coin_list()
    coin_map = {}

    for coin in coins:
        coin_map[coin['id']] = {
            'symbol': coin['symbol'],
            'name': coin['name'],
        }

    idx = 1
    total_coins = len(coin_map.keys())

    for coin in coin_map.keys():
        if idx > 3100:
            _data = coin_data(coin)
            print(f"[{idx}/{total_coins}={idx/total_coins}][{coin}][tickers:{len(_data['tickers'])}]")
            time.sleep(1)
        idx += 1
    ...


def exit_program():
    exit()


def help_menu():
    ...


def print_app_header():
    print('╔════════════════════════════════════════════════╗')
    print('║ Witnet Price Feed Builder      (Version 0.0.1) ║')
    print('╚════════════════════════════════════════════════╝')


def numeric_menu(menu_name, menu_items, menu_size, func_map):
    def _printer(options: list):
        idx = 1
        print(f"{fixed_length_text(f' │ {menu_name}', width=menu_size)}│")
        for option in options:
            print(f"{fixed_length_text(f' │ [{idx}] {option}', width=menu_size)}│")
            time.sleep(DEFAULT_PAUSE)
            idx += 1
    _printer(menu_items)

    ...


def main_menu():
    main_menu_size = 24
    print_app_header()

    def _printer(options: list):
        idx = 1
        print(f"{fixed_length_text(f' │ Main Menu', width=main_menu_size)}│")
        for option in options:
            print(f"{fixed_length_text(f' │ [{idx}] {option}', width=main_menu_size)}│")
            time.sleep(DEFAULT_PAUSE)
            idx += 1

    _printer(['New Price Feed', 'Coin Snapshot', 'Exit', 'Help'])
    print(f"{fixed_length_text(f' └─┬', width=main_menu_size, fill='─')}┘")
    time.sleep(DEFAULT_PAUSE)

    menu_options = {
        1: new_price_feed,
        2: coin_snapshot,
        3: exit_program,
        4: help_menu,
    }
    menu_select = input('   ├─ witnet:$» ')

    try:
        menu_options[int(menu_select)]()
    except ValueError as value_error:
        print(type(value_error))
        print(value_error.args[0])
        print(f'   ├─> ValueError({value_error.args[0]})\n exiting...')


if __name__ == '__main__':
    main_menu()

