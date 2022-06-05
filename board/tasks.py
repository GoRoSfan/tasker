from celery import shared_task


@shared_task
def update_terms_list(description_pk):
    from board.models import Description, Term
    description = Description.objects.get(pk=description_pk)
    terms = Term.objects.values('id', 'name').all()

    description.terms.set([term['id'] for term in terms if term['name'] in description.text])

    description.save()

    return 'Terms list was successfully updated.'
