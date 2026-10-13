import json

from pydbzengine import DebeziumEngine, BasePythonChangeHandler

class MyHandler(BasePythonChangeHandler):
    def handleJsonBatch(self, records):
        for record in records:
            val_str = record.value()
            if val_str:
                data = json.loads(str(val_str))
                payload = data.get("payload", {})
                
                op = payload.get("op")
                before = payload.get("before")
                after = payload.get("after")
                
                print(f"""
                      {op}
                      before: {before}
                      after: {after}""")

props = {
    # 1. Name of the engine
    "name": "my-postgres-engine",
    
    # 2. Connector and database config
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "database.hostname": "localhost",
    "database.port": "5432",
    "database.user": "postgres",
    "database.password": "secret",
    "database.dbname": "mydb",
    "topic.prefix": "my-cdc-stream",
    "plugin.name": "pgoutput",

    # 3. Offset storage
    "offset.storage": "org.apache.kafka.connect.storage.FileOffsetBackingStore",
    "offset.storage.file.filename": "/tmp/offsets.dat",
    "offset.flush.interval.ms": "60000",

    # 4. Schema history
    "schema.history.internal": "io.debezium.relational.history.FileSchemaHistory",
    "schema.history.internal.file.filename": "/tmp/schemahistory.dat",
}

engine = DebeziumEngine(properties=props, handler=MyHandler())
engine.run()
