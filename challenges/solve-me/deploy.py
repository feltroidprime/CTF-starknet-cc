# Usage:
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

    call = contract.functions['solve'].prepare()
    tx_r = await account_client.execute(call, auto_estimate=True)
    await account_client.wait_for_tx(tx_r.transaction_hash)
    print(tx_r)
    print(tx_r.transaction_hash)


if __name__ == "__main__":
    asyncio.run(run())
