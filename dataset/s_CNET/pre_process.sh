cat $1 | while read line
do
	echo "---------------------"
	n=0
	cat more_threads/$line.text | while read post
	do
		let 'n=n+1'
	   	echo $post > more_fragments/$line.text.frag_$n 
		echo $line.text.frag_$n >> more_threads/$line.text.IDs 
	done
	 
done

