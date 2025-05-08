# System Overview

Ghost is built as a modern web application that interfaces with the Internet Computer blockchain. The system architecture follows a modular design with clear separation of concerns:

<figure><img src="../.gitbook/assets/Ghost - C4 L1 Diagram.png" alt=""><figcaption></figcaption></figure>

The architecture consists of these primary layers:

1. **Presentation Layer**: React-based UI components, responsive design
2. **Application Layer**: Business logic, state management, data flow
3. **Service Layer**: API connectors, wallet integration, AI services
4. **Blockchain Layer**: Internet Computer canister interaction

Data flows from the user through the presentation layer to the service layer, which communicates with the blockchain to generate and verify proofs. The system is designed to maintain privacy by keeping sensitive operations client-side whenever possible.
