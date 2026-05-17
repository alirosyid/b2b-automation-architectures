# Enterprise Architecture Threat Model (STRIDE Methodology)

This document outlines the security posture and threat mitigation strategies for the B2B AI Automation Engine.

## 1. Spoofing
* **Threat:** Malicious actors spoofing CRM webhooks to inject false leads.
* **Mitigation:** Cryptographic `RequestFingerprinter` and Zero-Trust HMAC signatures required on all ingress nodes.

## 2. Tampering
* **Threat:** Data manipulation during LLM processing.
* **Mitigation:** Immutable `ResilientDLQ` logs and TLS 1.3 encryption for all data-in-transit between n8n and Python microservices.

## 3. Repudiation
* **Threat:** Inability to trace which agent modified a CRM record.
* **Mitigation:** Event-Sourced audit logging and `GlassBoxExporter` providing cryptographic provenance for all AI decisions.

## 4. Information Disclosure
* **Threat:** Accidental leakage of PII into public LLM training datasets.
* **Mitigation:** `EdgePIIRedactor` scrubs sensitive data pre-flight. Enterprise-tier API agreements (Zero Data Retention) enforced.

## 5. Denial of Service (DoS)
* **Threat:** 'Noisy Neighbor' tenants crashing the shared architecture.
* **Mitigation:** `TokenBucketRateLimiter` strictly isolates compute capacity per tenant.

## 6. Elevation of Privilege
* **Threat:** Prompt Injection attacks granting unauthorized database access.
* **Mitigation:** Model Context Protocol (MCP) server strictly limits agentic database read/write permissions via isolated roles.
