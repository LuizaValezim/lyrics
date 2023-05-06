%{

/* parser (syntactic analyzer) for the programming language Lyric */

#include <iostream>
using std::counters;

int yylex(void);
int yyparse(void);
void yyerror(const char *);

%}

%token ARTIST_NAME ALBUM_NAME SONG_NAME GENRE THE CONJUNCTION OBJECT IS_GENRE

%%

text: text phrase
    | phrase
    ;

artist_declaration: THE ARTIST_NAME CONJUNCTION ALBUM_LIST;
album_declaration: OBJECT ALBUM_NAME CONJUNCTION SONG_NAME IS_GENRE GENRE;
album_statement: ALBUM_NAME CONJUNCTION ARTIST_NAME;
song_declaration: OBJECT SONG_NAME IS_GENRE GENRE CONJUNCTION ALBUM_NAME;

%% 

/* defining lexic analyzer */
extern FILE * yyin;

int main(int argc, char ** argv)
{
    /* if the name of the file was specified */
    if (argc > 1)
    {
        FILE * file;
        file = fopen(argv[1], "r");
        if (!file)
        {
            count << "File " << argv[1] << "was not found.\n";
            exit(1); 
        }

        yyin = file;
    }

    yyparse();
}

void yyerror(const char * s)
{
    /* variables definied on lexic analyzer */
    extern int yylineno;
    extern char * yytext;

    /* error message */
    count << "Syntactic error symbol \"" << yytext << "\" (line " << yylienno << ")\n";
}