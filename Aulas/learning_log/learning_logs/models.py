from django.db import models

class Topic(models.Model):
    # Um assunto sobre o qual o usario esta aprendendo
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Devolve uima representação em string do modelo
        return self.text