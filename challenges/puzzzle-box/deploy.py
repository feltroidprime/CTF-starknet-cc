# Usage:
import asyncio
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import TESTNET
from starknet_py.net import AccountClient, KeyPair
from starknet_py.contract import Contract
from starknet_py.net.models.chains import StarknetChainId
uuid = '18f560a1-2c7f-41c8-9333-545b95b486c9'
rpc_endpoint = 'http://18f560a1-2c7f-41c8-9333-545b95b486c9@18.157.198.111:5060'
private_key = 0xfa7ffc884bf5d72df8c58dc098b98f31
player_address = 0x5816110afbcef8e7ef68bbe9d87871b5aa98cf01c0ba056abd443459ba3f674
contract_address = 0x599df3c1c72d303ba92294265f2ad94aa56e4780f8e092c8c25db1ac0de81c


PRIME = 3618502788666131213697322783095070105623107215331596699973092056135872020481

print("h")


async def run():

    gateway_client = GatewayClient(rpc_endpoint, TESTNET)
    account_client = AccountClient(
        client=gateway_client,
        address=player_address,
        key_pair=KeyPair.from_private_key(private_key),
        chain=StarknetChainId.TESTNET,
        supported_tx_version=1,
    )

    # block = await gateway_client.get_block(block_number=0)
    # print(block)
    # ts = block.timestamp
    # print('timestamp1', ts)
    print("MAIN")

    block = await gateway_client.get_block(0)
    print(block)

    contract = await Contract.from_address(contract_address, account_client)

    print(contract.functions)
    prod = (3609145100 + 12345 + int(player_address, 16)) % PRIME
    call = contract.functions['solve_step_1'].prepare(prod)
    tx_r = await account_client.execute(call, auto_estimate=True)
    await account_client.wait_for_tx(tx_r.transaction_hash)
    print(tx_r)
    print(tx_r.transaction_hash)


if __name__ == "__main__":
    asyncio.run(run())
