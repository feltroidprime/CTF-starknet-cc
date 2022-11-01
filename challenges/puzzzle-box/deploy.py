# Usage:
import asyncio
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import TESTNET
from starknet_py.net import AccountClient, KeyPair
from starknet_py.contract import Contract
from starknet_py.net.models.chains import StarknetChainId
uuid = 'e591c074-0e91-4483-b3ac-a7b03d512acb'
rpc_endpoint = 'http://e591c074-0e91-4483-b3ac-a7b03d512acb@18.157.198.111:5060'
private_key = 0xc0dbb4a6d2fe14a182def90dfba34b0d
player_address = 0x12c401cf37fe384a715ad5dd3114cede09b7de8119081ea9bd2edabc9f728fd
contract_address = 0x57dbbcc4a0036dd5b06146cf366630b5398c3c35de403c657046d96dbcb990
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
    prod = (3609145100 + 12345 + player_address) % PRIME
    call = contract.functions['solve_step_1'].prepare(prod)
    tx_r = await account_client.execute(call, auto_estimate=True)
    await account_client.wait_for_tx(tx_r.transaction_hash)
    print(tx_r)
    print(tx_r.transaction_hash)

    prod = ((1010886179 + 965647271) % PRIME + contract_address) % PRIME
    call = contract.functions['solve_step_2'].prepare(prod)
    tx_r = await account_client.execute(call, auto_estimate=True)
    await account_client.wait_for_tx(tx_r.transaction_hash)
    print(tx_r)
    print(tx_r.transaction_hash)

    ap_0 = 3
    ap_1 = 4

    ap_2 = ap_1*ap_0 % PRIME
    ap_3 = ap_2 * ap_1 % PRIME
    ap_4 = ap_3 * ap_2 % PRIME
    ap_5 = ap_4 * ap_3 % PRIME

    ap_6 = ap_4 + ap_2 % PRIME
    ap_7 = ap_6 + ap_3 % PRIME

    prod = ap_6*ap_7 % PRIME
    call = contract.functions['solve_step_3'].prepare(prod)
    tx_r = await account_client.execute(call, auto_estimate=True)
    await account_client.wait_for_tx(tx_r.transaction_hash)
    print(tx_r)
    print(tx_r.transaction_hash)

    prod = 84092830
    call = contract.functions['solve_step_4'].prepare(prod)
    tx_r = await account_client.execute(call, auto_estimate=True)
    await account_client.wait_for_tx(tx_r.transaction_hash)
    print(tx_r)
    print(tx_r.transaction_hash)

    call = contract.functions['solve'].prepare()
    tx_r = await account_client.execute(call, auto_estimate=True)
    await account_client.wait_for_tx(tx_r.transaction_hash)
    print(tx_r)
    print(tx_r.transaction_hash)

if __name__ == "__main__":
    asyncio.run(run())
