# Solution by Siarhei Kazak
# Assuming you already have pyenv installed and $PATH variable modificated to use it

#!/bin/bash

# Logfile can be specified here

LOGFILE="/dev/null"

VERSIONS="$@"

function usage() {
	echo -e "\nUsage: \n$0 [<VERSION_1> <VERSION_2> .. <VERSION_N>]"
	echo -e "\nDefault values: 2.7.17 3.8.1"
	echo "Script will proceed in 5 seconds..."
	echo -e "<CTRL-C> to cancel\n"
}

# Check arguments

if [[ "$#" == 0  ]]; then
	echo "****************************************************"
	echo -e "*WARN* - Script takes valid python versions as args"
	echo "****************************************************"
	usage
	sleep 6s
	VERSIONS=("2.7.17" "3.8.1")
fi

NAME_PREFIX="testenv"

touch $LOGFILE

# Install versions and create virtualenvs

for V in ${VERSIONS[@]}; do
	NAME="$NAME_PREFIX-$V"
	pyenv install -s $V >> $LOGFILE && echo -e "ok\n" || echo -e "\nERROR - not installed"
	echo -e "Creating virtualenv for Python-$V...\n"
	pyenv virtualenv $V $NAME >> $LOGFILE && echo -e "ok\n" || echo -e "\nERROR - not created"
	pyenv local $NAME
	echo "*****************************************"
	echo -e "\nvirtualenv $(pyenv local) is using:"
 	echo "$(python -V)"
	echo "*****************************************"
done

echo "Done"

exit 0
