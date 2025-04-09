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