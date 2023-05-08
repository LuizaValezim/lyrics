%{
#include <stdio.h>
#include <stdlib.h>
#include "lyric.tab.h"
%}

%%

[ \t\n]                 ;

"play"                  { printf("PLAY\n"); return PLAY;}
"pause"                 { printf("PAUSE\n"); return PAUSE;}

"album"                 { printf("ALBUM\n"); return ALBUM;}
"artist"                { printf("ARTIST\n"); return ARTIST;}
"song"                  { printf("SONG\n"); return SONG;}
"songs"                 { printf("SONGS\n"); return SONGS;}
"duration"              { printf("DURATION\n"); return DURATION;}
"genre"                 { printf("GENRE\n"); return GENRE;}
"record comapny"        { printf("RECORD\n"); return RECORD;}
"format"                { printf("FORMAT\n"); return FORMAT;}

"released"              { printf("RELEASED\n"); return RELEASED;}
"including"             { printf("INCLUDING\n"); return INCLUDING;}

"and"			{ printf("AND\n"); return AND;}
"of"                    { printf("OF\n"); return OF;}
"in"                    { printf("IN\n"); return IN;}
"has"                   { printf("HAS\n"); return HAS;}
"is"                    { printf("IS\n"); return IS;}
"a"                     { printf("A\n"); return A;}
"from"                  { printf("FROM\n"); return FROM;}
"the"                   { printf("THE\n"); return THE;}
"by"                    { printf("BY\n"); return BY;}
"with"                  { printf("WITH\n"); return WITH;}
"else"                  { printf("ELSE\n"); return ELSE;}

"when"                  { printf("WHEN\n"); return WHEN;}
"then"                  { printf("THEN\n"); return THEN;}

"minutes"               { printf("MINUTES\n"); return MINUTES;}

"the beatles"           { printf("ARTIST_ID\n"); return ARTIST_IDENTIFIER; }

"please please me"      { printf("ALBUM_ID\n"); return ALBUM_IDENTIFIER; }

"chains"                { printf("SONG_ID\n"); return SONGS_IDENTIFIER; }

"rock"                  { printf("GENRE_ID\n"); return GENRE_IDENTIFIER; }

"31:59"                 { printf("DURATION_ID\n"); return DURATION_IDENTIFIER; }

"1963"                  { printf("YEAR_ID\n"); return YEAR_IDENTIFIER; }

"parklophone"           { printf("RECORD_ID\n"); return RECORD_IDENTIFIER; }

"LP"                    { printf("FORMAT_ID\n"); return FORMAT_IDENTIFIER; }

[0-9]+                  { printf("DIGIT\n"); return DIGIT; }
[a-zA-Z][a-zA-Z0-9_]*   { printf("IDENTIFIER\n"); return IDENTIFIER; }

"{"                     { printf("LKEY\n"); return LKEY; }
"}"                     { printf("RKEY\n"); return RKEY; }
":"                     { printf("COLON\n"); return COLON; }
","                     { printf("COMMA\n"); return COMMA; }

.                       printf("Unknown token!\n"); yyterminate();

%%
