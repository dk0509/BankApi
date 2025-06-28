import csv
import os
from django.core.management.base import BaseCommand
from banks.models import Bank,Branch

class Command(BaseCommand):
    help = 'Load banks from CSV file'

    def handle(self, *args, **kwargs):
        csv_path = os.path.join('banks','data','bank_branches.csv')
        bank_map={}
        branch_list=[]

        with open(csv_path,newline='',encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                bank_id=int(row['bank_id'])
                bank_name=row['bank_name'].strip()

                if bank_id not in bank_map:
                    bank_map[bank_id] = Bank(bank_id=bank_id, name=bank_name)
        
        Bank.objects.bulk_create(bank_map.values(),ignore_conflicts=True)

        bank_objs=Bank.objects.in_bulk(field_name='bank_id')

        count=0
        with open(csv_path,newline='',encoding='utf-8') as csvfile:
            reader=csv.DictReader(csvfile)

            for row in reader:
                 branch_list.append(Branch(
                    ifsc=row['ifsc'],
                    bank=bank_objs[int(row['bank_id'])],
                    branch=row['branch'],
                    address=row['address'],
                    city=row['city'],
                    district=row['district'],
                    state=row['state']
                ))
                 count+=1
        
        Branch.objects.bulk_create(branch_list, batch_size=1000, ignore_conflicts=True)
            
        self.stdout.write(self.style.SUCCESS(f'Imported {count} branches. '))