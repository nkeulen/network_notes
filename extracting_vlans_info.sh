# save all the vlan tags on subinterfaces of an interface to a file and also sort it

# below is for dot1ad change it to dot1q to extract those (was tested on asr9k):
ssh cisco@10.0.0.1 "sh run formal int | inc Bundle-Ether10 | inc dot1ad | utility egrep -e \"dot1ad [0-9]+$\" -o | utility cut -c 8-12" | tail -n +4 | sort -n > vlans_pe1
ssh cisco@10.0.0.2 "sh run formal int | inc Bundle-Ether10 | inc dot1ad | utility egrep -e \"dot1ad [0-9]+$\" -o | utility cut -c 8-12" | tail -n +4 | sort -n > vlans_pe2

