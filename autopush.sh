#!/usr/bin/env bash

function get_message() {
	echo "Commit message:"
	echo -n ">>> "
	eval "read $1"
}

message=''
get_message message
file_name=$(echo message | md5sum | cut -b 1-32).autopush
git add *
if [ $? == 0 ] ; then
	echo "[$(date "+%x %R")] $message" > /tmp/$file_name
	git commit -F /tmp/$file_name
	if [ $? == 0 ] ; then
		git push
	fi
	rm /tmp/$file_name
fi

