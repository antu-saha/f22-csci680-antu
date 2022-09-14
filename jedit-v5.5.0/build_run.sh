#!/bin/sh

# change the JAVA_HOME path (JDK/JRE 8)
export JAVA_HOME="/Library/Java/JavaVirtualMachines/zulu-8.jdk/Contents/Home"

ant retrieve build run
