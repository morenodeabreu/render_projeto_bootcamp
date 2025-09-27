# 🚗 Dashboard de Análise de Dados de Veículos

## 🌐 Aplicação Online

**Acesse a aplicação:** <https://render-projeto-bootcamp.onrender.com>

## 📋 Sobre o Projeto
Este projeto é uma aplicação web interativa desenvolvida com **Streamlit** para análise de dados de veículos. A aplicação permite aos usuários explorar e visualizar informações sobre anúncios de vendas de carros através de gráficos interativos.

## 🎯 Funcionalidades

- **Histograma Interativo**: Visualização da distribuição de quilometragem (odômetro) dos veículos
- **Gráfico de Dispersão**: Análise da relação entre quilometragem e preço dos veículos
- **Interface Intuitiva**: Controles simples com botões e caixas de seleção
- **Visualizações Responsivas**: Gráficos que se adaptam ao tamanho da tela

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Streamlit** - Framework para criação de aplicações web
- **Pandas** - Manipulação e análise de dados
- **Plotly Express** - Criação de gráficos interativos
- **SciPy** - Análises estatísticas

## 📊 Dados

O projeto utiliza um conjunto de dados de veículos (`vehicles.csv`) contendo informações sobre:

- Quilometragem (odômetro)
- Preços dos veículos
- Outras características relacionadas a anúncios de vendas

## 🚀 Como Executar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/render_projeto_bootcamp.git
cd render_projeto_bootcamp
```

2. Instale as dependências:

```bash
pip install streamlit pandas plotly scipy
```

3. Execute a aplicação:

```bash
streamlit run app.py
```

4. Acesse no navegador: `http://localhost:8501`

## 📁 Estrutura do Projeto

```text
render_projeto_bootcamp/
├── app.py              # Aplicação principal Streamlit
├── vehicles.csv        # Conjunto de dados dos veículos
├── README.md          # Documentação do projeto
└── requirements.txt   # Dependências do projeto
```

## 🎨 Interface da Aplicação

A aplicação possui uma interface limpa e intuitiva com:

1. **Cabeçalho Informativo**: Título, descrição e funcionalidades do projeto
2. **Controles Interativos**:
   - Botão "Criar histograma" para gerar histograma de quilometragem
   - Checkbox "Criar um histograma" para gerar gráfico de dispersão quilometragem vs preço
3. **Visualizações Dinâmicas**: Gráficos que aparecem conforme a interação do usuário

## 📈 Análises Disponíveis

### Histograma de Quilometragem

- Mostra a distribuição da quilometragem dos veículos no conjunto de dados
- Permite identificar padrões na distribuição dos dados
- Útil para entender a faixa de quilometragem mais comum

### Gráfico de Dispersão: Quilometragem vs Preço

- Visualiza a relação entre quilometragem e preço dos veículos
- Permite identificar tendências e correlações
- Ajuda a entender como a quilometragem afeta o valor do veículo

## 👨‍💻 Autor

- **Nome:** Roberto Moreno
- **Data:** 2025-09-27
- **Projeto:** Desenvolvido durante bootcamp de análise de dados

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

*Aplicação desenvolvida como parte de um projeto de bootcamp focado em análise e visualização de dados usando Python e Streamlit.*