Title: A Good Example of HTTP HEAD Method
Date: 2016-12-23 10:00
Modified: 2018-04-03 20:00
Tags: http, restful, api
Summary: HEAD method is not the most popular, but still it has a role.

I've never been used `HEAD` method in HTTP. I even don't know what
is in the HTTP method list. Usually I only use `GET` and `POST`. I
rarely use `DELETE` and `FETCH`. But other than that I don't use
anything.

But I had an issue. I got a RESTFul API for file storage. And at some
point I needed to check if the file exists. It's too much to `GET` all
the payload of the file contents for checking if the file exists.
I was thinking if I should introduce the new API, but it's not RESTFul.

And here we are. We have `HEAD` method.

The [w3](https://www.w3.org) explains about `HEAD` following;
> The HEAD method is identical to GET except that the server MUST NOT
> return a message-body in the response. The metainformation contained
> in the HTTP headers in response to a HEAD request SHOULD be identical
> to the information sent in response to a GET request. This method can
> be used for obtaining metainformation about the entity implied by the
> request without transferring the entity-body itself. This method is
> often used for testing hypertext links for validity, accessibility,
> and recent modification.
>
> The response to a HEAD request MAY be cacheable in the sense that the
> information contained in the response MAY be used to update a previously
> cached entity from that resource. If the new field values indicate that
> the cached entity differs from the current entity (as would be indicated
> by a change in Content-Length, Content-MD5, ETag or Last-Modified),
> then the cache MUST treat the cache entry as stale.
>
> from [HTTP methods](https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)

Now I can just get the header with `HEAD` method and check if the file exists
without downloading all the payload.
