import xadmin

from .models import (ComponentCategory, ComponentCategoryTab,
                     Component, ComponentImage)
# from .models import IndexAd


class ComponentCategoryAdmin(object):
    list_display = ['name', 'category_type', 'parent_category', 'add_time']
    list_filter = ['category_type', 'parent_category', 'name']
    search_fields = ['name']


class ComponentTabAdmin(object):
    list_display = ['category', 'image', 'name', 'desc']

    def get_context(self):
        context = super(ComponentTabAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = ComponentCategory.objects.filter(
                category_type=1)
        return context


class ComponentAdmin(object):
    list_display = ['name', 'click_num', 'fav_num', 'collect_num', 'easy_to_use',
                    'component_brief', 'component_desc', 'is_new', 'is_hot', 'add_time']
    search_fields = ['name']
    list_editable = ['is_hot']
    list_filter = ['name', 'click_num', 'fav_num', 'collect_num', 'easy_to_use',
                   'is_new', 'is_hot', 'add_time', 'category__name']
    style_fields = {'component_desc': 'ueditor'}

    class ComponentImagesInline(object):
        model = ComponentImage
        exclude = ['add_time']
        extra = 1
        style = 'tab'

    inlines = [ComponentImagesInline]


xadmin.site.register(ComponentCategory, ComponentCategoryAdmin)
xadmin.site.register(Component, ComponentAdmin)
xadmin.site.register(ComponentCategoryTab, ComponentTabAdmin)
