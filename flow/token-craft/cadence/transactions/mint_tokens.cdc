import TokenCraftToken from "../contracts/TokenCraftToken.cdc"

transaction(amount: UFix64, recipient: Address) {
    prepare(admin: AuthAccount) {
        let adminRef = admin.borrow<&TokenCraftToken.Admin>(from: /storage/TokenCraftAdmin)
            ?? panic("No Admin resource")
        
        let recipientAcc: &Account = getAccount(recipient)
        let recipientVault = recipientAcc.getCapability(/public/TokenCraftTokenVault)
            .borrow<&TokenCraftToken.Vault>()
            ?? panic("No Vault found")
        
        TokenCraftToken.mintTokens(amount: amount, recipient: recipientVault)
    }
}