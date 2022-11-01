import { Provider, constants } from "starknet";
 
let uuid = "import { Provider, constants } from "starknet";
 
let baseUrl = "http://3749e5f4-b16f-4b4c-9f1c-c08c48bfe07b@18.157.198.111:5056";
 
const provider = new Provider({
  sequencer: {
    baseUrl: `${baseUrl}`,
    chainId: constants.StarknetChainId.TESTNET,
    feederGatewayUrl: `${baseUrl}/feeder_gateway`,
    gatewayUrl: `${baseUrl}/gateway`,
    headers: {
      Authorization: `Basic ${Buffer.from(uuid + ":").toString("base64")}`,
    },
  },
});
 
async function main() {
  let block = await provider.getBlock(0);
  console.log(block);
}
 
main();