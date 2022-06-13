def one_bch(token_0: str, token_1: str):
    # 1BCH
    raise NotImplementedError


def aave(token_0: str, token_1: str):
    # Aave
    raise NotImplementedError


def aax(token_0: str, token_1: str):
    # AAX
    raise NotImplementedError


def aax_futures(token_0: str, token_1: str):
    # AAX Futures
    raise NotImplementedError


def abcc(token_0: str, token_1: str):
    # ABCC
    raise NotImplementedError


def acdx(token_0: str, token_1: str):
    # ACDX
    raise NotImplementedError


def acdx_futures(token_0: str, token_1: str):
    # ACDX Futures
    raise NotImplementedError


def acsi_finance(token_0: str, token_1: str):
    # Acsi Finance
    raise NotImplementedError


def aex(token_0: str, token_1: str):
    # AEX
    return ('aex', f'''// Retrieves {token_1.upper()} price of {token_0.upper()} from AEX.ZONE
const aex = new Witnet.Source("https://api.aex.zone/v3/ticker.php?mk_type={token_1.upper()}&coinname={token_0.upper()}")
  .parseJSONMap()
  .getMap("data")
  .getMap("ticker")
  .getFloat("last")
  .multiply(10 ** 6)
  .round()''')


def agora_swap(token_0: str, token_1: str):
    # Agora Swap
    raise NotImplementedError


def algebra_finance(token_0: str, token_1: str):
    # Algebra finance
    raise NotImplementedError


def allcoin(token_0: str, token_1: str):
    # Allcoin
    raise NotImplementedError


def alpha_five(token_0: str, token_1: str):
    # Alpha5
    raise NotImplementedError


def altcointrader(token_0: str, token_1: str):
    # AltcoinTrader
    raise NotImplementedError


def alterdice(token_0: str, token_1: str):
    # AlterDice
    raise NotImplementedError


def altmarkets(token_0: str, token_1: str):
    # Altmarkets
    raise NotImplementedError


def anyswap(token_0: str, token_1: str):
    # Anyswap
    raise NotImplementedError


def apeswap(token_0: str, token_1: str):
    # ApeSwap
    raise NotImplementedError


def apeswap_polygon(token_0: str, token_1: str):
    # ApeSwap (Polygon)
    raise NotImplementedError


def aprobit(token_0: str, token_1: str):
    # Aprobit
    raise NotImplementedError


def artisturba(token_0: str, token_1: str):
    # Artis Turba
    raise NotImplementedError


def astroport(token_0: str, token_1: str):
    # Astroport
    raise NotImplementedError


def atomars(token_0: str, token_1: str):
    # Atomars
    raise NotImplementedError


def auroraswap(token_0: str, token_1: str):
    # AuroraSwap
    raise NotImplementedError


def autoshark_finance(token_0: str, token_1: str):
    # AutoShark Finance
    raise NotImplementedError


def azbit(token_0: str, token_1: str):
    # Azbit
    raise NotImplementedError


def b2bx(token_0: str, token_1: str):
    # B2BX
    raise NotImplementedError


def babyswap(token_0: str, token_1: str):
    # BabySwap
    raise NotImplementedError


def baguette(token_0: str, token_1: str):
    # Baguette
    raise NotImplementedError


def bakeryswap(token_0: str, token_1: str):
    # Bakeryswap
    raise NotImplementedError


def bakkt(token_0: str, token_1: str):
    # Bakkt
    raise NotImplementedError


def balanced_network(token_0: str, token_1: str):
    # Balanced Network
    raise NotImplementedError


def balancer(token_0: str, token_1: str):
    # Balancer (v2)
    raise NotImplementedError


def balancer_arbitrum(token_0: str, token_1: str):
    # Balancer (Arbitrum)
    raise NotImplementedError


def balancer_polygon(token_0: str, token_1: str):
    # Balancer (Polygon)
    raise NotImplementedError


def balancer_v1(token_0: str, token_1: str):
    # Balancer (v1)
    raise NotImplementedError


def bamboo_relay(token_0: str, token_1: str):
    # Bamboo Relay
    raise NotImplementedError


def bancor(token_0: str, token_1: str):
    # Bancor Network
    raise NotImplementedError


def basefex(token_0: str, token_1: str):
    # BaseFEX
    raise NotImplementedError


def bcex(token_0: str, token_1: str):
    # BCEX
    raise NotImplementedError


def beamswap(token_0: str, token_1: str):
    # Beamswap
    raise NotImplementedError


def beaxy(token_0: str, token_1: str):
    # Beaxy
    raise NotImplementedError


def beethovenx(token_0: str, token_1: str):
    # Beethoven X
    raise NotImplementedError


def benswap_smart_bitcoin_cash(token_0: str, token_1: str):
    # Benswap
    raise NotImplementedError


def bgogo(token_0: str, token_1: str):
    # Bgogo
    raise NotImplementedError


def bibo(token_0: str, token_1: str):
    # Bibo
    raise NotImplementedError


def bibox(token_0: str, token_1: str):
    # Bibox
    raise NotImplementedError


def bibox_futures(token_0: str, token_1: str):
    # Bibox (Futures)
    raise NotImplementedError


def biconomy(token_0: str, token_1: str):
    # Biconomy
    raise NotImplementedError


def bidesk(token_0: str, token_1: str):
    # Bidesk
    raise NotImplementedError


def bigone(token_0: str, token_1: str):
    # BigONE
    raise NotImplementedError


def bigone_futures(token_0: str, token_1: str):
    # BigONE Futures
    raise NotImplementedError


def bilaxy(token_0: str, token_1: str):
    # Bilaxy
    raise NotImplementedError


def binance(token_0: str, token_1: str):
    # Binance
    return ('binance', f'''// Retrieve {token_0.upper()}/{token_1.upper()}-6 price from the Binance HTTP-GET API
    const binance = new Witnet.Source("https://api.binance.us/api/v3/ticker/price?symbol={token_0.upper()}{token_1.upper()}")
      .parseJSONMap()
      .getFloat("price")
      .multiply(10 ** 6)
      .round()''')


def binance_dex(token_0: str, token_1: str):
    # Binance DEX
    raise NotImplementedError


def binance_dex_mini(token_0: str, token_1: str):
    # Binance DEX (Mini)
    raise NotImplementedError


def binance_futures(token_0: str, token_1: str):
    # Binance (Futures)
    raise NotImplementedError


def binance_jersey(token_0: str, token_1: str):
    # Binance Jersey
    raise NotImplementedError


def binance_us(token_0: str, token_1: str):
    # Binance US
    raise NotImplementedError


def bingx(token_0: str, token_1: str):
    # BingX
    raise NotImplementedError


def bione(token_0: str, token_1: str):
    # BiONE
    raise NotImplementedError


def birake(token_0: str, token_1: str):
    # Birake
    raise NotImplementedError


def bisq(token_0: str, token_1: str):
    # Bisq
    raise NotImplementedError


def biswap(token_0: str, token_1: str):
    # Biswap
    raise NotImplementedError


def bit2c(token_0: str, token_1: str):
    # Bit2c
    raise NotImplementedError


def bitalong(token_0: str, token_1: str):
    # Bitalong
    raise NotImplementedError


def bitazza(token_0: str, token_1: str):
    # Bitazza
    raise NotImplementedError


def bitbank(token_0: str, token_1: str):
    # Bitbank
    raise NotImplementedError


def bitbay(token_0: str, token_1: str):
    # Zonda
    raise NotImplementedError


def bitbns(token_0: str, token_1: str):
    # BitBNS
    raise NotImplementedError


def bitbox(token_0: str, token_1: str):
    # BITFRONT
    raise NotImplementedError


def bitbuy(token_0: str, token_1: str):
    # Bitbuy
    raise NotImplementedError


def bitci(token_0: str, token_1: str):
    # Bitci
    raise NotImplementedError


def bitcoin_com(token_0: str, token_1: str):
    # FMFW.io
    raise NotImplementedError


def bit_com(token_0: str, token_1: str):
    # Bit.com
    raise NotImplementedError


def bit_com_futures(token_0: str, token_1: str):
    # Bit.com (Futures)
    raise NotImplementedError


def bitcratic(token_0: str, token_1: str):
    # Bitcratic
    raise NotImplementedError


def bitexbook(token_0: str, token_1: str):
    # BITEXBOOK
    raise NotImplementedError


def bitexen(token_0: str, token_1: str):
    # Bitexen
    raise NotImplementedError


