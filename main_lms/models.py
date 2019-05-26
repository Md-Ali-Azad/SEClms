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

class StuInsert(models.Model):  
    sid = models.CharField(max_length=100)  
    sname = models.CharField(max_length=500)    
    sdept = models.CharField(max_length=200)
    ssession = models.CharField(max_length=400)
    saddress=models.CharField(max_length=400)
    scontact=models.CharField(max_length=400)
    semail=models.EmailField(max_length=400)
    sgender=models.CharField(max_length=50)
    screated_at= models.DateTimeField(auto_now_add=True) 
    class Meta:  
        db_table = "stuinsert"  
    def __str__(self):
        return self.sname

class StuDept(models.Model):
    cdept = models.CharField(max_length=400)
    cscreated_at= models.DateTimeField(auto_now_add=True)
    class Meta:  
        db_table = "studept"  
    def __str__(self):
        return self.cdept
class StuSession(models.Model):
    csession = models.CharField(max_length=400)
    cscreated_at= models.DateTimeField(auto_now_add=True)
    class Meta:  
        db_table = "stusession"  
    def __str__(self):
        return self.csession

class BorrowInsert(models.Model):  
    brsid = models.CharField(max_length=100)  
    brsname = models.CharField(max_length=500)    
    brbname = models.CharField(max_length=500)
    brdate= models.DateField(auto_now_add=True)
    brreturn= models.DateField() 
    class Meta:  
        db_table = "borrowinsert"  
    def __str__(self):
        return self.brsname

class HeaderColor(models.Model):
    hcolor = models.CharField(max_length=500)
    class Meta:  
        db_table = "headercolor"  
    def __str__(self):
        return self.hcolor