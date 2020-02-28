# Solution by Siarhei Kazak

#!/bin/bash

VERSIONS="$@"

function usage() {
	echo -e "\nUsage: \n$0 <VERSION> <VERSION>"
	echo -e "\nDefault values: 2.7.17 3.8.1"
	echo "Script will proceed in 5 seconds..."
	echo -e "<CTRL-C> to cancel\n"
}

if [[ "$#" == 0  ]]; then
	echo "*********************************************************"
	echo -e "*WARN* - Script takes valid python versions as args"
	echo "*********************************************************"
	usage
	sleep 6s
	VERSIONS=("2.7.17" "3.8.1")
fi

NAME_PREFIX="testenv"
echo $PATH
for V in ${VERSIONS[@]}; do
	NAME="$NAME_PREFIX-$V"
	pyenv install -s $V >/dev/null
	pyenv virtualenv $V $NAME
	pyenv local $NAME
	echo -e "\nvirtualenv $(pyenv local) is using:"
 	echo "$(python -V)"
done

exit 0
