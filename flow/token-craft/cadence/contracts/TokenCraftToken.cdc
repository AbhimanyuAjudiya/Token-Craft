access(all) contract TokenCraftToken {
    access(all) event TokensMinted(amount: UFix64, to: Address)
    access(all) event TokensStaked(amount: UFix64, from: Address)
    
    access(all) resource Vault {
        access(all) var balance: UFix64
        
        access(all) fun deposit(amount: UFix64) {
            self.balance = self.balance + amount
        }
        
        access(all) fun withdraw(amount: UFix64): @Vault {
            pre { self.balance >= amount }
            self.balance = self.balance - amount
            return <- create Vault(balance: amount)
        }
        
        init(balance: UFix64) {
            self.balance = balance
        }
    }

    access(all) resource Admin {
        access(all) fun createVault(): @Vault {
            return <- create Vault(balance: 0.0)
        }
    }

    access(all) fun mintTokens(amount: UFix64, recipient: &Vault) {
        recipient.deposit(amount: amount)
        emit TokensMinted(amount: amount, to: recipient.owner!.address)
    }

    access(all) fun stakeTokens(amount: UFix64, from: &Vault): @Vault {
        let stakedVault: @TokenCraftToken.Vault <- from.withdraw(amount: amount)
        emit TokensStaked(amount: amount, from: from.owner!.address)
        return <- stakedVault
    }

    init() {
        self.account.storage.save(
            <- create Admin(),
            to: /storage/TokenCraftAdmin
        )
    }
}