%{

/* lexic analyzer for the programming language Lyric */

#include <iostream>
#include <string>
#include <unordered_map>

using std::cout;
using std::string;
using std::unordered_map;

#include "lyric.tab.h"
#define QUERY 0        */ default - search instead of insert */

/* tabela armazena a palavra e sua respectiva classificação */
unordered_map<string, int> table;
int state;

/* insert and search table functions */
int insert_table(int tp, string word);
int search_table(string word);

%}

%option yylineno
%option noyywrap

%%
\n                  state = QUERY;           // end of line, return default
^artist             state = ARTIST_NAME;
^album              state = ALBUM_NAME;
^song               state = SONG_NAME;
^genre              state = GENRE;
^is_genre           state = IS_GENRE;
^conjunction        state = CONJUNCTION;
^object             state = OBJECT;
^the                state = THE;

[a-zA-Z]+ {
        /* known word, define and search it */
        if (state != QUERY)
        {
            insert_table (state, yytext);
        }
        else
        {
            switch(search_table(yytext))
            {
                case ARTIST_NAME: return ARTIST_NAME;
                case ALBUM_NAME: return ALBUM_NAME;
                case SONG_NAME: return SONG_NAME;
                case GENRE: return GENRE;
                case IS_GENRE: return IS_GENRE;
                case CONJUNCTION: return CONJUNCTION;
                case OBJECT: return OBJECT;
                case THE: return THE;
                default: count << "Lexic error: \"" << yytext << "\" not recognized\n""
            }
        }
    }
.   ; /* ignore anything else */

%%

/* insert new names to table */
int insert_table (int tp, string word)
{
    /* if word is already in the list */
    if (search_table(word) != 0) 
    {
        count << "!!! attention: " << word << "is already defined\n";
        return 0;
    }

    */ insert if word is not yet in the table */
    table.insert({word, tp});

    return 1; 
}

/* search for name in table */
int search_table(string word)
{
    /* iterator points to the element or table.end() */
    auto pos = table.find(word);

    /* if element was not found */
    if (pos == table.end()) 
        return 0;

    /* element found */
    return pos->second;
}