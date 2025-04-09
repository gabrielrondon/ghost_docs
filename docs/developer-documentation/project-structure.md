The Ghost project follows a modular structure organized by feature and responsibility:

```
/src
  /components        # React components
    /ZKProofGenerator  # Proof generation components
    /ZKProofVerifier   # Proof verification components
    /ZKProofSummary    # AI summary components
    /ZKProofTest       # Testing components
    /ui                # UI component library
  /hooks             # React hooks
    /useZKProofGeneration  # Logic for generating proofs
    /useZKProofVerification # Logic for verifying proofs
    /wallet              # Wallet connection hooks
  /services          # Application services
    /zkProof            # ZK proof service
    /aiService          # AI integration service
    /authService        # Authentication service
    /balanceService     # Token balance service
  /utils             # Utility functions
    /icpLedger          # ICP ledger utilities
    /plugWallet         # Plug wallet utilities
  /pages             # Top-level page components
  /lib               # Shared libraries
```