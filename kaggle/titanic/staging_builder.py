import sqlalchemy

class StagingBuilder():
    def build_training_staging_table():
        with sqlalchemy.create_engine('postgresql://postgres:')