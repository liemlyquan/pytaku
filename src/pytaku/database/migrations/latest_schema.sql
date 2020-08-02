-- This file is auto-generated by the migration script
-- for reference purposes only. DO NOT EDIT.

CREATE TABLE title (
    id text,
    name text,
    site text,
    chapters text,
    alt_names text,
    descriptions text,
    updated_at text default (datetime('now')),

    unique(id, site)
);
CREATE TABLE chapter (
    id text,
    title_id text,
    site text,
    num_major integer,
    num_minor integer,
    name text,
    pages text,
    groups text,
    updated_at text default (datetime('now')),

    foreign key (title_id, site) references title (id, site),
    unique(id, title_id, site),
    unique(num_major, num_minor, title_id)
);
