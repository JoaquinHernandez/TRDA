# TRDA
The Red Dragon Audit (RDA) Framework: Enterprise-Grade Architecture

<img width="1024" height="339" alt="image" src="https://github.com/user-attachments/assets/9fd26fdc-1bea-43f9-b238-79a8487b4078" />

# 🐉 Red Dragon Audit (RDA)

**Red Dragon Audit (RDA)** is an enterprise-grade, asynchronous security orchestrator designed to detect misconfigurations and vulnerabilities across six major infrastructure domains: **Web, Active Directory, Linux, Windows, Databases, and Cloud (AWS/Azure).**

Built for senior security engineers and DevOps teams, RDA acts as a unified central dispatcher. Instead of juggling dozens of disjointed scripts, RDA provides a single configuration-driven framework to assess your entire attack surface rapidly, safely, and comprehensively.

---

## 💡 How It Helps

Security auditing often suffers from fragmented tooling, slow execution, and outputs that are difficult to integrate into developer workflows. RDA solves these problems through four core pillars:

* **🚀 Blazing Fast Execution (Async-First):** Network and Cloud API checks are powered by an asynchronous execution engine (`asyncio`). What traditionally takes minutes runs in seconds, allowing you to scan hundreds of web endpoints and cloud resources concurrently.
* **🛡️ Safe for the Enterprise (Read-Only):** RDA is strictly a **detection and enumeration** tool. It executes zero destructive payloads, credential dumps, or auto-exploits, making it safe to run against production environments without triggering aggressive endpoint defenses.
* **🔌 Frictionless Extensibility (Hot-Swappable Plugins):** Want to add a new check? Just drop a new `.py` script into the `modules/` directory. RDA’s dynamic registry automatically discovers and loads the module—no complex wiring or manual imports required.
* **⚙️ DevSecOps Ready (SARIF Integration):** Export findings directly to the Static Analysis Results Interchange Format (SARIF). Upload the output to your repository, and vulnerabilities will natively populate in the **GitHub Security Tab**, allowing you to block vulnerable Pull Requests automatically.

---

## ⚙️ Installation

RDA is built on Python and designed to be lightweight. It is highly recommended to run it within an isolated virtual environment.

**1. Clone the repository:**

```bash
git clone https://github.com/your-username/red-dragon-audit.git
cd red-dragon-audit

```

**2. Create and activate a virtual environment:**

```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate

```

**3. Install the required dependencies:**

```bash
pip install --upgrade pip
pip install -r requirements.txt

```

---

## 🚀 Usage

RDA is driven by a YAML configuration file that defines your target scope and credentials (for authorized testing only).

### 1. Define your targets

Create a `config.yaml` file targeting the systems you have authorization to audit:

```yaml
web:
  enabled: true
  targets:
    - "https://app.example.com"
aws:
  enabled: true
  profile: "security-audit-role"
linux:
  enabled: false

```

### 2. Run the audit

To execute the tool, you **must** supply the `--confirm-auth` flag. RDA will not run without explicit confirmation that you are authorized to test the targets.

**Standard Console Output:**

```bash
python -m rda.cli -c config.yaml --confirm-auth

```

**Export to SARIF (For GitHub DevSecOps Integration):**

```bash
python -m rda.cli -c config.yaml --confirm-auth --sarif

```

---

## ⚖️ Legal & Ethical Disclaimer

**RDA is a defensive security tool intended strictly for authorized auditing and hardening.**

By using this software, you agree to the following:

1. You have explicit, written authorization from the system owner to evaluate the targets specified in your configuration.
2. The `--confirm-auth` gate is a mandatory legal acknowledgment. Tampering with this gate violates the intended use of the software.
3. The authors and contributors of Red Dragon Audit are not responsible for any misuse, damage, or illegal activities conducted with this tool.
