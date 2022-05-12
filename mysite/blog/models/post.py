from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Post(models.Model): # essa é a função que cria as tabelas no banco de dados do djanto.
    title = models.CharField(max_length= 200, unique= True) # Tabela titulo do post
    slug = models.SlugField(max_length= 200, unique= True) # Tabela slug do post
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts') # Tabela nome do criado do post
    updated_on = models.DateTimeField(auto_now= True) # Tabela quando foi atualizado o post
    content = models.TextField() # Tabela texto do post
    created_on = models.DateTimeField(auto_now_add= True) # Tabela quanto o post foi criado
    status = models.IntegerField(choices=STATUS, default=0) # Tabela status do post se ele foi criado ou esta em rescunho


    class Meta:
        ordering = ['-created_on'] # Ordem de apresentação do post


    def __str__(self):
        return self.title # Nome que vai aparecer no admin do sql do djanto

