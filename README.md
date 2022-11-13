<img src="https://user-images.githubusercontent.com/98171057/177011197-5763bda7-fe1a-4c03-b782-3b2f6f1f2cea.png" min-width="400px" max-width="400px" width="400px" align="right" alt="Computador iuriCode">

### <h1 align="center">`<>Descomplicando a Criação de pacotes de-processamento de imagens em Python - Unimed-BH</>` </h1> 

<h2> Digital Innovation One

Desafios Avançado Python - Unimed BH

Bootcamp  Geração Tech Unimed-BH - Ciência de Dados</h2>

<h3> Tecnologias que foram utilizadas: </h3>

![Python](https://img.shields.io/badge/-Python-white?style=flat&logo=python)

##
<h4> Descomplicando a criação de pacotes de processamento de imagens em Python  </h4>

<p> Neste projeto você aprenderá a criar o seu primeiro pacote de processamento de imagens e disponibilizá-lo no repositório Pypi. Assim você pode reutilizá-lo e compartilhá-lo facilmente com outras pessoas. </p>


## Image_Processing

The package "image_processing-test" is used to:

-   Processing:

    -   Histogram matching;
    -   Structural similarity;
    -   Resize image;

-   Utils:
    -   Read image;
    -   Save image;
    -   Plot image;
    -   Plot result;
    -   Plot Histogram;

---

## Installation

-   [x] Instalação das últimas versões de "setuptools" e "wheel"

```
py -m pip install --upgrade pip
py -m pip install --user setuptools wheel twine
```

-   [x] Tenha certeza que o diretório no terminal seja o mesmo do arquivo "setup.py"

```
py setup.py sdist bdist_wheel
```

-   [x] Após completar a instalação, verifique se as pastas abaixo foram adicionadas ao projeto:

    -   [x] build;
    -   [x] dist;
    -   [x] image_processing_test.egg-info.

-   [x] Basta subir os arquivos, usando o Twine, para o Test Pypi:

```
py -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

-   [x] Após rodar o comando acima no terminal, será pedido para inserir o usuário e senha. Feito isso, o projeto estará hospedado no Test Pypi.hospedá-lo no Pypi diretamente.
        Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
pip install python-pacotes-processamento-imagens
```

## Local Installation

-   [x] Instalação de dependências

```
pip install -r requirements.txt
```

-   [x] Instalção do Pacote

Use o gerenciador de pacotes `pip install -i https://test.pypi.org/simple/ image-processing-test `para instalar image_processing-test

```bash
pip install image-processing-test
```

---

