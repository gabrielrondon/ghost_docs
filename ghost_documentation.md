# Ghost: The ZK Notary Agent

## Comprehensive Documentation

---

# Table of Contents

1. [Introduction](#1-introduction)
   - [What is Ghost?](#what-is-ghost)
   - [Key Features](#key-features)
   - [Project Vision](#project-vision)

2. [Technical Architecture](#2-technical-architecture)
   - [System Overview](#system-overview)
   - [Component Breakdown](#component-breakdown)
   - [Zero-Knowledge Proof System](#zero-knowledge-proof-system)
   - [AI Enhancement Layer](#ai-enhancement-layer)

3. [Getting Started](#3-getting-started)
   - [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Development Environment Setup](#development-environment-setup)
   - [Configuration](#configuration)

4. [User Guide](#4-user-guide)
   - [Connecting Your Wallet](#connecting-your-wallet)
   - [Generating ZK Proofs](#generating-zk-proofs)
   - [Verifying ZK Proofs](#verifying-zk-proofs)
   - [Understanding AI-Enhanced Explanations](#understanding-ai-enhanced-explanations)
   - [Testing ZK Proof System](#testing-zk-proof-system)

5. [Developer Documentation](#5-developer-documentation)
   - [Project Structure](#project-structure)
   - [Core Services](#core-services)
   - [Key Components](#key-components)
   - [Integration Points](#integration-points)
   - [Testing Framework](#testing-framework)

6. [ZK Proof Canister](#6-zk-proof-canister)
   - [Canister Overview](#canister-overview)
   - [API Documentation](#api-documentation)
   - [Canister Deployment](#canister-deployment)
   - [Integration with Frontend](#integration-with-frontend)

7. [AI Components](#7-ai-components)
   - [OpenAI Integration](#openai-integration)
   - [Prompt Engineering](#prompt-engineering)
   - [AI Summary Generation](#ai-summary-generation)

8. [Security Considerations](#8-security-considerations)
   - [Privacy Guarantees](#privacy-guarantees)
   - [Data Protection](#data-protection)
   - [Client-Side Security](#client-side-security)

9. [Future Roadmap](#9-future-roadmap)
   - [Expanded Use Cases](#expanded-use-cases)
   - [Enhanced AI Features](#enhanced-ai-features)
   - [Additional Token Support](#additional-token-support)

10. [API Reference](#10-api-reference)
    - [ZK Proof API](#zk-proof-api)
    - [AI Enhancement API](#ai-enhancement-api)
    - [Wallet Integration API](#wallet-integration-api)

11. [Troubleshooting](#11-troubleshooting)
    - [Common Issues](#common-issues)
    - [Error Messages](#error-messages)
    - [Support Resources](#support-resources)

12. [Contributing](#12-contributing)
    - [Development Workflow](#development-workflow)
    - [Code Standards](#code-standards)
    - [Pull Request Process](#pull-request-process)

13. [Glossary](#13-glossary)
    - [Zero-Knowledge Terminology](#zero-knowledge-terminology)
    - [Internet Computer Terms](#internet-computer-terms)
    - [Project-Specific Terms](#project-specific-terms)

---

# 1. Introduction

## What is Ghost?

Ghost (The ZK Notary Agent) is a privacy-focused application that enables users to create and verify Zero-Knowledge Proofs (ZKPs) on the Internet Computer blockchain. It serves as a bridge between complex cryptographic technology and everyday use cases, allowing users to prove ownership of digital assets without revealing sensitive information such as their account balances or complete identities.

The project combines cutting-edge zero-knowledge cryptography with artificial intelligence to provide easily understandable explanations of what each proof demonstrates. This combination makes privacy technology more accessible to users who may not have technical backgrounds in cryptography.

## Key Features

- **Zero-Knowledge Proof Generation**: Create cryptographic proofs that verify token ownership without revealing the actual balance
- **Anonymous Verification**: Share proofs through unique links that can be verified by third parties without revealing user identity
- **AI-Enhanced Explanations**: Get plain-language summaries of what each proof demonstrates
- **Internet Computer Integration**: Built on the Internet Computer blockchain with native ICP token support
- **End-to-End Testing**: Comprehensive test suite to validate the full proof lifecycle
- **Privacy Preservation**: All sensitive operations happen client-side to maintain privacy
- **User-Friendly Interface**: Intuitive UI designed for users of all technical levels

## Project Vision

Ghost represents the first step in creating a comprehensive Zero-Knowledge service for the Internet Computer ecosystem. The vision extends beyond the current implementation to create a privacy-preserving infrastructure layer that can be used across a wide range of applications.

Our mission is to make privacy technology accessible to everyone by:

1. Simplifying complex cryptographic concepts through intuitive interfaces
2. Providing AI-enhanced explanations that demystify zero-knowledge technology
3. Creating building blocks for developers to integrate privacy features into their own applications
4. Establishing standards for private attestations on the Internet Computer

In the rapidly evolving digital landscape where data privacy concerns continue to grow, Ghost aims to empower users with the tools to maintain control over their sensitive information while still participating fully in the digital economy.

---

# 2. Technical Architecture

## System Overview

Ghost is built as a modern web application that interfaces with the Internet Computer blockchain. The system architecture follows a modular design with clear separation of concerns:

![Ghost System Architecture](https://i.imgur.com/2pApLMl.png)

The architecture consists of these primary layers:

1. **Presentation Layer**: React-based UI components, responsive design
2. **Application Layer**: Business logic, state management, data flow
3. **Service Layer**: API connectors, wallet integration, AI services
4. **Blockchain Layer**: Internet Computer canister interaction

Data flows from the user through the presentation layer to the service layer, which communicates with the blockchain to generate and verify proofs. The system is designed to maintain privacy by keeping sensitive operations client-side whenever possible.

## Component Breakdown

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

## Zero-Knowledge Proof System

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

## AI Enhancement Layer

The AI enhancement layer adds a unique dimension to Ghost, making complex cryptographic operations more accessible to non-technical users. This layer:

1. Takes information about a generated proof
2. Constructs a prompt for the OpenAI API
3. Receives the AI response with a plain-language explanation
4. Presents the explanation to the user alongside the technical proof details

The implementation uses carefully designed prompts to ensure the AI explains the proof accurately while maintaining appropriate security boundaries. The AI never has access to the actual proof data or user's private information.

---

# 3. Getting Started

## Installation

To install Ghost locally for development or testing purposes, follow these steps:

```bash
# Clone the repository
git clone https://github.com/gabrielrondon/ghost_dev.git
cd ghost_dev

# Install dependencies
npm install

# Start the development server
npm run dev
```

## Prerequisites

Before installing Ghost, ensure you have the following prerequisites:

- **Node.js**: v16.0.0 or higher
- **npm**: v8.0.0 or higher
- **Internet Computer wallet**: Either Internet Identity or Plug wallet
- **OpenAI API key**: (Optional) For AI-enhanced explanations

## Development Environment Setup

To set up a complete development environment:

1. **Install Node.js and npm**: Download from [nodejs.org](https://nodejs.org/)

2. **Set up an Internet Computer wallet**:
   - [Internet Identity](https://identity.ic0.app/)
   - [Plug Wallet](https://plugwallet.ooo/)

3. **Get an OpenAI API key** (optional):
   - Create an account at [OpenAI](https://platform.openai.com/)
   - Generate an API key in your account dashboard

4. **Configure environment variables**:
   - No environment variables are needed for basic functionality
   - API keys are stored in the browser's localStorage for security

## Configuration

Ghost is designed to be used without extensive configuration. The primary configuration points are:

- **API Key for AI Features**: Set in the Settings > API Configuration section of the application
- **Theme Selection**: Toggle between light and dark mode in the user interface
- **Network Configuration**: By default, Ghost connects to the Internet Computer mainnet

Advanced users can modify the application's behavior by editing constants in the source code:

- `src/utils/icpLedger.ts`: LEDGER_CANISTER_ID for the ICP ledger canister
- `src/services/zkProof/canisterDefinition.ts`: ZK_PROOF_CANISTER_ID for the ZK proof canister

---

# 4. User Guide

## Connecting Your Wallet

To use Ghost, you'll first need to connect your Internet Computer wallet. Ghost supports two wallet providers:

### Internet Identity

1. Navigate to the Ghost application
2. Click on "Connect with Internet Identity" button
3. You will be redirected to the Internet Identity service
4. Authenticate using your preferred method (security key, passphrase, etc.)
5. After successful authentication, you'll be redirected back to Ghost
6. Your wallet will now be connected and your token balances will be displayed

### Plug Wallet

1. Ensure the Plug wallet extension is installed in your browser
2. Navigate to the Ghost application
3. Click on "Connect with Plug Wallet" button
4. A popup from the Plug wallet will appear asking for connection approval
5. Approve the connection request
6. Your wallet will now be connected and your token balances will be displayed

If you don't see the Plug wallet option, you may need to install the Plug browser extension first.

## Generating ZK Proofs

Once your wallet is connected, you can generate a Zero-Knowledge Proof of token ownership:

1. In the main interface, locate the "ZK Proof Generator" card
2. Select the token you want to create a proof for (currently only ICP is supported)
3. Click the "Generate ZK Proof" button
4. The application will create a cryptographic proof, which may take a few seconds
5. When complete, you'll see a dialog with your proof details
6. The dialog includes:
   - Proof ID: A unique identifier for this proof
   - Shareable Link: A URL that can be shared with others to verify the proof
   - Token: The token this proof is for
   - Generated At: Timestamp of proof creation
   - AI-Enhanced Summary: A plain-language explanation of what the proof demonstrates

### Sharing Proofs

To share your proof with someone else:

1. From the proof result dialog, click the "Share Proof" button to copy the shareable link
2. Send this link to the person who needs to verify your token ownership
3. When they open the link, they'll be able to verify your proof without seeing your actual balance

Alternatively, you can copy just the Proof ID by clicking the copy button next to it, and instruct the verifier to enter it manually in the verification page.

## Verifying ZK Proofs

To verify a proof that someone has shared with you:

1. Access the shared verification link, or navigate to the "Verify" page
2. If using a link, the proof will be verified automatically
3. If entering manually, paste the Proof ID in the verification form and click "Verify"
4. The system will check the cryptographic proof and display the result
5. If valid, you'll see:
   - A success message confirming the proof is valid
   - Details about what the proof demonstrates
   - An AI-enhanced explanation of the proof's significance
6. If invalid, you'll see an error message explaining why the verification failed

The verification process confirms that the person owns the specified token without revealing their actual balance or account details.

## Understanding AI-Enhanced Explanations

Each successful proof generation and verification includes an AI-enhanced explanation to help understand what the proof demonstrates in plain language.

### Setting Up AI Explanations

To enable AI explanations:

1. Go to the Settings page
2. Navigate to the "API Configuration" tab
3. Enter your OpenAI API key
4. Click "Save Key"

Once configured, AI explanations will be automatically generated when:
- You create a new ZK proof
- You verify a valid proof

### Interpreting AI Summaries

AI summaries typically include:

1. **Brief Summary**: A one-sentence explanation of what the proof demonstrates
2. **Detailed Explanation**: A longer explanation of the proof's significance and how zero-knowledge technology protects privacy

These explanations help non-technical users understand the value and meaning of the cryptographic proof in everyday terms.

## Testing ZK Proof System

Ghost includes a comprehensive test suite to validate the ZK proof system's functionality:

1. Navigate to the "Test" page in the application
2. Connect your wallet if not already connected
3. Select a token to test with from the dropdown
4. Click "Run End-to-End Tests"
5. The system will execute a series of tests:
   - Generate ZK Proof: Tests proof generation
   - Verify ZK Proof: Tests verification of the generated proof
   - Anonymous Verification: Tests verification with an anonymous agent
6. Test results will be displayed showing the success or failure of each step
7. For detailed analysis, click "View Detailed Results"

This testing functionality ensures the entire proof lifecycle works correctly and helps diagnose any issues.

---

# 5. Developer Documentation

## Project Structure

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

## Core Services

### ZK Proof Service

Located in `src/services/zkProof`, this service handles all interaction with the ZK proof canister:

```typescript
// Key functions
export const generateZKProof = async (
  agent: HttpAgent,
  token: string,
  principal: Principal
): Promise<ZKProofResponse>;

export const verifyZKProof = async (
  agent: HttpAgent,
  proofId: string,
  proofData?: string
): Promise<ProofVerificationResult>;
```

### AI Service

Located in `src/services/aiService.ts`, this service manages AI interaction:

```typescript
// Key functions
export const generateProofSummary = async (
  proofData: {
    proofId: string;
    token: string;
    timestamp: number;
  },
  config?: Partial<AIConfig>
): Promise<AISummaryResponse>;

export const getOpenAIKey = (): string;
export const saveOpenAIKey = (key: string): void;
export const clearOpenAIKey = (): void;
```

### Auth Service

Located in `src/services/authService.ts`, this service handles wallet connections:

```typescript
// Key functions
export const createAgent = async (identity: Identity): Promise<HttpAgent>;
export const createAuthClient = async (): Promise<AuthClient>;
export const login = async (authClient: AuthClient, onSuccess: () => void): Promise<void>;
export const logout = async (authClient: AuthClient): Promise<void>;
export const connectWithPlug = async (canisterIds: string[] = [], silentReconnect = false): Promise<{
  agent: HttpAgent;
  principal: Principal;
}>;
```

### Balance Service

Located in `src/services/balanceService.ts`, this service fetches token balances:

```typescript
// Key functions
export const fetchICPBalance = async (
  agent: HttpAgent,
  userPrincipal: Principal
): Promise<Token[]>;
```

## Key Components

### ZKProofGenerator

Located in `src/components/ZKProofGenerator`, this component handles the UI and logic for generating ZK proofs:

```typescript
interface ZKProofGeneratorProps {
  agent: HttpAgent | null;
  principal: string | null;
  tokens: Token[] | null;
}
```

The component uses the `useZKProofGeneration` hook to handle the generation logic.

### ZKProofVerifier

Located in `src/components/ZKProofVerifier`, this component handles proof verification:

```typescript
interface ZKProofVerifierProps {
  proofId?: string;
}
```

The component uses the `useZKProofVerification` hook for verification logic.

### ZKProofSummary

Located in `src/components/ZKProofSummary`, this component generates and displays AI summaries:

```typescript
interface ZKProofSummaryProps {
  proofResult: ZKProofResponse;
  principal?: string | null;
}
```

### ZKProofTest

Located in `src/components/ZKProofTest`, this component provides end-to-end testing:

```typescript
interface ZKProofTestRunnerProps {
  agent: HttpAgent | null;
  principal: string | null;
  tokens: Token[] | null;
}
```

## Integration Points

Ghost integrates with several external systems:

### Internet Computer Ledger

Integration with the ICP ledger canister for balance fetching:

```typescript
// src/utils/icpLedger.ts
export const LEDGER_CANISTER_ID = "ryjl3-tyaaa-aaaaa-aaaba-cai";
```

### ZK Proof Canister

Integration with the custom ZK proof canister:

```typescript
// src/services/zkProof/canisterDefinition.ts
export const ZK_PROOF_CANISTER_ID = "hi7bu-myaaa-aaaad-aaloa-cai";
```

### OpenAI API

Integration with OpenAI for AI-enhanced explanations:

```typescript
// src/services/aiService.ts
const response = await fetch("https://api.openai.com/v1/chat/completions", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify({
    model,
    messages: [
      {
        role: "system",
        content: "You are an AI assistant that explains Zero-Knowledge Proofs in plain language..."
      },
      {
        role: "user",
        content: prompt
      }
    ],
    temperature: 0.3,
    max_tokens: 300
  }),
});
```

## Testing Framework

Ghost includes a comprehensive testing framework for the ZK proof system:

```typescript
// src/utils/zkProofTesting.ts
export const runZKProofTest = async (
  agent: HttpAgent,
  principal: Principal,
  token: Token
): Promise<TestSuiteResults>;
```

The testing framework verifies:
1. Proof generation
2. Proof verification
3. Anonymous verification

Results are structured in a test suite format:

```typescript
export interface TestSuiteResults {
  allPassed: boolean;
  results: TestResult[];
  startTime: number;
  endTime: number;
  duration: number;
}
```

---

# 6. ZK Proof Canister

## Canister Overview

The ZK proof canister is a custom Internet Computer canister that handles the cryptographic operations for proof generation and verification. It is deployed on the IC mainnet with the canister ID: `hi7bu-myaaa-aaaad-aaloa-cai`.

The canister provides:
- Cryptographic proof generation for token ownership
- Verification of generated proofs
- Support for multiple token standards

## API Documentation

The canister exposes two primary methods:

### 1. prove_ownership

Generates a Zero-Knowledge Proof of token ownership.

**Input**:
- `token`: String identifier for the token
- `input`: TokenOwnershipInput structure containing:
  - `token_metadata`: Information about the token
  - `token_id`: For non-fungible tokens (empty for fungible)
  - `balance`: Byte representation of the balance amount
  - `owner_hash`: Hash of the owner's principal ID
  - `merkle_path`: For tokens with Merkle tree representations
  - `path_indices`: Indices for the Merkle path
  - `token_specific_data`: Optional additional data

**Output**:
- `Ok`: Uint8Array representing the proof
- `Err`: String error message

### 2. verify_proof

Verifies a previously generated proof.

**Input**:
- `proofData`: Uint8Array containing the proof data

**Output**:
- `Ok`: Boolean indicating if the proof is valid
- `Err`: String error message

## Canister Deployment

The ZK proof canister is already deployed on the Internet Computer mainnet. When developing locally, the frontend communicates with this production canister.

To view the canister in the Candid UI:
- Visit [https://a4gq6-oaaaa-aaaab-qaa4q-cai.raw.ic0.app/?id=hi7bu-myaaa-aaaad-aaloa-cai](https://a4gq6-oaaaa-aaaab-qaa4q-cai.raw.ic0.app/?id=hi7bu-myaaa-aaaad-aaloa-cai)

## Integration with Frontend

The frontend integrates with the canister using the Internet Computer JavaScript Agent:

```typescript
// src/services/zkProof/actorService.ts
export const createZKProofActor = async (
  agent: HttpAgent
): Promise<ActorSubclass<ZKProofCanister>> => {
  try {
    console.log("Creating ZK Proof actor");
    
    // Check if agent is anonymous in a safer way
    const isAnonymous = agent instanceof HttpAgent && !agent.getPrincipal;
    
    console.log(`Agent is anonymous: ${isAnonymous}`);
    
    // Create the actor with special options for anonymous verification
    const actorOptions = {
      agent,
      canisterId: ZK_PROOF_CANISTER_ID,
    };
    
    // For anonymous verification, we need to bypass authentication
    // Create actor with explicit configuration for query transforms
    const actor: ActorSubclass<ZKProofCanister> = Actor.createActor(
      zkProofCanisterIDL,
      {
        ...actorOptions,
        queryTransform: (args: any) => {
          return { ...args, certified: false };
        }
      }
    );
    
    console.log("ZK Proof actor created successfully");
    return actor;
  } catch (error) {
    console.error("Error creating ZK Proof actor:", error);
    throw error;
  }
};
```

Communication with the canister happens through this actor interface.

---

# 7. AI Components

## OpenAI Integration

Ghost integrates with OpenAI's API to provide AI-enhanced explanations of Zero-Knowledge Proofs. The integration is designed to:

1. Maintain user privacy (no sensitive data is sent to OpenAI)
2. Provide clear, accurate explanations of complex cryptographic concepts
3. Make ZK technology more accessible to non-technical users

The integration is implemented in `src/services/aiService.ts`.

### API Key Management

For privacy and security reasons, Ghost does not include any API keys. Instead, users must provide their own OpenAI API key to use the AI features:

```typescript
export const getOpenAIKey = (): string => {
  // Only use user-provided keys from localStorage
  const userProvidedKey = localStorage.getItem("openai_api_key");
  return userProvidedKey || "";
};

export const saveOpenAIKey = (key: string): void => {
  localStorage.setItem("openai_api_key", key);
};

export const clearOpenAIKey = (): void => {
  localStorage.removeItem("openai_api_key");
};
```

Keys are stored only in the browser's localStorage and are never sent to any server other than OpenAI's API endpoint.

## Prompt Engineering

The AI component uses carefully designed prompts to generate consistent, accurate explanations:

```typescript
const prompt = `
You are an assistant that explains Zero-Knowledge Proofs (ZKPs) in simple terms.

Here's information about a ZK proof that was generated:
- Token: ${proofData.token}
- Generation Time: ${new Date(proofData.timestamp).toLocaleString()}
- Proof ID: ${proofData.proofId}

This proof specifically verifies ownership of the ${proofData.token} token without revealing the actual balance. The proof uses cryptographic techniques to confirm the user holds this token without exposing sensitive wallet information.

Please provide:
1. A brief, one-sentence summary of what this proof verifies about the ${proofData.token} token ownership (for non-technical users)
2. A more detailed explanation (2-3 sentences) about what this ${proofData.token} ownership proof demonstrates, how zero-knowledge technology protects the user's privacy, and why this approach is valuable for verifying digital assets
`;
```

The prompt is designed to:
- Set clear expectations for the AI's role
- Provide only non-sensitive information about the proof
- Request specific types of explanations at different detail levels
- Focus on explaining the concept rather than technical details

## AI Summary Generation

The AI summary generation process:

1. Collects non-sensitive proof metadata (token type, timestamp, proof ID)
2. Constructs a prompt for the OpenAI API
3. Makes a request to the OpenAI Chat Completions API
4. Parses the response to extract the summary and detailed explanation
5. Returns the formatted response to the UI for display

The result provides users with:
- A brief, one-sentence explanation of what the proof shows
- A more detailed explanation of the significance and privacy benefits

Example implementation:

```typescript
export const generateProofSummary = async (
  proofData: {
    proofId: string;
    token: string;
    timestamp: number;
  },
  config?: Partial<AIConfig>
): Promise<AISummaryResponse> => {
  try {
    const { apiKey, model } = { ...defaultConfig, ...config };
    
    if (!apiKey) {
      return {
        summary: "API key required for AI summaries",
        detailed: "Please provide an OpenAI API key to generate summaries.",
        error: "No API key provided"
      };
    }

    // Create and send the prompt to OpenAI
    const response = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        model,
        messages: [
          {
            role: "system",
            content: "You are an AI assistant that explains Zero-Knowledge Proofs in plain language, with a focus on explaining token ownership verification."
          },
          {
            role: "user",
            content: prompt
          }
        ],
        temperature: 0.3,
        max_tokens: 300
      }),
    });

    // Process the response
    const result = await response.json();
    const content = result.choices[0]?.message?.content;
    
    // Parse and format the AI's response
    const sections = content.split(/\d+\.\s+/).filter(Boolean);
    
    let summary = `This proves you own the ${proofData.token} token without revealing your balance.`;
    let detailed = `The zero-knowledge proof cryptographically verifies your ownership of ${proofData.token} without sharing sensitive details like account balance or transaction history.`;
    
    if (sections.length >= 2) {
      summary = sections[0].trim();
      detailed = sections[1].trim();
    }

    return { summary, detailed };
  } catch (error) {
    // Error handling
    return {
      summary: "Unable to generate AI summary",
      detailed: "There was an error when trying to generate the summary.",
      error: error instanceof Error ? error.message : "Unknown error"
    };
  }
};
```

---

# 8. Security Considerations

## Privacy Guarantees

Ghost is designed with privacy as a central principle. The privacy guarantees include:

### Zero-Knowledge Proofs

- **No Balance Disclosure**: The ZK proof system allows users to prove token ownership without revealing their actual balance
- **Cryptographic Verification**: All proofs are verified cryptographically, ensuring mathematical certainty
- **Selective Disclosure**: Users control exactly what information is shared with verifiers

### Data Minimization

- Only the minimum necessary data is included in proofs
- Proofs contain no personally identifiable information
- Verification requires only the proof itself, not user account details

## Data Protection

Ghost implements several data protection measures:

### Client-Side Storage

- Proofs are stored in the client's browser localStorage
- No server-side storage of sensitive information
- Proofs have a built-in expiration period (7 days)

### API Key Protection

- OpenAI API keys are stored only in the browser's localStorage
- Keys are never sent to any server except OpenAI directly
- Users can clear their API keys at any time

### Secure Communication

- All blockchain interactions use secure HTTPS connections
- Wallet connections follow the Internet Computer's security standards
- AI API calls use secure HTTPS with API key authentication

## Client-Side Security

The application includes several client-side security measures:

### Input Validation

```typescript
// src/services/zkProof/proofValidator.ts
export const validateProofId = (proofId: string): { isValid: boolean; errorMessage?: string } => {
  // Trim whitespace
  const trimmedProofId = proofId.trim();
  
  // Check if empty
  if (!trimmedProofId) {
    return { 
      isValid: false, 
      errorMessage: "Proof ID cannot be empty" 
    };
  }
  
  // Check length
  if (trimmedProofId.length < 8 || trimmedProofId.length > 64) {
    return { 
      isValid: false, 
      errorMessage: "Proof ID must be between 8 and 64 characters" 
    };
  }

  // Check format
  if (!/^[a-zA-Z0-9]+$/.test(trimmedProofId)) {
    return { 
      isValid: false, 
      errorMessage: "Proof ID must contain only alphanumeric characters" 
    };
  }
  
  return { isValid: true };
};
```

### Input Sanitization

```typescript
export const sanitizeInput = (input: string): string => {
  if (!input) return '';
  
  // Replace potential HTML/script tags
  return input
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
};
```

### Rate Limiting

To prevent abuse, Ghost implements client-side rate limiting for verification attempts:

```typescript
// src/services/rateLimiter.ts
export const checkRateLimit = (
  operationKey: string, 
  options: RateLimitOptions = { maxRequests: 5, timeWindowMs: 60000 }
): { allowed: boolean; timeRemaining?: number } => {
  const now = Date.now();
  const tracker = rateLimitStore[operationKey];
  
  // If no tracker exists or the reset time has passed, create a new one
  if (!tracker || now > tracker.resetTime) {
    rateLimitStore[operationKey] = {
      count: 1,
      resetTime: now + options.timeWindowMs
    };
    return { allowed: true };
  }
  
  // Check if under the limit
  if (tracker.count < options.maxRequests) {
    tracker.count++;
    return { allowed: true };
  }
  
  // Rate limit exceeded
  const timeRemaining = tracker.resetTime - now;
  return { 
    allowed: false, 
    timeRemaining 
  };
};
```

### Error Handling

Comprehensive error handling prevents information leakage and provides users with clear error messages:

```typescript
// Error types for ZK proof verification
export enum ProofVerificationErrorType {
  PROOF_NOT_FOUND = "PROOF_NOT_FOUND",
  INVALID_PROOF_FORMAT = "INVALID_PROOF_FORMAT",
  EXPIRED_PROOF = "EXPIRED_PROOF",
  CANISTER_ERROR = "CANISTER_ERROR",
  UNKNOWN_ERROR = "UNKNOWN_ERROR"
}

// Error response for ZK proof verification
export interface ProofVerificationError {
  type: ProofVerificationErrorType;
  message: string;
  details?: string;
}
```

---

# 9. Future Roadmap

## Expanded Use Cases

Ghost's roadmap includes several planned expansions to its use cases:

### Multi-Token Support

Future versions will support a wider range of tokens:

- Additional fungible tokens (ICRC-1, ICRC-2)
- Non-fungible tokens (NFTs) with specialized proof generation
- Custom tokens on the Internet Computer

### Enhanced Proof Types

Beyond simple token ownership, Ghost will add support for:

- **Threshold Proofs**: Prove ownership of at least X tokens without revealing the exact amount
- **Range Proofs**: Prove a balance falls within a specific range
- **Time-Locked Proofs**: Proofs that expire or become valid at specific times
- **Conditional Proofs**: Proofs that depend on external conditions

### Credential Verification

A key expansion area is using ZK proofs for credential verification:

- Academic credential verification
- Age verification without revealing birth date
- Membership verification for DAO access
- Identity verification preserving anonymity

## Enhanced AI Features

The AI component will be expanded to provide more sophisticated capabilities:

### Interactive Explainers

- Conversational interfaces to explain ZK concepts
- Visual explainers that illustrate how proofs work
- Step-by-step guides for specific ZK applications

### Proof Recommendation Engine

- AI-driven suggestion of appropriate proof types
- Context-aware recommendations based on user needs
- Integration with common verification scenarios

### Multi-Modal Explanations

- Visual representations of complex ZK concepts
- Audio explanations for accessibility
- Interactive demonstrations of key principles

## Additional Token Support

Ghost's token support roadmap includes:

### Internet Computer Ecosystem

- Full support for all ICRC token standards
- Integration with Internet Computer NFT standards
- Support for specialized IC tokens

### Cross-Chain Integration

- Support for Ethereum tokens through bridge technologies
- Integration with other blockchain ecosystems
- Multi-chain proof verification

### Custom Token Registration

- Developer API for registering custom tokens
- Self-service token integration
- Extensible token metadata system

---

# 10. API Reference

## ZK Proof API

### Types

```typescript
// Token standard types
export type TokenStandard = {
  'ERC20': null;
} | {
  'ERC721': null;
} | {
  'ERC1155': null;
} | {
  'ICRC1': null;
} | {
  'ICRC2': null;
} | {
  'ICP': null;
};

// Token metadata structure
export type TokenMetadata = {
  canister_id: string;
  token_standard: TokenStandard;
  decimals: [] | [number];
};

// Input structure for token ownership proofs
export type TokenOwnershipInput = {
  token_metadata: TokenMetadata;
  token_id: Uint8Array;
  balance: Uint8Array;
  owner_hash: Uint8Array;
  merkle_path: Uint8Array[];
  path_indices: Uint8Array;
  token_specific_data: [] | [Uint8Array];
};

// Result type for canister calls
export type Result = {
  'Ok': boolean;
} | {
  'Err': string;
};

// Response format for frontend
export interface ZKProofResponse {
  proofId: string;
  proofLink: string;
  token: string;
  name?: string;
  description?: string;
  timestamp: number;
}

// Error response for ZK proof verification
export interface ProofVerificationError {
  type: ProofVerificationErrorType;
  message: string;
  details?: string;
}

// Result of a proof verification
export interface ProofVerificationResult {
  isValid: boolean;
  error?: ProofVerificationError;
}
```

### Methods

#### Generate ZK Proof

```typescript
/**
 * Generates a ZK proof for a token
 */
export const generateZKProof = async (
  agent: HttpAgent,
  token: string,
  principal: Principal
): Promise<ZKProofResponse>;
```

#### Verify ZK Proof

```typescript
/**
 * Verifies a ZK proof
 */
export const verifyZKProof = async (
  agent: HttpAgent,
  proofId: string,
  proofData?: string
): Promise<ProofVerificationResult>;
```

## AI Enhancement API

### Types

```typescript
// Interface for AI service responses
export interface AISummaryResponse {
  summary: string;
  detailed: string;
  error?: string;
}

// Configuration for AI requests
export interface AIConfig {
  apiKey: string;
  model: string;
}
```

### Methods

#### Generate Proof Summary

```typescript
/**
 * Generate a natural language summary of a ZK proof
 * @param proofData Information about the proof to summarize
 * @param config OpenAI API configuration
 */
export const generateProofSummary = async (
  proofData: {
    proofId: string;
    token: string;
    timestamp: number;
  },
  config?: Partial<AIConfig>
): Promise<AISummaryResponse>;
```

#### API Key Management

```typescript
/**
 * Get the API key from user-provided storage only
 */
export const getOpenAIKey = (): string;

/**
 * Save a user-provided API key
 */
export const saveOpenAIKey = (key: string): void;

/**
 * Clear a saved API key
 */
export const clearOpenAIKey = (): void;
```

## Wallet Integration API

### Internet Identity

```typescript
/**
 * Creates an auth client for Internet Computer authentication
 */
export const createAuthClient = async (): Promise<AuthClient>;

/**
 * Initiates the login flow with Internet Computer identity service
 */
export const login = async (
  authClient: AuthClient, 
  onSuccess: () => void
): Promise<void>;

/**
 * Logs out the current user
 */
export const logout = async (authClient: AuthClient): Promise<void>;
```

### Plug Wallet

```typescript
/**
 * Connect using Plug wallet
 */
export const connectWithPlug = async (
  canisterIds: string[] = [], 
  silentReconnect = false
): Promise<{
  agent: HttpAgent;
  principal: Principal;
}>;

/**
 * Disconnect from Plug wallet
 */
export const disconnectFromPlug = async (): Promise<void>;
```

---

# 11. Troubleshooting

## Common Issues

### Wallet Connection Problems

#### Internet Identity Connection Fails

**Symptoms**: 
- Unable to connect using Internet Identity
- Connection process starts but returns to the application without authentication
- Error message about authentication failure

**Solutions**:
1. Ensure your Internet Identity is properly set up
2. Clear browser cookies and try again
3. Try using a different authentication method (security key, passphrase)
4. Check if you're using a supported browser (Chrome, Firefox, Safari)

#### Plug Wallet Not Detected

**Symptoms**:
- "Plug wallet extension is not installed" message
- Plug connect button is disabled

**Solutions**:
1. Install the Plug wallet extension from [plugwallet.ooo](https://plugwallet.ooo/)
2. If already installed, refresh the page
3. Check if the extension is enabled in your browser
4. Try restarting your browser

### Proof Generation Issues

#### Generation Fails with Error

**Symptoms**:
- Error message when trying to generate a proof
- Process starts but doesn't complete

**Solutions**:
1. Check your internet connection
2. Verify your wallet is still connected
3. Try selecting a different token
4. Refresh the page and try again

#### Created Proof is Not Appearing

**Symptoms**:
- Proof generation completes but no proof appears
- No confirmation dialog

**Solutions**:
1. Check browser console for errors
2. Verify localStorage is enabled in your browser
3. Try generating the proof again
4. Clear browser cache and reload the application

### Verification Problems

#### Proof Not Found

**Symptoms**:
- "Proof not found" error when trying to verify
- Shareable link doesn't work

**Solutions**:
1. Check if the proof ID is correct
2. Ensure the proof hasn't expired (proofs expire after 7 days)
3. Try using the full verification link instead of just the ID
4. Ask the proof creator to generate a new proof

#### Invalid Proof Format

**Symptoms**:
- "Invalid proof format" error during verification
- Verification process starts but fails

**Solutions**:
1. Ensure you're using the complete proof link
2. Check for any characters that might have been lost when copying the link
3. Try asking the proof creator to send the link again
4. Use the verification form directly rather than a link

### AI Features Not Working

#### API Key Issues

**Symptoms**:
- "API key required" message
- AI summaries don't appear

**Solutions**:
1. Check if you've added your OpenAI API key in the settings
2. Verify the API key is valid and has the correct permissions
3. Save the API key again
4. Check for any leading/trailing spaces in the API key

#### Summary Generation Fails

**Symptoms**:
- "Unable to generate AI summary" error
- Summary section shows error message

**Solutions**:
1. Check your OpenAI API key billing status
2. Verify your internet connection
3. Try refreshing the page
4. Check if the API key has the correct permissions

## Error Messages

### "Failed to connect to Plug wallet"

This error indicates a problem with the Plug wallet connection process.

**Possible causes**:
- Plug extension not installed correctly
- Plug extension needs to be updated
- Browser permissions issue

**Resolution**:
1. Reinstall the Plug wallet extension
2. Update to the latest version of Plug
3. Check browser permissions for the extension

### "Verification failed: Proof not found"

This error indicates the system couldn't find the proof data for verification.

**Possible causes**:
- Incorrect proof ID
- Proof has expired
- Proof was generated on a different device
- localStorage was cleared

**Resolution**:
1. Verify the proof ID is correct
2. Request a new proof if the original has expired
3. Use the complete verification link that includes the proof data
4. Generate a new proof

### "API error: 429"

This error indicates you've exceeded OpenAI's rate limits.

**Possible causes**:
- Too many API requests in a short time
- API key usage limits exceeded
- Account billing issue

**Resolution**:
1. Wait a few minutes and try again
2. Check your OpenAI account usage limits
3. Verify your billing status is active
4. Consider upgrading your OpenAI account tier

## Support Resources

If you encounter issues not covered by this troubleshooting guide, you can seek help through these channels:

- **GitHub Issues**: File an issue on the [Ghost GitHub repository](https://github.com/gabrielrondon/ghost_dev/issues)
- **Documentation**: Reference this documentation for detailed information
- **Community Forums**: Seek help from the Internet Computer developer community

---

# 12. Contributing

## Development Workflow

Ghost follows a standard GitHub-based development workflow:

1. **Fork the Repository**: Create your own fork of the [Ghost repository](https://github.com/gabrielrondon/ghost_dev)
2. **Create Feature Branch**: Create a branch for your feature or fix
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Develop and Test**: Make your changes and test thoroughly
4. **Commit Changes**: Commit with a clear message
   ```bash
   git commit -m "Add feature: your feature description"
   ```
5. **Push to Your Fork**: Push your branch to your fork
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create Pull Request**: Open a pull request to the main repository

## Code Standards

When contributing to Ghost, please follow these code standards:

### TypeScript

- Use TypeScript for all new code
- Include proper type definitions
- Avoid using `any` types where possible
- Add JSDoc comments for public functions

Example:

```typescript
/**
 * Validates a proof ID format
 * @param proofId The proof ID to validate
 * @returns Object containing validation result and any error message
 */
export const validateProofId = (proofId: string): ValidationResult => {
  // Implementation
};
```

### React Components

- Use functional components with hooks
- Keep components small and focused
- Use proper prop types
- Follow the existing component structure

Example:

```typescript
interface MyComponentProps {
  data: SomeType;
  onAction: (id: string) => void;
}

const MyComponent: React.FC<MyComponentProps> = ({ data, onAction }) => {
  // Implementation
};
```

### Styling

- Use the Tailwind CSS classes following the existing patterns
- Maintain a consistent look and feel
- Follow the theme system conventions

## Pull Request Process

When submitting a pull request:

1. **Provide a Clear Description**: Explain what your changes do and why they're needed
2. **Reference Issues**: Link to any related issues
3. **Include Screenshots**: For UI changes, include before/after screenshots
4. **Update Documentation**: Update relevant documentation to match your changes
5. **Review CI Results**: Ensure all CI checks pass
6. **Address Feedback**: Be responsive to review comments

---

# 13. Glossary

## Zero-Knowledge Terminology

### Zero-Knowledge Proof (ZK Proof)

A cryptographic method where one party (the prover) can prove to another (the verifier) that they know a value, without revealing the actual value.

### Prover

The party generating a Zero-Knowledge Proof to demonstrate knowledge of some information.

### Verifier

The party checking a Zero-Knowledge Proof to confirm the prover's knowledge without learning the actual information.

### ZK-SNARK

Zero-Knowledge Succinct Non-Interactive Argument of Knowledge - a type of cryptographic proof that is small in size and quick to verify.

### Commitment

A cryptographic way to commit to a value without revealing it, with the ability to unveil it later.

## Internet Computer Terms

### Internet Computer Protocol (ICP)

The native utility token of the Internet Computer blockchain.

### Canister

A smart contract on the Internet Computer that contains both code and state.

### Principal ID

A unique identifier for users and canisters on the Internet Computer.

### Internet Identity

Authentication system for the Internet Computer that enables secure, anonymous authentication.

### Cycles

The computational resources used to power smart contracts (canisters) on the Internet Computer.

## Project-Specific Terms

### Ghost

The project name for the Zero-Knowledge Notary Agent system.

### ZK Notary Agent

The role the Ghost system plays in facilitating and verifying Zero-Knowledge Proofs.

### Proof ID

A unique identifier for a generated Zero-Knowledge Proof in the Ghost system.

### Shareable Link

A URL containing or referencing a Zero-Knowledge Proof that can be shared with others for verification.

### AI-Enhanced Explanation

A plain-language explanation of a Zero-Knowledge Proof generated using AI to make the concept more accessible.

---

# Appendix A: Implementation Details

## Token Representation

Ghost handles ICP tokens as follows:

```typescript
// Token representation
export interface Token {
  name: string;
  symbol: string;
  amount: string;
  decimals: number;
  logo?: string;
}

// Convert e8s (ICP's smallest unit) to ICP with proper decimal places
export const formatE8sToICP = (e8s: bigint): string => {
  const icp = Number(e8s) / 100000000;
  return icp.toFixed(8);
};
```

## Proof Storage

Proofs are stored in the browser's localStorage:

```typescript
// Store proof data
localStorage.setItem(`proof_${proofId}`, proofBase64);

// Store metadata
localStorage.setItem(`metadata_${proofId}`, JSON.stringify(response));

// Retrieve proof data
const proofBase64 = localStorage.getItem(`proof_${proofId}`);

// Retrieve metadata
const metadata = JSON.parse(localStorage.getItem(`metadata_${proofId}`));
```

## Wallet Session Management

Wallet sessions are managed to enable reconnections:

```typescript
// Store session data
export const storeSession = (principal: string, provider: string) => {
  localStorage.setItem(STORAGE_KEY_PRINCIPAL, principal);
  localStorage.setItem(STORAGE_KEY_AUTH_PROVIDER, provider);
};

// Get stored session data
export const getStoredSession = () => {
  const principal = localStorage.getItem(STORAGE_KEY_PRINCIPAL);
  const provider = localStorage.getItem(STORAGE_KEY_AUTH_PROVIDER);
  
  return { principal, provider };
};
```

# Appendix B: Zero-Knowledge Proofs - Technical Deep Dive

## Cryptographic Foundations

Zero-Knowledge Proofs (ZKPs) rely on several cryptographic primitives and techniques:

### Commitment Schemes

A commitment scheme allows a prover to commit to a chosen value while keeping it hidden, with the ability to reveal it later. Ghost uses cryptographic commitments to secure token balance information:

```typescript
// Creating a commitment to the token balance
const balanceBytes = new Uint8Array(8);
const balanceBigInt = BigInt(Math.floor(Number(balance) * 100000000)); // Convert to e8s
  
// Convert BigInt to byte array (little-endian)
for (let i = 0; i < 8; i++) {
  balanceBytes[i] = Number((balanceBigInt >> BigInt(i * 8)) & BigInt(0xff));
}
```

### Interactive vs. Non-Interactive Proofs

Ghost uses non-interactive zero-knowledge proofs, which don't require back-and-forth communication between prover and verifier. This is essential for online verification where the prover and verifier may not be online simultaneously.

### Soundness and Completeness

A good zero-knowledge proof system has two key properties:
- **Soundness**: If the statement is false, no cheating prover can convince the verifier that it's true
- **Completeness**: If the statement is true, an honest prover can convince the verifier that it's true

The ZK proof canister implements both properties in its cryptographic protocol.

## Zero-Knowledge Proof Generation

The proof generation process in Ghost involves several steps:

1. **Token Ownership Preparation**:
   ```typescript
   const tokenInput = await createTokenOwnershipInput(token, principal, agent);
   ```

2. **Cryptographic Proof Creation**:
   ```typescript
   const result = await zkProofActor.prove_ownership(token, tokenInput);
   ```

3. **Proof Encoding and Storage**:
   ```typescript
   const proofBytes = result.Ok;
   const proofBase64 = btoa(String.fromCharCode.apply(null, [...proofBytes]));
   localStorage.setItem(`proof_${proofId}`, proofBase64);
   ```

## Zero-Knowledge Proof Verification

The verification process is the counterpart to generation:

1. **Proof Retrieval and Decoding**:
   ```typescript
   let proofBase64 = proofData || localStorage.getItem(`proof_${proofId}`);
   const proofString = atob(proofBase64);
   proofBytes = new Uint8Array(proofString.length);
   for (let i = 0; i < proofString.length; i++) {
     proofBytes[i] = proofString.charCodeAt(i);
   }
   ```

2. **Cryptographic Verification**:
   ```typescript
   const result = await zkProofActor.verify_proof(proofBytes);
   ```

3. **Result Interpretation**:
   ```typescript
   const isValid = result.Ok;
   return { isValid };
   ```

## Properties of Ghost's ZK System

The Zero-Knowledge proof system implemented in Ghost has several important properties:

### Zero-Knowledge

The verifier learns nothing about the prover's token balance beyond what's specifically being proven (ownership).

### Succinctness

Proofs are relatively small (compared to the original data) and quick to verify, making them practical for web applications.

### Non-Interactivity

Proofs can be generated once and verified many times without requiring further interaction with the prover.

### Universality

The system is designed to be extended to various token types and proof statements beyond simple ownership.

# Appendix C: AI Enhancement - Technical Details

## Model Selection

Ghost uses OpenAI's models for generating explanations:

```typescript
const defaultConfig: AIConfig = {
  apiKey: "", // Will be filled from user input
  model: "gpt-4o-mini" // Default to a cheaper, faster model
};
```

The model selection balances several factors:
- Cost efficiency for users
- Response quality for explanations
- Response speed for good user experience

## Prompt Design Principles

The prompts for AI explanations follow these design principles:

1. **Privacy-First**: No sensitive information is included
2. **Clear Instruction**: Specific output format and requirements
3. **Context-Rich**: Enough context about ZK proofs to generate quality responses
4. **Consistent Structure**: Predictable output format for easier parsing

## Response Parsing Strategy

AI responses are parsed to extract structured information:

```typescript
// Parse the AI response - normally it will have numbered responses
const sections = content.split(/\d+\.\s+/).filter(Boolean);

// Default fallbacks in case parsing doesn't work as expected
let summary = `This proves you own the ${proofData.token} token without revealing your balance.`;
let detailed = `The zero-knowledge proof cryptographically verifies your ownership of ${proofData.token} without sharing sensitive details like account balance or transaction history.`;

if (sections.length >= 2) {
  summary = sections[0].trim();
  detailed = sections[1].trim();
} else if (sections.length === 1) {
  // If we only got one section, use it as the summary and use a default detailed message
  summary = sections[0].trim();
} else if (content) {
  // If the numbering parsing failed, just use the whole content
  summary = content.split('.')[0] + '.';
  detailed = content.substring(summary.length).trim();
}
```

This approach ensures robustness even when AI responses don't follow the expected format exactly.

## Usage Tracking and Analysis

Ghost implements a simple usage tracking system to help users monitor their API usage:

```typescript
export const trackAPIUsage = (userId: string): number => {
  const usageKey = `openai_usage_${userId || "anonymous"}`;
  const currentUsage = parseInt(localStorage.getItem(usageKey) || "0", 10);
  const newUsage = currentUsage + 1;
  localStorage.setItem(usageKey, newUsage.toString());
  return newUsage;
};
```

This tracking is entirely client-side and private to the user.

# Appendix D: Internet Computer Integration

## Internet Computer Agent

Ghost interacts with the Internet Computer blockchain using the agent pattern:

```typescript
export const createAgent = async (identity: Identity): Promise<HttpAgent> => {
  // Create an agent using the identity
  const agent = new HttpAgent({ 
    identity, 
    host: IC_HOST // Always use mainnet
  });
  
  // Only fetch the root key in development
  if (!isProduction) {
    try {
      await agent.fetchRootKey();
      console.log("Agent root key fetched");
    } catch (error) {
      console.warn("Could not fetch root key, calls will fail in development:", error);
    }
  } else {
    console.log("Running in production, skipping root key fetch");
  }
  
  return agent;
};
```

## Canister Interaction

Communication with Internet Computer canisters happens through the Actor interface:

```typescript
// Create an actor to interact with the ZK Proof canister
export const createZKProofActor = async (
  agent: HttpAgent
): Promise<ActorSubclass<ZKProofCanister>> => {
  // Create the actor with special options for anonymous verification
  const actorOptions = {
    agent,
    canisterId: ZK_PROOF_CANISTER_ID,
  };
  
  // For anonymous verification, we need to bypass authentication
  const actor: ActorSubclass<ZKProofCanister> = Actor.createActor(
    zkProofCanisterIDL,
    {
      ...actorOptions,
      queryTransform: (args: any) => {
        return { ...args, certified: false };
      }
    }
  );
  
  return actor;
};
```

## Account Identification

Internet Computer accounts are identified using a specific transformation of principal IDs:

```typescript
export const principalToAccountIdentifier = (principal: Principal, subAccount?: Uint8Array): Uint8Array => {
  // Ensure the principal is included in the account identifier
  const principalBytes = principal.toUint8Array();
  
  // Prepare message components
  const prefix = new Uint8Array([10]); // Prefix for account IDs
  const label = new TextEncoder().encode("account-id");
  const defaultSubAccount = new Uint8Array(32).fill(0);
  const subAccountToUse = subAccount || defaultSubAccount;
  
  // Concatenate all parts for hashing
  const messageLength = prefix.length + label.length + principalBytes.length + subAccountToUse.length;
  const message = new Uint8Array(messageLength);
  
  let offset = 0;
  message.set(prefix, offset);
  offset += prefix.length;
  message.set(label, offset);
  offset += label.length;
  message.set(principalBytes, offset);
  offset += principalBytes.length;
  message.set(subAccountToUse, offset);
  
  // Generate hash using sha224
  const hash = sha224(message);
  const checksum = getCrc32(hash);
  
  // Combine checksum and hash to create account ID
  const checksumArray = new Uint8Array(4);
  checksumArray[0] = checksum >> 24 & 0xFF;
  checksumArray[1] = checksum >> 16 & 0xFF;
  checksumArray[2] = checksum >> 8 & 0xFF;
  checksumArray[3] = checksum & 0xFF;
  
  // Create the final account identifier
  const accountId = new Uint8Array(checksumArray.length + hash.length);
  accountId.set(checksumArray, 0);
  accountId.set(hash, checksumArray.length);
  
  return accountId;
};
```
```

# Appendix I: Installation and Deployment Guide

## Local Development Environment

Setting up a complete local development environment for Ghost:

### Prerequisites

Ensure you have the following installed:
- Node.js (v16.0.0 or higher)
- npm (v8.0.0 or higher)
- Git

### Step-by-Step Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gabrielrondon/ghost_dev.git
   cd ghost_dev
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm run dev
   ```

4. **Access the application**:
   Open your browser and navigate to `http://localhost:8080`

### Development Modes

Ghost supports different development modes:

- **Standard Development**: `npm run dev`
- **Production Build**: `npm run build`
- **Development Build**: `npm run build:dev`
- **Preview Production Build**: `npm run preview`

## Production Deployment

Deploying Ghost to a production environment:

### Building for Production

Generate a production-ready build:
```bash
npm run build
```

This creates optimized files in the `dist` directory.

### Deployment Options

Ghost can be deployed to various hosting platforms:

#### Static Hosting (Recommended)

Deploy to any static hosting service:
- Netlify
- Vercel
- GitHub Pages
- AWS S3 + CloudFront
- Internet Computer Web Hosting

Steps for deployment to Netlify:
1. Connect your GitHub repository
2. Set build command: `npm run build`
3. Set publish directory: `dist`
4. Deploy

#### Self-Hosted Deployment

To deploy on your own server:
1. Build the application: `npm run build`
2. Copy the contents of the `dist` directory to your web server
3. Configure your web server to serve the application
4. Set up proper HTTPS certificates for security

### Environment Configuration

Ghost requires minimal environment configuration:

- No API keys are needed in the deployment environment
- HTTPS is strongly recommended for security
- CORS configuration should allow access to Internet Computer APIs

## Canister Integration

Connecting to the ZK Proof canister:

### Canister Configuration

The application is pre-configured to connect to the production ZK Proof canister. The canister ID is defined in:
```typescript
// src/services/zkProof/canisterDefinition.ts
export const ZK_PROOF_CANISTER_ID = "hi7bu-myaaa-aaaad-aaloa-cai";
```

### Custom Canister Deployment

For advanced users who want to deploy their own canister:

1. Deploy your ZK Proof canister to the Internet Computer
2. Update the `ZK_PROOF_CANISTER_ID` constant with your canister ID
3. Rebuild and deploy the application

### Testing Canister Connectivity

Verify canister connectivity:
1. Open the application
2. Navigate to the "Test" page
3. Connect your wallet
4. Run the end-to-end tests
5. Verify that all tests pass, especially the "Verify ZK Proof" test

# Appendix J: Performance Optimization

## Client-Side Performance

Ghost implements several client-side performance optimizations:

### Code Splitting

The application uses dynamic imports for code splitting:

```typescript
// Lazy load the VerificationResult component
const VerificationResult = lazy(() => import("./VerificationResult"));

// Lazy load the ZKProofSummary component
const ZKProofSummary = lazy(() => import("@/components/ZKProofSummary"));
```

This reduces the initial bundle size and improves load times.

### Memory Management

Careful memory management is implemented:

- Local storage is used efficiently with cleanup mechanisms
- Large objects like proofs are properly disposed when no longer needed
- Careful handling of binary data to prevent memory leaks

### Rendering Optimization

React rendering optimization techniques:

- Components are properly memoized to prevent unnecessary re-renders
- State is localized to the components that need it
- Effects have proper dependency arrays to prevent unnecessary re-execution

## Blockchain Interaction Optimization

Optimizing interactions with the Internet Computer:

### Caching

Ghost implements caching strategies for blockchain data:

- Canister health checks are cached to reduce repeated queries
- Token balances are cached and only refreshed when necessary
- API responses are cached with appropriate expiration policies

```typescript
// Cache for health check results
let healthCache: CanisterHealth | null = null;
const CACHE_TTL = 60000; // 1 minute in milliseconds

export const checkCanisterHealth = async (agent: HttpAgent): Promise<CanisterHealth> => {
  const now = Date.now();
  
  // Return cached result if valid
  if (healthCache && now - healthCache.lastChecked < CACHE_TTL) {
    return healthCache;
  }
  
  // Perform health check and update cache
  // ...
}
```

### Query Optimization

Optimization of blockchain queries:

- Queries are batched where possible
- Only necessary data is requested
- Query parameters are optimized for minimum data transfer

### Error Handling and Retries

Robust error handling for blockchain interactions:

- Automatic retries for transient errors
- Fallback mechanisms for network issues
- Graceful degradation when services are unavailable

## User Experience Improvements

Performance optimizations for better user experience:

### Perceived Performance

Techniques to improve perceived performance:

- Loading states for all asynchronous operations
- Progressive disclosure of complex interfaces
- Immediate feedback for user actions

### Responsive Design

Responsive design principles for all device sizes:

- Mobile-first design approach
- Adaptive layouts for different screen sizes
- Touch-friendly interfaces for mobile users

# Appendix K: Quality Assurance

## Testing Strategy

Ghost employs a comprehensive testing strategy:

### Unit Testing

Unit tests for core functions:

- Proof validation functions
- Sanitization utilities
- Data transformations
- State management logic

### Integration Testing

Integration tests for component interactions:

- Wallet connection flow
- Proof generation and verification
- API integration with OpenAI

### End-to-End Testing

Built-in end-to-end testing for the ZK proof system:

```typescript
export const runZKProofTest = async (
  agent: HttpAgent,
  principal: Principal,
  token: Token
): Promise<TestSuiteResults> => {
  const results: TestResult[] = [];
  const startTime = Date.now();
  let allPassed = true;
  
  // Test 1: Generate ZK Proof
  try {
    console.log(`Test 1: Generating ZK proof for token ${token.symbol}`);
    const proofResponse = await generateZKProof(agent, token.symbol, principal);
    
    results.push({
      name: "Generate ZK Proof",
      success: true,
      message: `Successfully generated proof with ID: ${proofResponse.proofId}`,
      timestamp: Date.now()
    });
    
    // Test 2: Verify the generated ZK Proof
    // ...
    
    // Test 3: Verify with anonymous agent
    // ...
    
  } catch (error) {
    allPassed = false;
    // Handle error...
  }
  
  const endTime = Date.now();
  
  return {
    allPassed,
    results,
    startTime,
    endTime,
    duration: endTime - startTime
  };
};
```

### User Testing

Guidelines for user testing:

- Recruit diverse users with varying technical backgrounds
- Provide specific test scenarios and tasks
- Collect both quantitative and qualitative feedback
- Iterate based on user testing results

## Bug Reporting

Process for reporting and tracking bugs:

### Bug Report Template

When filing a bug report, include:

1. **Description**: Clear description of the issue
2. **Steps to Reproduce**: Detailed steps to reproduce the bug
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**: Browser, device, operating system
6. **Screenshots/Videos**: Visual evidence if applicable
7. **Console Logs**: Any relevant error messages from the console

### Issue Prioritization

Bugs are prioritized based on:

- **Critical**: Application unusable, security vulnerabilities
- **High**: Major functionality impacted, no workaround
- **Medium**: Important functionality impacted, workaround available
- **Low**: Minor issues, minimal impact on user experience

### Regression Testing

After bug fixes:

- Test the specific bug is fixed
- Test related functionality for potential side effects
- Run the full test suite to ensure no new issues

## Security Testing

Security testing protocols:

### Static Analysis

Static code analysis to identify security issues:

- Code scanning for security vulnerabilities
- Dependency analysis for known issues
- Security anti-patterns detection

### Penetration Testing

Guidelines for penetration testing:

- Test input validation and sanitization
- Attempt authentication bypasses
- Test rate limiting mechanisms
- Attempt code injection attacks

### Privacy Audits

Regular privacy audits:

- Verify no sensitive data is leaked
- Confirm all proof data remains private
- Ensure AI prompts contain no sensitive information
- Check all storage mechanisms for security

# Appendix L: Contribution Guide

## Getting Started with Contributions

How to start contributing to Ghost:

### Finding Issues to Work On

Ways to find issues to contribute to:

- Check the GitHub Issues tab for open issues
- Look for issues labeled "good first issue" for beginners
- Read the project roadmap for future development areas
- Propose new features or improvements

### Setting Up for Development

Steps to set up for development:

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment
4. Create a new branch for your feature or fix
5. Make your changes
6. Run tests to ensure everything works
7. Push your changes to your fork
8. Create a pull request

## Coding Guidelines

Standards for code contributions:

### Code Style

General code style guidelines:

- Use consistent indentation (2 spaces)
- Follow naming conventions:
  - CamelCase for React components and types
  - camelCase for variables and functions
  - UPPER_CASE for constants
- Keep functions small and focused
- Write self-documenting code with clear variable names

### TypeScript Best Practices

TypeScript-specific guidelines:

- Use strong typing, avoid `any` where possible
- Create interfaces for component props
- Use union types for state that can have multiple values
- Leverage TypeScript's type system for error prevention

```typescript
// Good example
interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
  variant?: 'primary' | 'secondary' | 'danger';
}

// Avoid
interface BadButtonProps {
  [key: string]: any; // Avoid using any
}
```

### React Component Guidelines

Best practices for React components:

- Use functional components with hooks
- Keep components small and composable
- Extract logic to custom hooks when appropriate
- Use proper prop types and default values

```typescript
// Good example
const Button: React.FC<ButtonProps> = ({ 
  label, 
  onClick, 
  disabled = false, 
  variant = 'primary' 
}) => {
  // Component implementation
};

// Avoid
const BadButton = (props) => {
  // Using untyped props is discouraged
};
```

## Pull Request Process

Guidelines for submitting pull requests:

### PR Checklist

Before submitting a PR, ensure:

- [ ] Code follows the project's style guidelines
- [ ] All tests pass
- [ ] New code is covered by tests
- [ ] Documentation is updated to reflect changes
- [ ] The PR addresses only one concern (feature or bug)
- [ ] The PR includes a descriptive title and detailed description

### Review Process

What to expect during code review:

1. Automated checks will run on your PR
2. Maintainers will review your code
3. Feedback may be provided requesting changes
4. Address feedback and push updates to your branch
5. Once approved, your PR will be merged

### After Merging

After your PR is merged:

- Delete your feature branch
- Update your local repository
- Look for a new issue to work on

# Appendix M: License and Legal Information

## License

Ghost is released under the MIT License:

```
MIT License

Copyright (c) 2024 Ghost

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Third-Party Licenses

Ghost uses several third-party libraries, each with its own license:

### Key Dependencies

- **React**: MIT License
- **Tailwind CSS**: MIT License
- **shadcn/ui**: MIT License
- **Internet Computer SDK**: Apache License 2.0
- **OpenAI API**: Proprietary (API usage subject to OpenAI's terms)

For a complete list of dependencies and their licenses, see the `package.json` file or run:
```bash
npm list --depth=0
```

## Legal Considerations

Important legal aspects of using Ghost:

### Privacy Considerations

Ghost is designed with privacy as a central principle:

- No user data is collected by the application itself
- All sensitive data remains client-side
- Third-party services (OpenAI, Internet Computer) are subject to their own privacy policies
- Users should review the privacy policies of connected services

### Liability Disclaimer

As stated in the MIT License, Ghost is provided "as is" without warranty:

- The developers are not liable for any damages or losses
- Users should perform their own security assessments
- The application is not guaranteed to be suitable for any particular purpose

### Export Compliance

Cryptographic software may be subject to export regulations:

- Users are responsible for compliance with local laws
- Some jurisdictions may restrict the use of zero-knowledge cryptography
- The application is not officially audited for compliance with specific regulations

# Appendix N: Frequently Asked Questions

## General Questions

### What is Ghost?

Ghost (The ZK Notary Agent) is a privacy-focused application that enables users to create and verify Zero-Knowledge Proofs (ZKPs) on the Internet Computer blockchain. It serves as a bridge between complex cryptographic technology and everyday use cases.

### Why use Zero-Knowledge Proofs?

Zero-Knowledge Proofs allow you to prove certain information without revealing the underlying data. This is valuable for privacy preservation, selective disclosure, and reducing trust requirements in digital interactions.

### What tokens does Ghost support?

Currently, Ghost supports the Internet Computer Protocol (ICP) token. Future versions will expand to support additional tokens on the Internet Computer and potentially other blockchains.

## Technical Questions

### How secure are the ZK proofs?

The ZK proofs generated by Ghost use cryptographic techniques that provide mathematical guarantees of security. The proofs cannot be forged without knowing the original information, and they reveal nothing about the underlying data beyond what is explicitly being proven.

### Where is my data stored?

Ghost keeps all sensitive data client-side:
- Proofs are stored in your browser's localStorage
- OpenAI API keys are stored in localStorage
- No sensitive data is sent to any server except as required for proof verification

### How long do proofs remain valid?

Proofs generated by Ghost remain valid for 7 days after creation. After this period, they will expire and show as invalid during verification. This time limit helps maintain security and ensures proofs remain relevant.

### Ghost: The ZK Notary Agent

## Comprehensive Documentation

---

# Table of Contents

1. [Introduction](#1-introduction)
   - [What is Ghost?](#what-is-ghost)
   - [Key Features](#key-features)
   - [Project Vision](#project-vision)

2. [Technical Architecture](#2-technical-architecture)
   - [System Overview](#system-overview)
   - [Component Breakdown](#component-breakdown)
   - [Zero-Knowledge Proof System](#zero-knowledge-proof-system)
   - [AI Enhancement Layer](#ai-enhancement-layer)

3. [Getting Started](#3-getting-started)
   - [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Development Environment Setup](#development-environment-setup)
   - [Configuration](#configuration)

4. [User Guide](#4-user-guide)
   - [Connecting Your Wallet](#connecting-your-wallet)
   - [Generating ZK Proofs](#generating-zk-proofs)
   - [Verifying ZK Proofs](#verifying-zk-proofs)
   - [Understanding AI-Enhanced Explanations](#understanding-ai-enhanced-explanations)
   - [Testing ZK Proof System](#testing-zk-proof-system)

5. [Developer Documentation](#5-developer-documentation)
   - [Project Structure](#project-structure)
   - [Core Services](#core-services)
   - [Key Components](#key-components)
   - [Integration Points](#integration-points)
   - [Testing Framework](#testing-framework)

6. [ZK Proof Canister](#6-zk-proof-canister)
   - [Canister Overview](#canister-overview)
   - [API Documentation](#api-documentation)
   - [Canister Deployment](#canister-deployment)
   - [Integration with Frontend](#integration-with-frontend)

7. [AI Components](#7-ai-components)
   - [OpenAI Integration](#openai-integration)
   - [Prompt Engineering](#prompt-engineering)
   - [AI Summary Generation](#ai-summary-generation)

8. [Security Considerations](#8-security-considerations)
   - [Privacy Guarantees](#privacy-guarantees)
   - [Data Protection](#data-protection)
   - [Client-Side Security](#client-side-security)

9. [Future Roadmap](#9-future-roadmap)
   - [Expanded Use Cases](#expanded-use-cases)
   - [Enhanced AI Features](#enhanced-ai-features)
   - [Additional Token Support](#additional-token-support)

10. [API Reference](#10-api-reference)
    - [ZK Proof API](#zk-proof-api)
    - [AI Enhancement API](#ai-enhancement-api)
    - [Wallet Integration API](#wallet-integration-api)

11. [Troubleshooting](#11-troubleshooting)
    - [Common Issues](#common-issues)
    - [Error Messages](#error-messages)
    - [Support Resources](#support-resources)

12. [Contributing](#12-contributing)
    - [Development Workflow](#development-workflow)
    - [Code Standards](#code-standards)
    - [Pull Request Process](#pull-request-process)

13. [Glossary](#13-glossary)
    - [Zero-Knowledge Terminology](#zero-knowledge-terminology)
    - [Internet Computer Terms](#internet-computer-terms)
    - [Project-Specific Terms](#project-specific-terms)

---

# 1. Introduction

## What is Ghost?

Ghost (The ZK Notary Agent) is a privacy-focused application that enables users to create and verify Zero-Knowledge Proofs (ZKPs) on the Internet Computer blockchain. It serves as a bridge between complex cryptographic technology and everyday use cases, allowing users to prove ownership of digital assets without revealing sensitive information such as their account balances or complete identities.

The project combines cutting-edge zero-knowledge cryptography with artificial intelligence to provide easily understandable explanations of what each proof demonstrates. This combination makes privacy technology more accessible to users who may not have technical backgrounds in cryptography.

## Key Features

- **Zero-Knowledge Proof Generation**: Create cryptographic proofs that verify token ownership without revealing the actual balance
- **Anonymous Verification**: Share proofs through unique links that can be verified by third parties without revealing user identity
- **AI-Enhanced Explanations**: Get plain-language summaries of what each proof demonstrates
- **Internet Computer Integration**: Built on the Internet Computer blockchain with native ICP token support
- **End-to-End Testing**: Comprehensive test suite to validate the full proof lifecycle
- **Privacy Preservation**: All sensitive operations happen client-side to maintain privacy
- **User-Friendly Interface**: Intuitive UI designed for users of all technical levels

## Project Vision

Ghost represents the first step in creating a comprehensive Zero-Knowledge service for the Internet Computer ecosystem. The vision extends beyond the current implementation to create a privacy-preserving infrastructure layer that can be used across a wide range of applications.

Our mission is to make privacy technology accessible to everyone by:

1. Simplifying complex cryptographic concepts through intuitive interfaces
2. Providing AI-enhanced explanations that demystify zero-knowledge technology
3. Creating building blocks for developers to integrate privacy features into their own applications
4. Establishing standards for private attestations on the Internet Computer

In the rapidly evolving digital landscape where data privacy concerns continue to grow, Ghost aims to empower users with the tools to maintain control over their sensitive information while still participating fully in the digital economy.

---

# 2. Technical Architecture

## System Overview

Ghost is built as a modern web application that interfaces with the Internet Computer blockchain. The system architecture follows a modular design with clear separation of concerns:

![Ghost System Architecture](https://i.imgur.com/2pApLMl.png)

The architecture consists of these primary layers:

1. **Presentation Layer**: React-based UI components, responsive design
2. **Application Layer**: Business logic, state management, data flow
3. **Service Layer**: API connectors, wallet integration, AI services
4. **Blockchain Layer**: Internet Computer canister interaction

Data flows from the user through the presentation layer to the service layer, which communicates with the blockchain to generate and verify proofs. The system is designed to maintain privacy by keeping sensitive operations client-side whenever possible.

## Component Breakdown

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

## Zero-Knowledge Proof System

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

## AI Enhancement Layer

The AI enhancement layer adds a unique dimension to Ghost, making complex cryptographic operations more accessible to non-technical users. This layer:

1. Takes information about a generated proof
2. Constructs a prompt for the OpenAI API
3. Receives the AI response with a plain-language explanation
4. Presents the explanation to the user alongside the technical proof details

The implementation uses carefully designed prompts to ensure the AI explains the proof accurately while maintaining appropriate security boundaries. The AI never has access to the actual proof data or user's private information.

---

# 3. Getting Started

## Installation

To install Ghost locally for development or testing purposes, follow these steps:

```bash
# Clone the repository
git clone https://github.com/gabrielrondon/ghost_dev.git
cd ghost_dev

# Install dependencies
npm install

# Start the development server
npm run dev
```

## Prerequisites

Before installing Ghost, ensure you have the following prerequisites:

- **Node.js**: v16.0.0 or higher
- **npm**: v8.0.0 or higher
- **Internet Computer wallet**: Either Internet Identity or Plug wallet
- **OpenAI API key**: (Optional) For AI-enhanced explanations

## Development Environment Setup

To set up a complete development environment:

1. **Install Node.js and npm**: Download from [nodejs.org](https://nodejs.org/)

2. **Set up an Internet Computer wallet**:
   - [Internet Identity](https://identity.ic0.app/)
   - [Plug Wallet](https://plugwallet.ooo/)

3. **Get an OpenAI API key** (optional):
   - Create an account at [OpenAI](https://platform.openai.com/)
   - Generate an API key in your account dashboard

4. **Configure environment variables**:
   - No environment variables are needed for basic functionality
   - API keys are stored in the browser's localStorage for security

## Configuration

Ghost is designed to be used without extensive configuration. The primary configuration points are:

- **API Key for AI Features**: Set in the Settings > API Configuration section of the application
- **Theme Selection**: Toggle between light and dark mode in the user interface
- **Network Configuration**: By default, Ghost connects to the Internet Computer mainnet

Advanced users can modify the application's behavior by editing constants in the source code:

- `src/utils/icpLedger.ts`: LEDGER_CANISTER_ID for the ICP ledger canister
- `src/services/zkProof/canisterDefinition.ts`: ZK_PROOF_CANISTER_ID for the ZK proof canister

---

# 4. User Guide

## Connecting Your Wallet

To use Ghost, you'll first need to connect your Internet Computer wallet. Ghost supports two wallet providers:

### Internet Identity

1. Navigate to the Ghost application
2. Click on "Connect with Internet Identity" button
3. You will be redirected to the Internet Identity service
4. Authenticate using your preferred method (security key, passphrase, etc.)
5. After successful authentication, you'll be redirected back to Ghost
6. Your wallet will now be connected and your token balances will be displayed

### Plug Wallet

1. Ensure the Plug wallet extension is installed in your browser
2. Navigate to the Ghost application
3. Click on "Connect with Plug Wallet" button
4. A popup from the Plug wallet will appear asking for connection approval
5. Approve the connection request
6. Your wallet will now be connected and your token balances will be displayed

If you don't see the Plug wallet option, you may need to install the Plug browser extension first.

## Generating ZK Proofs

Once your wallet is connected, you can generate a Zero-Knowledge Proof of token ownership:

1. In the main interface, locate the "ZK Proof Generator" card
2. Select the token you want to create a proof for (currently only ICP is supported)
3. Click the "Generate ZK Proof" button
4. The application will create a cryptographic proof, which may take a few seconds
5. When complete, you'll see a dialog with your proof details
6. The dialog includes:
   - Proof ID: A unique identifier for this proof
   - Shareable Link: A URL that can be shared with others to verify the proof
   - Token: The token this proof is for
   - Generated At: Timestamp of proof creation
   - AI-Enhanced Summary: A plain-language explanation of what the proof demonstrates

### Sharing Proofs

To share your proof with someone else:

1. From the proof result dialog, click the "Share Proof" button to copy the shareable link
2. Send this link to the person who needs to verify your token ownership
3. When they open the link, they'll be able to verify your proof without seeing your actual balance

Alternatively, you can copy just the Proof ID by clicking the copy button next to it, and instruct the verifier to enter it manually in the verification page.

## Verifying ZK Proofs

To verify a proof that someone has shared with you:

1. Access the shared verification link, or navigate to the "Verify" page
2. If using a link, the proof will be verified automatically
3. If entering manually, paste the Proof ID in the verification form and click "Verify"
4. The system will check the cryptographic proof and display the result
5. If valid, you'll see:
   - A success message confirming the proof is valid
   - Details about what the proof demonstrates
   - An AI-enhanced explanation of the proof's significance
6. If invalid, you'll see an error message explaining why the verification failed

The verification process confirms that the person owns the specified token without revealing their actual balance or account details.

## Understanding AI-Enhanced Explanations

Each successful proof generation and verification includes an AI-enhanced explanation to help understand what the proof demonstrates in plain language.

### Setting Up AI Explanations

To enable AI explanations:

1. Go to the Settings page
2. Navigate to the "API Configuration" tab
3. Enter your OpenAI API key
4. Click "Save Key"

Once configured, AI explanations will be automatically generated when:
- You create a new ZK proof
- You verify a valid proof

### Interpreting AI Summaries

AI summaries typically include:

1. **Brief Summary**: A one-sentence explanation of what the proof demonstrates
2. **Detailed Explanation**: A longer explanation of the proof's significance and how zero-knowledge technology protects privacy

These explanations help non-technical users understand the value and meaning of the cryptographic proof in everyday terms.

## Testing ZK Proof System

Ghost includes a comprehensive test suite to validate the ZK proof system's functionality:

1. Navigate to the "Test" page in the application
2. Connect your wallet if not already connected
3. Select a token to test with from the dropdown
4. Click "Run End-to-End Tests"
5. The system will execute a series of tests:
   - Generate ZK Proof: Tests proof generation
   - Verify ZK Proof: Tests verification of the generated proof
   - Anonymous Verification: Tests verification with an anonymous agent
6. Test results will be displayed showing the success or failure of each step
7. For detailed analysis, click "View Detailed Results"

This testing functionality ensures the entire proof lifecycle works correctly and helps diagnose any issues.

---

# 5. Developer Documentation

## Project Structure

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

## Core Services

### ZK Proof Service

Located in `src/services/zkProof`, this service handles all interaction with the ZK proof canister:

```typescript
// Key functions
export const generateZKProof = async (
  agent: HttpAgent,
  token: string,
  principal: Principal
): Promise<ZKProofResponse>;

export const verifyZKProof = async (
  agent: HttpAgent,
  proofId: string,
  proofData?: string
): Promise<ProofVerificationResult>;
```

### AI Service

Located in `src/services/aiService.ts`, this service manages AI interaction:

```typescript
// Key functions
export const generateProofSummary = async (
  proofData: {
    proofId: string;
    token: string;
    timestamp: number;
  },
  config?: Partial<AIConfig>
): Promise<AISummaryResponse>;

export const getOpenAIKey = (): string;
export const saveOpenAIKey = (key: string): void;
export const clearOpenAIKey = (): void;
```

### Auth Service

Located in `src/services/authService.ts`, this service handles wallet connections:

```typescript
// Key functions
export const createAgent = async (identity: Identity): Promise<HttpAgent>;
export const createAuthClient = async (): Promise<AuthClient>;
export const login = async (authClient: AuthClient, onSuccess: () => void): Promise<void>;
export const logout = async (authClient: AuthClient): Promise<void>;
export const connectWithPlug = async (canisterIds: string[] = [], silentReconnect = false): Promise<{
  agent: HttpAgent;
  principal: Principal;
}>;
```

### Balance Service

Located in `src/services/balanceService.ts`, this service fetches token balances:

```typescript
// Key functions
export const fetchICPBalance = async (
  agent: HttpAgent,
  userPrincipal: Principal
): Promise<Token[]>;
```

## Key Components

### ZKProofGenerator

Located in `src/components/ZKProofGenerator`, this component handles the UI and logic for generating ZK proofs:

```typescript
interface ZKProofGeneratorProps {
  agent: HttpAgent | null;
  principal: string | null;
  tokens: Token[] | null;
}
```

The component uses the `useZKProofGeneration` hook to handle the generation logic.

### ZKProofVerifier

Located in `src/components/ZKProofVerifier`, this component handles proof verification:

```typescript
interface ZKProofVerifierProps {
  proofId?: string;
}
```

The component uses the `useZKProofVerification` hook for verification logic.

### ZKProofSummary

Located in `src/components/ZKProofSummary`, this component generates and displays AI summaries:

```typescript
interface ZKProofSummaryProps {
  proofResult: ZKProofResponse;
  principal?: string | null;
}
```

### ZKProofTest

Located in `src/components/ZKProofTest`, this component provides end-to-end testing:

```typescript
interface ZKProofTestRunnerProps {
  agent: HttpAgent | null;
  principal: string | null;
  tokens: Token[] | null;
}
```

## Integration Points

Ghost integrates with several external systems:

### Internet Computer Ledger

Integration with the ICP ledger canister for balance fetching:

```typescript
// src/utils/icpLedger.ts
export const LEDGER_CANISTER_ID = "ryjl3-tyaaa-aaaaa-aaaba-cai";
```

### ZK Proof Canister

Integration with the custom ZK proof canister:

```typescript
// src/services/zkProof/canisterDefinition.ts
export const ZK_PROOF_CANISTER_ID = "hi7bu-myaaa-aaaad-aaloa-cai";
```

### OpenAI API

Integration with OpenAI for AI-enhanced explanations:

```typescript
// src/services/aiService.ts
const response = await fetch("https://api.openai.com/v1/chat/completions", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify({
    model,
    messages: [
      {
        role: "system",
        content: "You are an AI assistant that explains Zero-Knowledge Proofs in plain language..."
      },
      {
        role: "user",
        content: prompt
      }
    ],
    temperature: 0.3,
    max_tokens: 300
  }),
});
```

## Testing Framework

Ghost includes a comprehensive testing framework for the ZK proof system:

```typescript
// src/utils/zkProofTesting.ts
export const runZKProofTest = async (
  agent: HttpAgent,
  principal: Principal,
  token: Token
): Promise<TestSuiteResults>;
```

The testing framework verifies:
1. Proof generation
2. Proof verification
3. Anonymous verification

Results are structured in a test suite format:

```typescript
export interface TestSuiteResults {
  allPassed: boolean;
  results: TestResult[];
  startTime: number;
  endTime: number;
  duration: number;
}
```

---

# 6. ZK Proof Canister

## Canister Overview

The ZK proof canister is a custom Internet Computer canister that handles the cryptographic operations for proof generation and verification. It is deployed on the IC mainnet with the canister ID: `hi7bu-myaaa-aaaad-aaloa-cai`.

The canister provides:
- Cryptographic proof generation for token ownership
- Verification of generated proofs
- Support for multiple token standards

## API Documentation

The canister exposes two primary methods:

### 1. prove_ownership

Generates a Zero-Knowledge Proof of token ownership.

**Input**:
- `token`: String identifier for the token
- `input`: TokenOwnershipInput structure containing:
  - `token_metadata`: Information about the token
  - `token_id`: For non-fungible tokens (empty for fungible)
  - `balance`: Byte representation of the balance amount
  - `owner_hash`: Hash of the owner's principal ID
  - `merkle_path`: For tokens with Merkle tree representations
  - `path_indices`: Indices for the Merkle path
  - `token_specific_data`: Optional additional data

**Output**:
- `Ok`: Uint8Array representing the proof
- `Err`: String error message

### 2. verify_proof

Verifies a previously generated proof.

**Input**:
- `proofData`: Uint8Array containing the proof data

**Output**:
- `Ok`: Boolean indicating if the proof is valid
- `Err`: String error message

## Canister Deployment

The ZK proof canister is already deployed on the Internet Computer mainnet. When developing locally, the frontend communicates with this production canister.

To view the canister in the Candid UI:
- Visit [https://a4gq6-oaaaa-aaaab-qaa4q-cai.raw.ic0.app/?id=hi7bu-myaaa-aaaad-aaloa-cai](https://a4gq6-oaaaa-aaaab-qaa4q-cai.raw.ic0.app/?id=hi7bu-myaaa-aaaad-aaloa-cai)

## Integration with Frontend

The frontend integrates with the canister using the Internet Computer JavaScript Agent:

```typescript
// src/services/zkProof/actorService.ts
export const createZKProofActor = async (
  agent: HttpAgent
): Promise<ActorSubclass<ZKProofCanister>> => {
  try {
    console.log("Creating ZK Proof actor");
    
    // Check if agent is anonymous in a safer way
    const isAnonymous = agent instanceof HttpAgent && !agent.getPrincipal;
    
    console.log(`Agent is anonymous: ${isAnonymous}`);
    
    // Create the actor with special options for anonymous verification
    const actorOptions = {
      agent,
      canisterId: ZK_PROOF_CANISTER_ID,
    };
    
    // For anonymous verification, we need to bypass authentication
    // Create actor with explicit configuration for query transforms
    const actor: ActorSubclass<ZKProofCanister> = Actor.createActor(
      zkProofCanisterIDL,
      {
        ...actorOptions,
        queryTransform: (args: any) => {
          return { ...args, certified: false };
        }
      }
    );
    
    console.log("ZK Proof actor created successfully");
    return actor;
  } catch (error) {
    console.error("Error creating ZK Proof actor:", error);
    throw error;
  }
};
```

Communication with the canister happens through this actor interface.

---

# 7. AI Components

## OpenAI Integration

Ghost integrates with OpenAI's API to provide AI-enhanced explanations of Zero-Knowledge Proofs. The integration is designed to:

1. Maintain user privacy (no sensitive data is sent to OpenAI)
2. Provide clear, accurate explanations of complex cryptographic concepts
3. Make ZK technology more accessible to non-technical users

The integration is implemented in `src/services/aiService.ts`.

### API Key Management

For privacy and security reasons, Ghost does not include any API keys. Instead, users must provide their own OpenAI API key to use the AI features:

```typescript
export const getOpenAIKey = (): string => {
  // Only use user-provided keys from localStorage
  const userProvidedKey = localStorage.getItem("openai_api_key");
  return userProvidedKey || "";
};

export const saveOpenAIKey = (key: string): void => {
  localStorage.setItem("openai_api_key", key);
};

export const clearOpenAIKey = (): void => {
  localStorage.removeItem("openai_api_key");
};
```

Keys are stored only in the browser's localStorage and are never sent to any server other than OpenAI's API endpoint.

## Prompt Engineering

The AI component uses carefully designed prompts to generate consistent, accurate explanations:

```typescript
const prompt = `
You are an assistant that explains Zero-Knowledge Proofs (ZKPs) in simple terms.

Here's information about a ZK proof that was generated:
- Token: ${proofData.token}
- Generation Time: ${new Date(proofData.timestamp).toLocaleString()}
- Proof ID: ${proofData.proofId}

This proof specifically verifies ownership of the ${proofData.token} token without revealing the actual balance. The proof uses cryptographic techniques to confirm the user holds this token without exposing sensitive wallet information.

Please provide:
1. A brief, one-sentence summary of what this proof verifies about the ${proofData.token} token ownership (for non-technical users)
2. A more detailed explanation (2-3 sentences) about what this ${proofData.token} ownership proof demonstrates, how zero-knowledge technology protects the user's privacy, and why this approach is valuable for verifying digital assets
`;
```

The prompt is designed to:
- Set clear expectations for the AI's role
- Provide only non-sensitive information about the proof
- Request specific types of explanations at different detail levels
- Focus on explaining the concept rather than technical details

## AI Summary Generation

The AI summary generation process:

1. Collects non-sensitive proof metadata (token type, timestamp, proof ID)
2. Constructs a prompt for the OpenAI API
3. Makes a request to the OpenAI Chat Completions API
4. Parses the response to extract the summary and detailed explanation
5. Returns the formatted response to the UI for display

The result provides users with:
- A brief, one-sentence explanation of what the proof shows
- A more detailed explanation of the significance and privacy benefits

Example implementation:

```typescript
export const generateProofSummary = async (
  proofData: {
    proofId: string;
    token: string;
    timestamp: number;
  },
  config?: Partial<AIConfig>
): Promise<AISummaryResponse> => {
  try {
    const { apiKey, model } = { ...defaultConfig, ...config };
    
    if (!apiKey) {
      return {
        summary: "API key required for AI summaries",
        detailed: "Please provide an OpenAI API key to generate summaries.",
        error: "No API key provided"
      };
    }

    // Create and send the prompt to OpenAI
    const response = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        model,
        messages: [
          {
            role: "system",
            content: "You are an AI assistant that explains Zero-Knowledge Proofs in plain language, with a focus on explaining token ownership verification."
          },
          {
            role: "user",
            content: prompt
          }
        ],
        temperature: 0.3,
        max_tokens: 300
      }),
    });

    // Process the response
    const result = await response.json();
    const content = result.choices[0]?.message?.content;
    
    // Parse and format the AI's response
    const sections = content.split(/\d+\.\s+/).filter(Boolean);
    
    let summary = `This proves you own the ${proofData.token} token without revealing your balance.`;
    let detailed = `The zero-knowledge proof cryptographically verifies your ownership of ${proofData.token} without sharing sensitive details like account balance or transaction history.`;
    
    if (sections.length >= 2) {
      summary = sections[0].trim();
      detailed = sections[1].trim();
    }

    return { summary, detailed };
  } catch (error) {
    // Error handling
    return {
      summary: "Unable to generate AI summary",
      detailed: "There was an error when trying to generate the summary.",
      error: error instanceof Error ? error.message : "Unknown error"
    };
  }
};
```

---

# 8. Security Considerations

## Privacy Guarantees

Ghost is designed with privacy as a central principle. The privacy guarantees include:

### Zero-Knowledge Proofs

- **No Balance Disclosure**: The ZK proof system allows users to prove token ownership without revealing their actual balance
- **Cryptographic Verification**: All proofs are verified cryptographically, ensuring mathematical certainty
- **Selective Disclosure**: Users control exactly what information is shared with verifiers

### Data Minimization

- Only the minimum necessary data is included in proofs
- Proofs contain no personally identifiable information
- Verification requires only the proof itself, not user account details

## Data Protection

Ghost implements several data protection measures:

### Client-Side Storage

- Proofs are stored in the client's browser localStorage
- No server-side storage of sensitive information
- Proofs have a built-in expiration period (7 days)

### API Key Protection

- OpenAI API keys are stored only in the browser's localStorage
- Keys are never sent to any server except OpenAI directly
- Users can clear their API keys at any time

### Secure Communication

- All blockchain interactions use secure HTTPS connections
- Wallet connections follow the Internet Computer's security standards
- AI API calls use secure HTTPS with API key authentication

## Client-Side Security

The application includes several client-side security measures:

### Input Validation

```typescript
// src/services/zkProof/proofValidator.ts
export const validateProofId = (proofId: string): { isValid: boolean; errorMessage?: string } => {
  // Trim whitespace
  const trimmedProofId = proofId.trim();
  
  // Check if empty
  if (!trimmedProofId) {
    return { 
      isValid: false, 
      errorMessage: "Proof ID cannot be empty" 
    };
  }
  
  // Check length
  if (trimmedProofId.length < 8 || trimmedProofId.length > 64) {
    return { 
      isValid: false, 
      errorMessage: "Proof ID must be between 8 and 64 characters" 
    };
  }

  // Check format
  if (!/^[a-zA-Z0-9]+$/.test(trimmedProofId)) {
    return { 
      isValid: false, 
      errorMessage: "Proof ID must contain only alphanumeric characters" 
    };
  }
  
  return { isValid: true };
};
```

### Input Sanitization

```typescript
export const sanitizeInput = (input: string): string => {
  if (!input) return '';
  
  // Replace potential HTML/script tags
  return input
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
};
```

### Rate Limiting

To prevent abuse, Ghost implements client-side rate limiting for verification attempts:

```typescript
// src/services/rateLimiter.ts
export const checkRateLimit = (
  operationKey: string, 
  options: RateLimitOptions = { maxRequests: 5, timeWindowMs: 60000 }
): { allowed: boolean; timeRemaining?: number } => {
  const now = Date.now();
  const tracker = rateLimitStore[operationKey];
  
  // If no tracker exists or the reset time has passed, create a new one
  if (!tracker || now > tracker.resetTime) {
    rateLimitStore[operationKey] = {
      count: 1,
      resetTime: now + options.timeWindowMs
    };
    return { allowed: true };
  }
  
  // Check if under the limit
  if (tracker.count < options.maxRequests) {
    tracker.count++;
    return { allowed: true };
  }
  
  // Rate limit exceeded
  const timeRemaining = tracker.resetTime - now;
  return { 
    allowed: false, 
    timeRemaining 
  };
};
```

### Error Handling

Comprehensive error handling prevents information leakage and provides users with clear error messages:

```typescript
// Error types for ZK proof verification
export enum ProofVerificationErrorType {
  PROOF_NOT_FOUND = "PROOF_NOT_FOUND",
  INVALID_PROOF_FORMAT = "INVALID_PROOF_FORMAT",
  EXPIRED_PROOF = "EXPIRED_PROOF",
  CANISTER_ERROR = "CANISTER_ERROR",
  UNKNOWN_ERROR = "UNKNOWN_ERROR"
}

// Error response for ZK proof verification
export interface ProofVerificationError {
  type: ProofVerificationErrorType;
  message: string;
  details?: string;
}
```

---

# 9. Future Roadmap

## Expanded Use Cases

Ghost's roadmap includes several planned expansions to its use cases:

### Multi-Token Support

Future versions will support a wider range of tokens:

- Additional fungible tokens (ICRC-1, ICRC-2)
- Non-fungible tokens (NFTs) with specialized proof generation
- Custom tokens on the Internet Computer

### Enhanced Proof Types

Beyond simple token ownership, Ghost will add support for:

- **Threshold Proofs**: Prove ownership of at least X tokens without revealing the exact amount
- **Range Proofs**: Prove a balance falls within a specific range
- **Time-Locked Proofs**: Proofs that expire or become valid at specific times
- **Conditional Proofs**: Proofs that depend on external conditions

### Credential Verification

A key expansion area is using ZK proofs for credential verification:

- Academic credential verification
- Age verification without revealing birth date
- Membership verification for DAO access
- Identity verification preserving anonymity

## Enhanced AI Features

The AI component will be expanded to provide more sophisticated capabilities:

### Interactive Explainers

- Conversational interfaces to explain ZK concepts
- Visual explainers that illustrate how proofs work
- Step-by-step guides for specific ZK applications

### Proof Recommendation Engine

- AI-driven suggestion of appropriate proof types
- Context-aware recommendations based on user needs
- Integration with common verification scenarios

### Multi-Modal Explanations

- Visual representations of complex ZK concepts
- Audio explanations for accessibility
- Interactive demonstrations of key principles

## Additional Token Support

Ghost's token support roadmap includes:

### Internet Computer Ecosystem

- Full support for all ICRC token standards
- Integration with Internet Computer NFT standards
- Support for specialized IC tokens

### Cross-Chain Integration

- Support for Ethereum tokens through bridge technologies
- Integration with other blockchain ecosystems
- Multi-chain proof verification

### Custom Token Registration

- Developer API for registering custom tokens
- Self-service token integration
- Extensible token metadata system

---

# 10. API Reference

## ZK Proof API

### Types

```typescript
// Token standard types
export type TokenStandard = {
  'ERC20': null;
} | {
  'ERC721': null;
} | {
  'ERC1155': null;
} | {
  'ICRC1': null;
} | {
  'ICRC2': null;
} | {
  'ICP': null;
};

// Token metadata structure
export type TokenMetadata = {
  canister_id: string;
  token_standard: TokenStandard;
  decimals: [] | [number];
};

// Input structure for token ownership proofs
export type TokenOwnershipInput = {
  token_metadata: TokenMetadata;
  token_id: Uint8Array;
  balance: Uint8Array;
  owner_hash: Uint8Array;
  merkle_path: Uint8Array[];
  path_indices: Uint8Array;
  token_specific_data: [] | [Uint8Array];
};

// Result type for canister calls
export type Result = {
  'Ok': boolean;
} | {
  'Err': string;
};

// Response format for frontend
export interface ZKProofResponse {
  proofId: string;
  proofLink: string;
  token: string;
  name?: string;
  description?: string;
  timestamp: number;
}

// Error response for ZK proof verification
export interface ProofVerificationError {
  type: ProofVerificationErrorType;
  message: string;
  details?: string;
}

// Result of a proof verification
export interface ProofVerificationResult {
  isValid: boolean;
  error?: ProofVerificationError;
}
```

### Methods

#### Generate ZK Proof

```typescript
/**
 * Generates a ZK proof for a token
 */
export const generateZKProof = async (
  agent: HttpAgent,
  token: string,
  principal: Principal
): Promise<ZKProofResponse>;
```

#### Verify ZK Proof

```typescript
/**
 * Verifies a ZK proof
 */
export const verifyZKProof = async (
  agent: HttpAgent,
  proofId: string,
  proofData?: string
): Promise<ProofVerificationResult>;
```

## AI Enhancement API

### Types

```typescript
// Interface for AI service responses
export interface AISummaryResponse {
  summary: string;
  detailed: string;
  error?: string;
}

// Configuration for AI requests
export interface AIConfig {
  apiKey: string;
  model: string;
}
```

### Methods

#### Generate Proof Summary

```typescript
/**
 * Generate a natural language summary of a ZK proof
 * @param proofData Information about the proof to summarize
 * @param config OpenAI API configuration
 */
export const generateProofSummary = async (
  proofData: {
    proofId: string;
    token: string;
    timestamp: number;
  },
  config?: Partial<AIConfig>
): Promise<AISummaryResponse>;
```

#### API Key Management

```typescript
/**
 * Get the API key from user-provided storage only
 */
export const getOpenAIKey = (): string;

/**
 * Save a user-provided API key
 */
export const saveOpenAIKey = (key: string): void;

/**
 * Clear a saved API key
 */
export const clearOpenAIKey = (): void;
```

## Wallet Integration API

### Internet Identity

```typescript
/**
 * Creates an auth client for Internet Computer authentication
 */
export const createAuthClient = async (): Promise<AuthClient>;

/**
 * Initiates the login flow with Internet Computer identity service
 */
export const login = async (
  authClient: AuthClient, 
  onSuccess: () => void
): Promise<void>;

/**
 * Logs out the current user
 */
export const logout = async (authClient: AuthClient): Promise<void>;
```

### Plug Wallet

```typescript
/**
 * Connect using Plug wallet
 */
export const connectWithPlug = async (
  canisterIds: string[] = [], 
  silentReconnect = false
): Promise<{
  agent: HttpAgent;
  principal: Principal;
}>;

/**
 * Disconnect from Plug wallet
 */
export const disconnectFromPlug = async (): Promise<void>;
```

---

# 11. Troubleshooting

## Common Issues

### Wallet Connection Problems

#### Internet Identity Connection Fails

**Symptoms**: 
- Unable to connect using Internet Identity
- Connection process starts but returns to the application without authentication
- Error message about authentication failure

**Solutions**:
1. Ensure your Internet Identity is properly set up
2. Clear browser cookies and try again
3. Try using a different authentication method (security key, passphrase)
4. Check if you're using a supported browser (Chrome, Firefox, Safari)

#### Plug Wallet Not Detected

**Symptoms**:
- "Plug wallet extension is not installed" message
- Plug connect button is disabled

**Solutions**:
1. Install the Plug wallet extension from [plugwallet.ooo](https://plugwallet.ooo/)
2. If already installed, refresh the page
3. Check if the extension is enabled in your browser
4. Try restarting your browser

### Proof Generation Issues

#### Generation Fails with Error

**Symptoms**:
- Error message when trying to generate a proof
- Process starts but doesn't complete

**Solutions**:
1. Check your internet connection
2. Verify your wallet is still connected
3. Try selecting a different token
4. Refresh the page and try again

#### Created Proof is Not Appearing

**Symptoms**:
- Proof generation completes but no proof appears
- No confirmation dialog

**Solutions**:
1. Check browser console for errors
2. Verify localStorage is enabled in your browser
3. Try generating the proof again
4. Clear browser cache and reload the application

### Verification Problems

#### Proof Not Found

**Symptoms**:
- "Proof not found" error when trying to verify
- Shareable link doesn't work

**Solutions**:
1. Check if the proof ID is correct
2. Ensure the proof hasn't expired (proofs expire after 7 days)
3. Try using the full verification link instead of just the ID
4. Ask the proof creator to generate a new proof

#### Invalid Proof Format

**Symptoms**:
- "Invalid proof format" error during verification
- Verification process starts but fails

**Solutions**:
1. Ensure you're using the complete proof link
2. Check for any characters that might have been lost when copying the link
3. Try asking the proof creator to send the link again
4. Use the verification form directly rather than a link

### AI Features Not Working

#### API Key Issues

**Symptoms**:
- "API key required" message
- AI summaries don't appear

**Solutions**:
1. Check if you've added your OpenAI API key in the settings
2. Verify the API key is valid and has the correct permissions
3. Save the API key again
4. Check for any leading/trailing spaces in the API key

#### Summary Generation Fails

**Symptoms**:
- "Unable to generate AI summary" error
- Summary section shows error message

**Solutions**:
1. Check your OpenAI API key billing status
2. Verify your internet connection
3. Try refreshing the page
4. Check if the API key has the correct permissions

## Error Messages

### "Failed to connect to Plug wallet"

This error indicates a problem with the Plug wallet connection process.

**Possible causes**:
- Plug extension not installed correctly
- Plug extension needs to be updated
- Browser permissions issue

**Resolution**:
1. Reinstall the Plug wallet extension
2. Update to the latest version of Plug
3. Check browser permissions for the extension

### "Verification failed: Proof not found"

This error indicates the system couldn't find the proof data for verification.

**Possible causes**:
- Incorrect proof ID
- Proof has expired
- Proof was generated on a different device
- localStorage was cleared

**Resolution**:
1. Verify the proof ID is correct
2. Request a new proof if the original has expired
3. Use the complete verification link that includes the proof data
4. Generate a new proof

### "API error: 429"

This error indicates you've exceeded OpenAI's rate limits.

**Possible causes**:
- Too many API requests in a short time
- API key usage limits exceeded
- Account billing issue

**Resolution**:
1. Wait a few minutes and try again
2. Check your OpenAI account usage limits
3. Verify your billing status is active
4. Consider upgrading your OpenAI account tier

## Support Resources

If you encounter issues not covered by this troubleshooting guide, you can seek help through these channels:

- **GitHub Issues**: File an issue on the [Ghost GitHub repository](https://github.com/gabrielrondon/ghost_dev/issues)
- **Documentation**: Reference this documentation for detailed information
- **Community Forums**: Seek help from the Internet Computer developer community


---

# 12. Contributing

## Development Workflow

Ghost follows a standard GitHub-based development workflow:

1. **Fork the Repository**: Create your own fork of the [Ghost repository](https://github.com/gabrielrondon/ghost_dev)
2. **Create Feature Branch**: Create a branch for your feature or fix
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Develop and Test**: Make your changes and test thoroughly
4. **Commit Changes**: Commit with a clear message
   ```bash
   git commit -m "Add feature: your feature description"
   ```
5. **Push to Your Fork**: Push your branch to your fork
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create Pull Request**: Open a pull request to the main repository

## Code Standards

When contributing to Ghost, please follow these code standards:

### TypeScript

- Use TypeScript for all new code
- Include proper type definitions
- Avoid using `any` types where possible
- Add JSDoc comments for public functions

Example:

```typescript
/**
 * Validates a proof ID format
 * @param proofId The proof ID to validate
 * @returns Object containing validation result and any error message
 */
export const validateProofId = (proofId: string): ValidationResult => {
  // Implementation
};
```

### React Components

- Use functional components with hooks
- Keep components small and focused
- Use proper prop types
- Follow the existing component structure

Example:

```typescript
interface MyComponentProps {
  data: SomeType;
  onAction: (id: string) => void;
}

const MyComponent: React.FC<MyComponentProps> = ({ data, onAction }) => {
  // Implementation
};
```

### Styling

- Use the Tailwind CSS classes following the existing patterns
- Maintain a consistent look and feel
- Follow the theme system conventions

## Pull Request Process

When submitting a pull request:

1. **Provide a Clear Description**: Explain what your changes do and why they're needed
2. **Reference Issues**: Link to any related issues
3. **Include Screenshots**: For UI changes, include before/after screenshots
4. **Update Documentation**: Update relevant documentation to match your changes
5. **Review CI Results**: Ensure all CI checks pass
6. **Address Feedback**: Be responsive to review comments

---

# 13. Glossary

## Zero-Knowledge Terminology

### Zero-Knowledge Proof (ZK Proof)

A cryptographic method where one party (the prover) can prove to another (the verifier) that they know a value, without revealing the actual value.

### Prover

The party generating a Zero-Knowledge Proof to demonstrate knowledge of some information.

### Verifier

The party checking a Zero-Knowledge Proof to confirm the prover's knowledge without learning the actual information.

### ZK-SNARK

Zero-Knowledge Succinct Non-Interactive Argument of Knowledge - a type of cryptographic proof that is small in size and quick to verify.

### Commitment

A cryptographic way to commit to a value without revealing it, with the ability to unveil it later.

## Internet Computer Terms

### Internet Computer Protocol (ICP)

The native utility token of the Internet Computer blockchain.

### Canister

A smart contract on the Internet Computer that contains both code and state.

### Principal ID

A unique identifier for users and canisters on the Internet Computer.

### Internet Identity

Authentication system for the Internet Computer that enables secure, anonymous authentication.

### Cycles

The computational resources used to power smart contracts (canisters) on the Internet Computer.

## Project-Specific Terms

### Ghost

The project name for the Zero-Knowledge Notary Agent system.

### ZK Notary Agent

The role the Ghost system plays in facilitating and verifying Zero-Knowledge Proofs.

### Proof ID

A unique identifier for a generated Zero-Knowledge Proof in the Ghost system.

### Shareable Link

A URL containing or referencing a Zero-Knowledge Proof that can be shared with others for verification.

### AI-Enhanced Explanation

A plain-language explanation of a Zero-Knowledge Proof generated using AI to make the concept more accessible.

---

# Appendix A: Implementation Details

## Token Representation

Ghost handles ICP tokens as follows:

```typescript
// Token representation
export interface Token {
  name: string;
  symbol: string;
  amount: string;
  decimals: number;
  logo?: string;
}

// Convert e8s (ICP's smallest unit) to ICP with proper decimal places
export const formatE8sToICP = (e8s: bigint): string => {
  const icp = Number(e8s) / 100000000;
  return icp.toFixed(8);
};
```

## Proof Storage

Proofs are stored in the browser's localStorage:

```typescript
// Store proof data
localStorage.setItem(`proof_${proofId}`, proofBase64);

// Store metadata
localStorage.setItem(`metadata_${proofId}`, JSON.stringify(response));

// Retrieve proof data
const proofBase64 = localStorage.getItem(`proof_${proofId}`);

// Retrieve metadata
const metadata = JSON.parse(localStorage.getItem(`metadata_${proofId}`));
```

## Wallet Session Management

Wallet sessions are managed to enable reconnections:

```typescript
// Store session data
export const storeSession = (principal: string, provider: string) => {
  localStorage.setItem(STORAGE_KEY_PRINCIPAL, principal);
  localStorage.setItem(STORAGE_KEY_AUTH_PROVIDER, provider);
};

// Get stored session data
export const getStoredSession = () => {
  const principal = localStorage.getItem(STORAGE_KEY_PRINCIPAL);
  const provider = localStorage.getItem(STORAGE_KEY_AUTH_PROVIDER);
  
  return { principal, provider };
};
```

# Appendix B: Zero-Knowledge Proofs - Technical Deep Dive

## Cryptographic Foundations

Zero-Knowledge Proofs (ZKPs) rely on several cryptographic primitives and techniques:

### Commitment Schemes

A commitment scheme allows a prover to commit to a chosen value while keeping it hidden, with the ability to reveal it later. Ghost uses cryptographic commitments to secure token balance information:

```typescript
// Creating a commitment to the token balance
const balanceBytes = new Uint8Array(8);
const balanceBigInt = BigInt(Math.floor(Number(balance) * 100000000)); // Convert to e8s
  
// Convert BigInt to byte array (little-endian)
for (let i = 0; i < 8; i++) {
  balanceBytes[i] = Number((balanceBigInt >> BigInt(i * 8)) & BigInt(0xff));
}
```

### Interactive vs. Non-Interactive Proofs

Ghost uses non-interactive zero-knowledge proofs, which don't require back-and-forth communication between prover and verifier. This is essential for online verification where the prover and verifier may not be online simultaneously.

### Soundness and Completeness

A good zero-knowledge proof system has two key properties:
- **Soundness**: If the statement is false, no cheating prover can convince the verifier that it's true
- **Completeness**: If the statement is true, an honest prover can convince the verifier that it's true

The ZK proof canister implements both properties in its cryptographic protocol.

## Zero-Knowledge Proof Generation

The proof generation process in Ghost involves several steps:

1. **Token Ownership Preparation**:
   ```typescript
   const tokenInput = await createTokenOwnershipInput(token, principal, agent);
   ```

2. **Cryptographic Proof Creation**:
   ```typescript
   const result = await zkProofActor.prove_ownership(token, tokenInput);
   ```

3. **Proof Encoding and Storage**:
   ```typescript
   const proofBytes = result.Ok;
   const proofBase64 = btoa(String.fromCharCode.apply(null, [...proofBytes]));
   localStorage.setItem(`proof_${proofId}`, proofBase64);
   ```

## Zero-Knowledge Proof Verification

The verification process is the counterpart to generation:

1. **Proof Retrieval and Decoding**:
   ```typescript
   let proofBase64 = proofData || localStorage.getItem(`proof_${proofId}`);
   const proofString = atob(proofBase64);
   proofBytes = new Uint8Array(proofString.length);
   for (let i = 0; i < proofString.length; i++) {
     proofBytes[i] = proofString.charCodeAt(i);
   }
   ```

2. **Cryptographic Verification**:
   ```typescript
   const result = await zkProofActor.verify_proof(proofBytes);
   ```

3. **Result Interpretation**:
   ```typescript
   const isValid = result.Ok;
   return { isValid };
   ```

## Properties of Ghost's ZK System

The Zero-Knowledge proof system implemented in Ghost has several important properties:

### Zero-Knowledge

The verifier learns nothing about the prover's token balance beyond what's specifically being proven (ownership).

### Succinctness

Proofs are relatively small (compared to the original data) and quick to verify, making them practical for web applications.

### Non-Interactivity

Proofs can be generated once and verified many times without requiring further interaction with the prover.

### Universality

The system is designed to be extended to various token types and proof statements beyond simple ownership.

# Appendix C: AI Enhancement - Technical Details

## Model Selection

Ghost uses OpenAI's models for generating explanations:

```typescript
const defaultConfig: AIConfig = {
  apiKey: "", // Will be filled from user input
  model: "gpt-4o-mini" // Default to a cheaper, faster model
};
```

The model selection balances several factors:
- Cost efficiency for users
- Response quality for explanations
- Response speed for good user experience

## Prompt Design Principles

The prompts for AI explanations follow these design principles:

1. **Privacy-First**: No sensitive information is included
2. **Clear Instruction**: Specific output format and requirements
3. **Context-Rich**: Enough context about ZK proofs to generate quality responses
4. **Consistent Structure**: Predictable output format for easier parsing

## Response Parsing Strategy

AI responses are parsed to extract structured information:

```typescript
// Parse the AI response - normally it will have numbered responses
const sections = content.split(/\d+\.\s+/).filter(Boolean);

// Default fallbacks in case parsing doesn't work as expected
let summary = `This proves you own the ${proofData.token} token without revealing your balance.`;
let detailed = `The zero-knowledge proof cryptographically verifies your ownership of ${proofData.token} without sharing sensitive details like account balance or transaction history.`;

if (sections.length >= 2) {
  summary = sections[0].trim();
  detailed = sections[1].trim();
} else if (sections.length === 1) {
  // If we only got one section, use it as the summary and use a default detailed message
  summary = sections[0].trim();
} else if (content) {
  // If the numbering parsing failed, just use the whole content
  summary = content.split('.')[0] + '.';
  detailed = content.substring(summary.length).trim();
}
```

This approach ensures robustness even when AI responses don't follow the expected format exactly.

## Usage Tracking and Analysis

Ghost implements a simple usage tracking system to help users monitor their API usage:

```typescript
export const trackAPIUsage = (userId: string): number => {
  const usageKey = `openai_usage_${userId || "anonymous"}`;
  const currentUsage = parseInt(localStorage.getItem(usageKey) || "0", 10);
  const newUsage = currentUsage + 1;
  localStorage.setItem(usageKey, newUsage.toString());
  return newUsage;
};
```

This tracking is entirely client-side and private to the user.

# Appendix D: Internet Computer Integration

## Internet Computer Agent

Ghost interacts with the Internet Computer blockchain using the agent pattern:

```typescript
export const createAgent = async (identity: Identity): Promise<HttpAgent> => {
  // Create an agent using the identity
  const agent = new HttpAgent({ 
    identity, 
    host: IC_HOST // Always use mainnet
  });
  
  // Only fetch the root key in development
  if (!isProduction) {
    try {
      await agent.fetchRootKey();
      console.log("Agent root key fetched");
    } catch (error) {
      console.warn("Could not fetch root key, calls will fail in development:", error);
    }
  } else {
    console.log("Running in production, skipping root key fetch");
  }
  
  return agent;
};
```

## Canister Interaction

Communication with Internet Computer canisters happens through the Actor interface:

```typescript
// Create an actor to interact with the ZK Proof canister
export const createZKProofActor = async (
  agent: HttpAgent
): Promise<ActorSubclass<ZKProofCanister>> => {
  // Create the actor with special options for anonymous verification
  const actorOptions = {
    agent,
    canisterId: ZK_PROOF_CANISTER_ID,
  };
  
  // For anonymous verification, we need to bypass authentication
  const actor: ActorSubclass<ZKProofCanister> = Actor.createActor(
    zkProofCanisterIDL,
    {
      ...actorOptions,
      queryTransform: (args: any) => {
        return { ...args, certified: false };
      }
    }
  );
  
  return actor;
};
```

## Account Identification

Internet Computer accounts are identified using a specific transformation of principal IDs:

```typescript
export const principalToAccountIdentifier = (principal: Principal, subAccount?: Uint8Array): Uint8Array => {
  // Ensure the principal is included in the account identifier
  const principalBytes = principal.toUint8Array();
  
  // Prepare message components
  const prefix = new Uint8Array([10]); // Prefix for account IDs
  const label = new TextEncoder().encode("account-id");
  const defaultSubAccount = new Uint8Array(32).fill(0);
  const subAccountToUse = subAccount || defaultSubAccount;
  
  // Concatenate all parts for hashing
  const messageLength = prefix.length + label.length + principalBytes.length + subAccountToUse.length;
  const message = new Uint8Array(messageLength);
  
  let offset = 0;
  message.set(prefix, offset);
  offset += prefix.length;
  message.set(label, offset);
  offset += label.length;
  message.set(principalBytes, offset);
  offset += principalBytes.length;
  message.set(subAccountToUse, offset);
  
  // Generate hash using sha224
  const hash = sha224(message);
  const checksum = getCrc32(hash);
  
  // Combine checksum and hash to create account ID
  const checksumArray = new Uint8Array(4);
  checksumArray[0] = checksum >> 24 & 0xFF;
  checksumArray[1] = checksum >> 16 & 0xFF;
  checksumArray[2] = checksum >> 8 & 0xFF;
  checksumArray[3] = checksum & 0xFF;
  
  // Create the final account identifier
  const accountId = new Uint8Array(checksumArray.length + hash.length);
  accountId.set(checksumArray, 0);
  accountId.set(hash, checksumArray.length);
  
  return accountId;
};
```
```