:- module(compile,[
        compile/1
    ]).

:- meta_predicate
    catch_messages(0, -).

catch_messages(Goal, Messages) :-
    nb_setval(messages, []),
    thread_self(Me),
    setup_call_cleanup(assert((user:message_hook(Term, Kind, Lines) :-
                                    catch_message(Me, message(Term,Kind,Lines))),
                            Ref),
                    once(Goal),
                    collect_messages(Messages, Ref)).

catch_message(Me, message(Term,Kind,Lines)) :-
    Kind \= silent,
    thread_self(Me),
    !,    
    nb_getval(messages, L0),
    message_to_string(Term, String),
    (   source_location(File, Line)
    ->  true
    ;   File = "",
        Line = 0
    ),
    nb_linkval(messages, [message(Term,Kind,Lines,File,Line,String)|L0]).

collect_messages(Messages, Ref) :-
    erase(Ref),
    nb_getval(messages, L),
    nb_delete(messages),
    reverse(L, Messages).

compile(Errors) :-
    catch_messages(
        load_files(['code.pl'],[]),
        Messages
    ),
    maplist(format_message,Messages,Errors).

format_message(message(_Term,_Kind,_Lines,_File,Line,Error),error(Line,Error)).