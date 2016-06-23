
zcat stats_$1 | awk -F '\t' '{print int($2)}' | sort -k1,1n -T ~/grandata/temp | uniq -c | awk '{print $2 "\t" $1}' > stats/dist_callNumber_$1
b=$(cat stats/dist_callNumber_$1 | awk -F '\t' '{c+=$2} END{print c}')
cat stats/dist_callNumber_$1 | awk -F '\t' 'BEGIN{a='$b'; n=0} {print $1 "\t" a-n;n+=$2}' > stats/icd_callNumber_$1

echo "Number done"

zcat stats_$1 | awk -F '\t' '{print int($3)}' | sort -k1,1n -T ~/grandata/temp | uniq -c | awk '{print $2 "\t" $1}' > stats/dist_callDuration_$1
b=$(cat stats/dist_callDuration_$1 | awk -F '\t' '{c+=$2} END{print c}')
cat stats/dist_callDuration_$1 | awk -F '\t' 'BEGIN{a='$b'; n=0} {print $1 "\t" a-n;n+=$2}' > stats/icd_callDuration_$1

echo "Call Duration done"

zcat stats_$1 | awk -F '\t' '{print int($4)}' | sort -k1,1n -T ~/grandata/temp | uniq -c | awk '{print $2 "\t" $1}' > stats/dist_interArrDuration_$1
b=$(cat stats/dist_interArrDuration_$1 | awk -F '\t' '{c+=$2} END{print c}')
cat stats/dist_interArrDuration_$1 | awk -F '\t' 'BEGIN{a='$b'; n=0} {print $1 "\t" a-n;n+=$2}' > stats/icd_interArrDuration_$1

echo "InterArr Duration"

zcat stats_$1 | awk -F '\t' '{print int($5)}' | sort -k1,1n -T ~/grandata/temp | uniq -c | awk '{print $2 "\t" $1}' > stats/dist_switchNumber_$1
b=$(cat stats/dist_switchNumber_$1 | awk -F '\t' '{c+=$2} END{print c}')
cat stats/dist_switchNumber_$1 | awk -F '\t' 'BEGIN{a='$b'; n=0} {print $1 "\t" a-n;n+=$2}' > stats/icd_switchNumber_$1

echo "Switch Number"

zcat stats_$1 | awk -F '\t' '{print int($6)}' | sort -k1,1n -T ~/grandata/temp | uniq -c | awk '{print $2 "\t" $1}' > stats/dist_switchDuration_$1
b=$(cat stats/dist_switchDuration_$1 | awk -F '\t' '{c+=$2} END{print c}')
cat stats/dist_switchDuration_$1 | awk -F '\t' 'BEGIN{a='$b'; n=0} {print $1 "\t" a-n;n+=$2}' > stats/icd_switchDuration_$1

echo "Switch Duration"

zcat stats_$1 | awk -F '\t' '{print int($7)}' | sort -k1,1n -T ~/grandata/temp | uniq -c | awk '{print $2 "\t" $1}' > stats/dist_interSwitchNumber_$1
b=$(cat stats/dist_interSwitchNumber_$1 | awk -F '\t' '{c+=$2} END{print c}')
cat stats/dist_interSwitchNumber_$1 | awk -F '\t' 'BEGIN{a='$b'; n=0} {print $1 "\t" a-n;n+=$2}' > stats/icd_interSwitchNumber_$1

echo "Inter Switch Number"

zcat stats_$1 | awk -F '\t' '{print int($8)}' | sort -k1,1n -T ~/grandata/temp | uniq -c | awk '{print $2 "\t" $1}' > stats/dist_callInSwitch_$1
b=$(cat stats/dist_callInSwitch_$1 | awk -F '\t' '{c+=$2} END{print c}')
cat stats/dist_callInSwitch_$1 | awk -F '\t' 'BEGIN{a='$b'; n=0} {print $1 "\t" a-n;n+=$2}' > stats/icd_callInSwitch_$1

echo "Call In Switch"

zcat stats_$1 | awk -F '\t' '{print int($10-$9)/3600}' | sort -k1,1n -T ~/grandata/temp | uniq -c | awk '{print $2 "\t" $1}' > stats/dist_activeDuration_$1
b=$(cat stats/dist_activeDuration_$1 | awk -F '\t' '{c+=$2} END{print c}')
cat stats/dist_activeDuration_$1 | awk -F '\t' 'BEGIN{a='$b'; n=0} {print $1 "\t" a-n;n+=$2}' > stats/icd_activeDuration_$1

echo "Active Duration"

zcat stats_$1 | awk -F '\t' '{print int($11)}' | sort -k1,1n -T ~/grandata/temp | uniq -c | awk '{print $2}' | sort -k1,1n  > stats/dist_numberUser_$1

echo "Number User per BS"
