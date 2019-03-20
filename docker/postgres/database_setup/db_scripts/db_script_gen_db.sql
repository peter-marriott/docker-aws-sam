DO LANGUAGE plpgsql $$
    BEGIN
        IF (select current_database()) not like '%prod%' THEN
          drop schema if exists app cascade;
          create schema app AUTHORIZATION "app_owner";
        ELSE
          RAISE EXCEPTION 'Wrong database';
        END IF;
    END;
$$;

SET search_path = app;

DROP TABLE IF EXISTS welcome;

CREATE TABLE welcome (my_id int, my_text text);

SET search_path = app;

GRANT ALL ON SCHEMA app TO app_read_write;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA app TO app_read_write;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA app TO app_read_write;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA app TO app_read_write;
ALTER DEFAULT PRIVILEGES IN SCHEMA app GRANT ALL ON TABLES TO app_read_write;
ALTER DEFAULT PRIVILEGES IN SCHEMA app GRANT ALL ON SEQUENCES TO app_read_write;
ALTER DEFAULT PRIVILEGES IN SCHEMA app GRANT ALL ON FUNCTIONS TO app_read_write;

GRANT USAGE ON SCHEMA app TO app_read;
GRANT SELECT ON ALL TABLES IN SCHEMA app TO app_read;
ALTER DEFAULT PRIVILEGES IN SCHEMA app GRANT SELECT ON TABLES TO app_read;

GRANT USAGE ON SCHEMA app TO app_write;
GRANT INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA app TO app_write;
ALTER DEFAULT PRIVILEGES IN SCHEMA app GRANT INSERT, UPDATE, DELETE ON TABLES TO app_write;