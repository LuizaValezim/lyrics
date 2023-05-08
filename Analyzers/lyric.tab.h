/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_LYRIC_TAB_H_INCLUDED
# define YY_YY_LYRIC_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    ALBUM = 258,                   /* ALBUM  */
    ARTIST = 259,                  /* ARTIST  */
    SONG = 260,                    /* SONG  */
    SONGS = 261,                   /* SONGS  */
    DURATION = 262,                /* DURATION  */
    GENRE = 263,                   /* GENRE  */
    PLAY = 264,                    /* PLAY  */
    PAUSE = 265,                   /* PAUSE  */
    RELEASED = 266,                /* RELEASED  */
    INCLUDING = 267,               /* INCLUDING  */
    AND = 268,                     /* AND  */
    OF = 269,                      /* OF  */
    IN = 270,                      /* IN  */
    HAS = 271,                     /* HAS  */
    IS = 272,                      /* IS  */
    A = 273,                       /* A  */
    FROM = 274,                    /* FROM  */
    THE = 275,                     /* THE  */
    WITH = 276,                    /* WITH  */
    WHEN = 277,                    /* WHEN  */
    THEN = 278,                    /* THEN  */
    BY = 279,                      /* BY  */
    ELSE = 280,                    /* ELSE  */
    MINUTES = 281,                 /* MINUTES  */
    FORMAT = 282,                  /* FORMAT  */
    YEAR = 283,                    /* YEAR  */
    RECORD = 284,                  /* RECORD  */
    ARTIST_IDENTIFIER = 285,       /* ARTIST_IDENTIFIER  */
    ALBUM_IDENTIFIER = 286,        /* ALBUM_IDENTIFIER  */
    SONGS_IDENTIFIER = 287,        /* SONGS_IDENTIFIER  */
    GENRE_IDENTIFIER = 288,        /* GENRE_IDENTIFIER  */
    DURATION_IDENTIFIER = 289,     /* DURATION_IDENTIFIER  */
    YEAR_IDENTIFIER = 290,         /* YEAR_IDENTIFIER  */
    RECORD_IDENTIFIER = 291,       /* RECORD_IDENTIFIER  */
    FORMAT_IDENTIFIER = 292,       /* FORMAT_IDENTIFIER  */
    DIGIT = 293,                   /* DIGIT  */
    IDENTIFIER = 294,              /* IDENTIFIER  */
    LKEY = 295,                    /* LKEY  */
    RKEY = 296,                    /* RKEY  */
    COLON = 297,                   /* COLON  */
    COMMA = 298                    /* COMMA  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_LYRIC_TAB_H_INCLUDED  */
