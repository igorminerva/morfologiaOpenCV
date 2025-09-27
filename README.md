# 🔬 Morphology with OpenCV

Uma aplicação interativa feita em **Python + Streamlit** que permite carregar imagens do seu computador, aplicar operações de **morfologia matemática** com **OpenCV** e baixar o resultado processado.

## 🚀 Funcionalidades

* Upload de imagens (`.png`, `.jpg`, `.jpeg`).
* Escolha de operações morfológicas:

  * Erosão
  * Dilatação
  * Abertura (Opening)
  * Fechamento (Closing)
  * Gradiente
  * Top-hat
  * Black-hat
* Ajuste de parâmetros:

  * Tamanho do kernel (1 a 15).
  * Número de iterações (1 a 5).
* Visualização da imagem original e do resultado.
* Download da imagem processada em **PNG**.

## 🛠️ Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/morfologia-opencv.git
cd morfologia-opencv
pip install streamlit opencv-python pillow numpy
```

## ▶️ Como Executar

No terminal, rode:

```bash
streamlit run main.py
```

O Streamlit abrirá automaticamente no navegador em:
👉 [http://localhost:8501](http://localhost:8501)

## 📸 Exemplo de Uso

1. Carregue uma imagem (exemplo: formas geométricas em preto e branco).
2. Escolha "Erosão" e ajuste o kernel para 5x5.
3. Veja como os objetos encolhem.
4. Baixe o resultado para salvar no seu PC.

## 📚 Referências

* [Documentação OpenCV - Morfologia](https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html)
* [Streamlit Docs](https://docs.streamlit.io/)
* [Mathematical Morphology - Wikipedia](https://en.wikipedia.org/wiki/Mathematical_morphology)

---

✨ Desenvolvido para fins de estudo de **Processamento de Imagens** e **Morfologia Matemática**.

