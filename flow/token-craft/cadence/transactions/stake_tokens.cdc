import TokenCraftToken from "../contracts/TokenCraftToken.cdc"

transaction(amount: UFix64): @TokenCraftToken.Vault {
    prepare(user: AuthAccount) {
        let vault = user.borrow<&TokenCraftToken.Vault>(from: /storage/TokenCraftTokenVault)
            ?? panic("No Vault found")
        
        self.stakedVault <- TokenCraftToken.stakeTokens(amount: amount, from: vault)
    }

    execute {
        return <- self.stakedVault
    }
}