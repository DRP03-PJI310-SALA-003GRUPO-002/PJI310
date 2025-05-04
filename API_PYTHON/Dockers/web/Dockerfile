# Usa uma imagem Nginx oficial
FROM nginx:alpine

# Remove a configuração padrão do Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copia uma nova configuração
COPY nginx.conf /etc/nginx/conf.d/

# Copia os arquivos HTML para o diretório público do Nginx
COPY site/ /usr/share/nginx/html/
