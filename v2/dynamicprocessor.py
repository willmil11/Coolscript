__all__ = ['dynamicprocessor']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['processor', 'peg$subclass', 'peg$parse', 'peg$SyntaxError'])
@Js
def PyJsHoistedNonPyName(child, parent, this, arguments, var=var):
    var = Scope({'child':child, 'parent':parent, 'this':this, 'arguments':arguments}, var)
    var.registers(['ctor', 'child', 'parent'])
    @Js
    def PyJsHoisted_ctor_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get(u"this").put('constructor', var.get('child'))
    PyJsHoisted_ctor_.func_name = 'ctor'
    var.put('ctor', PyJsHoisted_ctor_)
    pass
    var.get('ctor').put('prototype', var.get('parent').get('prototype'))
    var.get('child').put('prototype', var.get('ctor').create())
PyJsHoistedNonPyName.func_name = 'peg$subclass'
var.put('peg$subclass', PyJsHoistedNonPyName)
@Js
def PyJsHoistedNonPyName(message, expected, found, location, this, arguments, var=var):
    var = Scope({'message':message, 'expected':expected, 'found':found, 'location':location, 'this':this, 'arguments':arguments}, var)
    var.registers(['found', 'location', 'expected', 'message'])
    var.get(u"this").put('message', var.get('message'))
    var.get(u"this").put('expected', var.get('expected'))
    var.get(u"this").put('found', var.get('found'))
    var.get(u"this").put('location', var.get('location'))
    var.get(u"this").put('name', Js('SyntaxError'))
    if PyJsStrictEq(var.get('Error').get('captureStackTrace').typeof(),Js('function')):
        var.get('Error').callprop('captureStackTrace', var.get(u"this"), var.get('peg$SyntaxError'))
