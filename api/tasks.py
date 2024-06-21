# Create your tasks here

from celery import shared_task


@shared_task(queue='status_pagamento_pedido')
def atualizar_status_pagamento_queue(id_pedido: str, status: str):
    return True


