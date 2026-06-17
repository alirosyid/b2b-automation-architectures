class DatabaseProvisioner:
    def __init__(self, db_connection_mock):
        self.db = db_connection_mock

    def provision_new_tenant(self, client_name):
        sanitized_name = "".join([c for c in client_name.lower() if c.isalnum()])
        schema_name = f"tenant_{sanitized_name}"
        
        print(f"[Data] Initiating Zero-Touch Provisioning for schema: {schema_name}")
        
        # SQL Execution commands
        sql_commands = [
            f"CREATE SCHEMA IF NOT EXISTS {schema_name};",
            f"SET search_path TO {schema_name};",
            "CREATE TABLE interactions (id SERIAL PRIMARY KEY, payload JSONB, created_at TIMESTAMP DEFAULT NOW());"
        ]
        
        for query in sql_commands:
            print(f"Executing: {query}")
            # self.db.execute(query)
            
        print(f"[Data] Schema {schema_name} successfully isolated and provisioned.")
        return schema_name

if __name__ == "__main__":
    provisioner = DatabaseProvisioner("mock_conn")
    provisioner.provision_new_tenant("Stark Industries")
