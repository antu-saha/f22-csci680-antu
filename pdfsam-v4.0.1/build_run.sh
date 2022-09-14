#!/bin/sh

#change the JAVA_HOME path (JRE/JDK 11+)
export JAVA_HOME="/Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home"

mvn install:install-file "-Dfile=extra_libs/sejda-injector-1.0.2.jar" "-DgroupId=org.sejda" "-DartifactId=sejda-injector" "-Dversion=1.0.2" "-Dpackaging=jar" "-Dsources=extra_libs/sejda-injector-1.0.2-sources.jar"
mvn install -DskipTests -Drelease -Dgpg.skip

#it is possible the sh script is created using LF+CR characters for new lines.
#if this is the case, we need to convert LF+CR to LF, by running the following command (dos2unix need to be installed first):
#dos2unix ./pdfsam-basic/target/assembled/bin/pdfsam.sh
./pdfsam-basic/target/assembled/bin/pdfsam.sh
