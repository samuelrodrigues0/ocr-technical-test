# OCR Teste Técnico

Este projeto implementa uma solução para Optical Character Recognition (OCR), usando Tesseract OCR para extrair o texto de imagens nos formato (JPG, PNG, JPEG) e documentos PDF. Inclui funcionalidades para pre-processamento da imagem e extração do texto, com opções para mostrar o texto no console, salvar em arquivo txt ou ambos.

## Funcionalidades

*   **Imagens e PDF:** Suporta o processamento de imagens `.jpg`, `.png`, `.jpeg` e documentos `.pdf`.
*   **Pré-processamento de imagem:** Aplica escala cinza e transformação binária para aumentar o desempenho do OCR.
*   **Extração do texto:** Utiliza Tesseract OSR para extrair texto de imagens pré-processadas.
*   **Output flexível:** Permitir exibir o texto no console, salvar em arquivo `.txt` ou ambos.
*   **Suporte para multiplos idiomas:** Extrai textos em portugues e inglês.

## Instalação

Para executar o projeto, segue o passo a passo:

1.  **Clonar o repositório:**
    ```bash
    git clone https://github.com/your-repo/ocr-technical-test.git
    cd ocr-technical-test
    ```

2.  **Instalar o motor Tesseract OCR:**
    Este projeto utiliza o motor Tesseract OCR. Você precisa instalar separadamente no seu sistema:

    *   **Ubuntu/Debian:**
        ```bash
        sudo apt update
        sudo apt install tesseract-ocr
        sudo apt install tesseract-ocr-por tesseract-ocr-eng # Suporte para portugues e pacotes do inglês
        ```
    *   **macOS (Homebrew):**
        ```bash
        brew install tesseract
        brew install tesseract-lang # Instalando pacotes de linguagem
        ```
    *   **Windows:**
        Baixa o executavel em [Tesseract OCR GitHub page](https://tesseract-ocr.github.io/tessdoc/Downloads.html). Não esqueça de incluir o Tesseract no seu Path.

3.  **Instalar dependências do Python:**
    Gerar um ambiente virtual:

    ```bash
    python -m venv .venv
    source .venv/bin/activate # Para windows: `.venv\Scripts\activate`
    pip install -e .
    ```

## Uso

O script principal `main.py` deve ser rodado na linha de comando com os seguintes argumentos:

*   `--input` (obrigatório): Caminho para o arquivo de imagem ou pdf (exemplo : `imagens/imagem_1.png` ou `imagens/documento_escaneado_internet.pdf`).
*   `--output` (Opcional): Especifica como o texto deve ser processado.
    *   `cli` (Padrão): Mostra o texto no console.
    *   `txt`: Salva o texto em arquivo `.txt` na pasta `outputs/`.
    *   `both`: Mostra no console e salva em arquivo `.txt`.

### Exemplos

1.  **Extrair texto da imagem e mostrar no console:**
    ```bash
    python main.py --input imagens/imagem_1.png
    ```

2.  **Extrair o texto de documento PDF e salvar em arquivo `.txt`:**
    ```bash
    python main.py --input imagens/documento_escaneado_internet.pdf --output txt
    ```
    (Quando documentos possuirem mais de uma páginas, os textos serão salvos por página, exemplo: `documento_escaneado_internet_0.txt`, `documento_escaneado_internet_1.txt`, etc.)

3.  **Extrair texto da imagem, mostrar no console e salvar em arquivo `.txt`:**
    ```bash
    python main.py --input imagens/imagem_2.jpg --output both
    ```

## Estrutura do projeto

```
.
├── main.py                     # Aplicação principal
├── pyproject.toml              # Dependências e metadados
├── README.md                   # Documentação
├── imagens/                    # Pasta para arquivos de entrada (Imagens e PDFs)
│   ├── documento_escaneado_internet.pdf
│   ├── imagem_1.png
│   ├── imagem_2.jpg
│   └── imagem_3.jpeg
├── outputs/                    # Diretório de textos extraidos e salvos em `.txt`
│   ├── documento_escaneado_internet_0.txt
│   ├── documento_escaneado_internet_1.txt
│   ├── imagem_1.txt
│   ├── imagem_2.txt
│   └── imagem_3.txt
└── src/
    ├── __init__.py
    └── tesseract_ocr/
        ├── __init__.py
        ├── image_handler.py    # Carregamento e pré-processamento de imagens e PDFs
        └── text_extractor.py   # Extração de textos em imagens e salvamento de arquivos `.txt`
```

## Dependências

O projeto utiliza as seguinte bibliotecas em Python:

*   `numpy`
*   `pytesseract`
*   `pdf2image`
*   `opencv-python`

Essas, estão listadas em `pyproject.toml` e pode ser instaladas com `pip install -e .`.