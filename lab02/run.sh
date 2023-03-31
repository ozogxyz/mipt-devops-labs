#/bin/bash
# container_ids=$(docker ps -a -q) | sed 's/ .*//'
# container=$(${container_id} | sed 's/ .*//')

container_id=$(docker ps --format "{{.ID}}" | head -n 2)

echo $container_id

docker exec 02e2 mongoimport \
   --collection='fieldfile_option' \
   --file=/data/data.csv \
   --type=csv \
   --fieldFile=field_file.txt