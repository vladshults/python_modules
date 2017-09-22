#!/bin/bash

TIME1=$(date +%s)
CTXT1=$(cat /proc/stat | grep ctx | cut -d" " -f2)

for i in {1..5000}
do
ls /tmp > /dev/null
ls /boot > /dev/null
done

TIME2=$(date +%s)
CTXT2=$(cat /proc/stat | grep ctx | cut -d" " -f2)

TIMEDELTA=$(($TIME2 - $TIME1))
CTXTDELTA=$(($CTXT2 - $CTXT1))

SWITCHING_RATE=$(echo "scale=0; $CTXTDELTA/$TIMEDELTA" | bc -l)
SWITCHING_SPEED=$(echo "scale=8; $TIMEDELTA/$CTXTDELTA" | bc -l)

echo "During $TIMEDELTA seconds we found context switching amount per 1 second:"
echo "   $SWITCHING_RATE"
echo "One switching takes amount of time in seconds:"
echo "   $SWITCHING_SPEED"
echo ""
