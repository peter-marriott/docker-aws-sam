\copy app.welcome (my_id, my_text) from '/docker-entrypoint-initdb.d/db_scripts/data_little.dat' delimiter E'\t' CSV;
