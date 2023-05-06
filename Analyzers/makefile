all: lyric

# Compilers
CPP = g++
FLEX = flex
BISON = bison

phrases: lex.yy.c lyric.tab.c
	$(CPP) lex.yy.c lyric.tab.c -std=c++17 -o lyric

lex.yy.c: lyric.l
	$(FLEX) lyric.l

lyric.tab.c: lyric.y
	$(BISON) -d lyric.y

clean: 
	rm lyric lex.yy.c lyric.tab.c lyric.tab.h