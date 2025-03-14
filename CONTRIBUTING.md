# Guia de Contribuição

Obrigado por considerar contribuir para o projeto WhatsApp Message Sender! Este documento fornece diretrizes para contribuir com este projeto.

## Índice

- [Código de Conduta](#código-de-conduta)
- [Como Posso Contribuir?](#como-posso-contribuir)
  - [Reportando Bugs](#reportando-bugs)
  - [Sugerindo Melhorias](#sugerindo-melhorias)
  - [Pull Requests](#pull-requests)
- [Estilo de Código](#estilo-de-código)
- [Processo de Desenvolvimento](#processo-de-desenvolvimento)
- [Ambiente de Desenvolvimento](#ambiente-de-desenvolvimento)

## Código de Conduta

Este projeto e todos os participantes estão comprometidos com um ambiente acolhedor e respeitoso. Esperamos que todos os colaboradores sigam estas diretrizes:

- Use linguagem acolhedora e inclusiva
- Respeite diferentes pontos de vista e experiências
- Aceite críticas construtivas com elegância
- Foque no que é melhor para a comunidade
- Demonstre empatia com outros membros da comunidade

## Como Posso Contribuir?

### Reportando Bugs

Esta seção orienta você sobre como relatar bugs. Seguir estas diretrizes ajuda os mantenedores a entender seu relatório, reproduzir o comportamento e encontrar relatórios relacionados.

- Use o rastreador de problemas (issue tracker) para relatar bugs
- Verifique se o bug já não foi relatado
- Use um título claro e descritivo
- Inclua passos detalhados para reproduzir o problema
- Descreva o comportamento esperado e o comportamento atual
- Inclua screenshots se possível
- Mencione sua versão do Python, sistema operacional e outras informações relevantes

### Sugerindo Melhorias

Esta seção orienta você sobre como sugerir melhorias, incluindo recursos completamente novos e pequenas melhorias nas funcionalidades existentes.

- Use o rastreador de problemas para sugerir melhorias
- Verifique se a melhoria já não foi sugerida
- Use um título claro e descritivo
- Forneça uma descrição detalhada da melhoria sugerida
- Explique por que esta melhoria seria útil para a maioria dos usuários

### Pull Requests

- Preencha o modelo de pull request
- Não inclua números de problemas no título do pull request
- Inclua screenshots e GIFs animados em seu pull request sempre que possível
- Siga as convenções de estilo do projeto
- Escreva documentação para novos recursos
- Mantenha um commit por funcionalidade
- Escreva mensagens de commit descritivas

## Estilo de Código

- Siga o [PEP 8](https://www.python.org/dev/peps/pep-0008/) para código Python
- Use docstrings para documentar funções e classes
- Mantenha o código limpo e bem documentado
- Use nomes descritivos para variáveis e funções
- Escreva testes para novas funcionalidades

## Processo de Desenvolvimento

1. Fork o repositório
2. Clone seu fork localmente
3. Crie um branch para sua feature ou correção
4. Faça suas alterações
5. Execute os testes
6. Envie um pull request

## Ambiente de Desenvolvimento

### Configuração

1. Instale o Python 3.8 ou superior
2. Clone o repositório
3. Inicialize o ambiente com uv:
   ```bash
   uv init
   ```
4. Instale as dependências:
   ```bash
   uv pip install -r requirements.txt
   ```
5. Configure as variáveis de ambiente conforme descrito no README.md

### Testes

Execute os testes antes de enviar um pull request:

```bash
pytest
```

---

Agradecemos suas contribuições para tornar este projeto melhor!