def bitexlive(token_0: str, token_1: str):
    # Bitexlive
    raise NotImplementedError


def bitfex(token_0: str, token_1: str):
    # Bitfex
    raise NotImplementedError


def bitfinex(token_0: str, token_1: str):
    # Bitfinex
    raise NotImplementedError


def bitfinex_futures(token_0: str, token_1: str):
    # Bitfinex (Futures)
    raise NotImplementedError


def bitflyer(token_0: str, token_1: str):
    # bitFlyer
    raise NotImplementedError


def bitflyer_futures(token_0: str, token_1: str):
    # Bitflyer (Futures)
    raise NotImplementedError


def bitforex(token_0: str, token_1: str):
    # Bitforex
    raise NotImplementedError


def bitforex_futures(token_0: str, token_1: str):
    # Bitforex (Futures)
    raise NotImplementedError


def bitget(token_0: str, token_1: str):
    # Bitget
    raise NotImplementedError


def bitget_futures(token_0: str, token_1: str):
    # Bitget Futures
    raise NotImplementedError


def bithash(token_0: str, token_1: str):
    # BitHash
    raise NotImplementedError


def bitholic(token_0: str, token_1: str):
    # Bithumb Singapore
    raise NotImplementedError


def bithumb(token_0: str, token_1: str):
    # Bithumb
    raise NotImplementedError


def bithumb_futures(token_0: str, token_1: str):
    # Bithumb (Futures)
    raise NotImplementedError


def bithumb_global(token_0: str, token_1: str):
    # BitGlobal
    raise NotImplementedError


def bitinfi(token_0: str, token_1: str):
    # Bitinfi
    raise NotImplementedError


def bitinka(token_0: str, token_1: str):
    # Bitinka.com
    raise NotImplementedError


def bitkonan(token_0: str, token_1: str):
    # BitKonan
    raise NotImplementedError


def bitkub(token_0: str, token_1: str):
    # Bitkub
    raise NotImplementedError


def bitmart(token_0: str, token_1: str):
    # BitMart
    raise NotImplementedError


def bitmax(token_0: str, token_1: str):
    return ('ascendex', f'''// Retrieves {token_0.upper()}/{token_1.upper()}-6 price from the Bitmax API
const ascendex = new Witnet.Source("https://ascendex.com/api/pro/v1/spot/ticker?symbol=CRO/USDT")
  .parseJSONMap()
  .getMap("data")
  .getFloat("close")
  .multiply(10 ** 6)
  .round()''')


def bitmax_futures(token_0: str, token_1: str):
    # AscendEX  (BitMax) (Futures)
    raise NotImplementedError


def bitmesh(token_0: str, token_1: str):
    # Bitmesh
    raise NotImplementedError


def bitmex(token_0: str, token_1: str):
    # BitMEX
    raise NotImplementedError


def bitoffer(token_0: str, token_1: str):
    # Bitoffer
    raise NotImplementedError


def bitonbay(token_0: str, token_1: str):
    # BitOnBay
    raise NotImplementedError


def bitopro(token_0: str, token_1: str):
    # BitoPro
    raise NotImplementedError


def bitpanda(token_0: str, token_1: str):
    # Bitpanda Pro
    raise NotImplementedError


def bitrabbit(token_0: str, token_1: str):
    # BitRabbit
    raise NotImplementedError


def bitrue(token_0: str, token_1: str):
    # Bitrue
    raise NotImplementedError


def bitsdaq(token_0: str, token_1: str):
    # Bitsdaq
    raise NotImplementedError


def bitso(token_0: str, token_1: str):
    # Bitso
    raise NotImplementedError


def bitsonic(token_0: str, token_1: str):
    # Bitsonic
    raise NotImplementedError


def bitstamp(token_0: str, token_1: str):
    return ('bitstamp', f'''// Retrieve {token_0.upper()}/{token_1.lower()} price from BitStamp
const bitstamp = new Witnet.Source("https://www.bitstamp.net/api/v2/ticker/{token_0.lower()}{token_1.lower()}")
  .parseJSONMap()
  .getFloat("last")
  .multiply(10 ** 6)
  .round()''')


def bitsten(token_0: str, token_1: str):
    # Bitsten
    raise NotImplementedError


def bitstorage(token_0: str, token_1: str):
    # BitStorage
    raise NotImplementedError


def bittrex(token_0: str, token_1: str):
    return ('bittrex', f'''// Retrieve {token_0.upper()}/{token_1.upper()}-6 price from Bittrex
const bittrex = new Witnet.Source("https://api.bittrex.com/v3/markets/{token_0.upper()}-{token_1.upper()}/ticker")
  .parseJSONMap()
  .getFloat("lastTradeRate")
  .multiply(10 ** 6)
  .round()''')


def bitubu(token_0: str, token_1: str):
    # Bitubu Exchange
    raise NotImplementedError


def bitvavo(token_0: str, token_1: str):
    # Bitvavo
    raise NotImplementedError


def bitz_futures(token_0: str, token_1: str):
    # BitZ (Futures)
    raise NotImplementedError


def bkex(token_0: str, token_1: str):
    # BKEX
    raise NotImplementedError


def bleutrade(token_0: str, token_1: str):
    # bleutrade
    raise NotImplementedError


def blockchain_com(token_0: str, token_1: str):
    # Blockchain.com
    raise NotImplementedError


def blockonix(token_0: str, token_1: str):
    # Blockonix
    raise NotImplementedError


def boa(token_0: str, token_1: str):
    # BOA Exchange
    raise NotImplementedError


def bossswap(token_0: str, token_1: str):
    # BossSwap
    raise NotImplementedError


def braziliex(token_0: str, token_1: str):
    # Braziliex
    raise NotImplementedError


def bscswap(token_0: str, token_1: str):
    # BSCswap
    raise NotImplementedError


def btc_alpha(token_0: str, token_1: str):
    # BTC-Alpha
    raise NotImplementedError


def btcbox(token_0: str, token_1: str):
    # BTCBOX
    raise NotImplementedError


def btcc(token_0: str, token_1: str):
    # BTCC
    raise NotImplementedError


def btcc_futures(token_0: str, token_1: str):
    # BTCC Futures
    raise NotImplementedError


def btcex(token_0: str, token_1: str):
    # BTCEX
    raise NotImplementedError


def btc_exchange(token_0: str, token_1: str):
    # Btc Exchange
    raise NotImplementedError


def btcex_futures(token_0: str, token_1: str):
    # BTCEX (Futures)
    raise NotImplementedError


def btcmarkets(token_0: str, token_1: str):
    # BTCMarkets
    raise NotImplementedError


def btcmex(token_0: str, token_1: str):
    # BTCMEX
    raise NotImplementedError


def btcnext(token_0: str, token_1: str):
    # BTCNEXT
    raise NotImplementedError


def btcsquare(token_0: str, token_1: str):
    # BTCSquare
    raise NotImplementedError


def btc_trade_ua(token_0: str, token_1: str):
    # BTC Trade UA
    raise NotImplementedError


def btcturk(token_0: str, token_1: str):
    # BtcTurk PRO
    raise NotImplementedError


def btse(token_0: str, token_1: str):
    # BTSE
    raise NotImplementedError


def btse_futures(token_0: str, token_1: str):
    # BTSE (Futures)
    raise NotImplementedError


def buyucoin(token_0: str, token_1: str):
    # BuyUcoin
    raise NotImplementedError


def bvnex(token_0: str, token_1: str):
    # Bvnex
    raise NotImplementedError


def bw(token_0: str, token_1: str):
    # BW.com
    raise NotImplementedError


def bybit(token_0: str, token_1: str):
    # Bybit
    raise NotImplementedError


def bybit_spot(token_0: str, token_1: str):
    # Bybit (Spot)
    raise NotImplementedError


def c2cx(token_0: str, token_1: str):
    # C2CX
    raise NotImplementedError


def catex(token_0: str, token_1: str):
    # Catex
    raise NotImplementedError


def cbx(token_0: str, token_1: str):
    # CBX
    raise NotImplementedError


def ccex(token_0: str, token_1: str):
    # C-CEX
    raise NotImplementedError


def cex(token_0: str, token_1: str):
    # CEX.IO
    raise NotImplementedError


def chainex(token_0: str, token_1: str):
    # ChainEX
    raise NotImplementedError


def changelly(token_0: str, token_1: str):
    # Changelly PRO
    raise NotImplementedError


def cherryswap(token_0: str, token_1: str):
    # CherrySwap
    raise NotImplementedError


