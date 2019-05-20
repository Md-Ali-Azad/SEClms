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


class BooksType(models.Model):
    cbtype = models.CharField(max_length=400)
    cbcreated_at= models.DateTimeField(auto_now_add=True)
    class Meta:  
        db_table = "bookstype"  
    def __str__(self):
        return self.cbtype



class BooksShelf(models.Model):
    cbshelf = models.CharField(max_length=400)
    cbcreated_at= models.DateTimeField(auto_now_add=True)
    class Meta:  
        db_table = "booksshelf"  
    def __str__(self):
        return self.cbshelf

class HeaderColor(models.Model):
    hcolor = models.CharField(max_length=500)
    class Meta:  
        db_table = "headercolor"  
    def __str__(self):
        return self.hcolor