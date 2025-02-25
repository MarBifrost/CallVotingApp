class AuthDatabaseRouter:
    """
    Directs authentication-related models to 'auth_db' and everything else to 'default'.
    """

    auth_models = {'customuser', 'group', 'permission', 'contenttype', 'session'}

    def db_for_read(self, model, **hints):
        """ Reads from auth_db if model is authentication related """
        if model._meta.model_name in self.auth_models:
            return 'auth_db'
        return 'default'

    def db_for_write(self, model, **hints):
        """ Writes to auth_db if model is authentication related """
        if model._meta.model_name in self.auth_models:
            return 'auth_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """ Allow relations only within the same database """
        db_set = {'auth_db', 'default'}
        if {obj1._state.db, obj2._state.db}.issubset(db_set):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """ Ensure auth models only migrate to 'auth_db' """
        if model_name in self.auth_models:
            return db == 'auth_db'
        return db == 'default'
