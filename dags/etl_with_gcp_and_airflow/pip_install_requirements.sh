'''
### Windows ###
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py                             # Baixar diretório do pip
python get-pip.py                                                                   # Instalar o pip
python -m pip install --upgrade pip                                                 # Atualizar o pip
py -m pip freeze > requirements.txt                                                 # Um jeito simples de criar o seu próprio arquivo de depências
py -m pip install -r requirements.txt                                               # Instalar dependências
'''

'''
### Linux ###
sudo apt update                                                                     # Atualiza o ambiente
sudo apt install python3-pip                                                        # Instalar a versão recente do pip para python 3
sudo pip3 install --upgrade pip                                                     # Atualizar o pip
python3 -m pip freeze > requirements.txt                                            # Um jeito simples de criar o seu próprio arquivo de depências
# Garante instalação de dependências que o linux pode não identificar
pip install google-play-scraper==1.0.2
pip install google-api-core==2.3.2
pip install google-auth==2.3.3
pip install google-auth-oauthlib==0.4.6
pip install google-cloud-bigquery==2.31.0
pip install google-cloud-bigquery-storage==2.10.1
pip install google-cloud-core==2.2.1
pip install google-cloud-storage==1.43.0
pip install google-crc32c==1.3.0
pip install google-play-scraper==1.0.2
pip install google-resumable-media==2.1.0
pip install googleapis-common-protos==1.54.0
pip install pandas==1.3.5
pip install pandas-gbq==0.16.0
sudo apt-get install libcairo2-dev
python3 -m pip install -r requirements.txt                                          # Instala as dependências necessárias
'''