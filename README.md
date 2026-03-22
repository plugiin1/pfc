# 🛡️ Autenticação e Gestão de Credenciais.

Este projeto evoluiu para uma solução de autenticação completa, integrando não apenas o acesso seguro via MFA (Multi-Factor Authentication), mas também um Fluxo de Recuperação de Conta Seguro. A aplicação utiliza tokens temporários e logs de auditoria para garantir que a redefinição de senhas siga os padrões modernos de cibersegurança, evitando vetores de ataque como sequestro de contas e interceptação de credenciais.

## 📋 Requisitos Implementados

O sistema foi construído seguindo a checklist de segurança abaixo:

- [x] **Criptografia de Senhas:** Uso de hash seguro (PBKDF2-HMAC-SHA256).
- [x] **Parâmetros de Custo:** Configurado com 600.000 iterações para dificultar ataques de força bruta.
- [x] **Salt Criptográfico:** Salt único por usuário gerado automaticamente.
- [x] **Autenticação de Dois Fatores (2FA):** Implementação via TOTP (Time-based One-Time Password).
- [x] **Validação em Etapas:** O 2FA só é solicitado após a validação correta da senha.
- [x] **Gestão de Sessão:** Expiração automática em 15 minutos e invalidação total no logout.
- [x] **Proteção contra Força Bruta:** Rate limiting integrado para bloquear tentativas excessivas.
- [x] **Documentação Técnica:** Justificativas de segurança incluídas no código e neste documento.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Framework Web:** Flask
- **Segurança:** - `Werkzeug` (Hashing e Salting)
  - `PyOTP` (Geração de tokens 2FA)
  - `Flask-Limiter` (Prevenção de ataques de força bruta)

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o Python instalado. No terminal, instale as bibliotecas necessárias:

```bash
pip install flask flask-limiter pyotp.
