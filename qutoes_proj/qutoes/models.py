from django.db import models

# Create your models here.

class QutoesCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    


class Qutoes(models.Model):
    author = models.CharField(max_length = 50)
    qutoes = models.TextField()

    # def __str__(self):
    #     return self.author

    qutoes_category = models.ForeignKey(
        'QutoesCategory',
        on_delete=models.CASCADE
    )

    def __str__(self):
        if len(self.qutoes)>50:
            return self.qutoes[:50]+"..."
        else:
            return self.qutoes



