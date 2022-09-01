from django.db import models

class Inventory(models.Model):
    Unique_Number = models.CharField(max_length=100, null=False, blank=False)
    Product_Name = models.CharField(max_length=100, null=False, blank=False)
    Product_Type = models.CharField(max_length=90, null=False, blank=False)
    Cost = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    Stock = models.IntegerField(null=False, blank=False)
    Stock_Date = models.DateField()


    def __str__(self) -> str:
        return self.Unique_Number