from django.db import IntegrityError


class Repository:

    def __init__(self, model):
        self.model = model

    def save(self, models):
        result = []
        for model_data in models:
            try:
                result.append(self.model.objects.get_or_create(**model_data))
            except IntegrityError:
                # just skip the bad entries and continue
                continue

        return result

    def get(self):
        return list(self.model.objects.all())
