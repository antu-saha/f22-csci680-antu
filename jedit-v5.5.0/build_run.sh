#!/bin/sh

# change the JAVA_HOME path (JDK/JRE 8)
export JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk1.8.0_341.jdk/Contents/Home"

ant retrieve build run
