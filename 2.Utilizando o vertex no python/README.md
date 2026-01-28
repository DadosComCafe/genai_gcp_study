# Utilizando o Vertex no Python
Neste ponto é esperado que haja criado um projeto na gcp, e a api do vertex esteja habilitada, e que o arquivo json da sua service account, tenha sido gerado.

Este arquivo json, que deve ser omitido no repositório através do .gitignore, contem informações sensíveis referentes ao projeto. O arquivo deve possuir a seguinte forma:

{
  "type": "service_account",\
  "project_id": "genai-gcp-study",\
  "private_key_id": "e1f8b9215a5b1a1b9c48c3cd9b103ef7a68462c2",\
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQC3GZTpBLkYLKyX\no357LgCQKqQViFmKyH1MWi0hwf8FPv9s0jFNiDek+7vq0tC2mSf+K36+v5458qr6\nOPVUdA/vWU4Mq/q5r83Aw/SGpZZAAyPU6l67p0qDTtzKd69Ry/tumb/9BDpJcC7F\ncZGol1MR3wyf/KzTCoaQyWLyPTT7ZFCcGSORzlak3OQrBPAEqfG6VdtxE0C2pXlW\nodt9xrbIEgZbTzcnnoP01YImNq/k64OdWzBIKk3rJLSz7uHy/YWDtWNwyai9YUHE\ndoi1GcpdTu4ZghrV0pmeuO5RvW1o71g9KVkra7SnwgGA6NFh4VXDuBPbGtY5WAve\n9kex1fsTAgMBAAECgf8w/idaMmlUjp+f859kVmrQKJi/KjzLZdohE///iGk0fiba\nd2O52zkIbFNcAgzWzyRkXj8LyzoLR2N4kMUUU/nvkXXQ7jOoe+ISMly7qpMJjc2I\nqy2uCJVnjTKG+n9u46XjckBs8zSlcd8R9dGDyvnvTj+Sj4mu7qITG8/eAYKrwTax\n4I87CIzSJ6ZbojYRhV3FSUkc66ea5eb5Q/wQfCv3AQK+IjHPSi0GdA6l+4nSQc5p\ne0oah/w+TXSexKyAuSJEUnvd9kvbASmNGUCv3fYJYwiLqU5CzkkEnQ8eD0xttBfp\nh0fbulam5SjvfrxRaw3b0pHyYZrGFFOpXQGuRqUCgYEA+tPlMpuAkL9y7hCFKZYv\nP6MasHY3EY3uqT1J06svuNn2gqPREtHq2jGleHRRzdM4ZDjgtVXOOmwEBG5B9y0b\ntu6b3MG/BqvqwOgfm1PnPnynkl5phTwIBwHSYSoYiBhlMn98U1j8HaWdVDt9YJKI\nZeiXaA1I8O596rdS3BwtWZ0CgYEAuuAnx3MnWg+gQqsxCPJIfK4ExJUvRXyawaEg\nIMAEW4xIc9iWqxY6Qc/I9MKQGP3o1eJ328vJ/epubUpx5CdvT43KG3cvZRXxw+wu\njQNRwm1eOHrV3sRaSIbbDTni38CmGDpq5nqUOgbgPcmDF9CkKL+PL3gLoXFnxLE0\niy+yoG8CgYBa4eAQACwLRnMcMzwsn1ArXKvU+GBnqeepxp0zZrl53u/k0fp1OT5B\nJO/xvyPM0hWCquEwkxCQNocWG+Um7F84Xyh2SnUus6fxkamyHCqTh5MoA7F0JxY5\ng714m0ocNcqlC3A+uuVO0K060ftRvIZTdn01pGqjcaaKHzaUrlj4OQKBgGxq++kl\nD+GaSzoio9Iy7ocXVsDOZJyFzCsmVcNqY5zRaH99WvxrauUfrdECyCMXvGvKdgtY\n0hm0VtilZioeDuAyvNzuatrUvm0Sq3c4Q8jvNsjByy7w8Ag/5PppaQyzcimASuDo\noPKBZruyG5JHg9X4PRQnK2hAqRleTcOqqpGVAoGAJYBz5Qnzcn/DC/wR4xFK5lf9\nEBmfSEqUk6D7ntogHL0y+VmLtGiEPNFGCkaePiuI1dT0RrcciFB3NiA2qPf8La66\nMdvRhrf6geZydJv6uTf8+a48hmhoZH5Hsn3FY6jcGxwPd1bOARNma4MB6uOmdyzN\nxetnUNG2hBzoZjrFPcQ=\n-----END PRIVATE KEY-----\n",\
  "client_email": "vertex-ai-python-user@genai-gcp-study.iam.gserviceaccount.com",\
  "client_id": "112982116413362607715",\
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",\
  "token_uri": "https://oauth2.googleapis.com/token",\
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",\
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/vertex-ai-python-user%40genai-gcp-study.iam.gserviceaccount.com",\
  "universe_domain": "googleapis.com"\
}

# Como executar
- ## 1. Clone o repositório:
    - git clone https://github.com/DadosComCafe/genai_gcp_study

- ## 2. Configure o ambiente e instale as dependências do python
    - cd 2.Utilizando o vertex no python/hello_world_vertex
    - uv sync

- ## 3. Variáveis de ambiente
    - Utilize o arquivo .env_sample, para criar um arquivo .env que possua as mesmas chaves
    - Cole aqui, o arquivo .json com as credenciais referentes a sua service-account.
    - Renomeie o arquivo para __credentials.json__
    - Carregue as variávies executando o __env.sh__:
        - source env.sh

- ## 4. Finalmente, execute main.py
    - uv run main.py