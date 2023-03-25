# lyrics
This repository I'll be posting the development of my programming language. 

An example would be:

```
The Beatles has released ["Please Please Me", "With The Beatles"].

Album "Please Please Me" has songs ["I Saw Her Standing There", "Love Me Do", "Please Please Me"] and is of genre rock, released in 1963 including ["Twist and Shout", "Do You Want to Know a Secret"].
Album "With The Beatles" has songs ["It Won't Be Long", "All I've Got to Do", "All My Loving"] and is of genre rock, released in 1963 including ["I Wanna Be Your Man", "Money"].

Song "Twist and Shout" is a rock music with the duration of 02:33 minutes from "Please Please Me".
Song "Do You Want to Know a Secret" is a rock music with the duration of 01:57 minutes from "Please Please Me".
Song "I Wanna Be Your Man" is a rock music with the duration of 01:59 minutes from "With The Beatles".
Song "Money" is a rock music with the duration of 02:49 minutes from "With The Beatles".

The song with the shortest duration in "Please Please Me" is "Do You Want to Know a Secret".
The album with the longest total duration is "With The Beatles".

when "I Wanna Be Your Man" in "With The Beatles":
  Beatles_song = "I Saw Her Standing There"

Song "I Saw Her Standing There" is a rock music with the duration of 02:55 minutes from "Please Please Me".
```


## EBNF

**PROGRAM** = { statement } ;

**STATEMENT** = ARTIST_DECLARATION | ALBUM_DECLARATION | SONG_DECLARATION | FUNCTION_DECLARATION | ASSIGNMENT | IF_STATEMENT | FOR_LOOP;

**ASSIGNMENT**= VARIABLE_NAME, "is" , VALUE, "." ;

**ARTIST_NAME** = STRING;

**ARTIST_DECLARATION** = "The" , ARTIST_NAME, "has released" , ALBUM_LIST, "." ;

**ALBUM_NAME** = STRING;

**ALBUM_DECLARATION**= "Album" , ALBUM_NAME, "has songs" , SONG_LIST, "and is of genre" , GENRE, "." ;

**ALBUM_STATEMENT =** ALBUM_NAME, "is an album by", ARTIST_NAME,** "released in", YEAR, "in the genre", GENRE, "including", SONG_LIST

**ALBUM_LIST**= "[" , ALBUM_NAME, { "," , ALBUM_NAME} , "]" ;

**SONG_NAME** = STRING;

**SONG_DECLARATION** = "Song" , SONG_NAME, "is a”, GENRE, “music with the duration of” DURATION, “minutes from" , ALBUM_NAME;

**SONG_LIST** = "[" , SONG_NAME , { "," , SONG_NAME} , "]" ;

**FUNCTION_NAME** = STRING;

**FUNCTION_DECLARATION** = "The" , function_name , “of”, "(" , argument_list , ")" , "is" , FUNCTION_BODY;

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
