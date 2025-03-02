import TokenCraftToken from "../contracts/TokenCraftToken.cdc"

access(all) fun main(address: Address): UFix64 {
    let account = getAccount(address)
    let capability = account.getCapability<&TokenCraftToken.Vault>(/public/TokenCraftTokenVault)
    let vaultRef = capability.borrow()
                  ?? panic("No Vault found")
    return vaultRef.balance
}