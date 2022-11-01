# Usage:
import asyncio

from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import TESTNET
from starknet_py.net import AccountClient, KeyPair
from starknet_py.contract import Contract
from starknet_py.net.models.chains import StarknetChainId

uuid = "6f0c8844-9117-45c4-9224-a00f67620159"

player_address =0x357a5f6726bca218ed01bc69cffbc5b2b713d73daed185f29ced9aaaf969deb
contract_address = 0x27034138e2f783ae3ecf346c3d88b0b06cd8a5111fd8a2f553b957b5070a02c
async def run():
    rpc_endpoint = f"http://6f0c8844-9117-45c4-9224-a00f67620159@18.157.198.111:5059"

    gateway_client = GatewayClient(rpc_endpoint, TESTNET)
    account_client = AccountClient(
    client=gateway_client,
    address=player_address,
    key_pair=KeyPair.from_private_key(0xcf7f5c25b18e8fe2c5c3ae1a1e8c6e5c),
    chain=StarknetChainId.TESTNET,
    supported_tx_version=1,
)
    block = await gateway_client.get_block(0)
    print(block)

    contract = await Contract.from_address(contract_address, account_client)
    print(contract.functions)

    call = contract.functions['claim'].prepare(player_address)
    tx_r = await account_client.execute(call, auto_estimate=True)
    await account_client.wait_for_tx(tx_r.transaction_hash)
    print(tx_r)

    block = await gateway_client.get_block(1)
    print(block)

if __name__ == "__main__":
    asyncio.run(run())

