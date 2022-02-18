from django.core import serializers
from django.contrib.admin.utils import NestedObjects
from django.db import models, transaction, router

# assuming `obj` is the model instance for deletion:

objs = [obj]
using = router.db_for_write(obj._meta.model)
collector = NestedObjects(using=using)
collector.collect(objs)


def get_objects_callback():
    for qs in collector.data.values():
        for obj in qs:
            yield obj


output_format = "json"
with open("deleted-objects.json", "w") as f:
    serializers.serialize(output_format, get_objects_callback(), indent=2,
            use_natural_foreign_keys=True,
            use_natural_primary_keys=True,
            stream=f)