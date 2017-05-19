#!/bin/bash
THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd  )"

pushd $THIS_DIR
java -Xmx500M -cp -Dfile.encoding=UTF-8 -Xmx500M -cp "antlr-4.5.3-complete.jar:$CLASSPATH" org.antlr.v4.Tool -Dlanguage=Python3 Fcl.g4
mv -f *.py py3_src

java -Xmx500M -cp -Dfile.encoding=UTF-8 -Xmx500M -cp "antlr-4.5.3-complete.jar:$CLASSPATH" org.antlr.v4.Tool -Dlanguage=Python2 Fcl.g4
mv -f *.py py2_src

popd