# lyrics
This repository I'll be posting the development of my programming language. 

An example would be:

```
beatles = "The Beatles"
number_of_albuns_beatles = 12
debuted_beatles = 1960

beyonce = "Beyonce"
number_of_albuns_beyonce = 7
debuted_beyonce = 1997

def numberOfDifferentAlbuns(albuns1, albuns2) {

    difference = albuns1 - albuns2

    if (difference > 0) {
        print("The first artist has " + difference + " albuns more than the second")
    }
    if (difference < 0) {
        difference = difference + 2*difference
        print("The second artist has " + difference + " albuns more than the first")
    }
}

differenceNumbers = 0
differenceYears = debuted_beyonce - debuted_beatles

while (differenceYears > 0) {
    differenceYears = differenceYears - 1
    differenceNumbers = differenceNumbers + 1
}

use numberOfDifferentAlbuns(number_of_albuns_beatles, number_of_albuns_beyonce)

print("Beyonce debuted " + differenceNumbers + " after The Beatles.")
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

## Lexic and Syntactic Analyzers

How to run it:
```
bison -dv lyric.y
flex -l lyric.l
gcc -o flex_analyzer lex.yy.c -lfl
gcc -o bison_analyzer lyric.tab.c lex.yy.c -lfl
./flex_analyzer < input.txt
./bison_analyzer < input.txt
```

## Compiling the code

```
python main.py example.txt
```

Resultado: 
![image](https://github.com/LuizaValezim/lyrics/assets/62949391/6b4bd839-2701-454a-a936-aeab08574bb9)
