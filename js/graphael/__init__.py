import fanstatic
import js.raphael


library = fanstatic.Library('graphael', 'resources')


g_raphael = fanstatic.Resource(
    library,
    'g.raphael.js',
    minified='g.raphael-min.js',
    depends=[js.raphael.raphael])


g_bar = fanstatic.Resource(
    library,
    'g.bar.js',
    minified='g.bar-min.js',
    depends=[g_raphael])


g_dot = fanstatic.Resource(
    library,
    'g.dot.js',
    minified='g.dot-min.js',
    depends=[g_raphael])


g_line = fanstatic.Resource(
    library,
    'g.line.js',
    minified='g.line-min.js',
    depends=[g_raphael])


g_pie = fanstatic.Resource(
    library,
    'g.pie.js',
    minified='g.pie-min.js',
    depends=[g_raphael])


graphael = fanstatic.Group([
    g_raphael,
    g_bar,
    g_dot,
    g_line,
    g_pie,
    ])
