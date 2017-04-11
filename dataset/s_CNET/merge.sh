cat $1 | while read line
do
	echo "======================================================"
	cat threads/$line.text.IDs | while read frag
	do
		cat cnet_fragments/$frag.sent >> xx/$line.text.all 
	done
	 
done

