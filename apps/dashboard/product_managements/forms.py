from django.forms import ModelForm
from apps.main.product_managements.models  import ProductManagement
from apps.main.products.models import Product


class ProductManagementForm(ModelForm):
    class Meta:
        model = ProductManagement
        fields = ['product_cod', 'product_name', 'product_unit', 'operation_type','product_quantity','product_unitary_amount','is_spare_part','is_maintenance']
    
    """
    def clean(self):
        super(ProductForm, self).clean()
        product_quantity = self.cleaned_data.get('product_quantity')
        product_unitary_amount = self.cleaned_data.get('product_unitary_amount')
        product_total_ammount = self.cleaned_data.get('product_total_amount')

        if product_quantity < 0:
            self._errors['product_quantity'] = self.error_class([
                'Cantidad negativa'])  
        if product_unitary_amount < 0:
            self._errors['product_unitary_amount'] = self.error_class([
                'Cantidad negativa'])
        if product_total_amount < 0:
            self._errors['product_total_amount'] = self.error_class([
                'Cantidad negativa'])
    """



    """
    def clean(self):
        super(ProductForm, self).clean()
        quantity = self.cleaned_data.get('total_product_quantity')

        if quantity < 0:
            self._errors['total_product_quantity'] = self.error_class([
                'Cantidad negativa'])  
    """