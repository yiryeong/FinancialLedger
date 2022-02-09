from django.db import models


class Group(models.Model):
    # group_name = models.CharField(max_length=45)

    class meta:
        db_table = 'auth_group'
