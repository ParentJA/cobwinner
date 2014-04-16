from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    preferences = models.ManyToManyField('CustomerPreference', blank=True, null=True)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.email)


class CustomerPreference(models.Model):
    name = models.SlugField(max_length=150)
    display_name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.display_name


class Bank(models.Model):
    name = models.SlugField(max_length=150)
    display_name = models.CharField(max_length=150)
    branch = models.CharField(max_length=10)
    branch_id = models.CharField(max_length=50, blank=True, null=True)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)

    def __unicode__(self):
        return '%s (%s: %s, %s)' % (self.display_name, self.branch, self.city, self.state)


class Prize(models.Model):
    name = models.SlugField(max_length=150)
    display_name = models.CharField(max_length=150)
    code = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, blank=True, null=True)
    date_time_redeemed = models.DateTimeField(blank=True, null=True)
    employee = models.CharField(max_length=150, blank=True, null=True)

    def __unicode__(self):
        return '%s (%s)' % (self.display_name, self.code)