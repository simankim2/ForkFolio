from django import template

register = template.Library()


@register.filter
def multiply(value, multiplier):
    try:
        # Safely cast to float to handle fractional multipliers
        return float(value) * float(multiplier)
    except (ValueError, TypeError):
        return 0


@register.filter(name='starify')
def starify(value):
    """Converts a numerical star rating into a string of star characters."""
    stars_full = int(value)
    stars = '★' * stars_full + '☆' * (5 - stars_full)
    return stars
