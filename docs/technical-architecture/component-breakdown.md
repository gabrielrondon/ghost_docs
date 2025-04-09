The Ghost application consists of several key components that work together:

### Frontend Components

- **Wallet Connection**: Interfaces with Internet Computer wallets (Internet Identity and Plug)
- **ZK Proof Generator**: Creates zero-knowledge proofs of token ownership
- **ZK Proof Verifier**: Validates ZK proofs shared by others
- **AI Summary Generator**: Produces plain-language explanations of proofs
- **Test Suite**: Provides end-to-end testing of the proof system

### Backend Components

- **ZK Proof Canister**: Internet Computer canister responsible for generating and verifying proofs
- **OpenAI Integration**: Connects to OpenAI services to generate proof summaries

### Service Components

- **Authentication Service**: Manages wallet connections and identity
- **Proof Service**: Handles proof generation, storage, and verification logic
- **AI Service**: Manages AI prompt construction and response processing
- **Balance Service**: Fetches token balances from the Internet Computer ledger