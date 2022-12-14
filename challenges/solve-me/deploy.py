# Usage:
import asyncio
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import TESTNET
from starknet_py.net import AccountClient, KeyPair
from starknet_py.contract import Contract
from starknet_py.net.models.chains import StarknetChainId
uuid = '2f530e87-a2c5-47c9-8ebf-e704dc06e9d8'
rpc_endpoint = 'http://2f530e87-a2c5-47c9-8ebf-e704dc06e9d8@18.157.198.111:5061'
private_key = 0x417ea85a3231ed89e745f9623ee2c32b
player_address = 0x6fb14af9a52544466d0b00b536930d57c49f9140c3ee989102a930a88cec521
contract_address = 0x22307a497c26e0766e6701e3ed78c21166ba691e9fad47d2f3e836cbbdaf52c

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
