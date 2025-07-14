from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE) 
    #cascade=>if author is deleted ,post related to author is also deleted
    created_at=models.DateTimeField(auto_now_add=True)
    #autonowadd=true => present date and time haldincha but for first time only
    updated_at=models.DateTimeField(auto_now=True)
    #autonow=true =>harek choti date and time add huncha
    published_at=models.DateTimeField(null=True,blank=True)
    #null,blank=true ko matlab kei pani nahalda pani huncha

    def __str__(self):
        return self.title
    
    #1-1 relationship 
    # 1 user can have only one profile
    # 1 profile is associated with only 1 user
    #OneToOneField()=>Any Model

    #1 to many relationship
    #1 user can add n post 
    #ForeignKey() manyko sidema use garcham , here post many model ho

    #many to many relationship
    #ManytoManyField()
