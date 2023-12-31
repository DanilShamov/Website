from django import template
from blogs.models import Category, Post

register = template.Library()

#@register.simple_tag()
#def get_cotegories():
#   """Вывод всех категорий"""
#   return Category.objects.all()


@register.inclusion_tag('blogs/include/tags/top_menu.html')
def get_categories():
    category = Category.objects.all()#.order_by("name")#?????
    return {"list_category": category}

@register.inclusion_tag('blogs/include/tags/recipes_tag.html')
def get_last_posts():
    posts = Post.objects.select_related("category").order_by("-id")[:5]
    return {"list_last_post": posts}


def get_all_categories():
    return Category.objects.all()

@register.simple_tag()
def get_list_category():
    """ вывод все категорий"""
    return get_all_categories()