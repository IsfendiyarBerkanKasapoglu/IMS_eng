from django.shortcuts import get_object_or_404, render, redirect
from .models import Inventory
from django.contrib.auth.decorators import login_required
from .forms import AddInventoryForm, UpdateInventoryForm

@login_required
def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {
        "title": "Inventory List",
        "inventories": inventories
    }
    return render(request, "inventory/inventory_list.html", context=context)

@login_required
def per_product_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'inventory': inventory
    }

    return render(request, "inventory/per_product.html", context=context)

@login_required
def add_product(request):
    add_form = AddInventoryForm()
    if request.method == "POST":
        add_form = AddInventoryForm(data=request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('/')
  
    return render(request, "inventory/inventory_add.html", {"form": add_form})

@login_required
def delete_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    return redirect("/inventory")


@login_required
def update_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        updateForm = UpdateInventoryForm(data=request.POST)
        if updateForm.is_valid():
            inventory.Unique_Number = updateForm.data['Unique_Number']
            inventory.Product_Name = updateForm.data['Product_Name']
            inventory.Product_Type = updateForm.data['Product_Type']
            inventory.Cost = updateForm.data['Cost']
            inventory.Stock = updateForm.data['Stock']
            inventory.Stock_Date = updateForm.data['Stock_Date']
            inventory.save()
            return redirect(f"/inventory/per_product/{pk}")
            
    else:
        updateForm = UpdateInventoryForm(instance=inventory)

    context = {"form": updateForm}
    return render(request, "inventory/inventory_update.html", context=context)
