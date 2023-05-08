%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lyric.tab.h"

extern int yylex();
void yyerror(const char *s) { printf("ERROR: %s\n", s); }
%}

%token ALBUM SONG SONGS DURATION GENRE

%token PLAY PAUSE

%token RELEASED INCLUDING

%token AND OF IN HAS IS A FROM THE WITH WHEN THEN BY

%token DIGIT IDENTIFIER LKEY RKEY COLON COMMA

%start program

%%

program:
    PLAY statements PAUSE { printf("Parsing complete.\n"); }
    ;

statements:
    statement
    | statements statement
    ;

statement:
    artist_statement
    | album_statement
    | song_statement
    | genre_statement
    | duration_statement
    | year_statement
    | record_statement
    | format_statement
    | if_statement
    | repeat_statement
    ;

artist_statement:
    THE ARTIST IS ARTIST_IDENTIFIER { printf("Found artist statement: %s %s\n", $1, $3); }
    ;

album_statement:
    THE ALBUM IS ALBUM_IDENTIFIER { printf("Found album statement: %s %s\n", $1, $3); }
    ;

songs_statement:
    WITH THE SONGS COLON SONGS_IDENTIFIER { printf("Found songs statement: %s %s\n", $1, $3); }
    ;

genre_statement:
    THE GENRE IS GENRE_IDENTIFIER { printf("Found genre statement: %s %s\n", $1, $3); }
    ;

duration_statement:
    WITH DURATION OF DURATION_IDENTIFIER MINUTES { printf("Found duration statement: %s %s\n", $1, $3); }
    ;

year_statement:
    RELEASED IN YEAR_IDENTIFIER { printf("Found year statement: %s %s\n", $1, $3); }
    ;

record_statement:
    RELEASED BY RECORD_IDENTIFIER { printf("Found record statement: %s %s\n", $1, $3); }
    ;

format_statement:
    IN FORMAT FORMAT_IDENTIFIER { printf("Found format statement: %s %s\n", $1, $3); }
    ;

if_statement:
    WHEN ARTIST_IDENTIFIER IS THE ARTIST COMMA THEN LKEY statements RKEY ELSE LKEY statements RKEY
    | WHEN ALBUM_IDENTIFIER IS THE ALBUM COMMA THEN LKEY statements RKEY ELSE LKEY statements RKEY 
    | WHEN SONGS_IDENTIFIER IS IN THE SONGS COMMA THEN LKEY statements RKEY ELSE LKEY statements RKEY
    | WHEN GENRE_IDENTIFIER IS THE GENRE COMMA THEN LKEY statements RKEY ELSE LKEY statements RKEY 
    | WHEN DURATION_IDENTIFIER IS THE DURATION COMMA THEN LKEY statements RKEY ELSE LKEY statements RKEY  
    | WHEN YEAR_IDENTIFIER IS THE RELEASED YEAR COMMA THEN LKEY statements RKEY ELSE LKEY statements RKEY  
    | WHEN RECORD_IDENTIFIER IS THE RECORD COMMA THEN LKEY statements RKEY ELSE LKEY statements RKEY   
    | WHEN FORMAT_IDENTIFIER IS THE FORMAT COMMA THEN LKEY statements RKEY ELSE LKEY statements RKEY  
    ;

%%

int main(void) {
    yyparse();
    return 0;
}
