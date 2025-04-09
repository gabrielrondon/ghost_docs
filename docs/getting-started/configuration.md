Ghost is designed to be used without extensive configuration. The primary configuration points are:

- **API Key for AI Features**: Set in the Settings > API Configuration section of the application
- **Theme Selection**: Toggle between light and dark mode in the user interface
- **Network Configuration**: By default, Ghost connects to the Internet Computer mainnet

Advanced users can modify the application's behavior by editing constants in the source code:

- `src/utils/icpLedger.ts`: LEDGER_CANISTER_ID for the ICP ledger canister
- `src/services/zkProof/canisterDefinition.ts`: ZK_PROOF_CANISTER_ID for the ZK proof canister

---