def chiliz(token_0: str, token_1: str):
    # Chiliz
    raise NotImplementedError


def citex(token_0: str, token_1: str):
    # CITEX
    raise NotImplementedError


def clipper_ethereum(token_0: str, token_1: str):
    # Clipper (Ethereum)
    raise NotImplementedError


def clipper_polygon(token_0: str, token_1: str):
    # Clipper (Polygon)
    raise NotImplementedError


def cme_futures(token_0: str, token_1: str):
    # CME Group
    raise NotImplementedError


def coinasset(token_0: str, token_1: str):
    # CoinAsset
    raise NotImplementedError


def coinbene(token_0: str, token_1: str):
    # CoinBene
    raise NotImplementedError


def coinbit(token_0: str, token_1: str):
    # Coinbit
    raise NotImplementedError


def coincheck(token_0: str, token_1: str):
    # Coincheck
    raise NotImplementedError


def coindcx(token_0: str, token_1: str):
    # CoinDCX
    raise NotImplementedError


def coindeal(token_0: str, token_1: str):
    # Coindeal
    raise NotImplementedError


def coineal(token_0: str, token_1: str):
    # Coineal
    raise NotImplementedError


def coin_egg(token_0: str, token_1: str):
    # CoinEgg
    raise NotImplementedError


def coinex(token_0: str, token_1: str):
    # CoinEx
    raise NotImplementedError


def coinex_futures(token_0: str, token_1: str):
    # CoinEx (Futures)
    raise NotImplementedError


def coinfalcon(token_0: str, token_1: str):
    # Coinfalcon
    raise NotImplementedError


def coinfield(token_0: str, token_1: str):
    # Coinfield
    raise NotImplementedError


def coinflex(token_0: str, token_1: str):
    # CoinFLEX
    raise NotImplementedError


def coinflex_futures(token_0: str, token_1: str):
    # CoinFLEX (Futures)
    raise NotImplementedError


def coinfloor(token_0: str, token_1: str):
    # Coinfloor
    raise NotImplementedError


def coingi(token_0: str, token_1: str):
    # Coingi
    raise NotImplementedError


def coinhe(token_0: str, token_1: str):
    # CoinHe
    raise NotImplementedError


def coinhub(token_0: str, token_1: str):
    # Coinhub
    raise NotImplementedError


def coinjar(token_0: str, token_1: str):
    # CoinJar Exchange
    raise NotImplementedError


def coinlim(token_0: str, token_1: str):
    # Coinlim
    raise NotImplementedError


def coinlist(token_0: str, token_1: str):
    # Coinlist
    raise NotImplementedError


def coinmargin(token_0: str, token_1: str):
    # CoinMargin
    raise NotImplementedError


def coin_metro(token_0: str, token_1: str):
    # Coinmetro
    raise NotImplementedError


def coinone(token_0: str, token_1: str):
    # Coinone
    raise NotImplementedError


def coinpark(token_0: str, token_1: str):
    # Coinpark
    raise NotImplementedError


def coinplace(token_0: str, token_1: str):
    # Coinplace
    raise NotImplementedError


def coinsbank(token_0: str, token_1: str):
    # Coinsbank
    raise NotImplementedError


def coinsbit(token_0: str, token_1: str):
    # Coinsbit
    raise NotImplementedError


def coinstore(token_0: str, token_1: str):
    # Coinstore
    raise NotImplementedError


def coinsuper(token_0: str, token_1: str):
    # Coinsuper
    raise NotImplementedError


def cointiger(token_0: str, token_1: str):
    # CoinTiger
    raise NotImplementedError


def cointiger_futures(token_0: str, token_1: str):
    # CoinTiger (Futures)
    raise NotImplementedError


def coinxpro(token_0: str, token_1: str):
    # COINX.PRO
    raise NotImplementedError


def coinzo(token_0: str, token_1: str):
    # Coinzo
    raise NotImplementedError


def coinzoom(token_0: str, token_1: str):
    # Coinzoom
    raise NotImplementedError


def comethswap(token_0: str, token_1: str):
    # ComethSwap
    raise NotImplementedError


def concave(token_0: str, token_1: str):
    # Concave
    raise NotImplementedError


def c_patex(token_0: str, token_1: str):
    # C-Patex
    raise NotImplementedError


def cpdax(token_0: str, token_1: str):
    # CPDAX
    raise NotImplementedError


def crex24(token_0: str, token_1: str):
    # CREX24
    raise NotImplementedError


def crodex(token_0: str, token_1: str):
    # Crodex
    raise NotImplementedError


def cronaswap(token_0: str, token_1: str):
    # Cronaswap
    raise NotImplementedError


def cronus_finance(token_0: str, token_1: str):
    # Cronus Finance
    raise NotImplementedError


def crxzone(token_0: str, token_1: str):
    # CRXzone
    raise NotImplementedError


def cryptaldash(token_0: str, token_1: str):
    # CryptalDash
    raise NotImplementedError


def cryptlocex(token_0: str, token_1: str):
    # Cryptlocex
    raise NotImplementedError


def crypto_com(token_0: str, token_1: str):
    # Crypto.com Exchange
    raise NotImplementedError


def crypto_com_futures(token_0: str, token_1: str):
    # Crypto.com Exchange (Futures)
    raise NotImplementedError


def cryptology(token_0: str, token_1: str):
    # Cryptology
    raise NotImplementedError


def c_trade(token_0: str, token_1: str):
    # C-Trade
    raise NotImplementedError


def currency(token_0: str, token_1: str):
    # Currency.com
    raise NotImplementedError


def curve(token_0: str, token_1: str):
    # Curve Finance
    raise NotImplementedError


def curve_factory(token_0: str, token_1: str):
    # Curve (Factory Pools)
    raise NotImplementedError


def cybex(token_0: str, token_1: str):
    # Cybex DEX
    raise NotImplementedError


def darb_finance(token_0: str, token_1: str):
    # Darb Finance
    raise NotImplementedError


def darkknight(token_0: str, token_1: str):
    # Dark KnightSwap
    raise NotImplementedError


def daybit(token_0: str, token_1: str):
    # Daybit
    raise NotImplementedError


def dcoin(token_0: str, token_1: str):
    # Dcoin
    raise NotImplementedError


def ddex(token_0: str, token_1: str):
    # DDEX
    raise NotImplementedError


def decoin(token_0: str, token_1: str):
    # Decoin
    raise NotImplementedError


def defichain(token_0: str, token_1: str):
    # DeFiChain DEX
    raise NotImplementedError


def defi_kingdoms(token_0: str, token_1: str):
    # Defi Kingdoms
    raise NotImplementedError


def defi_kingdoms_crystalvale(token_0: str, token_1: str):
    # Defi Kingdoms (Crystalvale)
    raise NotImplementedError


def defi_swap(token_0: str, token_1: str):
    # DeFi Swap
    raise NotImplementedError


def delta_futures(token_0: str, token_1: str):
    # Delta Exchange (Futures)
    raise NotImplementedError


def delta_spot(token_0: str, token_1: str):
    # Delta Exchange
    raise NotImplementedError


def dem_exchange(token_0: str, token_1: str):
    # Demex
    raise NotImplementedError


def deribit(token_0: str, token_1: str):
    # Deribit
    raise NotImplementedError


def deversifi(token_0: str, token_1: str):
    # Deversifi
    raise NotImplementedError


def dexalot(token_0: str, token_1: str):
    # Dexalot
    raise NotImplementedError


def dextrade(token_0: str, token_1: str):
    # Dex-Trade
    raise NotImplementedError


def dfx(token_0: str, token_1: str):
    # DFX
    raise NotImplementedError


def dfx_polygon(token_0: str, token_1: str):
    # DFX (Polygon)
    raise NotImplementedError


def dfyn(token_0: str, token_1: str):
    # Dfyn
    raise NotImplementedError


def diffusion(token_0: str, token_1: str):
    # Diffusion
    raise NotImplementedError


def digifinex(token_0: str, token_1: str):
    # Digifinex
    raise NotImplementedError


def dmm(token_0: str, token_1: str):
    # KyberSwap (Ethereum)
    raise NotImplementedError


def dmm_avalanche(token_0: str, token_1: str):
    # KyberSwap (Avalanche)
    raise NotImplementedError


def dmm_bsc(token_0: str, token_1: str):
    # KyberSwap (BSC)
    raise NotImplementedError


def dmm_fantom(token_0: str, token_1: str):
    # KyberSwap (Fantom)
    raise NotImplementedError


