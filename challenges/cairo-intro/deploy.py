# Usage:
import asyncio
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import TESTNET
from starknet_py.net import AccountClient, KeyPair
from starknet_py.contract import Contract
from starknet_py.net.models.chains import StarknetChainId
uuid = 'a9119689-cbe6-4b8c-931a-36c82c2039e4'
rpc_endpoint = 'http://a9119689-cbe6-4b8c-931a-36c82c2039e4@18.157.198.111:5056'
private_key = 0x231c6cea1430a522db1d2a8605dc3d1
player_address = 0x4e1d801f8a92a6ef06381eecd5e10f2cbe6de9607d1c6e5b159456d0aeef1ea
contract_address = 0x3214d9c4ab9349270c9f0beab2191841589994e37b50174d15217286e6ae7c3

PRIME = 3618502788666131213697322783095070105623107215331596699973092056135872020481


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
    (ts,) = await contract.functions['get_balance'].call()
    print('timestamp2', ts)
    x = (31333333388-ts) % PRIME

    call = contract.functions['increase_balance'].prepare(
        x)
    tx_r = await account_client.execute(call, auto_estimate=True)
    await account_client.wait_for_tx(tx_r.transaction_hash)
    print(tx_r)
    print(tx_r.transaction_hash)

    call = contract.functions['solve_challenge'].prepare()
    tx_r = await account_client.execute(call, auto_estimate=True)
    await account_client.wait_for_tx(tx_r.transaction_hash)
    print(tx_r)
    print(tx_r.transaction_hash)

    # call = contract.functions['is_challenge_done'].prepare()
    # tx_r = await account_client.execute(call, auto_estimate=True)
    # await account_client.wait_for_tx(tx_r.transaction_hash)
    # print(tx_r)
    # print(tx_r.transaction_hash)


if __name__ == "__main__":
    asyncio.run(run())
