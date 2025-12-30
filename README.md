# 🛡️ Iron Dome: Zero-Trust Network Architecture on Kubernetes

## 🚀 Project Overview
This project demonstrates a **DevSecOps** approach to hardening a Kubernetes cluster. By implementing a **Zero-Trust Network Architecture**, I successfully blocked unauthorized "Lateral Movement" attacks between microservices.

## 🏗️ Architecture
* **Orchestration:** Kubernetes (Minikube)
* **Security Engine:** Calico CNI (Container Network Interface)
* **Policy Object:** `NetworkPolicy` (Layer 3/4 Traffic Filtering)
* **Offensive Tools:** Nmap & Netcat (simulating an internal breach)

## 🧪 The "Attack & Defense" Simulation

### 1. The Vulnerability (Before Hardening)
* **Scenario:** A compromised "Hacker" pod attempts to connect to the critical "Database" pod.
* **Result:** Connection **OPEN**. The attacker has full access to data.
* *(Insert your first screenshot here)*

### 2. The Defense (Zero-Trust Implementation)
I applied a strict `NetworkPolicy` (Deny-All Ingress) to the Database, creating a firewall that drops all unauthorized packets.

### 3. The Validation (After Hardening)
* **Scenario:** The same Hacker pod attempts the connection again.
* **Result:** Connection **TIMED OUT**. The firewall successfully blocked the traffic.
* *(Insert your second "Time Out" screenshot here)*

## 💻 Technical Implementation
```yaml
# The Policy that blocked the attack
kind: NetworkPolicy
spec:
  podSelector:
    matchLabels:
      app: database
  policyTypes:
  - Ingress
  ingress: [] # Deny ALL traffic