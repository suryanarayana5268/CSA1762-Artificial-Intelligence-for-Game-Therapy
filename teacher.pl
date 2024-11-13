% Facts for students and their subjects
studies(charlie, csc135).
studies(olivia, csc135).
studies(jack, csc131).
studies(arthur, csc134).

% Facts for teachers and the subjects they teach
teaches(kirke, csc135).
teaches(collins, csc131).
teaches(collins, csc171).
teaches(juniper, csc134).

% Rule to find the professor of a student for a given subject
professor(X, Y) :-
    teaches(X, C),
    studies(Y, C).
