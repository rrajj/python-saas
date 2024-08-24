# Learnings

* views should always return a `HttpResponse` or some Django object. Returning for example a string object would give an error saying: `'str' object has no attribute 'get'`. Django has built-in functions to secure the responses, which comes in when we use `HttpResponse`. 