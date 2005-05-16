def build_application(conf):
    if conf.get('publish_dir'):
        from paste.webkit import wsgiwebkit
        app = wsgiwebkit.webkit(conf['publish_dir'], use_lint=conf.get('lint'))
    elif conf.get('publish_app'):
        app = conf['publish_app']
        if isinstance(app, (str, unicode)):
            from paste.util import import_string
            app = import_string.eval_import(app)
    else:
        # @@ ianb 2005-03-23: This should be removed sometime
        if conf.get('webkit_dir'):
            print 'The webkit_dir configuration variable is no longer supported'
            print 'Use publish_dir instead'
        print "You must provide publish_dir or publish_app"
        sys.exit(2)
    return app