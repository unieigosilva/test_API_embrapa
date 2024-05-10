from setuptools import setup, find_packages

setup(
    name='TEST_API_EMBRAPA',
    version='0.1.0',
    description='{Preencher com a descrição....}',  # Substitua isso pela descrição adequada.
    long_description=open('README.md').read(),  # Certifique-se de que você tem um README.md no seu projeto.
    author='Igor Silva',
    author_email='igor.bruno2012@gmail.com',
    url='https://github.com/unieigosilva',
    packages=find_packages(),  # Isso automaticamente encontra e inclui todos os pacotes que devem ser instalados.
    install_requires=open('requirements.txt').read().splitlines(),
    python_requires='>=3.9',  # Adapte conforme necessário, essa é uma suposição comum
    package_data={
        # Inclua quaisquer pacotes que contêm arquivos não-Python que precisam ser incluídos no pacote
        # Exemplo: 'meu_pacote': ['dados/*.data']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',  # Mudar conforme o progresso do seu projeto (Alpha, Beta, Stable)
        'Intended Audience :: Developers',
        'Natural Language :: Portuguese',
        'License :: OSI Approved :: MIT License',  # Substitua pela licença que você está usando
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering',
    ],
    entry_points={
        'console_scripts': [
            # Se o seu pacote incluir scripts executáveis ou interfaces de linha de comando, especifique-os aqui
            # Exemplo: 'nome_do_script = meu_pacote.modulo:funcao_principal'
        ]
    },
)

"""
Quando você estiver pronto para escrever a descrição e tiver todas as dependências em seu requirements.txt, simplesmente substitua os valores 
correspondentes. Certifique-se de que seu projeto tem um arquivo README.md formatado em Markdown, pois ele é referenciado para a descrição 
longa (long_description). Isso é importante para documentação e também para a apresentação do pacote em plataformas como PyPI.
"""

