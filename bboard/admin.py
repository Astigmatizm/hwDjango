from django.contrib import admin
from django.db.models import F

from bboard.models import Bb, Rubric

# user = admin4
# password = qwerty123
# email = admin@bk.ru



# def title_and_rubric(rec):
#     return f'{rec.title} ({rec.rubric.name})'

class PriceListFilter(admin.SimpleListFilter):
    title = ''
    parameter_name = 'price'
    def lookups(self, request, model_admin):
        return (
            ('low', 'Низкая цена'),
            ('medium', 'Средняя цена'),
            ('high', 'Высокая цена'),
        )
    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(price__lt=500)
        if self.value() == 'medium':
            return queryset.filter(price__lt=500, price__lte=5000)
        if self.value() == 'high':
            return queryset.filter(price__gt=5000)




@admin.register(Bb)
class BbAdmin(admin.ModelAdmin):
    # list_display = ('title', 'content', 'price', 'published', 'rubric')
    # list_display = ('title_and_price', 'content', 'price', 'published', 'rubric')
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    # list_display = (title_and_rubric, 'content', 'price', 'published', 'rubric')
    # list_display_links = ('title', 'content')
    # search_fields = ('title', 'content')

    # @admin.display(description='Название и рубрика')
    # def title_and_rubric(self, rec):
    #     return f'{rec.title} ({rec.rubric.name})'

    def query_set(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(is_hidden=False)

    search_fields = ('title', 'content')
    search_help_text = 'Поиск по названиям товаров и содержимому'

    list_filter = ('title', 'rubric__name')

    # Набор полей внутри записей
    # fields = ('title', 'price', 'content')
    # fields = (('title','price'),'content')
    fields = ('title', 'price', 'content', 'published')
    readonly_fields = ('published', )
    # exclude = ('rubric', 'kind')

    @admin.action(description='Уменьшить цену вдвое')
    def discount(self, request, queryset):
        f = F('price')
        for rec in queryset:
            rec.price = f / 2
            rec.save()
        self.message_user(request, 'Действие выполнено')
    
    actions = (discount,)
class BbInLine(admin.StackedInline):
    model = Bb
    extra = 1
    # can_delete = True
    max_num = 3


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'order')
    inlines = (BbInLine, )




# admin.site.register(Bb, BbAdmin)
# admin.site.register(Rubric, RubricAdmin)