def dmm_polygon(token_0: str, token_1: str):
    # KyberSwap (Polygon)
    raise NotImplementedError


def dobitrade(token_0: str, token_1: str):
    # Dobitrade
    raise NotImplementedError


def dodo(token_0: str, token_1: str):
    # DODO
    raise NotImplementedError


def dodo_arbitrum(token_0: str, token_1: str):
    # Dodo (Arbitrum)
    raise NotImplementedError


def dodo_bsc(token_0: str, token_1: str):
    # Dodo (BSC)
    raise NotImplementedError


def dodo_polygon(token_0: str, token_1: str):
    # Dodo (Polygon)
    raise NotImplementedError


def dolomite(token_0: str, token_1: str):
    # Dolomite
    raise NotImplementedError


def dove_wallet(token_0: str, token_1: str):
    # Dove Wallet
    raise NotImplementedError


def dragonex(token_0: str, token_1: str):
    # DragonEx
    raise NotImplementedError


def drift_protocol(token_0: str, token_1: str):
    # Drift Protocol
    raise NotImplementedError


def duedex(token_0: str, token_1: str):
    # DueDEX
    raise NotImplementedError


def dydx(token_0: str, token_1: str):
    # dYdX
    raise NotImplementedError


def dydx_perpetual(token_0: str, token_1: str):
    # dYdX Perpetual
    raise NotImplementedError


def ecxx(token_0: str, token_1: str):
    # Ecxx
    raise NotImplementedError


def elk_finance_avax(token_0: str, token_1: str):
    # Elk Finance (Avalanche)
    raise NotImplementedError


def elk_finance_telos(token_0: str, token_1: str):
    # Elk Finance (Telos)
    raise NotImplementedError


def emirex(token_0: str, token_1: str):
    # Emirex
    raise NotImplementedError


def empiredex(token_0: str, token_1: str):
    # EmpireDEX
    raise NotImplementedError


def empiredex_bsc(token_0: str, token_1: str):
    # EmpireDEX (BSC)
    raise NotImplementedError


def energiswap(token_0: str, token_1: str):
    # Energiswap
    raise NotImplementedError


def equos(token_0: str, token_1: str):
    # EQONEX
    raise NotImplementedError


def equos_perpetual(token_0: str, token_1: str):
    # EQONEX (Perpetual)
    raise NotImplementedError


def eterbase(token_0: str, token_1: str):
    # Eterbase
    raise NotImplementedError


def etherflyer(token_0: str, token_1: str):
    # EtherFlyer
    raise NotImplementedError


def ethex(token_0: str, token_1: str):
    # Ethex
    raise NotImplementedError


def etorox(token_0: str, token_1: str):
    # eToroX
    raise NotImplementedError


def excalibur(token_0: str, token_1: str):
    # Excalibur
    raise NotImplementedError


def exmarkets(token_0: str, token_1: str):
    # ExMarkets
    raise NotImplementedError


def exmo(token_0: str, token_1: str):
    # EXMO
    raise NotImplementedError


def exrates(token_0: str, token_1: str):
    # Exrates
    raise NotImplementedError


def fatbtc(token_0: str, token_1: str):
    # FatBTC
    raise NotImplementedError


def fex(token_0: str, token_1: str):
    # FEX
    raise NotImplementedError


def financex(token_0: str, token_1: str):
    # FinanceX
    raise NotImplementedError


def finexbox(token_0: str, token_1: str):
    # FinexBox
    raise NotImplementedError


def firebird_finance_polygon(token_0: str, token_1: str):
    # Firebird Finance (Polygon)
    raise NotImplementedError


def floatsv(token_0: str, token_1: str):
    # Float SV
    raise NotImplementedError


def flybit(token_0: str, token_1: str):
    # Flybit
    raise NotImplementedError


def forkdelta(token_0: str, token_1: str):
    # ForkDelta
    raise NotImplementedError


def four_swap(token_0: str, token_1: str):
    # 4swap
    raise NotImplementedError


def foxbit(token_0: str, token_1: str):
    # Foxbit
    raise NotImplementedError


def freiexchange(token_0: str, token_1: str):
    # Freiexchange
    raise NotImplementedError


def ftx(token_0: str, token_1: str):
    # FTX (Derivatives)
    raise NotImplementedError


def ftx_spot(token_0: str, token_1: str):
    # FTX
    raise NotImplementedError


def ftx_us(token_0: str, token_1: str):
    # FTX.US
    raise NotImplementedError


def futureswap(token_0: str, token_1: str):
    # Futureswap
    raise NotImplementedError


def fuzz_finance(token_0: str, token_1: str):
    # FuzzSwap
    raise NotImplementedError


def gate(token_0: str, token_1: str):
    return ('gateio', f'''// Retrieves {token_1.upper()} price of {token_0.upper()} from the Gate.io API
const gateio = new Witnet.Source("https://data.gateapi.io/api2/1/ticker/{token_0.lower()}_{token_1.lower()}")
  .parseJSONMap() // Parse a `Map` from the retrieved `String`
  .getFloat("last") // Get the `Float` value associated to the `last` key
  .multiply(10 ** 6) // Use 6 digit precision
  .round() // Cast to integer''')


def gate_futures(token_0: str, token_1: str):
    # Gate.io (Futures)
    raise NotImplementedError


def gbx(token_0: str, token_1: str):
    # Global Blockchain Exchange
    raise NotImplementedError


def gdac(token_0: str, token_1: str):
    # GDAC
    raise NotImplementedError


def gdax(token_0: str, token_1: str):
    return ('coinbase', f'''// Retrieve {token_0.upper()}/{token_1.upper()}-6 price from Coinbase
const coinbase = new Witnet.Source("https://api.coinbase.com/v2/exchange-rates?currency={token_1.upper()}")
  .parseJSONMap()
  .getMap("data")
  .getMap("rates")
  .getFloat("{token_0.upper()}")
  .power(-1)
  .multiply(10 ** 6)
  .round()''')


def gemini(token_0: str, token_1: str):
    # Gemini
    raise NotImplementedError


def getbtc(token_0: str, token_1: str):
    # GetBTC
    raise NotImplementedError


def glide_finance(token_0: str, token_1: str):
    # Glide Finance
    raise NotImplementedError


def gmo_japan(token_0: str, token_1: str):
    # GMO Japan
    raise NotImplementedError


def gmo_japan_futures(token_0: str, token_1: str):
    # GMO Japan (Futures)
    raise NotImplementedError


def gobaba(token_0: str, token_1: str):
    # Gobaba
    raise NotImplementedError


def goku(token_0: str, token_1: str):
    # GokuMarket
    raise NotImplementedError


def gopax(token_0: str, token_1: str):
    # GoPax
    raise NotImplementedError


def graviex(token_0: str, token_1: str):
    # Graviex
    raise NotImplementedError


def hades_swap(token_0: str, token_1: str):
    # Hades Swap
    raise NotImplementedError


def hakuswap(token_0: str, token_1: str):
    # HakuSwap
    raise NotImplementedError


def hanbitco(token_0: str, token_1: str):
    # Hanbitco
    raise NotImplementedError


def hbtc(token_0: str, token_1: str):
    # BHEX
    raise NotImplementedError


def hbtc_futures(token_0: str, token_1: str):
    # BHEX (Futures)
    raise NotImplementedError


def hb_top(token_0: str, token_1: str):
    # Hb.top
    raise NotImplementedError


def hitbtc(token_0: str, token_1: str):
    # HitBTC
    raise NotImplementedError


def honeyswap(token_0: str, token_1: str):
    # Honeyswap
    raise NotImplementedError


def honeyswap_polygon(token_0: str, token_1: str):
    # Honeyswap (Polygon)
    raise NotImplementedError


def hoo(token_0: str, token_1: str):
    return ('hoo', f'''// Retrieves {token_0.upper()}/USDT-6 from the Hoo HTTP-GET API
    const hoo = new Witnet.Source("https://api.hoolgd.com/open/v1/tickers/market")
      .parseJSONMap() // Parse a `Map` from the retrieved `String`
      .getArray("data") // Access to the `Map` object at `data` key
      .filter( 
        // From all elements in the map,
        // select the one which "symbol" field
        // matches "{token_0.upper()}-{token_1.upper()}":
        new Witnet.Script([ Witnet.TYPES.MAP ])
          .getString("symbol")
          .match({{ "{token_0.upper()}-{token_1.upper()}": true }}, false)
      )
      .getMap(0) // Get first (and only) element from the resulting Map
      .getFloat("price") // Get the `Float` value associated to the `price` key
      .multiply(10 ** 6) // Use 6 digit precision
      .round() // Cast to integer''')


