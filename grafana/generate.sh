values="20 5 10 15 12 -3 30 80"
for i in $values; 
do 
curl -i -XPOST  "http://localhost:8086/write?db=testdb" --data-binary "mymeasure,type=points point=$i"
sleep 1
done
