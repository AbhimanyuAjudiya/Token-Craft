import Test

access(all) let account = Test.createAccount()

access(all) fun testContract() {
    let err = Test.deployContract(
        name: "TokenCraftToken",
        path: "../contracts/TokenCraftToken.cdc",
        arguments: [],
    )

    Test.expect(err, Test.beNil())
}