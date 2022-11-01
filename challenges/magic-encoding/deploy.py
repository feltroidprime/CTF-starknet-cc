# Usage:
import asyncio

from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import TESTNET
from starknet_py.net import AccountClient, KeyPair
from starknet_py.contract import Contract
from starknet_py.net.models.chains import StarknetChainId
uuid = '7a90e4f2-d4a0-4165-a5f2-63e491072c02'
rpc_endpoint = 'http://7a90e4f2-d4a0-4165-a5f2-63e491072c02@18.157.198.111:5050'
private_key = 0x73a69424f5023de6ca9785425693eb7
player_address = 0x40c15f89d113e280b2ee5b717a7551d1586ab23236767d2e1a69555340f1d6d
contract_address = 0x6652e4eb74bc3ea5ae754af4c25f6663b510346c22da21b4cf3f3f1694ce61a


async def run():

    gateway_client = GatewayClient(rpc_endpoint, TESTNET)
    account_client = AccountClient(
        client=gateway_client,
        address=player_address,
        key_pair=KeyPair.from_private_key(private_key),
        chain=StarknetChainId.TESTNET,
        supported_tx_version=1,
    )
    block = await gateway_client.get_block(0)
    print(block)

    contract = await Contract.from_address(contract_address, account_client)
    print(contract.functions)

    call = contract.functions['test_password'].prepare(31718)
    tx_r = await account_client.execute(call, auto_estimate=True)
    await account_client.wait_for_tx(tx_r.transaction_hash)
    print(tx_r)
    print(tx_r.transaction_hash)

    call = contract.functions['is_challenge_done'].prepare()
    tx_r = await account_client.execute(call, auto_estimate=True)
    await account_client.wait_for_tx(tx_r.transaction_hash)
    print(tx_r)
    print(tx_r.transaction_hash)


if __name__ == "__main__":
    asyncio.run(run())
