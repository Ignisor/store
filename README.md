Before run server:

install django-bootstrap-form:
    > pip install django-bootstrap-form

change file: /environment/lib/python2.7/site-packages/bootstrapform/templates/bootstrapform/field.html
remove 3 lines (https://github.com/tzangms/django-bootstrap-form/blob/master/bootstrapform/templates/bootstrapform/field.html#L48):

    {% if field.auto_id %}
        <label class="control-label {{ classes.label }} {% if field.field.required %}{{ form.required_css_class }}{% endif %}" for="{{ field.auto_id }}">{{ field.label }}</label>
    {% endif %}