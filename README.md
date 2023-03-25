# Lyrics
This repository I`ll be posting the development of my programming language.

## EBNF

**PROGRAM** = { statement } ;

**STATEMENT** = ARTIST_DECLARATION | ALBUM_DECLARATION | SONG_DECLARATION | FUNCTION_DECLARATION | ASSIGNMENT | IF_STATEMENT | FOR_LOOP;

**ASSIGNMENT**= VARIABLE_NAME, "is" , VALUE, "." ;

**ARTIST_NAME** = STRING;

**ARTIST_DECLARATION** = "The" , ARTIST_NAME, "has released" , ALBUM_LIST, "." ;

**ALBUM_NAME** = STRING;

**ALBUM_DECLARATION**= "Album" , ALBUM_NAME, "has songs" , SONG_LIST, "and is of genre" , GENRE, "." ;

**ALBUM_STATEMENT =** ALBUM_NAME, ****"is an album by", ****ARTIST_NAME**,** "released in", YEAR, ****"in the genre", ****GENRE**,** "including", ****SONG_LIST

**ALBUM_LIST**= "[" , ALBUM_NAME, { "," , ALBUM_NAME} , "]" ;

**SONG_NAME** = STRING;

**SONG_DECLARATION** = "Song" , SONG_NAME, "is a”, GENRE, “music with the duration of” DURATION, “minutes from" , ALBUM_NAME;

**SONG_LIST** = "[" , SONG_NAME , { "," , SONG_NAME} , "]" ;

**FUNCTION_NAME** = STRING;

**FUNCTION_DECLARATION** = "The" , function_name , “of”, "(" , argument_list , ")" , "is" , FUNCTION_BODY**, “**!**”**;

**FUNCTION_BODY**= if_statement | for_loop | boolean_expression ;

**ARGUMENT_LIST**= [ VARIABLE_NAME, { "," , VARIABLE_NAME} ] ;

**GENRE** = "pop" | "rock" | "punk" | "indie" | …;

**IF_STATEMENT** = "when" , boolean_expression , "in" , ALBUM_NAME, ":" , FUNCTION_BODY;

**FOR_LOOP** = "when" , SONG_NAME, "in" , ALBUM_NAME, ":" , FUNCTION_BODY;

**BOOLEAN_EXPRESSION** = VARIABLE_NAME, COMPARISON_OPERATOR, VARIABLE_NAME;

**VARIABLE_NAME** = STRING;

**YEAR** = DIGIT{4};

**DURATION** = DIGIT{2}, “:”, DIGIT{2};

**STRING** = '"' , CHARACTERS, '"' ;

**COMPARISON_OPERATOR** = ">" | "<" | "==" | "!=" ;

**CHARACTERS** =  a | ... | z | A | ... | Z ;

**DIGIT** = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ;
