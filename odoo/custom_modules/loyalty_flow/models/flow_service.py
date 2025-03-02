from flow_py_sdk import flow_client, Script, Tx
import json

class FlowService:
    def __init__(self):
        self.client = flow_client(host="localhost", port=3569)  # Flow emulator

    async def mint_tokens(self, customer_address, amount):
        script = Script.from_file("flow/token-craft/cadence/transactions/mint_tokens.cdc")
        result = await self.client.execute_script(
            script=script,
            arguments=[customer_address, amount]
        )
        return json.loads(result.json_value)

    async def stake_tokens(self, customer_address, amount):
        # Similar logic for staking
        script = Script.from_file("flow/token-craft/cadence/transactions/stake_tokens.cdc")
        result = await self.client.execute_script(
            script=script,
            arguments=[customer_address, amount]
        )
        return json.loads(result.json_value)