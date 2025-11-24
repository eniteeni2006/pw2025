Alterações aplicadas - comentários e posts

Data: 24-11-2025

Resumo:
- Post.titulo: aumentei o limite para 255 caracteres (antes 50).
- Post.texto: removi o limite (TextField sem max_length) para permitir textos longos.
- Comentario.comentario: trocado para TextField() para permitir comentários longos.
- Validação servidor: `comentar_post` agora valida:
  - comentário não pode ser vazio (após strip)
  - comentário não pode exceder 5000 caracteres (retorna mensagem de erro)
- Frontend: `post_detail.html` recebeu contador de caracteres (0/5000) e bloqueio do botão de submit quando o comentário está vazio ou excede o limite. Também impede envio de comentário com apenas espaços.
- Otimizações anteriores: select_related nas ListViews e cálculo de média via aggregate (veja commits anteriores).

Como testar:
1) Suba o servidor:
   python manage.py runserver 127.0.0.1:8000
2) Abra um post e tente:
   - Enviar comentário vazio -> deverá exibir mensagem de erro e não criar comentário.
   - Enviar comentário apenas com espaços -> impedido no frontend e backend.
   - Enviar comentário muito grande (>5000 bytes) -> backend retornará mensagem de erro.
   - Enviar comentário válido -> sucesso.
3) Rodar testes:
   python manage.py test -v 2

Reversão:
- Reverter alterações nos arquivos alterados (`paginas/models.py`, `paginas/views.py`, templates) e executar:
  python manage.py makemigrations paginas
  python manage.py migrate

Observações:
- Não foi adicionada sanitização HTML específica; as templates do Django escapam conteúdo por padrão. Se você precisa permitir HTML seguro, considere usar uma biblioteca como `bleach` para sanitização.
- Se quiser mudar o limite de 5000 caracteres, edite a constante `MAX_COMMENT_LENGTH` em `paginas/views.py` e o atributo `maxlength` no `post_detail.html`.
