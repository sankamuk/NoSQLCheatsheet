# Overview

## Definition

Redis by defination is an In-Memory datastore which can be used as a Key-Value based NoSQL DB, Cache or Message Broker. But though In-Memory it also persist data to permanent storage and thus differ from MemCache.

It is meant to be used for explicit key based reading and not for advoc query retrival with SQL. Also data in Redis is in Live memory thus you should be carefull about storing non active data in Redis. In case your data system asking features mentioned Redis should not be your choice.

## Suported Datatypes

- String
- Set
- List
- Sorted Set
- Hashes
- Bitmaps
- HyperLogs
- Geospatial
- Indexes

### Questions defining types

- Do our values need Keys. 
- Storing Objects.
- Multiple value to a key.
- Count elements.
- Sorted.
- Uniqueness.
- Value exist check.

## Security

Allow access by trusted client only, thus not good to expose it to open network. It is build for performance and thus probably not the most end to end secure component of your infrastructure. 

> Notes
> - Simple authentication can be setup if at all needed. Password stored in configuration file and user should use AUTH command with password to authicate its access. 
> - Ideally Redis should be setup for with firewalled blocked access except for specific hosts having access to the service.
> - No Data encrption support for Redis. In case needed use front end SSL proxy.
> - Disable commands (e.g. CONFIG & FLUSSALL) that could cause collatral damage to system by remaning them from config files.

## Engine discussion

- It doesnot serve raw data, neither it uses schemas and fields.
- User should figure out how data will be represented from supported datatypes. You should keep speed in mind.
- Traditional DB either scan rows or scans index, while in Redis you do direct data retrival.
- Redis doesnot have a query engine and you define your retrival.

## Custom Indexing

When you need to retrived value from not only from natural primary key (e.g. id) but also using other attribute, e.g. name.

## Considerations

Redis was not meant 

