from django.db import models
import datetime


class BooksInsert(models.Model):  
    bid = models.CharField(max_length=100)  
    bname = models.CharField(max_length=500)    
    btype = models.CharField(max_length=200)
    bwriter = models.CharField(max_length=400)
    bquantity=models.IntegerField()
    bshelf=models.CharField(max_length=400)
    bcreated_at= models.DateTimeField(auto_now_add=True) 
    class Meta:  
        db_table = "booksinsert"  
    def __str__(self):
        return self.bname
