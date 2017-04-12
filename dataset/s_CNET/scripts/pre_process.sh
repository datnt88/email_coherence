cat $1 | while read line
do
	echo "---------------------"
	n=0
	cat threads/$line.text | while read post
	do
		let 'n=n+1'
	   	echo $post > fragments/$line.text.frag_$n 
		echo $line.text.frag_$n >> threads/$line.text.IDs 
	done
	 
done

