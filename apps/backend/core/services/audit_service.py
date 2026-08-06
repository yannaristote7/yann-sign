from core.models import AuditLog


def create_audit_log(
    user,
    action,
    resource,
    resource_id,
    description,
    metadata=None,
    ip_address=None,
    user_agent="",
):
    """
    Création centralisée des logs d'audit.
    """

    return AuditLog.objects.create(
        user=user,
        action=action,
        resource=resource,
        resource_id=resource_id,
        description=description,
        metadata=metadata or {},
        ip_address=ip_address,
        user_agent=user_agent,
    )