def hopex(token_0: str, token_1: str):
    # Hopex
    raise NotImplementedError


def hotbit(token_0: str, token_1: str):
    # Hotbit
    return ('hotbit', f'''// Retrieves {token_1.upper()} price of {token_0.upper()} from the HOTBIT API
const hotbit = new Witnet.Source("https://api.hotbit.io/api/v1/market.last?market={token_0.upper()}{token_1.upper()}")
  .parseJSONMap() // Parse a `Map` from the retrieved `String`
  .getFloat("result") // Get the `Float` value associated to the `result` key
  .multiply(10 ** 6) // Use 6 digit precision
  .round() // Cast to integer''')


def hpx(token_0: str, token_1: str):
    # HPX
    raise NotImplementedError


def hubi(token_0: str, token_1: str):
    # Hubi
    raise NotImplementedError


def huckleberry(token_0: str, token_1: str):
    # Huckleberry
    raise NotImplementedError


def huobi(token_0: str, token_1: str):
    return ('huobi', f'''// Retrieves {token_0.upper()}/{token_1.upper()} price from the HUOBI API
const huobi = new Witnet.Source("https://api.huobi.pro/market/detail/merged?symbol={token_0.lower()}{token_1.lower()}")
  .parseJSONMap() // Parse a `Map` from the retrieved `String`
  .getMap("tick") // Access to the `Map` object at index 0
  .getFloat("close") // Get the `String` value associated to the `last` key
  .multiply(10 ** 6) // Use 6 digit precision
  .round() // Cast to integer''')


def huobi_dm(token_0: str, token_1: str):
    # Huobi Futures
    raise NotImplementedError


def huobi_id(token_0: str, token_1: str):
    # Huobi Indonesia
    raise NotImplementedError


def huobi_japan(token_0: str, token_1: str):
    # Huobi Japan
    raise NotImplementedError


def huobi_korea(token_0: str, token_1: str):
    # Huobi Korea
    raise NotImplementedError


def huobi_thailand(token_0: str, token_1: str):
    # Huobi Thailand
    raise NotImplementedError


def ice3x(token_0: str, token_1: str):
    # Ice3x
    raise NotImplementedError


def idex(token_0: str, token_1: str):
    # Idex
    raise NotImplementedError


def impossible_finance(token_0: str, token_1: str):
    # Impossible Finance
    raise NotImplementedError


def incorex(token_0: str, token_1: str):
    # IncoreX
    raise NotImplementedError


def independent_reserve(token_0: str, token_1: str):
    # Independent Reserve
    raise NotImplementedError


def indodax(token_0: str, token_1: str):
    # Indodax
    raise NotImplementedError


def infinity_coin(token_0: str, token_1: str):
    # Infinity Coin
    raise NotImplementedError


def injective(token_0: str, token_1: str):
    # Injective Pro
    raise NotImplementedError


def injective_futures(token_0: str, token_1: str):
    # Injective Pro (Futures)
    raise NotImplementedError


def instantbitex(token_0: str, token_1: str):
    # Instant Bitex
    raise NotImplementedError


def iqfinex(token_0: str, token_1: str):
    # IQFinex
    raise NotImplementedError


def islandswap(token_0: str, token_1: str):
    # Islandswap
    raise NotImplementedError


def itbit(token_0: str, token_1: str):
    # itBit
    raise NotImplementedError


def jetswap(token_0: str, token_1: str):
    # JetSwap
    raise NotImplementedError


def jex(token_0: str, token_1: str):
    # Binance JEX
    raise NotImplementedError


def jex_futures(token_0: str, token_1: str):
    # Binance JEX (Futures)
    raise NotImplementedError


def jswap(token_0: str, token_1: str):
    # Jswap
    raise NotImplementedError


def julswap(token_0: str, token_1: str):
    # Julswap
    raise NotImplementedError


def jupiter(token_0: str, token_1: str):
    # Jupiter
    raise NotImplementedError


def justswap(token_0: str, token_1: str):
    # SunSwap (v2)
    raise NotImplementedError


def kaidex(token_0: str, token_1: str):
    # Kaidex
    raise NotImplementedError


def kanga(token_0: str, token_1: str):
    # Kanga
    raise NotImplementedError


def katana(token_0: str, token_1: str):
    # Katana
    raise NotImplementedError


def kava(token_0: str, token_1: str):
    # Kava Swap
    raise NotImplementedError


def kickex(token_0: str, token_1: str):
    # KickEX
    raise NotImplementedError


def kkcoin(token_0: str, token_1: str):
    # KKCoin
    raise NotImplementedError


def k_kex(token_0: str, token_1: str):
    # KKEX
    raise NotImplementedError


def knightswap(token_0: str, token_1: str):
    # KnightSwap
    raise NotImplementedError


def koinbazar(token_0: str, token_1: str):
    # Koinbazar
    raise NotImplementedError


def korbit(token_0: str, token_1: str):
    # Korbit
    raise NotImplementedError


def kraken(token_0: str, token_1: str):
    return ('kraken', f'''// Retrieve {token_0.upper()}/{token_1.upper()}-6 price from Kraken
const kraken = new Witnet.Source("https://api.kraken.com/0/public/Ticker?pair={token_0.upper()}{token_1.upper()}")
  .parseJSONMap()
  .getMap("result")
  .getMap("{token_0.upper()}{token_1.upper()}")
  .getArray("a")
  .getFloat(0)
  .multiply(10 ** 6)
  .round()''')


def kraken_futures(token_0: str, token_1: str):
    # Kraken (Futures)
    raise NotImplementedError


def kucoin(token_0: str, token_1: str):
    return ('kucoin', f'''// Retrieves {token_0.upper()}/{token_1.upper()}-6 from KUCOIN API
    const kucoin = new Witnet.Source("https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={token_0.upper()}-{token_1.upper()}")
      .parseJSONMap() 
      .getMap("data")
      .getFloat("price")
      .multiply(10 ** 6)
      .round()''')


def kumex(token_0: str, token_1: str):
    # KuCoin Futures
    raise NotImplementedError


def kuna(token_0: str, token_1: str):
    # Kuna Exchange
    raise NotImplementedError


def kuswap(token_0: str, token_1: str):
    # Kuswap
    raise NotImplementedError


def lakebtc(token_0: str, token_1: str):
    # LakeBTC
    raise NotImplementedError


def latoken(token_0: str, token_1: str):
    # LATOKEN
    raise NotImplementedError


def lbank(token_0: str, token_1: str):
    # LBank
    raise NotImplementedError


def lcx(token_0: str, token_1: str):
    # LCX Exchange
    raise NotImplementedError


def leonicornswap(token_0: str, token_1: str):
    # LeonicornSwap
    raise NotImplementedError


def levinswap_xdai(token_0: str, token_1: str):
    # Levinswap (xDai)
    raise NotImplementedError


def liquid_derivatives(token_0: str, token_1: str):
    # Liquid Perpetuals
    raise NotImplementedError


def localtrade(token_0: str, token_1: str):
    # LocalTrade
    raise NotImplementedError


def loop(token_0: str, token_1: str):
    # Loop Markets
    raise NotImplementedError


def loopring(token_0: str, token_1: str):
    # Loopring
    raise NotImplementedError


def loopring_amm(token_0: str, token_1: str):
    # Loopring AMM
    raise NotImplementedError


def luaswap(token_0: str, token_1: str):
    # Luaswap
    raise NotImplementedError


def lucent(token_0: str, token_1: str):
    # Lucent
    raise NotImplementedError


def lukki(token_0: str, token_1: str):
    # Lukki
    raise NotImplementedError


def luno(token_0: str, token_1: str):
    # Luno
    raise NotImplementedError


def lydia_finance(token_0: str, token_1: str):
    # Lydia Finance
    raise NotImplementedError


def lykke(token_0: str, token_1: str):
    # Lykke
    raise NotImplementedError


def maiar(token_0: str, token_1: str):
    # Maiar
    raise NotImplementedError


def makiswap(token_0: str, token_1: str):
    # Makiswap
    raise NotImplementedError


def mars_ecosystem(token_0: str, token_1: str):
    # Mars Ecosystem
    raise NotImplementedError


def max_maicoin(token_0: str, token_1: str):
    # Max Maicoin
    raise NotImplementedError


def mcdex(token_0: str, token_1: str):
    # MCDEX (Arbitrum)
    raise NotImplementedError


