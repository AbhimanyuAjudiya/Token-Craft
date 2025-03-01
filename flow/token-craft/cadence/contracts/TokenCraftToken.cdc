pub contract TokenCraftToken {
  pub resource Vault {
    pub var balance: UFix64

    init(balance: UFix64) {
      self.balance = balance
    }

    // Mint tokens (called by Odoo when a purchase is made)
    pub fun mint(amount: UFix64) {
      self.balance = self.balance + amount
    }

    // Stake tokens (called when customer stakes)
    pub fun stake(amount: UFix64): @Vault {
      let stakedVault <- create Vault(balance: amount)
      self.balance = self.balance - amount
      return <-stakedVault
    }
  }
}