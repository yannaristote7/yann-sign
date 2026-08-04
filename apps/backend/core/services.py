from core.models import AuditLog


def create_audit_log(
    *,
    user,
    action,
    resource,
    description,
    resource_id=None,
    metadata=None,
    ip_address=None,
    user_agent=""
):
    """
    Crée un enregistrement d'audit.
    """

    AuditLog.objects.create(
        user=user,
        action=action,
        resource=resource,
        resource_id=resource_id,
        description=description,
        metadata=metadata or {},
        ip_address=ip_address,
        user_agent=user_agent,
    )