def mcdex_bsc(token_0: str, token_1: str):
    # MCDEX (BSC)
    raise NotImplementedError


def mdex(token_0: str, token_1: str):
    # Mdex
    raise NotImplementedError


def mdex_bsc(token_0: str, token_1: str):
    # Mdex BSC
    raise NotImplementedError


def mercado_bitcoin(token_0: str, token_1: str):
    # Mercado Bitcoin
    raise NotImplementedError


def mercatox(token_0: str, token_1: str):
    # Mercatox
    raise NotImplementedError


def mercuriex(token_0: str, token_1: str):
    # MercuriEx
    raise NotImplementedError


def milkyswap_milkada(token_0: str, token_1: str):
    # MilkySwap
    raise NotImplementedError


def mimo(token_0: str, token_1: str):
    # Mimo
    raise NotImplementedError


def mistswap_smart_bitcoin_cash(token_0: str, token_1: str):
    # Mistswap
    raise NotImplementedError


def mm_finance(token_0: str, token_1: str):
    # MM Finance
    raise NotImplementedError


def mojitoswap(token_0: str, token_1: str):
    # MojitoSwap
    raise NotImplementedError


def morpheus_swap(token_0: str, token_1: str):
    # Morpheus Swap
    raise NotImplementedError


def muesliswap_milkada(token_0: str, token_1: str):
    # Muesliswap (Milkada)
    raise NotImplementedError


def multi(token_0: str, token_1: str):
    # Multi.io
    raise NotImplementedError


def mxc(token_0: str, token_1: str):
    return ('mexc', f'''// Retrieves {token_1.upper()} price of {token_0.upper()} from the MEXC API
const mexc = new Witnet.Source("https://www.mexc.com/open/api/v2/market/ticker?symbol={token_0.upper()}_{token_1.lower()}")
  .parseJSONMap() // Parse a `Map` from the retrieved `String`
  .getArray("data") // Access to the `Array` object at `data` key
  .getMap(0) // Access to the `Map` object at index 0
  .getFloat("last") // Get the `String` value associated to the `last` key
  .multiply(10 ** 6) // Use 6 digit precision
  .round() // Cast to integer
''')


def mxc_futures(token_0: str, token_1: str):
    # MEXC Global (Futures)
    raise NotImplementedError


def mycoinstory(token_0: str, token_1: str):
    # MCS
    raise NotImplementedError


def nachoswap(token_0: str, token_1: str):
    # NachoSwap
    raise NotImplementedError


def namebase(token_0: str, token_1: str):
    # Namebase
    raise NotImplementedError


def nami_exchange(token_0: str, token_1: str):
    # Nami.Exchange
    raise NotImplementedError


def nanu_exchange(token_0: str, token_1: str):
    # Nanu Exchange
    raise NotImplementedError


def narkasa(token_0: str, token_1: str):
    # Narkasa
    raise NotImplementedError


def nash(token_0: str, token_1: str):
    # Nash
    raise NotImplementedError


def nearpad(token_0: str, token_1: str):
    # NearPAD
    raise NotImplementedError


def negociecoins(token_0: str, token_1: str):
    # Negociecoins
    raise NotImplementedError


def neraex(token_0: str, token_1: str):
    # Neraex
    raise NotImplementedError


def netswap(token_0: str, token_1: str):
    # Netswap
    raise NotImplementedError


def newdex(token_0: str, token_1: str):
    # Newdex
    raise NotImplementedError


def nexus_mutual(token_0: str, token_1: str):
    # Nexus Mutual
    raise NotImplementedError


def nice_hash(token_0: str, token_1: str):
    # NiceHash
    raise NotImplementedError


def nominex(token_0: str, token_1: str):
    # Nominex
    raise NotImplementedError


def novadax(token_0: str, token_1: str):
    # NovaDAX
    raise NotImplementedError


def oasis_trade(token_0: str, token_1: str):
    # OasisDEX
    raise NotImplementedError


def occamx(token_0: str, token_1: str):
    # OccamX
    raise NotImplementedError


def oceanex(token_0: str, token_1: str):
    # Oceanex
    raise NotImplementedError


def okcoin(token_0: str, token_1: str):
    # Okcoin
    raise NotImplementedError


def okex(token_0: str, token_1: str):

    # OKX
    return ('okex', f'''// Retrieves {token_1.upper()} price of {token_0.upper()} from the OkEx API (derived from USDT/USD exchange rate)
const okex = new Witnet.Source("https://www.okex.com/api/index/v3/{token_0.upper()}-{token_1.upper()}/constituents")
  .parseJSONMap() // Parse a `Map` from the retrieved `String`
  .getMap("data") // Access to the `Map` object at `data` key
  .getFloat("last") // Get the `Float` value associated to the `last` key
  .multiply(10 ** 6) // Use 6 digit precision
  .round() // Cast to integer''')


def okex_swap(token_0: str, token_1: str):
    # OKX (Futures)
    raise NotImplementedError


def omgfin(token_0: str, token_1: str):
    # Omgfin
    raise NotImplementedError


def omnidex(token_0: str, token_1: str):
    # OmniDex
    raise NotImplementedError


def one_inch(token_0: str, token_1: str):
    # 1inch
    raise NotImplementedError


def one_inch_liquidity_protocol(token_0: str, token_1: str):
    # 1inch Liquidity Protocol
    raise NotImplementedError


def one_inch_liquidity_protocol_bsc(token_0: str, token_1: str):
    # 1inch Liquidity Protocol (BSC)
    raise NotImplementedError


def oolongswap(token_0: str, token_1: str):
    return ('oolongswap', f'''// Retrieve {token_0}/{token_1}-6 price from Oolongswap DEX at Boba mainnet
const oolongswap = new Witnet.Source("https://graph.witnet.io/?endpoint=https://graph.mainnet.boba.network/subgraphs/name/oolongswap/mainnet&data=%7B%22query%22%3A%22%7Bpairs(where%3A%20%7Btoken0%3A%20%5C%220x5008f837883ea9a07271a1b5eb0658404f5a9610%5C%22%2C%20token1%3A%20%5C%220x66a2a913e447d6b4bf33efbec43aaef87890fbbc%5C%22%7D)%20%7Btoken1Price%7D%7D%20%22%7D")
  .parseJSONMap()
  .getArray("pairs")
  .getMap(0)
  .getFloat("token1Price")
  .multiply(10 ** 6)
  .round()''')


def openocean_finance(token_0: str, token_1: str):
    # OpenOcean
    raise NotImplementedError


def openswap(token_0: str, token_1: str):
    # OpenSwap
    raise NotImplementedError


def orca(token_0: str, token_1: str):
    # Orca
    raise NotImplementedError


def orderbook(token_0: str, token_1: str):
    # Orderbook.io
    raise NotImplementedError


def osmosis(token_0: str, token_1: str):
    # Osmosis
    raise NotImplementedError


def otcbtc(token_0: str, token_1: str):
    # OTCBTC
    raise NotImplementedError


def ovex(token_0: str, token_1: str):
    # Ovex
    raise NotImplementedError


def p2pb2b(token_0: str, token_1: str):
    # P2PB2B
    raise NotImplementedError


def paintswap(token_0: str, token_1: str):
    # Paintswap
    raise NotImplementedError


def pancakeswap_new(token_0: str, token_1: str):
    # PancakeSwap (v2)
    raise NotImplementedError


def pangolin(token_0: str, token_1: str):
    # Pangolin
    raise NotImplementedError


def pantherswap(token_0: str, token_1: str):
    # PantherSwap
    raise NotImplementedError


def paribu(token_0: str, token_1: str):
    # Paribu
    raise NotImplementedError


def paritex(token_0: str, token_1: str):
    # Paritex
    raise NotImplementedError


def paroexchange(token_0: str, token_1: str):
    # Paro Exchange
    raise NotImplementedError


def paymium(token_0: str, token_1: str):
    # Paymium
    raise NotImplementedError


def pegasys(token_0: str, token_1: str):
    # Pegasys
    raise NotImplementedError


def perpetual_protocol(token_0: str, token_1: str):
    # Perpetual Protocol
    raise NotImplementedError


def phemex(token_0: str, token_1: str):
    # Phemex
    raise NotImplementedError


def phemex_futures(token_0: str, token_1: str):
    # Phemex (Futures)
    raise NotImplementedError


def photonswap(token_0: str, token_1: str):
    # PhotonSwap
    raise NotImplementedError


