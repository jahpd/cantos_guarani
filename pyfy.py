def botlistfy(**kwargs):
    '''format dictionary in jekyll static mardown blog format 
        
        botfy_body(title=["awesome", ["title", "explanation"]], title_prefix="##", contents=["foo", ["bar", "baz"]])

    generates

        [awesome]: foo
        [[title]]: bar
        [[explanation]]: baz'''
    pass

def jekyllfy_head(**kwargs):
    '''format dictionary in jekyll static mardown blog format 
        
        jekyllfy_head(title="awesome")
    
    generates:

        ---
        layout: post
        title: AAuto-extraction - {0}
        date: {1}
        tags: update
        ---'''
    encode_with = kwargs['encode']
    print "=> makdowing text to jekyll format head ..."
    s = """---layout: post
    title: Data extraction about {0}
    date:
    tags: update
    ---\n\n""".format(encode_with(kwargs["title"]))

def jekyllfy_body(**kwargs):
    '''format dictionary in jekyll static mardown blog format 
        
        jekyllfy_body(title=["awesome", ["title", "explanation"]], contents=["foo", ["bar", "baz"]])

    generates

        ## awesome

        foo

        ### title

        bar

        ### explanation

        baz

    if you want Ruby Liquid::Tag or Liquid::Block, you need to add in string:

        jekyllfy_body(titles=["awesome", ["title", "explanation"]], 
                      title_prefix="##", 
                      contents=["foo", ["bar {% highlight text%}bum{% endhighlight %}", "baz"]])'''
    pyfy(titles=kwargs["titles"], title_prefix="## ", contents=kwargs["contents"])
        



def textfy(**kwargs):
    '''format to simple plain text (useful to LanguageCenter)
 
        textfy_body(title=["awesome", ["title", "explanation"]], contents=["foo", ["bar", "baz"]])

    generates

        * awesome: 
        foo
        **title
        bar
        **explanation
        baz'''
    print "=> textfying ..."
    return pyfy(titles=kwargs["titles"], title_prefix="*", contents=kwargs["contents"])

def pyfy(**kwargs):
    '''format to simple plain text according some rules:

       pyfy_body(title=["awesome", ["title", "explanation"]], title_prefix="->", contents=["foo", ["bar", "baz"]])'''
    s = ""
    for i in range(0, len(kwargs["titles"])):
        title = kwargs["title"][i]
        content = kwargs["content"][i]
        if isinstanceof(title, []):
            for j in range(0, len(title)):
                s+=kwargs["title_prefix"]+" "+title[j]+"\n\n"+content[j]
        else:
            s+=kwargs["title_prefix"]+" "+title+"\n\n"+content
    return s
        
