# Makefile for source rpm: redhat-menus
# $Id$
NAME := redhat-menus
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
