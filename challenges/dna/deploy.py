# Usage:
from starkware.crypto.signature.fast_pedersen_hash import pedersen_hash
import asyncio
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import TESTNET
from starknet_py.net import AccountClient, KeyPair
from starknet_py.contract import Contract
from starknet_py.net.models.chains import StarknetChainId
uuid = '2e825cd3-b8e3-4910-b3b1-763da8d975a8'
rpc_endpoint = 'http://2e825cd3-b8e3-4910-b3b1-763da8d975a8@18.157.198.111:5061'
private_key = 0xb77a8a7c71fb4e64c8bc292c37755d8d
player_address = 0x44ced1d5e0ee8a0f74f116680f40f3378f62d3bc24abad7adcdc912addfb5b3
contract_address = 0x378683fe8bf87012fbdfd72293e152081444e6980c107603866ee22f4fb56df

PRIME = 3618502788666131213697322783095070105623107215331596699973092056135872020481

PASSWORD = 3329738248317886966279794942297149793815292158761370755733235303955518040301
r = [0]*17
r[0] = [1498, 997, 2753, 6301]
r[1] = [5939, 1823, 5501, 2069]
r[2] = [113, 127, 131, 137]
r[3] = [1913, 7919, 7127, 7577]
r[4] = [877, 27644437, 35742549198872617291353508656626642567,
        359334085968622831041960188598043661065388726959079837]
r[5] = [16127, 1046527, 16769023, 1073676287]
r[6] = [2381, 2521, 3121, 3613]
r[7] = [3259, 3301, 3307, 3313]
r[8] = [479, 487, 491, 499]
r[9] = [23497, 24571, 25117, 26227]
r[10] = [60493, 63949, 65713, 69313]
r[11] = [87178291199, 479001599, 39916801, 5039]
r[12] = [13, 29, 53, 89]
r[13] = [433494437, 2971215073, 28657, 514229]
r[14] = [131071, 2147483647, 524287, 8191]
r[15] = [786433, 746497, 995329, 839809]
r[16] = [9091, 101, 333667, 9901]

for x in r:
    for i in x:
        if pedersen_hash(i, 317) == PASSWORD:
            print(i)


resX = pedersen_hash(0, 317)
PPP = 317 * 213841469519415116094330572703657595919530921861173819326117931051185480744 + \
    2089986280348253421170679821480865132823066470938446095505822317253594081284
alow = PASSWORD-PPP


async def run():

    gateway_client = GatewayClient(rpc_endpoint, TESTNET)
    account_client = AccountClient(
        client=gateway_client,
        address=player_address,
        key_pair=KeyPair.from_private_key(private_key),
        chain=StarknetChainId.TESTNET,
        supported_tx_version=1,
    )
    block = await gateway_client.get_block(block_number=1)
    print(block)
    ts = block.timestamp
    print('timestamp1', ts)

    contract = await Contract.from_address(contract_address, account_client)
    print(contract.functions)

    call = contract.functions['test_password'].prepare([17, 0])
    tx_r = await account_client.execute(call, auto_estimate=True)
    await account_client.wait_for_tx(tx_r.transaction_hash)
    print(tx_r)
    print(tx_r.transaction_hash)


if __name__ == "__main__":
    asyncio.run(run())
    r = []
    r[0] = res1 = [1498, 997, 2753, 6301]
    r[1] = res2 = [5939, 1823, 5501, 2069]
    r[2] = res3 = [113, 127, 131, 137]
    r[3] = res4 = [1913, 7919, 7127, 7577]
    r[4] = res5 = [877, 27644437, 35742549198872617291353508656626642567,
                   359334085968622831041960188598043661065388726959079837]
    r[5] = res6 = [16127, 1046527, 16769023, 1073676287]
    r[6] = res7 = [2381, 2521, 3121, 3613]
    r[7] = res8 = [3259, 3301, 3307, 3313]
    r[8] = res9 = [479, 487, 491, 499]
    r[9] = res10 = [23497, 24571, 25117, 26227]
    r[10] = res11 = [60493, 63949, 65713, 69313]
    r[11] = res12 = [87178291199, 479001599, 39916801, 5039]
    r[12] = res13 = [13, 29, 53, 89]
    r[13] = res14 = [433494437, 2971215073, 28657, 514229]
    r[14] = res15 = [131071, 2147483647, 524287, 8191]
    r[15] = res16 = [786433, 746497, 995329, 839809]
    r[16] = res17 = [9091, 101, 333667, 9901]

    for x in r:
        for i in x:
            if pedersen_hash(i, 317) == PASSWORD:
                print(i)
    resX = pedersen_hash(0, 317)
    PPP = 317 * 213841469519415116094330572703657595919530921861173819326117931051185480744 + \
        2089986280348253421170679821480865132823066470938446095505822317253594081284
    alow = PASSWORD-PPP
