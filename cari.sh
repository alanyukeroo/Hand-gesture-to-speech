until pacmd list-cards | grep 41_42_5A_00_82_42
do
	echo  "WAITING BLUETOOTH SPEAKER!!"
	sleep 1
done
. ~/activebt.sh
echo -e "Oke good"

