from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from .models import Product
from django import forms
from django.core.exceptions import ValidationError
# Create your views here.
class homePageView(TemplateView): 
    template_name='../templates/pages/home.html'
    
    


class ProductForm(forms.ModelForm):
    """ Class represents the Product form. """
    class Meta:
        model = Product
        fields = ['name', 'desc', 'price', 'category', 'quantity']
        
    def clean_price(self):
        """ Function checks if price is greater than zero. """
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError("Price must be greater than zero.")
        return price
    

class createProductView(View): 
    """ Class represents the Product Create page. """

    template_name = 'products/create.html' 
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products/create/success/')
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            
            return render(request, self.template_name, viewData) 

class showProductView(View): 
    """Class represents the Product Index page. """
    template_name = 'products/show.html'
    
    def get(self, request):
        """ Function returns the Product Index page. """
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["products"] = Product.objects.all()

        return render(request, self.template_name, viewData)

class showOneProductView(View): 
    """ Class represents the Product Show page. """

    template_name = 'products/each.html' 
    def get(self, request, id): 
        """ Function returns the Product Show page. """
        # Check if product id is valid 
        try:
            product_id = int(id)
            if product_id < 1:
                raise ValueError("Product id must be 1 or greater")
            product = get_object_or_404(Product, pk=product_id)
        except (ValueError, IndexError): 
            # If the product id is not valid, redirect to the home page
            return HttpResponseRedirect(reverse('home'))

        viewData = {}
        product = get_object_or_404(Product, pk=product_id)
        viewData["title"] = product.name + " - Online Store"
        viewData["subtitle"] =  product.name + " - Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData)
    
class deleteProductView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return redirect('showProduct')
    
    

class successProductView(TemplateView):
    template_name = 'products/created.html'
    
