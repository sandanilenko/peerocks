# Generated by Django 3.2.6 on 2021-08-18 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.classes


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('next', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prev_step', to='recipes.cookstep')),
                ('prev', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='next_step', to='recipes.cookstep')),
            ],
            options={
                'verbose_name': 'Шаг приготовления блюда',
                'verbose_name_plural': 'Шаги приготовления блюд',
                'db_table': 'recipes_cook_step',
            },
            bases=(utils.classes.ProjectClass, models.Model),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'db_table': 'recipes_recipe',
            },
            bases=(utils.classes.ProjectClass, models.Model),
        ),
        migrations.CreateModel(
            name='UserRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe', verbose_name='Рецепт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Рецепт пользователя',
                'verbose_name_plural': 'Рецепты пользователей',
                'db_table': 'recipes_user_recipe',
            },
            bases=(utils.classes.ProjectClass, models.Model),
        ),
        migrations.CreateModel(
            name='RecipeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Количество')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product', verbose_name='Продукт')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe', verbose_name='Рецепт')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.unit', verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Продукт используемый в рецепте',
                'verbose_name_plural': 'Продукты используемые в рецепте',
                'db_table': 'recipes_recipe_product',
            },
            bases=(utils.classes.ProjectClass, models.Model),
        ),
        migrations.CreateModel(
            name='RecipeFoodIntake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_intake', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.foodintake')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
            options={
                'verbose_name': 'Принадлежность рецепта к приему пищи',
                'verbose_name_plural': 'Принадлежность рецептов к приемам пищи',
                'db_table': 'recipes_recipe_food_intake',
            },
            bases=(utils.classes.ProjectClass, models.Model),
        ),
        migrations.CreateModel(
            name='CookStepRecipeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Количество')),
                ('cook_step', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipes.cookstep', verbose_name='Шаг приготовления блюда')),
                ('recipe_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipes.recipeproduct', verbose_name='Продукт используемый в рецепте')),
            ],
            options={
                'verbose_name': 'Продукт используемый на шаге приготовления блюда',
                'verbose_name_plural': 'Продукты используемые на шаге приготовления блюда',
                'db_table': 'recipes_cook_step_recipe_product',
            },
            bases=(utils.classes.ProjectClass, models.Model),
        ),
        migrations.AddField(
            model_name='cookstep',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe'),
        ),
    ]
