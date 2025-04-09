Ghost's zero-knowledge proof system is built on cryptographic principles that enable a prover to demonstrate knowledge of certain information without revealing the information itself. Specifically, the system allows users to prove they own a certain token without revealing their actual balance.

The proof generation process works as follows:

1. User connects their wallet to the application
2. The application retrieves the user's token balance
3. The token balance and user's principal ID are used to create a cryptographic commitment
4. This commitment and additional information are sent to the ZK canister
5. The canister generates a proof that can be verified without revealing the original data
6. The proof is returned to the client and stored locally
7. A shareable verification link is created containing the proof or a reference to it

The verification process then works in reverse:

1. A verifier accesses the proof via the shared link
2. The proof data is sent to the ZK canister for verification
3. The canister validates the cryptographic proof without seeing the original data
4. The result of the verification is returned to the client

This approach ensures complete privacy while still allowing for trustless verification.