PyJsHoistedNonPyName.func_name = 'peg$SyntaxError'
var.put('peg$SyntaxError', PyJsHoistedNonPyName)
@Js
def PyJsHoistedNonPyName(input, options, this, arguments, var=var):
    var = Scope({'input':input, 'options':options, 'this':this, 'arguments':arguments}, var)
    var.registers(['peg$c0', 'peg$c25', 'peg$c26', 'text', 'peg$c22', 'peg$silentFails', 'peg$parse_', 'peg$FAILED', 'peg$c14', 'peg$savedPos', 'peg$otherExpectation', 'peg$c30', 'peg$buildSimpleError', 'peg$c10', 'peg$computePosDetails', 'peg$currPos', 'peg$endExpectation', 'peg$c23', 'peg$computeLocation', 'options', 'peg$c17', 'peg$c3', 'peg$literalExpectation', 'peg$c2', 'peg$c8', 'peg$c29', 'peg$c5', 'peg$fail', 'peg$parseTerm', 'peg$c18', 'peg$c21', 'peg$maxFailPos', 'peg$c6', 'peg$parseExpression', 'peg$c20', 'peg$parseString', 'peg$parseNumber', 'peg$c1', 'peg$result', 'input', 'peg$startRuleFunction', 'peg$maxFailExpected', 'peg$c11', 'peg$c28', 'peg$c15', 'peg$classExpectation', 'peg$c19', 'peg$posDetailsCache', 'peg$c4', 'peg$c16', 'peg$c24', 'peg$anyExpectation', 'peg$c9', 'expected', 'peg$startRuleFunctions', 'peg$parseFactor', 'location', 'peg$c27', 'peg$c7', 'peg$c12', 'peg$buildStructuredError', 'peg$c13', 'error'])
    @Js
    def PyJsHoisted_text_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return var.get('input').callprop('substring', var.get('peg$savedPos'), var.get('peg$currPos'))
    PyJsHoisted_text_.func_name = 'text'
    var.put('text', PyJsHoisted_text_)
    @Js
    def PyJsHoisted_location_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return var.get('peg$computeLocation')(var.get('peg$savedPos'), var.get('peg$currPos'))
    PyJsHoisted_location_.func_name = 'location'
    var.put('location', PyJsHoisted_location_)
    @Js
    def PyJsHoisted_expected_(description, location, this, arguments, var=var):
        var = Scope({'description':description, 'location':location, 'this':this, 'arguments':arguments}, var)
        var.registers(['location', 'description'])
        var.put('location', (var.get('location') if PyJsStrictNeq(var.get('location'),PyJsComma(Js(0.0), Js(None))) else var.get('peg$computeLocation')(var.get('peg$savedPos'), var.get('peg$currPos'))))
        PyJsTempException = JsToPyException(var.get('peg$buildStructuredError')(Js([var.get('peg$otherExpectation')(var.get('description'))]), var.get('input').callprop('substring', var.get('peg$savedPos'), var.get('peg$currPos')), var.get('location')))
        raise PyJsTempException
    PyJsHoisted_expected_.func_name = 'expected'
    var.put('expected', PyJsHoisted_expected_)
    @Js
    def PyJsHoisted_error_(message, location, this, arguments, var=var):
        var = Scope({'message':message, 'location':location, 'this':this, 'arguments':arguments}, var)
        var.registers(['location', 'message'])
        var.put('location', (var.get('location') if PyJsStrictNeq(var.get('location'),PyJsComma(Js(0.0), Js(None))) else var.get('peg$computeLocation')(var.get('peg$savedPos'), var.get('peg$currPos'))))
        PyJsTempException = JsToPyException(var.get('peg$buildSimpleError')(var.get('message'), var.get('location')))
        raise PyJsTempException
    PyJsHoisted_error_.func_name = 'error'
    var.put('error', PyJsHoisted_error_)
    @Js
    def PyJsHoistedNonPyName(text, ignoreCase, this, arguments, var=var):
        var = Scope({'text':text, 'ignoreCase':ignoreCase, 'this':this, 'arguments':arguments}, var)
        var.registers(['ignoreCase', 'text'])
        return Js({'type':Js('literal'),'text':var.get('text'),'ignoreCase':var.get('ignoreCase')})
    PyJsHoistedNonPyName.func_name = 'peg$literalExpectation'
    var.put('peg$literalExpectation', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(parts, inverted, ignoreCase, this, arguments, var=var):
        var = Scope({'parts':parts, 'inverted':inverted, 'ignoreCase':ignoreCase, 'this':this, 'arguments':arguments}, var)
        var.registers(['parts', 'inverted', 'ignoreCase'])
        return Js({'type':Js('class'),'parts':var.get('parts'),'inverted':var.get('inverted'),'ignoreCase':var.get('ignoreCase')})
    PyJsHoistedNonPyName.func_name = 'peg$classExpectation'
    var.put('peg$classExpectation', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return Js({'type':Js('any')})
    PyJsHoistedNonPyName.func_name = 'peg$anyExpectation'
    var.put('peg$anyExpectation', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return Js({'type':Js('end')})
    PyJsHoistedNonPyName.func_name = 'peg$endExpectation'
    var.put('peg$endExpectation', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(description, this, arguments, var=var):
        var = Scope({'description':description, 'this':this, 'arguments':arguments}, var)
        var.registers(['description'])
        return Js({'type':Js('other'),'description':var.get('description')})
    PyJsHoistedNonPyName.func_name = 'peg$otherExpectation'
    var.put('peg$otherExpectation', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(pos, this, arguments, var=var):
        var = Scope({'pos':pos, 'this':this, 'arguments':arguments}, var)
        var.registers(['p', 'pos', 'details'])
        var.put('details', var.get('peg$posDetailsCache').get(var.get('pos')))
        if var.get('details'):
            return var.get('details')
        else:
            var.put('p', (var.get('pos')-Js(1.0)))
            while var.get('peg$posDetailsCache').get(var.get('p')).neg():
                (var.put('p',Js(var.get('p').to_number())-Js(1))+Js(1))
            var.put('details', var.get('peg$posDetailsCache').get(var.get('p')))
            var.put('details', Js({'line':var.get('details').get('line'),'column':var.get('details').get('column')}))
            while (var.get('p')<var.get('pos')):
                if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('p')),Js(10.0)):
                    (var.get('details').put('line',Js(var.get('details').get('line').to_number())+Js(1))-Js(1))
                    var.get('details').put('column', Js(1.0))
                else:
                    (var.get('details').put('column',Js(var.get('details').get('column').to_number())+Js(1))-Js(1))
                (var.put('p',Js(var.get('p').to_number())+Js(1))-Js(1))
            var.get('peg$posDetailsCache').put(var.get('pos'), var.get('details'))
            return var.get('details')
    PyJsHoistedNonPyName.func_name = 'peg$computePosDetails'
    var.put('peg$computePosDetails', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(startPos, endPos, this, arguments, var=var):
        var = Scope({'startPos':startPos, 'endPos':endPos, 'this':this, 'arguments':arguments}, var)
        var.registers(['startPos', 'startPosDetails', 'endPosDetails', 'endPos'])
        var.put('startPosDetails', var.get('peg$computePosDetails')(var.get('startPos')))
        var.put('endPosDetails', var.get('peg$computePosDetails')(var.get('endPos')))
        return Js({'start':Js({'offset':var.get('startPos'),'line':var.get('startPosDetails').get('line'),'column':var.get('startPosDetails').get('column')}),'end':Js({'offset':var.get('endPos'),'line':var.get('endPosDetails').get('line'),'column':var.get('endPosDetails').get('column')})})
    PyJsHoistedNonPyName.func_name = 'peg$computeLocation'
    var.put('peg$computeLocation', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(expected, this, arguments, var=var):
        var = Scope({'expected':expected, 'this':this, 'arguments':arguments}, var)
        var.registers(['expected'])
        if (var.get('peg$currPos')<var.get('peg$maxFailPos')):
            return var.get('undefined')
        if (var.get('peg$currPos')>var.get('peg$maxFailPos')):
            var.put('peg$maxFailPos', var.get('peg$currPos'))
            var.put('peg$maxFailExpected', Js([]))
        var.get('peg$maxFailExpected').callprop('push', var.get('expected'))
    PyJsHoistedNonPyName.func_name = 'peg$fail'
    var.put('peg$fail', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(message, location, this, arguments, var=var):
        var = Scope({'message':message, 'location':location, 'this':this, 'arguments':arguments}, var)
        var.registers(['location', 'message'])
        return var.get('peg$SyntaxError').create(var.get('message'), var.get(u"null"), var.get(u"null"), var.get('location'))
    PyJsHoistedNonPyName.func_name = 'peg$buildSimpleError'
    var.put('peg$buildSimpleError', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(expected, found, location, this, arguments, var=var):
        var = Scope({'expected':expected, 'found':found, 'location':location, 'this':this, 'arguments':arguments}, var)
        var.registers(['location', 'expected', 'found'])
        return var.get('peg$SyntaxError').create(var.get('peg$SyntaxError').callprop('buildMessage', var.get('expected'), var.get('found')), var.get('expected'), var.get('found'), var.get('location'))
    PyJsHoistedNonPyName.func_name = 'peg$buildStructuredError'
    var.put('peg$buildStructuredError', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['s6', 's2', 's1', 's0', 's5', 's4', 's3', 's7'])
        pass
        var.put('s0', var.get('peg$currPos'))
        var.put('s1', var.get('peg$parseTerm')())
        if PyJsStrictNeq(var.get('s1'),var.get('peg$FAILED')):
            var.put('s2', Js([]))
            var.put('s3', var.get('peg$currPos'))
            var.put('s4', var.get('peg$parse_')())
            if PyJsStrictNeq(var.get('s4'),var.get('peg$FAILED')):
                if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(43.0)):
                    var.put('s5', var.get('peg$c0'))
                    (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                else:
                    var.put('s5', var.get('peg$FAILED'))
                    if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                        var.get('peg$fail')(var.get('peg$c1'))
                if PyJsStrictEq(var.get('s5'),var.get('peg$FAILED')):
                    if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(45.0)):
                        var.put('s5', var.get('peg$c2'))
                        (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                    else:
                        var.put('s5', var.get('peg$FAILED'))
                        if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                            var.get('peg$fail')(var.get('peg$c3'))
                if PyJsStrictNeq(var.get('s5'),var.get('peg$FAILED')):
                    var.put('s6', var.get('peg$parse_')())
                    if PyJsStrictNeq(var.get('s6'),var.get('peg$FAILED')):
                        var.put('s7', var.get('peg$parseTerm')())
                        if PyJsStrictNeq(var.get('s7'),var.get('peg$FAILED')):
                            var.put('s4', Js([var.get('s4'), var.get('s5'), var.get('s6'), var.get('s7')]))
                            var.put('s3', var.get('s4'))
                        else:
                            var.put('peg$currPos', var.get('s3'))
                            var.put('s3', var.get('peg$FAILED'))
                    else:
                        var.put('peg$currPos', var.get('s3'))
                        var.put('s3', var.get('peg$FAILED'))
                else:
                    var.put('peg$currPos', var.get('s3'))
                    var.put('s3', var.get('peg$FAILED'))
            else:
                var.put('peg$currPos', var.get('s3'))
                var.put('s3', var.get('peg$FAILED'))
            while PyJsStrictNeq(var.get('s3'),var.get('peg$FAILED')):
                var.get('s2').callprop('push', var.get('s3'))
                var.put('s3', var.get('peg$currPos'))
                var.put('s4', var.get('peg$parse_')())
                if PyJsStrictNeq(var.get('s4'),var.get('peg$FAILED')):
                    if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(43.0)):
                        var.put('s5', var.get('peg$c0'))
                        (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                    else:
                        var.put('s5', var.get('peg$FAILED'))
                        if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                            var.get('peg$fail')(var.get('peg$c1'))
                    if PyJsStrictEq(var.get('s5'),var.get('peg$FAILED')):
                        if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(45.0)):
                            var.put('s5', var.get('peg$c2'))
                            (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                        else:
                            var.put('s5', var.get('peg$FAILED'))
                            if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                                var.get('peg$fail')(var.get('peg$c3'))
                    if PyJsStrictNeq(var.get('s5'),var.get('peg$FAILED')):
                        var.put('s6', var.get('peg$parse_')())
                        if PyJsStrictNeq(var.get('s6'),var.get('peg$FAILED')):
                            var.put('s7', var.get('peg$parseTerm')())
                            if PyJsStrictNeq(var.get('s7'),var.get('peg$FAILED')):
                                var.put('s4', Js([var.get('s4'), var.get('s5'), var.get('s6'), var.get('s7')]))
                                var.put('s3', var.get('s4'))
                            else:
                                var.put('peg$currPos', var.get('s3'))
                                var.put('s3', var.get('peg$FAILED'))
                        else:
                            var.put('peg$currPos', var.get('s3'))
                            var.put('s3', var.get('peg$FAILED'))
                    else:
                        var.put('peg$currPos', var.get('s3'))
                        var.put('s3', var.get('peg$FAILED'))
                else:
                    var.put('peg$currPos', var.get('s3'))
                    var.put('s3', var.get('peg$FAILED'))
            if PyJsStrictNeq(var.get('s2'),var.get('peg$FAILED')):
                var.put('peg$savedPos', var.get('s0'))
                var.put('s1', var.get('peg$c4')(var.get('s1'), var.get('s2')))
                var.put('s0', var.get('s1'))
            else:
                var.put('peg$currPos', var.get('s0'))
                var.put('s0', var.get('peg$FAILED'))
        else:
            var.put('peg$currPos', var.get('s0'))
            var.put('s0', var.get('peg$FAILED'))
        return var.get('s0')
    PyJsHoistedNonPyName.func_name = 'peg$parseExpression'
    var.put('peg$parseExpression', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['s6', 's2', 's1', 's0', 's5', 's4', 's3', 's7'])
        pass
        var.put('s0', var.get('peg$currPos'))
        var.put('s1', var.get('peg$parseFactor')())
        if PyJsStrictNeq(var.get('s1'),var.get('peg$FAILED')):
            var.put('s2', Js([]))
            var.put('s3', var.get('peg$currPos'))
            var.put('s4', var.get('peg$parse_')())
            if PyJsStrictNeq(var.get('s4'),var.get('peg$FAILED')):
                if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(42.0)):
                    var.put('s5', var.get('peg$c5'))
                    (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                else:
                    var.put('s5', var.get('peg$FAILED'))
                    if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                        var.get('peg$fail')(var.get('peg$c6'))
                if PyJsStrictEq(var.get('s5'),var.get('peg$FAILED')):
                    if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(47.0)):
                        var.put('s5', var.get('peg$c7'))
                        (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                    else:
                        var.put('s5', var.get('peg$FAILED'))
                        if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                            var.get('peg$fail')(var.get('peg$c8'))
                if PyJsStrictNeq(var.get('s5'),var.get('peg$FAILED')):
                    var.put('s6', var.get('peg$parse_')())
                    if PyJsStrictNeq(var.get('s6'),var.get('peg$FAILED')):
                        var.put('s7', var.get('peg$parseFactor')())
                        if PyJsStrictNeq(var.get('s7'),var.get('peg$FAILED')):
                            var.put('s4', Js([var.get('s4'), var.get('s5'), var.get('s6'), var.get('s7')]))
                            var.put('s3', var.get('s4'))
                        else:
                            var.put('peg$currPos', var.get('s3'))
                            var.put('s3', var.get('peg$FAILED'))
                    else:
                        var.put('peg$currPos', var.get('s3'))
                        var.put('s3', var.get('peg$FAILED'))
                else:
                    var.put('peg$currPos', var.get('s3'))
                    var.put('s3', var.get('peg$FAILED'))
            else:
                var.put('peg$currPos', var.get('s3'))
                var.put('s3', var.get('peg$FAILED'))
            while PyJsStrictNeq(var.get('s3'),var.get('peg$FAILED')):
                var.get('s2').callprop('push', var.get('s3'))
                var.put('s3', var.get('peg$currPos'))
                var.put('s4', var.get('peg$parse_')())
                if PyJsStrictNeq(var.get('s4'),var.get('peg$FAILED')):
                    if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(42.0)):
                        var.put('s5', var.get('peg$c5'))
                        (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                    else:
                        var.put('s5', var.get('peg$FAILED'))
                        if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                            var.get('peg$fail')(var.get('peg$c6'))
                    if PyJsStrictEq(var.get('s5'),var.get('peg$FAILED')):
                        if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(47.0)):
                            var.put('s5', var.get('peg$c7'))
                            (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                        else:
                            var.put('s5', var.get('peg$FAILED'))
                            if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                                var.get('peg$fail')(var.get('peg$c8'))
                    if PyJsStrictNeq(var.get('s5'),var.get('peg$FAILED')):
                        var.put('s6', var.get('peg$parse_')())
                        if PyJsStrictNeq(var.get('s6'),var.get('peg$FAILED')):
                            var.put('s7', var.get('peg$parseFactor')())
                            if PyJsStrictNeq(var.get('s7'),var.get('peg$FAILED')):
                                var.put('s4', Js([var.get('s4'), var.get('s5'), var.get('s6'), var.get('s7')]))
                                var.put('s3', var.get('s4'))
                            else:
                                var.put('peg$currPos', var.get('s3'))
                                var.put('s3', var.get('peg$FAILED'))
                        else:
                            var.put('peg$currPos', var.get('s3'))
                            var.put('s3', var.get('peg$FAILED'))
                    else:
                        var.put('peg$currPos', var.get('s3'))
                        var.put('s3', var.get('peg$FAILED'))
                else:
                    var.put('peg$currPos', var.get('s3'))
                    var.put('s3', var.get('peg$FAILED'))
            if PyJsStrictNeq(var.get('s2'),var.get('peg$FAILED')):
                var.put('peg$savedPos', var.get('s0'))
                var.put('s1', var.get('peg$c9')(var.get('s1'), var.get('s2')))
                var.put('s0', var.get('s1'))
            else:
                var.put('peg$currPos', var.get('s0'))
                var.put('s0', var.get('peg$FAILED'))
        else:
            var.put('peg$currPos', var.get('s0'))
            var.put('s0', var.get('peg$FAILED'))
        return var.get('s0')
    PyJsHoistedNonPyName.func_name = 'peg$parseTerm'
    var.put('peg$parseTerm', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['s2', 's1', 's0', 's5', 's4', 's3'])
        pass
        var.put('s0', var.get('peg$currPos'))
        if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(40.0)):
            var.put('s1', var.get('peg$c10'))
            (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
        else:
            var.put('s1', var.get('peg$FAILED'))
            if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                var.get('peg$fail')(var.get('peg$c11'))
        if PyJsStrictNeq(var.get('s1'),var.get('peg$FAILED')):
            var.put('s2', var.get('peg$parse_')())
            if PyJsStrictNeq(var.get('s2'),var.get('peg$FAILED')):
                var.put('s3', var.get('peg$parseExpression')())
                if PyJsStrictNeq(var.get('s3'),var.get('peg$FAILED')):
                    var.put('s4', var.get('peg$parse_')())
                    if PyJsStrictNeq(var.get('s4'),var.get('peg$FAILED')):
                        if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(41.0)):
                            var.put('s5', var.get('peg$c12'))
                            (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                        else:
                            var.put('s5', var.get('peg$FAILED'))
                            if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                                var.get('peg$fail')(var.get('peg$c13'))
                        if PyJsStrictNeq(var.get('s5'),var.get('peg$FAILED')):
                            var.put('peg$savedPos', var.get('s0'))
                            var.put('s1', var.get('peg$c14')(var.get('s3')))
                            var.put('s0', var.get('s1'))
                        else:
                            var.put('peg$currPos', var.get('s0'))
                            var.put('s0', var.get('peg$FAILED'))
                    else:
                        var.put('peg$currPos', var.get('s0'))
                        var.put('s0', var.get('peg$FAILED'))
                else:
                    var.put('peg$currPos', var.get('s0'))
                    var.put('s0', var.get('peg$FAILED'))
            else:
                var.put('peg$currPos', var.get('s0'))
                var.put('s0', var.get('peg$FAILED'))
        else:
            var.put('peg$currPos', var.get('s0'))
            var.put('s0', var.get('peg$FAILED'))
        if PyJsStrictEq(var.get('s0'),var.get('peg$FAILED')):
            var.put('s0', var.get('peg$currPos'))
            var.put('s1', var.get('peg$parseString')())
            if PyJsStrictNeq(var.get('s1'),var.get('peg$FAILED')):
                var.put('peg$savedPos', var.get('s0'))
                var.put('s1', var.get('peg$c15')(var.get('s1')))
            var.put('s0', var.get('s1'))
            if PyJsStrictEq(var.get('s0'),var.get('peg$FAILED')):
                var.put('s0', var.get('peg$currPos'))
                var.put('s1', var.get('peg$parseNumber')())
                if PyJsStrictNeq(var.get('s1'),var.get('peg$FAILED')):
                    var.put('peg$savedPos', var.get('s0'))
                    var.put('s1', var.get('peg$c16')(var.get('s1')))
                var.put('s0', var.get('s1'))
        return var.get('s0')
    PyJsHoistedNonPyName.func_name = 'peg$parseFactor'
    var.put('peg$parseFactor', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['s6', 's2', 's1', 's0', 's5', 's4', 's3'])
        pass
        (var.put('peg$silentFails',Js(var.get('peg$silentFails').to_number())+Js(1))-Js(1))
        var.put('s0', var.get('peg$currPos'))
        if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(34.0)):
            var.put('s1', var.get('peg$c18'))
            (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
        else:
            var.put('s1', var.get('peg$FAILED'))
            if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                var.get('peg$fail')(var.get('peg$c19'))
        if PyJsStrictNeq(var.get('s1'),var.get('peg$FAILED')):
            var.put('s2', var.get('peg$currPos'))
            var.put('s3', Js([]))
            var.put('s4', var.get('peg$currPos'))
            var.put('s5', var.get('peg$currPos'))
            (var.put('peg$silentFails',Js(var.get('peg$silentFails').to_number())+Js(1))-Js(1))
            if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(34.0)):
                var.put('s6', var.get('peg$c18'))
                (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
            else:
                var.put('s6', var.get('peg$FAILED'))
                if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                    var.get('peg$fail')(var.get('peg$c19'))
            (var.put('peg$silentFails',Js(var.get('peg$silentFails').to_number())-Js(1))+Js(1))
            if PyJsStrictEq(var.get('s6'),var.get('peg$FAILED')):
                var.put('s5', PyJsComma(Js(0.0), Js(None)))
            else:
                var.put('peg$currPos', var.get('s5'))
                var.put('s5', var.get('peg$FAILED'))
            if PyJsStrictNeq(var.get('s5'),var.get('peg$FAILED')):
                if (var.get('input').get('length')>var.get('peg$currPos')):
                    var.put('s6', var.get('input').callprop('charAt', var.get('peg$currPos')))
                    (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                else:
                    var.put('s6', var.get('peg$FAILED'))
                    if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                        var.get('peg$fail')(var.get('peg$c20'))
                if PyJsStrictNeq(var.get('s6'),var.get('peg$FAILED')):
                    var.put('s5', Js([var.get('s5'), var.get('s6')]))
                    var.put('s4', var.get('s5'))
                else:
                    var.put('peg$currPos', var.get('s4'))
                    var.put('s4', var.get('peg$FAILED'))
            else:
                var.put('peg$currPos', var.get('s4'))
                var.put('s4', var.get('peg$FAILED'))
            while PyJsStrictNeq(var.get('s4'),var.get('peg$FAILED')):
                var.get('s3').callprop('push', var.get('s4'))
                var.put('s4', var.get('peg$currPos'))
                var.put('s5', var.get('peg$currPos'))
                (var.put('peg$silentFails',Js(var.get('peg$silentFails').to_number())+Js(1))-Js(1))
                if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(34.0)):
                    var.put('s6', var.get('peg$c18'))
                    (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                else:
                    var.put('s6', var.get('peg$FAILED'))
                    if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                        var.get('peg$fail')(var.get('peg$c19'))
                (var.put('peg$silentFails',Js(var.get('peg$silentFails').to_number())-Js(1))+Js(1))
                if PyJsStrictEq(var.get('s6'),var.get('peg$FAILED')):
                    var.put('s5', PyJsComma(Js(0.0), Js(None)))
                else:
                    var.put('peg$currPos', var.get('s5'))
                    var.put('s5', var.get('peg$FAILED'))
                if PyJsStrictNeq(var.get('s5'),var.get('peg$FAILED')):
                    if (var.get('input').get('length')>var.get('peg$currPos')):
                        var.put('s6', var.get('input').callprop('charAt', var.get('peg$currPos')))
                        (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                    else:
                        var.put('s6', var.get('peg$FAILED'))
                        if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                            var.get('peg$fail')(var.get('peg$c20'))
                    if PyJsStrictNeq(var.get('s6'),var.get('peg$FAILED')):
                        var.put('s5', Js([var.get('s5'), var.get('s6')]))
                        var.put('s4', var.get('s5'))
                    else:
                        var.put('peg$currPos', var.get('s4'))
                        var.put('s4', var.get('peg$FAILED'))
                else:
                    var.put('peg$currPos', var.get('s4'))
                    var.put('s4', var.get('peg$FAILED'))
            if PyJsStrictNeq(var.get('s3'),var.get('peg$FAILED')):
                var.put('s2', var.get('input').callprop('substring', var.get('s2'), var.get('peg$currPos')))
            else:
                var.put('s2', var.get('s3'))
            if PyJsStrictNeq(var.get('s2'),var.get('peg$FAILED')):
                if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(34.0)):
                    var.put('s3', var.get('peg$c18'))
                    (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                else:
                    var.put('s3', var.get('peg$FAILED'))
                    if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                        var.get('peg$fail')(var.get('peg$c19'))
                if PyJsStrictNeq(var.get('s3'),var.get('peg$FAILED')):
                    var.put('peg$savedPos', var.get('s0'))
                    var.put('s1', var.get('peg$c21')(var.get('s2')))
                    var.put('s0', var.get('s1'))
                else:
                    var.put('peg$currPos', var.get('s0'))
                    var.put('s0', var.get('peg$FAILED'))
            else:
                var.put('peg$currPos', var.get('s0'))
                var.put('s0', var.get('peg$FAILED'))
        else:
            var.put('peg$currPos', var.get('s0'))
            var.put('s0', var.get('peg$FAILED'))
        (var.put('peg$silentFails',Js(var.get('peg$silentFails').to_number())-Js(1))+Js(1))
        if PyJsStrictEq(var.get('s0'),var.get('peg$FAILED')):
            var.put('s1', var.get('peg$FAILED'))
            if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                var.get('peg$fail')(var.get('peg$c17'))
        return var.get('s0')
    PyJsHoistedNonPyName.func_name = 'peg$parseString'
    var.put('peg$parseString', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['s6', 's2', 's1', 's0', 's5', 's4', 's3'])
        pass
        (var.put('peg$silentFails',Js(var.get('peg$silentFails').to_number())+Js(1))-Js(1))
        var.put('s0', var.get('peg$currPos'))
        var.put('s1', var.get('peg$parse_')())
        if PyJsStrictNeq(var.get('s1'),var.get('peg$FAILED')):
            var.put('s2', Js([]))
            if var.get('peg$c23').callprop('test', var.get('input').callprop('charAt', var.get('peg$currPos'))):
                var.put('s3', var.get('input').callprop('charAt', var.get('peg$currPos')))
                (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
            else:
                var.put('s3', var.get('peg$FAILED'))
                if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                    var.get('peg$fail')(var.get('peg$c24'))
            if PyJsStrictNeq(var.get('s3'),var.get('peg$FAILED')):
                while PyJsStrictNeq(var.get('s3'),var.get('peg$FAILED')):
                    var.get('s2').callprop('push', var.get('s3'))
                    if var.get('peg$c23').callprop('test', var.get('input').callprop('charAt', var.get('peg$currPos'))):
                        var.put('s3', var.get('input').callprop('charAt', var.get('peg$currPos')))
                        (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                    else:
                        var.put('s3', var.get('peg$FAILED'))
                        if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                            var.get('peg$fail')(var.get('peg$c24'))
            else:
                var.put('s2', var.get('peg$FAILED'))
            if PyJsStrictNeq(var.get('s2'),var.get('peg$FAILED')):
                var.put('s3', var.get('peg$currPos'))
                if PyJsStrictEq(var.get('input').callprop('charCodeAt', var.get('peg$currPos')),Js(46.0)):
                    var.put('s4', var.get('peg$c25'))
                    (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                else:
                    var.put('s4', var.get('peg$FAILED'))
                    if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                        var.get('peg$fail')(var.get('peg$c26'))
                if PyJsStrictNeq(var.get('s4'),var.get('peg$FAILED')):
                    var.put('s5', Js([]))
                    if var.get('peg$c23').callprop('test', var.get('input').callprop('charAt', var.get('peg$currPos'))):
                        var.put('s6', var.get('input').callprop('charAt', var.get('peg$currPos')))
                        (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                    else:
                        var.put('s6', var.get('peg$FAILED'))
                        if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                            var.get('peg$fail')(var.get('peg$c24'))
                    if PyJsStrictNeq(var.get('s6'),var.get('peg$FAILED')):
                        while PyJsStrictNeq(var.get('s6'),var.get('peg$FAILED')):
                            var.get('s5').callprop('push', var.get('s6'))
                            if var.get('peg$c23').callprop('test', var.get('input').callprop('charAt', var.get('peg$currPos'))):
                                var.put('s6', var.get('input').callprop('charAt', var.get('peg$currPos')))
                                (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
                            else:
                                var.put('s6', var.get('peg$FAILED'))
                                if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                                    var.get('peg$fail')(var.get('peg$c24'))
                    else:
                        var.put('s5', var.get('peg$FAILED'))
                    if PyJsStrictNeq(var.get('s5'),var.get('peg$FAILED')):
                        var.put('s4', Js([var.get('s4'), var.get('s5')]))
                        var.put('s3', var.get('s4'))
                    else:
                        var.put('peg$currPos', var.get('s3'))
                        var.put('s3', var.get('peg$FAILED'))
                else:
                    var.put('peg$currPos', var.get('s3'))
                    var.put('s3', var.get('peg$FAILED'))
                if PyJsStrictEq(var.get('s3'),var.get('peg$FAILED')):
                    var.put('s3', var.get(u"null"))
                if PyJsStrictNeq(var.get('s3'),var.get('peg$FAILED')):
                    var.put('peg$savedPos', var.get('s0'))
                    var.put('s1', var.get('peg$c27')())
                    var.put('s0', var.get('s1'))
                else:
                    var.put('peg$currPos', var.get('s0'))
                    var.put('s0', var.get('peg$FAILED'))
            else:
                var.put('peg$currPos', var.get('s0'))
                var.put('s0', var.get('peg$FAILED'))
        else:
            var.put('peg$currPos', var.get('s0'))
            var.put('s0', var.get('peg$FAILED'))
        (var.put('peg$silentFails',Js(var.get('peg$silentFails').to_number())-Js(1))+Js(1))
        if PyJsStrictEq(var.get('s0'),var.get('peg$FAILED')):
            var.put('s1', var.get('peg$FAILED'))
            if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                var.get('peg$fail')(var.get('peg$c22'))
        return var.get('s0')
    PyJsHoistedNonPyName.func_name = 'peg$parseNumber'
    var.put('peg$parseNumber', PyJsHoistedNonPyName)
    @Js
    def PyJsHoistedNonPyName(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['s0', 's1'])
        pass
        (var.put('peg$silentFails',Js(var.get('peg$silentFails').to_number())+Js(1))-Js(1))
        var.put('s0', Js([]))
        if var.get('peg$c29').callprop('test', var.get('input').callprop('charAt', var.get('peg$currPos'))):
            var.put('s1', var.get('input').callprop('charAt', var.get('peg$currPos')))
            (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
        else:
            var.put('s1', var.get('peg$FAILED'))
            if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                var.get('peg$fail')(var.get('peg$c30'))
        while PyJsStrictNeq(var.get('s1'),var.get('peg$FAILED')):
            var.get('s0').callprop('push', var.get('s1'))
            if var.get('peg$c29').callprop('test', var.get('input').callprop('charAt', var.get('peg$currPos'))):
                var.put('s1', var.get('input').callprop('charAt', var.get('peg$currPos')))
                (var.put('peg$currPos',Js(var.get('peg$currPos').to_number())+Js(1))-Js(1))
            else:
                var.put('s1', var.get('peg$FAILED'))
                if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                    var.get('peg$fail')(var.get('peg$c30'))
        (var.put('peg$silentFails',Js(var.get('peg$silentFails').to_number())-Js(1))+Js(1))
        if PyJsStrictEq(var.get('s0'),var.get('peg$FAILED')):
            var.put('s1', var.get('peg$FAILED'))
            if PyJsStrictEq(var.get('peg$silentFails'),Js(0.0)):
                var.get('peg$fail')(var.get('peg$c28'))
        return var.get('s0')
    PyJsHoistedNonPyName.func_name = 'peg$parse_'
    var.put('peg$parse_', PyJsHoistedNonPyName)
    var.put('options', (var.get('options') if PyJsStrictNeq(var.get('options'),PyJsComma(Js(0.0), Js(None))) else Js({})))
    var.put('peg$FAILED', Js({}))
    var.put('peg$startRuleFunctions', Js({'Expression':var.get('peg$parseExpression')}))
    var.put('peg$startRuleFunction', var.get('peg$parseExpression'))
    var.put('peg$c0', Js('+'))
    var.put('peg$c1', var.get('peg$literalExpectation')(Js('+'), Js(False)))
    var.put('peg$c2', Js('-'))
    var.put('peg$c3', var.get('peg$literalExpectation')(Js('-'), Js(False)))
    @Js
    def PyJs_anonymous_12_(head, tail, this, arguments, var=var):
        var = Scope({'head':head, 'tail':tail, 'this':this, 'arguments':arguments}, var)
        var.registers(['head', 'tail'])
        @Js
        def PyJs_anonymous_13_(result, element, this, arguments, var=var):
            var = Scope({'result':result, 'element':element, 'this':this, 'arguments':arguments}, var)
            var.registers(['element', 'result'])
            if PyJsStrictEq(var.get('element').get('1'),Js('+')):
                return (var.get('result')+var.get('element').get('3'))
            if PyJsStrictEq(var.get('element').get('1'),Js('-')):
                return (var.get('result')-var.get('element').get('3'))
        PyJs_anonymous_13_._set_name('anonymous')
        return var.get('tail').callprop('reduce', PyJs_anonymous_13_, var.get('head'))
    PyJs_anonymous_12_._set_name('anonymous')
    var.put('peg$c4', PyJs_anonymous_12_)
    var.put('peg$c5', Js('*'))
    var.put('peg$c6', var.get('peg$literalExpectation')(Js('*'), Js(False)))
    var.put('peg$c7', Js('/'))
    var.put('peg$c8', var.get('peg$literalExpectation')(Js('/'), Js(False)))
    @Js
    def PyJs_anonymous_14_(head, tail, this, arguments, var=var):
        var = Scope({'head':head, 'tail':tail, 'this':this, 'arguments':arguments}, var)
        var.registers(['head', 'tail'])
        @Js
        def PyJs_anonymous_15_(result, element, this, arguments, var=var):
            var = Scope({'result':result, 'element':element, 'this':this, 'arguments':arguments}, var)
            var.registers(['element', 'result'])
            if PyJsStrictEq(var.get('element').get('1'),Js('*')):
                return (var.get('result')*var.get('element').get('3'))
            if PyJsStrictEq(var.get('element').get('1'),Js('/')):
                return (var.get('result')/var.get('element').get('3'))
        PyJs_anonymous_15_._set_name('anonymous')
        return var.get('tail').callprop('reduce', PyJs_anonymous_15_, var.get('head'))
    PyJs_anonymous_14_._set_name('anonymous')
    var.put('peg$c9', PyJs_anonymous_14_)
    var.put('peg$c10', Js('('))
    var.put('peg$c11', var.get('peg$literalExpectation')(Js('('), Js(False)))
    var.put('peg$c12', Js(')'))
    var.put('peg$c13', var.get('peg$literalExpectation')(Js(')'), Js(False)))
    @Js
    def PyJs_anonymous_16_(expr, this, arguments, var=var):
        var = Scope({'expr':expr, 'this':this, 'arguments':arguments}, var)
        var.registers(['expr'])
        return var.get('expr')
    PyJs_anonymous_16_._set_name('anonymous')
    var.put('peg$c14', PyJs_anonymous_16_)
    @Js
    def PyJs_anonymous_17_(str, this, arguments, var=var):
        var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
        var.registers(['str'])
        return var.get('str')
    PyJs_anonymous_17_._set_name('anonymous')
    var.put('peg$c15', PyJs_anonymous_17_)
    @Js
    def PyJs_anonymous_18_(num, this, arguments, var=var):
        var = Scope({'num':num, 'this':this, 'arguments':arguments}, var)
        var.registers(['num'])
        return var.get('num')
    PyJs_anonymous_18_._set_name('anonymous')
    var.put('peg$c16', PyJs_anonymous_18_)
    var.put('peg$c17', var.get('peg$otherExpectation')(Js('string')))
    var.put('peg$c18', Js('"'))
    var.put('peg$c19', var.get('peg$literalExpectation')(Js('"'), Js(False)))
    var.put('peg$c20', var.get('peg$anyExpectation')())
    @Js
    def PyJs_anonymous_19_(content, this, arguments, var=var):
        var = Scope({'content':content, 'this':this, 'arguments':arguments}, var)
        var.registers(['content'])
        return var.get('content')
    PyJs_anonymous_19_._set_name('anonymous')
    var.put('peg$c21', PyJs_anonymous_19_)
    var.put('peg$c22', var.get('peg$otherExpectation')(Js('number')))
    var.put('peg$c23', JsRegExp('/^[0-9]/'))
    var.put('peg$c24', var.get('peg$classExpectation')(Js([Js([Js('0'), Js('9')])]), Js(False), Js(False)))
    var.put('peg$c25', Js('.'))
    var.put('peg$c26', var.get('peg$literalExpectation')(Js('.'), Js(False)))
    @Js
    def PyJs_anonymous_20_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return var.get('parseFloat')(var.get('text')())
    PyJs_anonymous_20_._set_name('anonymous')
    var.put('peg$c27', PyJs_anonymous_20_)
    var.put('peg$c28', var.get('peg$otherExpectation')(Js('whitespace')))
    var.put('peg$c29', JsRegExp('/^[ \\t\\n\\r]/'))
    var.put('peg$c30', var.get('peg$classExpectation')(Js([Js(' '), Js('\t'), Js('\n'), Js('\r')]), Js(False), Js(False)))
    var.put('peg$currPos', Js(0.0))
    var.put('peg$savedPos', Js(0.0))
    var.put('peg$posDetailsCache', Js([Js({'line':Js(1.0),'column':Js(1.0)})]))
    var.put('peg$maxFailPos', Js(0.0))
    var.put('peg$maxFailExpected', Js([]))
    var.put('peg$silentFails', Js(0.0))
    if var.get('options').contains(Js('startRule')):
        if var.get('peg$startRuleFunctions').contains(var.get('options').get('startRule')).neg():
            PyJsTempException = JsToPyException(var.get('Error').create(((Js('Can\'t start parsing from rule "')+var.get('options').get('startRule'))+Js('".'))))
            raise PyJsTempException
        var.put('peg$startRuleFunction', var.get('peg$startRuleFunctions').get(var.get('options').get('startRule')))
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    var.put('peg$result', var.get('peg$startRuleFunction')())
    if (PyJsStrictNeq(var.get('peg$result'),var.get('peg$FAILED')) and PyJsStrictEq(var.get('peg$currPos'),var.get('input').get('length'))):
        return var.get('peg$result')
    else:
        if (PyJsStrictNeq(var.get('peg$result'),var.get('peg$FAILED')) and (var.get('peg$currPos')<var.get('input').get('length'))):
            var.get('peg$fail')(var.get('peg$endExpectation')())
        def PyJs_LONG_21_(var=var):
            return var.get('peg$buildStructuredError')(var.get('peg$maxFailExpected'), (var.get('input').callprop('charAt', var.get('peg$maxFailPos')) if (var.get('peg$maxFailPos')<var.get('input').get('length')) else var.get(u"null")), (var.get('peg$computeLocation')(var.get('peg$maxFailPos'), (var.get('peg$maxFailPos')+Js(1.0))) if (var.get('peg$maxFailPos')<var.get('input').get('length')) else var.get('peg$computeLocation')(var.get('peg$maxFailPos'), var.get('peg$maxFailPos'))))
        PyJsTempException = JsToPyException(PyJs_LONG_21_())
        raise PyJsTempException
PyJsHoistedNonPyName.func_name = 'peg$parse'
var.put('peg$parse', PyJsHoistedNonPyName)
Js('use strict')
pass
pass
var.get('peg$subclass')(var.get('peg$SyntaxError'), var.get('Error'))
@Js
def PyJs_anonymous_0_(expected, found, this, arguments, var=var):
    var = Scope({'expected':expected, 'found':found, 'this':this, 'arguments':arguments}, var)
    var.registers(['hex', 'describeExpected', 'literalEscape', 'expected', 'found', 'DESCRIBE_EXPECTATION_FNS', 'describeFound', 'classEscape', 'describeExpectation'])
    @Js
    def PyJsHoisted_hex_(ch, this, arguments, var=var):
        var = Scope({'ch':ch, 'this':this, 'arguments':arguments}, var)
        var.registers(['ch'])
        return var.get('ch').callprop('charCodeAt', Js(0.0)).callprop('toString', Js(16.0)).callprop('toUpperCase')
    PyJsHoisted_hex_.func_name = 'hex'
    var.put('hex', PyJsHoisted_hex_)
    @Js
    def PyJsHoisted_literalEscape_(s, this, arguments, var=var):
        var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['s'])
        def PyJs_LONG_8_(var=var):
            @Js
            def PyJs_anonymous_6_(ch, this, arguments, var=var):
                var = Scope({'ch':ch, 'this':this, 'arguments':arguments}, var)
                var.registers(['ch'])
                return (Js('\\x')+var.get('hex')(var.get('ch')))
            PyJs_anonymous_6_._set_name('anonymous')
            @Js
            def PyJs_anonymous_7_(ch, this, arguments, var=var):
                var = Scope({'ch':ch, 'this':this, 'arguments':arguments}, var)
                var.registers(['ch'])
                return (Js('\\x0')+var.get('hex')(var.get('ch')))
            PyJs_anonymous_7_._set_name('anonymous')
            return var.get('s').callprop('replace', JsRegExp('/\\\\/g'), Js('\\\\')).callprop('replace', JsRegExp('/"/g'), Js('\\"')).callprop('replace', JsRegExp('/\\0/g'), Js('\\0')).callprop('replace', JsRegExp('/\\t/g'), Js('\\t')).callprop('replace', JsRegExp('/\\n/g'), Js('\\n')).callprop('replace', JsRegExp('/\\r/g'), Js('\\r')).callprop('replace', JsRegExp('/[\\x00-\\x0F]/g'), PyJs_anonymous_7_).callprop('replace', JsRegExp('/[\\x10-\\x1F\\x7F-\\x9F]/g'), PyJs_anonymous_6_)
        return PyJs_LONG_8_()
    PyJsHoisted_literalEscape_.func_name = 'literalEscape'
    var.put('literalEscape', PyJsHoisted_literalEscape_)
    @Js
    def PyJsHoisted_classEscape_(s, this, arguments, var=var):
        var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['s'])
        @Js
        def PyJs_anonymous_9_(ch, this, arguments, var=var):
            var = Scope({'ch':ch, 'this':this, 'arguments':arguments}, var)
            var.registers(['ch'])
            return (Js('\\x')+var.get('hex')(var.get('ch')))
        PyJs_anonymous_9_._set_name('anonymous')
        @Js
        def PyJs_anonymous_10_(ch, this, arguments, var=var):
            var = Scope({'ch':ch, 'this':this, 'arguments':arguments}, var)
            var.registers(['ch'])
            return (Js('\\x0')+var.get('hex')(var.get('ch')))
        PyJs_anonymous_10_._set_name('anonymous')
        def PyJs_LONG_11_(var=var):
            return var.get('s').callprop('replace', JsRegExp('/\\\\/g'), Js('\\\\')).callprop('replace', JsRegExp('/\\]/g'), Js('\\]')).callprop('replace', JsRegExp('/\\^/g'), Js('\\^')).callprop('replace', JsRegExp('/-/g'), Js('\\-')).callprop('replace', JsRegExp('/\\0/g'), Js('\\0')).callprop('replace', JsRegExp('/\\t/g'), Js('\\t')).callprop('replace', JsRegExp('/\\n/g'), Js('\\n')).callprop('replace', JsRegExp('/\\r/g'), Js('\\r'))
        return PyJs_LONG_11_().callprop('replace', JsRegExp('/[\\x00-\\x0F]/g'), PyJs_anonymous_10_).callprop('replace', JsRegExp('/[\\x10-\\x1F\\x7F-\\x9F]/g'), PyJs_anonymous_9_)
    PyJsHoisted_classEscape_.func_name = 'classEscape'
    var.put('classEscape', PyJsHoisted_classEscape_)
    @Js
    def PyJsHoisted_describeExpectation_(expectation, this, arguments, var=var):
        var = Scope({'expectation':expectation, 'this':this, 'arguments':arguments}, var)
        var.registers(['expectation'])
        return var.get('DESCRIBE_EXPECTATION_FNS').callprop(var.get('expectation').get('type'), var.get('expectation'))
    PyJsHoisted_describeExpectation_.func_name = 'describeExpectation'
    var.put('describeExpectation', PyJsHoisted_describeExpectation_)
    @Js
    def PyJsHoisted_describeExpected_(expected, this, arguments, var=var):
        var = Scope({'expected':expected, 'this':this, 'arguments':arguments}, var)
        var.registers(['expected', 'i', 'descriptions', 'j'])
        var.put('descriptions', var.get('Array').create(var.get('expected').get('length')))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('expected').get('length')):
            var.get('descriptions').put(var.get('i'), var.get('describeExpectation')(var.get('expected').get(var.get('i'))))
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        var.get('descriptions').callprop('sort')
        if (var.get('descriptions').get('length')>Js(0.0)):
            #for JS loop
            PyJsComma(var.put('i', Js(1.0)),var.put('j', Js(1.0)))
            while (var.get('i')<var.get('descriptions').get('length')):
                if PyJsStrictNeq(var.get('descriptions').get((var.get('i')-Js(1.0))),var.get('descriptions').get(var.get('i'))):
                    var.get('descriptions').put(var.get('j'), var.get('descriptions').get(var.get('i')))
                    (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                # update
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.get('descriptions').put('length', var.get('j'))
        while 1:
            SWITCHED = False
            CONDITION = (var.get('descriptions').get('length'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                SWITCHED = True
                return var.get('descriptions').get('0')
            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                SWITCHED = True
                return ((var.get('descriptions').get('0')+Js(' or '))+var.get('descriptions').get('1'))
            if True:
                SWITCHED = True
                return ((var.get('descriptions').callprop('slice', Js(0.0), (-Js(1.0))).callprop('join', Js(', '))+Js(', or '))+var.get('descriptions').get((var.get('descriptions').get('length')-Js(1.0))))
            SWITCHED = True
            break
    PyJsHoisted_describeExpected_.func_name = 'describeExpected'
    var.put('describeExpected', PyJsHoisted_describeExpected_)
    @Js
    def PyJsHoisted_describeFound_(found, this, arguments, var=var):
        var = Scope({'found':found, 'this':this, 'arguments':arguments}, var)
        var.registers(['found'])
        return (((Js('"')+var.get('literalEscape')(var.get('found')))+Js('"')) if var.get('found') else Js('end of input'))
    PyJsHoisted_describeFound_.func_name = 'describeFound'
    var.put('describeFound', PyJsHoisted_describeFound_)
    @Js
    def PyJs_anonymous_1_(expectation, this, arguments, var=var):
        var = Scope({'expectation':expectation, 'this':this, 'arguments':arguments}, var)
        var.registers(['expectation'])
        return ((Js('"')+var.get('literalEscape')(var.get('expectation').get('text')))+Js('"'))
    PyJs_anonymous_1_._set_name('anonymous')
    @Js
    def PyJs_anonymous_2_(expectation, this, arguments, var=var):
        var = Scope({'expectation':expectation, 'this':this, 'arguments':arguments}, var)
        var.registers(['expectation', 'escapedParts', 'i'])
        var.put('escapedParts', Js(''))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('expectation').get('parts').get('length')):
            var.put('escapedParts', (((var.get('classEscape')(var.get('expectation').get('parts').get(var.get('i')).get('0'))+Js('-'))+var.get('classEscape')(var.get('expectation').get('parts').get(var.get('i')).get('1'))) if var.get('expectation').get('parts').get(var.get('i')).instanceof(var.get('Array')) else var.get('classEscape')(var.get('expectation').get('parts').get(var.get('i')))), '+')
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        return (((Js('[')+(Js('^') if var.get('expectation').get('inverted') else Js('')))+var.get('escapedParts'))+Js(']'))
    PyJs_anonymous_2_._set_name('anonymous')
    @Js
    def PyJs_anonymous_3_(expectation, this, arguments, var=var):
        var = Scope({'expectation':expectation, 'this':this, 'arguments':arguments}, var)
        var.registers(['expectation'])
        return Js('any character')
    PyJs_anonymous_3_._set_name('anonymous')
    @Js
    def PyJs_anonymous_4_(expectation, this, arguments, var=var):
        var = Scope({'expectation':expectation, 'this':this, 'arguments':arguments}, var)
        var.registers(['expectation'])
        return Js('end of input')
    PyJs_anonymous_4_._set_name('anonymous')
    @Js
    def PyJs_anonymous_5_(expectation, this, arguments, var=var):
        var = Scope({'expectation':expectation, 'this':this, 'arguments':arguments}, var)
        var.registers(['expectation'])
        return var.get('expectation').get('description')
    PyJs_anonymous_5_._set_name('anonymous')
    var.put('DESCRIBE_EXPECTATION_FNS', Js({'literal':PyJs_anonymous_1_,'class':PyJs_anonymous_2_,'any':PyJs_anonymous_3_,'end':PyJs_anonymous_4_,'other':PyJs_anonymous_5_}))
    pass
    pass
    pass
    pass
    pass
    pass
    return ((((Js('Expected ')+var.get('describeExpected')(var.get('expected')))+Js(' but '))+var.get('describeFound')(var.get('found')))+Js(' found.'))
PyJs_anonymous_0_._set_name('anonymous')
var.get('peg$SyntaxError').put('buildMessage', PyJs_anonymous_0_)
pass
var.put('processor', Js({'SyntaxError':var.get('peg$SyntaxError'),'parse':var.get('peg$parse')}))
pass


# Add lib to the module scope
dynamicprocessor = var.to_python()