# 🛡️ Autenticação e Gestão de Credenciais.

Este repositório contém uma implementação prática de um sistema de login de alta segurança, desenvolvido para cumprir rigorosos requisitos de proteção de dados e controle de acesso. O projeto utiliza o framework Flask e foca na defesa contra ataques comuns, como força bruta e vazamento de banco de dados.

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
