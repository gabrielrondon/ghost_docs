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