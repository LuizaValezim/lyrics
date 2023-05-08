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

"when"                  { printf("WHEN\n"); return WHEN;}
"then"                  { printf("THEN\n"); return THEN;}

"seconds"               { printf("SECONDS\n"); return SECONDS;}
"minutes"               { printf("MINUTES\n"); return MINUTES;}
"hours"                 { printf("HOURS\n"); return HOURS;}

"shortest"              { printf("SHORTEST\n"); return SHORTEST;}
"longest"               { printf("LONGEST\n"); return SHORTEST;}

"the beatles"           { printf("neutral\n"); return ARTIST_IDENTIFIER; }

"please please me"      { printf("pink\n"); return ALBUM_IDENTIFIER; }

"chains"                { printf("red\n"); return SONGS_IDENTIFIER; }

"rock"                  { printf("purple\n"); return GENRE_IDENTIFIER; }

"31:59"                 { printf("brown\n"); return DURATION_IDENTIFIER; }

"1963"                  { printf("glittery\n"); return YEAR_IDENTIFIER; }

"parklophone"           { printf("glittery\n"); return RECORD_IDENTIFIER; }

"LP"                    { printf("glittery\n"); return FORMAT_IDENTIFIER; }

[0-9]+                  { printf("DIGIT\n"); return DIGIT; }
[a-zA-Z][a-zA-Z0-9_]*   { printf("IDENTIFIER\n"); return IDENTIFIER; }

"{"                     { printf("LKEY\n"); return LKEY; }
"}"                     { printf("RKEY\n"); return RKEY; }
":"                     { printf("COLON\n"); return COLON; }
","                     { printf("COMMA\n"); return COMMA; }

.                       printf("Unknown token!\n"); yyterminate();

%%
