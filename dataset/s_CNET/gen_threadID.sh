cat list.exp.threads | while read line
do
	#echo "======================================================"
	n=0
	cat threads/$line.IDs | while read frag
	do
		let 'n=n+1'
		cat exp.fragments/$frag.sent | while read xxx
		do
			echo $n >> threads/$line.all.parsed.ner.commentIDs 
		done 
	done
	 
done

