from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=50)
    time = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='question')
    question = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'media/question/')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=300)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    checked = models.BooleanField(default=False)
    image = models.ImageField(upload_to = 'media/answer/')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer
