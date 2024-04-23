from django import template

register = template.Library()


@register.filter
def multiply(value, multiplier):
    try:
        # Safely cast to float to handle fractional multipliers
        return float(value) * float(multiplier)
    except (ValueError, TypeError):
        return 0
