from urllib.parse import quote
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Shop, Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['icon_img', 'name', 'is_public']
    list_display_links = ['name'] # 이름에 링크 걸기
    list_filter = ['is_public']
    search_fields = ['name']

    def icon_img(self, category): # admin에서 아이콘 보여주기
        if category.icon:
            img_tag = '<img src="{}" width="72" height="72"; />'
            return mark_safe(img_tag.format(category.icon.url))
        return None


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'address_link']
    list_display_links = ['name']
    list_filter = ['category']

    def address_link(self, shop):
        if shop.address:
            url = 'https://map.naver.com/?query=' + quote(shop.address)
            return mark_safe('<a href="{}" target="_blank">{}</a>'.format(url, shop.address))
        return None
    address_link.short_description = '주소(네이버지도)'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['shop', 'name']
    list_display_links = ['name']
    list_filter = ['shop']
    search_fields = ['name']

# admin.site.register([Shop, Item])
