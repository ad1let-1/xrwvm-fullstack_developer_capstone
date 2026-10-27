from django.db import migrations


CAR_MODELS = [
    ('NISSAN', 'Pathfinder'), ('NISSAN', 'Qashqai'), ('NISSAN', 'XTRAIL'),
    ('Mercedes', 'A-Class'), ('Mercedes', 'C-Class'), ('Mercedes', 'E-Class'),
    ('Audi', 'A4'), ('Audi', 'A5'), ('Audi', 'A6'),
    ('Kia', 'Sorrento'), ('Kia', 'Carnival'), ('Kia', 'Cerato'),
    ('Toyota', 'Corolla'), ('Toyota', 'Camry'), ('Toyota', 'Kluger'),
]


def seed_cars(apps, schema_editor):
    CarMake = apps.get_model('djangoapp', 'CarMake')
    CarModel = apps.get_model('djangoapp', 'CarModel')
    countries = {'NISSAN': 'Japan', 'Mercedes': 'Germany', 'Audi': 'Germany',
                 'Kia': 'South Korea', 'Toyota': 'Japan'}
    for make_name, model_name in CAR_MODELS:
        make, _ = CarMake.objects.get_or_create(
            name=make_name, defaults={'country_of_origin': countries[make_name]})
        CarModel.objects.get_or_create(car_make=make, name=model_name,
                                       defaults={'year': 2026})


class Migration(migrations.Migration):
    dependencies = [('djangoapp', '0001_initial')]
    operations = [migrations.RunPython(seed_cars, migrations.RunPython.noop)]