def pinkswap(token_0: str, token_1: str):
    # PinkSwap
    raise NotImplementedError


def planet_finance(token_0: str, token_1: str):
    # Planet Finance
    raise NotImplementedError


def platypus_finance(token_0: str, token_1: str):
    # Platypus Finance
    raise NotImplementedError


def polkaex_shiden(token_0: str, token_1: str):
    # PolkaEx (Shiden)
    raise NotImplementedError


def polkaswap(token_0: str, token_1: str):
    # Polkaswap
    raise NotImplementedError


def poloniex(token_0: str, token_1: str):
    # Poloniex
    raise NotImplementedError


def poloniex_futures(token_0: str, token_1: str):
    # Poloniex Futures
    raise NotImplementedError


def polycat_finance(token_0: str, token_1: str):
    # Polycat Finance
    raise NotImplementedError


def polydex(token_0: str, token_1: str):
    # PolyDEX
    raise NotImplementedError


def polyient_dex(token_0: str, token_1: str):
    # Polyient Dex
    raise NotImplementedError


def polyzap(token_0: str, token_1: str):
    # PolyZap
    raise NotImplementedError


def powertrade(token_0: str, token_1: str):
    # Powertrade
    raise NotImplementedError


def prime_xbt(token_0: str, token_1: str):
    # Prime XBT
    raise NotImplementedError


def prism(token_0: str, token_1: str):
    # Prism Protocol
    raise NotImplementedError


def probit(token_0: str, token_1: str):
    # ProBit Global
    raise NotImplementedError


def probit_kr(token_0: str, token_1: str):
    # Probit (Korea)
    raise NotImplementedError


def protofi(token_0: str, token_1: str):
    # ProtoFi
    raise NotImplementedError


def puddingswap(token_0: str, token_1: str):
    # PuddingSwap
    raise NotImplementedError


def qtrade(token_0: str, token_1: str):
    # qTrade
    raise NotImplementedError


def quickswap(token_0: str, token_1: str):
    # Quickswap
    raise NotImplementedError


def quipuswap(token_0: str, token_1: str):
    # Quipuswap
    raise NotImplementedError


def quoine(token_0: str, token_1: str):
    # Liquid
    raise NotImplementedError


def radar_relay(token_0: str, token_1: str):
    # Radar Relay
    raise NotImplementedError


def raydium2(token_0: str, token_1: str):
    # Raydium
    raise NotImplementedError


def ref_finance(token_0: str, token_1: str):
    # Ref Finance
    raise NotImplementedError


def resfinex(token_0: str, token_1: str):
    # Resfinex
    raise NotImplementedError


def rfinex(token_0: str, token_1: str):
    # Rfinex
    raise NotImplementedError


def saber(token_0: str, token_1: str):
    # Saber
    raise NotImplementedError


def safe_trade(token_0: str, token_1: str):
    # SafeTrade
    raise NotImplementedError


def sakeswap(token_0: str, token_1: str):
    # SakeSwap
    raise NotImplementedError


def saros(token_0: str, token_1: str):
    # Saros Finance
    raise NotImplementedError


def sashimiswap(token_0: str, token_1: str):
    # Sashimiswap
    raise NotImplementedError


def satoexchange(token_0: str, token_1: str):
    # SatoExchange
    raise NotImplementedError


def secondbtc(token_0: str, token_1: str):
    # SecondBTC
    raise NotImplementedError


def secretswap(token_0: str, token_1: str):
    # SecretSwap
    raise NotImplementedError


def serum_dex(token_0: str, token_1: str):
    # Serum DEX
    raise NotImplementedError


def shibaswap(token_0: str, token_1: str):
    # Shibaswap
    raise NotImplementedError


def siennaswap(token_0: str, token_1: str):
    # Siennaswap
    raise NotImplementedError


def sifchain(token_0: str, token_1: str):
    # Sifchain
    raise NotImplementedError


def sinegy(token_0: str, token_1: str):
    # SINEGY
    raise NotImplementedError


def sistemkoin(token_0: str, token_1: str):
    # Sistemkoin
    raise NotImplementedError


def six_x(token_0: str, token_1: str):
    # 6x
    raise NotImplementedError


def solarbeam(token_0: str, token_1: str):
    # Solarbeam
    raise NotImplementedError


def solarflare(token_0: str, token_1: str):
    # Solarflare
    raise NotImplementedError


def solidly(token_0: str, token_1: str):
    # Solidly
    raise NotImplementedError


def soulswap(token_0: str, token_1: str):
    # Soulswap
    raise NotImplementedError


def south_xchange(token_0: str, token_1: str):
    # SouthXchange
    raise NotImplementedError


def spiritswap(token_0: str, token_1: str):
    # SpiritSwap
    raise NotImplementedError


def spookyswap(token_0: str, token_1: str):
    # SpookySwap
    raise NotImplementedError


def stake_cube(token_0: str, token_1: str):
    # StakeCube Exchange
    raise NotImplementedError


def standard(token_0: str, token_1: str):
    # Standard
    raise NotImplementedError


def stellar_term(token_0: str, token_1: str):
    # StellarTerm
    raise NotImplementedError


def stellaswap(token_0: str, token_1: str):
    # StellaSwap
    raise NotImplementedError


def stocks_exchange(token_0: str, token_1: str):
    # STEX
    raise NotImplementedError


def stormgain(token_0: str, token_1: str):
    # Stormgain
    raise NotImplementedError


def stormgain_futures(token_0: str, token_1: str):
    # Stormgain Futures
    raise NotImplementedError


def sunswap_v1(token_0: str, token_1: str):
    # Sunswap (v1)
    raise NotImplementedError


def sushiswap(token_0: str, token_1: str):
    # Sushiswap
    raise NotImplementedError


def sushiswap_arbitrum(token_0: str, token_1: str):
    # Sushiswap (Arbitrum One)
    raise NotImplementedError


def sushiswap_avalanche(token_0: str, token_1: str):
    # Sushiswap (Avalanche)
    raise NotImplementedError


def sushiswap_bsc(token_0: str, token_1: str):
    # Sushiswap (BSC)
    raise NotImplementedError


def sushiswap_celo(token_0: str, token_1: str):
    # Sushiswap Celo
    raise NotImplementedError


def sushiswap_fantom(token_0: str, token_1: str):
    # Sushiswap (Fantom)
    raise NotImplementedError


def sushiswap_harmony(token_0: str, token_1: str):
    # Sushiswap (Harmony)
    raise NotImplementedError


def sushiswap_polygon_pos(token_0: str, token_1: str):
    # Sushiswap (Polygon POS)
    raise NotImplementedError


def sushiswap_xdai(token_0: str, token_1: str):
    # Sushiswap (xDai)
    raise NotImplementedError


def swappi(token_0: str, token_1: str):
    # Swappi
    raise NotImplementedError


def swapr_arbitrum(token_0: str, token_1: str):
    # Swapr (Arbitrum)
    raise NotImplementedError


def swapr_ethereum(token_0: str, token_1: str):
    # Swapr (Ethereum)
    raise NotImplementedError


def swapr_xdai(token_0: str, token_1: str):
    # Swapr (Xdai)
    raise NotImplementedError


def switcheo(token_0: str, token_1: str):
    # Switcheo
    raise NotImplementedError


def swop_fi(token_0: str, token_1: str):
    # Swop.Fi
    raise NotImplementedError


def synthetix(token_0: str, token_1: str):
    # Kwenta
    raise NotImplementedError


def tangoswap(token_0: str, token_1: str):
    # TangoSwap
    raise NotImplementedError


def tdax(token_0: str, token_1: str):
    # Satang Pro
    raise NotImplementedError


def templedao(token_0: str, token_1: str):
    # TempleDAO
    raise NotImplementedError


def terraswap(token_0: str, token_1: str):
    # Terraswap
    raise NotImplementedError


def tethys(token_0: str, token_1: str):
    # Tethys Finance
    raise NotImplementedError


def tetuswap(token_0: str, token_1: str):
    # Tetuswap
    raise NotImplementedError


def tfm(token_0: str, token_1: str):
    # Terraformer
    raise NotImplementedError


def therocktrading(token_0: str, token_1: str):
    # TheRockTrading
    raise NotImplementedError


def thorswap(token_0: str, token_1: str):
    # THORChain
    raise NotImplementedError


def thorus(token_0: str, token_1: str):
    # Thorus
    raise NotImplementedError


def thorus_moonbeam(token_0: str, token_1: str):
    # Thorus (Moonbeam)
    raise NotImplementedError


