REM change the JAVA_HOME path (JRE/JDK 11+)
set JAVA_HOME=C:\Program Files\Java\jdk-12.0.2

call mvn install:install-file "-Dfile=extra_libs\sejda-injector-1.0.2.jar" "-DgroupId=org.sejda" "-DartifactId=sejda-injector" "-Dversion=1.0.2" "-Dpackaging=jar" "-Dsources=extra_libs\sejda-injector-1.0.2-sources.jar"
call mvn install -DskipTests -Drelease -Dgpg.skip

call "%~dp0\pdfsam-basic\target\assembled\pdfsam.exe"
