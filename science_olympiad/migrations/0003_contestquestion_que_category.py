# Generated by Django 3.2 on 2022-02-18 16:33

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('science_olympiad', '0002_auto_20220201_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestquestion',
            name='que_category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('chm', 'الكيمياء'), ('mbi', 'الأحياء والكائنات'), ('phys', 'الفيزياء والذرات'), ('ast', 'الفضاء والكواكب'), ('math', 'الرياضيات والهندسة'), ('pro', 'التقنية والحاسوب')], default=1, max_length=25, verbose_name='التصنيف (يمكن اختيار أكثر من تصنيف)'),
            preserve_default=False,
        ),
    ]