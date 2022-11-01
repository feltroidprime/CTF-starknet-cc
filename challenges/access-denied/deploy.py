# Usage:
import asyncio

from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import TESTNET
from starknet_py.net import AccountClient, KeyPair
from starknet_py.contract import Contract
from starknet_py.net.models.chains import StarknetChainId
uuid = 'add6fdd6-48aa-48de-990b-f194c8881af8'
rpc_endpoint = 'http://add6fdd6-48aa-48de-990b-f194c8881af8@18.157.198.111:5054'
private_key = 0xe32c80b021e84e029595fc55f93d8979
player_address = 0x5fe13111623614fea36c3eb89fa8fda338e9b9071e492925879acbe121461dc
contract_address = 0x6a01657d98d1cfa6eed0196c9ec2b883ab947313f7dfdc7132c276908171968


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
    call = contract.functions['solve'].prepare()
    tx_r = await account_client.execute(call, auto_estimate=True)
    await account_client.wait_for_tx(tx_r.transaction_hash)
    print(tx_r)
    print(tx_r.transaction_hash)

if __name__ == "__main__":
    asyncio.run(run())
