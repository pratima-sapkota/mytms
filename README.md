## Create a Django application named mytms:
    - connect it to PostgreSQL for persistence, 
    <!-- - Redis for caching, and  -->
    <!-- - Celery for concurrency. -->

## Create the following Django Models: 
    - Campaign, 
    - Member, 
    - Task.
  
## Create a Django superuser to access the Django admin page (rename the default admin URL) and register these models.
    - Campaign: id (UUID) and name.
    - Member: role (trainer / lead), email (Primary Key) and full name
    - Task: id (UUID), status (choices, simple life cycle statuses), name, and score.
  
## Models considerations:
    - Models should have auto_add and auto_add_now fields for timestamps, give them the proper name.
    - Models must have help_texts definitions, __str__ method, ordering, and verbose for plural. Use docstrings to provide short model’s descriptions.
    - Propose a way to link those models based on the business logic: Campaigns are a group of trainers, trainers submit tasks, leads review tasks and leads can manage trainer’s campaign group associations.
    <!-- - Create a management command to create dummy data for all models. -->
    - Create three CRUD DRF endpoints: for Campaigns, Members and Tasks.
