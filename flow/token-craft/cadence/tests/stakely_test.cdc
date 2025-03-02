import Test
import TokenCraftToken from "../cadence/contracts/TokenCraftToken.cdc"

access(all) fun testMintAndStake() {
    let admin: Test.TestAccount = Test.createAccount()
    let user: Test.TestAccount = Test.createAccount()
    
    // Deploy contract
    Test.deployContract(
        name: "TokenCraftToken",
        path: "../cadence/contracts/TokenCraftToken.cdc",
        admin: admin
    )
    
    // Mint tokens
    Test.run(
        name: "Mint 50 tokens",
        transaction: "../cadence/transactions/mint_tokens.cdc",
        signers: [admin],
        args: [50.0, user.address]
    )
    // Check balance
    let balance: Test.ScriptResult = Test.executeScript(
        "../cadence/scripts/get_balance.cdc",
        [user.address]
    )
    Test.assertEqual(50.0, balance)
    // Stake tokens
    let stakedVault: Test.TransactionResult = Test.executeTransaction(
        "../cadence/transactions/stake_tokens.cdc",
        [user],
        [30.0]
    )
    // Verify balances
    let newBalance: Test.ScriptResult = Test.executeScript(
        "../cadence/scripts/get_balance.cdc",
        [user.address]
    )
    Test.assertEqual(20.0, newBalance)
    destroy stakedVault
}