def tidebit(token_0: str, token_1: str):
    # Tidebit
    raise NotImplementedError


def tidex(token_0: str, token_1: str):
    # Tidex
    raise NotImplementedError


def tokenize(token_0: str, token_1: str):
    # Tokenize
    raise NotImplementedError


def tokenlon(token_0: str, token_1: str):
    # Tokenlon
    raise NotImplementedError


def tokenomy(token_0: str, token_1: str):
    # Tokenomy
    raise NotImplementedError


def token_sets(token_0: str, token_1: str):
    # TokenSets
    raise NotImplementedError


def tokens_net(token_0: str, token_1: str):
    # TokensNet
    raise NotImplementedError


def toko_crypto(token_0: str, token_1: str):
    # TokoCrypto
    raise NotImplementedError


def tokok(token_0: str, token_1: str):
    # TOKOK
    raise NotImplementedError


def tokpie(token_0: str, token_1: str):
    # Tokpie
    raise NotImplementedError


def tomb_swap_fantom(token_0: str, token_1: str):
    # Tomb Swap (Fantom)
    raise NotImplementedError


def tomodex(token_0: str, token_1: str):
    # TomoDEX
    raise NotImplementedError


def topbtc(token_0: str, token_1: str):
    # TopBTC
    raise NotImplementedError


def trade_ogre(token_0: str, token_1: str):
    # TradeOgre
    raise NotImplementedError


def traderjoe(token_0: str, token_1: str):
    # Trader Joe
    raise NotImplementedError


def tranquil_finance(token_0: str, token_1: str):
    # Tranquil Finance
    raise NotImplementedError


def trisolaris(token_0: str, token_1: str):
    # Trisolaris
    raise NotImplementedError


def tron_trade(token_0: str, token_1: str):
    # TronTrade
    raise NotImplementedError


def tropical_finance(token_0: str, token_1: str):
    # Tropical Finance
    raise NotImplementedError


def trx_market(token_0: str, token_1: str):
    # PoloniDEX
    raise NotImplementedError


def txbit(token_0: str, token_1: str):
    # Txbit
    raise NotImplementedError


def ubeswap(token_0: str, token_1: str):
    # Ubeswap
    raise NotImplementedError


def unicly(token_0: str, token_1: str):
    # Unicly
    raise NotImplementedError


def uniswap(token_0: str, token_1: str):
    # Uniswap (v3)
    raise NotImplementedError


def uniswap_arbitrum(token_0: str, token_1: str):
    # Uniswap (Arbitrum One)
    raise NotImplementedError


def uniswap_optimism(token_0: str, token_1: str):
    # Uniswap (Optimism)
    raise NotImplementedError


def uniswap_polygon(token_0: str, token_1: str):
    # Uniswap (Polygon)
    raise NotImplementedError


def uniswap_v1(token_0: str, token_1: str):
    # Uniswap (v1)
    raise NotImplementedError


def uniswap_v2(token_0: str, token_1: str):
    # Uniswap (v2)
    raise NotImplementedError


def unnamed(token_0: str, token_1: str):
    # Unnamed
    raise NotImplementedError


def upbit(token_0: str, token_1: str):
    # Upbit
    raise NotImplementedError


def upbit_indonesia(token_0: str, token_1: str):
    # Upbit Indonesia
    raise NotImplementedError


def value_liquid(token_0: str, token_1: str):
    # Value Liquid
    raise NotImplementedError


def value_liquid_bsc(token_0: str, token_1: str):
    # vSwap BSC
    raise NotImplementedError


def vcc(token_0: str, token_1: str):
    # VCC Exchange
    raise NotImplementedError


def vebitcoin(token_0: str, token_1: str):
    # Vebitcoin
    raise NotImplementedError


def velic(token_0: str, token_1: str):
    # Velic
    raise NotImplementedError


def vindax(token_0: str, token_1: str):
    # Vindax
    raise NotImplementedError


def vinex(token_0: str, token_1: str):
    # Vinex
    raise NotImplementedError


def viperswap(token_0: str, token_1: str):
    # ViperSwap
    raise NotImplementedError


def virgox(token_0: str, token_1: str):
    # Virgox
    raise NotImplementedError


def vitex(token_0: str, token_1: str):
    # ViteX
    raise NotImplementedError


def voltage_finance(token_0: str, token_1: str):
    # Voltage Finance
    raise NotImplementedError


def voltswap_meter(token_0: str, token_1: str):
    # Voltswap (Meter)
    raise NotImplementedError


def voltswap_theta(token_0: str, token_1: str):
    # Voltswap (Theta)
    raise NotImplementedError


def vvs(token_0: str, token_1: str):
    # VVS Finance
    raise NotImplementedError


def wagyuswap(token_0: str, token_1: str):
    # WagyuSwap
    raise NotImplementedError


def wannaswap(token_0: str, token_1: str):
    # Wannaswap
    raise NotImplementedError


def wanswap(token_0: str, token_1: str):
    # WanSwap
    raise NotImplementedError


def wault_swap(token_0: str, token_1: str):
    # WaultSwap
    raise NotImplementedError


def waultswap_polygon(token_0: str, token_1: str):
    # WaultSwap Polygon
    raise NotImplementedError


def waves(token_0: str, token_1: str):
    # Waves.Exchange
    raise NotImplementedError


def wazirx(token_0: str, token_1: str):
    # WazirX
    raise NotImplementedError


def whale_ex(token_0: str, token_1: str):
    # WhaleEx
    raise NotImplementedError


def whitebit(token_0: str, token_1: str):
    # WhiteBIT
    raise NotImplementedError


def wigoswap(token_0: str, token_1: str):
    # Wigoswap
    raise NotImplementedError


def wootrade(token_0: str, token_1: str):
    # WOO Network
    raise NotImplementedError


def xcoex(token_0: str, token_1: str):
    # XCOEX
    raise NotImplementedError


def xfutures(token_0: str, token_1: str):
    # xFutures
    raise NotImplementedError


def xt(token_0: str, token_1: str):
    # XT.COM
    raise NotImplementedError


def yobit(token_0: str, token_1: str):
    # YoBit
    raise NotImplementedError


def yoshi_exchange_bsc(token_0: str, token_1: str):
    # Yoshi.exchange (BSC)
    raise NotImplementedError


def yoshi_exchange_ftm(token_0: str, token_1: str):
    # Yoshi.exchange (Fantom)
    raise NotImplementedError


def yunex(token_0: str, token_1: str):
    # Yunex.io
    raise NotImplementedError


def zaif(token_0: str, token_1: str):
    # Zaif
    raise NotImplementedError


def zappy(token_0: str, token_1: str):
    # Zappy
    raise NotImplementedError


def zb(token_0: str, token_1: str):
    # ZB
    raise NotImplementedError


def zb_derivatives(token_0: str, token_1: str):
    # ZB (Derivatives)
    raise NotImplementedError


def zbg(token_0: str, token_1: str):
    # ZBG
    raise NotImplementedError


def zbg_futures(token_0: str, token_1: str):
    # ZBG Futures
    raise NotImplementedError


def zbx(token_0: str, token_1: str):
    # ZBX
    raise NotImplementedError


def zebitex(token_0: str, token_1: str):
    # Zebitex
    raise NotImplementedError


def zebpay(token_0: str, token_1: str):
    # ZebPay
    raise NotImplementedError


def zenlink_moonbeam(token_0: str, token_1: str):
    # Zenlink (Moonbeam)
    raise NotImplementedError


def zenlink_moonriver(token_0: str, token_1: str):
    # Zenlink (Moonriver)
    raise NotImplementedError


def zero_ex(token_0: str, token_1: str):
    # 0x Protocol
    raise NotImplementedError


def zero_exchange(token_0: str, token_1: str):
    # Zero Exchange
    raise NotImplementedError


def zg(token_0: str, token_1: str):
    # ZG.com
    raise NotImplementedError


def zgtop(token_0: str, token_1: str):
    # ZG.TOP
    raise NotImplementedError


def zilswap(token_0: str, token_1: str):
    # ZilSwap
    raise NotImplementedError


def zipmex(token_0: str, token_1: str):
    # Zipmex
    raise NotImplementedError


def zipswap(token_0: str, token_1: str):
    # ZipSwap
    raise NotImplementedError


def zkswap(token_0: str, token_1: str):
    # ZKSwap (v1)
    raise NotImplementedError


def zkswap_v2(token_0: str, token_1: str):
    # ZKSpace
    raise NotImplementedError
