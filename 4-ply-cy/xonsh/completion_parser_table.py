
# completion_parser_table.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ANY ATDOLLAR_LPAREN AT_LPAREN BANG_LBRACKET BANG_LPAREN DOLLAR_LBRACKET DOLLAR_LPAREN NEWLINE OR PIPE RBRACKET RPAREN SEMI STRINGcontext : command\n        | commands\n        command : args\n        |\n        commands : commandcommands : commands SEMI command\n\t| commands AND command\n\t| commands PIPE command\n\t| commands OR command\n\t| commands NEWLINE commandsub_expression : DOLLAR_LPAREN commands RPAREN\n\t| BANG_LPAREN commands RPAREN\n\t| ATDOLLAR_LPAREN commands RPAREN\n\t| DOLLAR_LBRACKET commands RBRACKET\n\t| BANG_LBRACKET commands RBRACKET\n\t| AT_LPAREN commands RPAREN\n        | DOLLAR_LPAREN commands\n\t| BANG_LPAREN commands\n\t| ATDOLLAR_LPAREN commands\n\t| DOLLAR_LBRACKET commands\n\t| BANG_LBRACKET commands\n\t| AT_LPAREN commands\n    arg : sub_expressionarg : DOLLAR_LPAREN\n\t| DOLLAR_LBRACKET\n\t| BANG_LPAREN\n\t| BANG_LBRACKET\n\t| ATDOLLAR_LPAREN\n\t| AT_LPAREN\n\t| STRING\n\t| ANYargs : argargs : args arg'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-4,0,-1,-2,-3,-32,-23,-4,-4,-4,-4,-4,-4,-30,-31,-4,-4,-4,-4,-4,-33,-17,-5,-20,-18,-21,-19,-22,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'SEMI':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-4,-5,15,-3,-32,-23,-4,-4,-4,-4,-4,-4,-30,-31,-4,-4,-4,-4,-4,-33,15,-5,15,15,15,15,15,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'AND':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-4,-5,16,-3,-32,-23,-4,-4,-4,-4,-4,-4,-30,-31,-4,-4,-4,-4,-4,-33,16,-5,16,16,16,16,16,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'PIPE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-4,-5,17,-3,-32,-23,-4,-4,-4,-4,-4,-4,-30,-31,-4,-4,-4,-4,-4,-33,17,-5,17,17,17,17,17,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'OR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-4,-5,18,-3,-32,-23,-4,-4,-4,-4,-4,-4,-30,-31,-4,-4,-4,-4,-4,-33,18,-5,18,18,18,18,18,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'NEWLINE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-4,-5,19,-3,-32,-23,-4,-4,-4,-4,-4,-4,-30,-31,-4,-4,-4,-4,-4,-33,19,-5,19,19,19,19,19,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'DOLLAR_LPAREN':([0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[7,7,-32,-23,7,7,7,7,7,7,-30,-31,7,7,7,7,7,-33,-17,-5,-20,-18,-21,-19,-22,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'DOLLAR_LBRACKET':([0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[8,8,-32,-23,8,8,8,8,8,8,-30,-31,8,8,8,8,8,-33,-17,-5,-20,-18,-21,-19,-22,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'BANG_LPAREN':([0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[9,9,-32,-23,9,9,9,9,9,9,-30,-31,9,9,9,9,9,-33,-17,-5,-20,-18,-21,-19,-22,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'BANG_LBRACKET':([0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[10,10,-32,-23,10,10,10,10,10,10,-30,-31,10,10,10,10,10,-33,-17,-5,-20,-18,-21,-19,-22,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'ATDOLLAR_LPAREN':([0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[11,11,-32,-23,11,11,11,11,11,11,-30,-31,11,11,11,11,11,-33,-17,-5,-20,-18,-21,-19,-22,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'AT_LPAREN':([0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[12,12,-32,-23,12,12,12,12,12,12,-30,-31,12,12,12,12,12,-33,-17,-5,-20,-18,-21,-19,-22,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'STRING':([0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[13,13,-32,-23,13,13,13,13,13,13,-30,-31,13,13,13,13,13,-33,-17,-5,-20,-18,-21,-19,-22,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'ANY':([0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[14,14,-32,-23,14,14,14,14,14,14,-30,-31,14,14,14,14,14,-33,-17,-5,-20,-18,-21,-19,-22,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'RPAREN':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-32,-23,-4,-4,-4,-4,-4,-4,-30,-31,-4,-4,-4,-4,-4,-33,33,-5,-20,35,-21,37,38,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),'RBRACKET':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-32,-23,-4,-4,-4,-4,-4,-4,-30,-31,-4,-4,-4,-4,-4,-33,-17,-5,34,-18,36,-19,-22,-6,-7,-8,-9,-10,-11,-14,-12,-15,-13,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'context':([0,],[1,]),'command':([0,7,8,9,10,11,12,15,16,17,18,19,],[2,22,22,22,22,22,22,28,29,30,31,32,]),'commands':([0,7,8,9,10,11,12,],[3,21,23,24,25,26,27,]),'args':([0,7,8,9,10,11,12,15,16,17,18,19,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'arg':([0,4,7,8,9,10,11,12,15,16,17,18,19,],[5,20,5,5,5,5,5,5,5,5,5,5,5,]),'sub_expression':([0,4,7,8,9,10,11,12,15,16,17,18,19,],[6,6,6,6,6,6,6,6,6,6,6,6,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> context","S'",1,None,None,None),
  ('context -> command','context',1,'p_context_command','completion_context.py',484),
  ('context -> commands','context',1,'p_context_command','completion_context.py',485),
  ('command -> args','command',1,'p_command','completion_context.py',525),
  ('command -> <empty>','command',0,'p_command','completion_context.py',526),
  ('commands -> command','commands',1,'p_multiple_commands_first','completion_context.py',564),
  ('commands -> commands SEMI command','commands',3,'p_multiple_commands_many','completion_context.py',574),
  ('commands -> commands AND command','commands',3,'p_multiple_commands_many','completion_context.py',575),
  ('commands -> commands PIPE command','commands',3,'p_multiple_commands_many','completion_context.py',576),
  ('commands -> commands OR command','commands',3,'p_multiple_commands_many','completion_context.py',577),
  ('commands -> commands NEWLINE command','commands',3,'p_multiple_commands_many','completion_context.py',578),
  ('sub_expression -> DOLLAR_LPAREN commands RPAREN','sub_expression',3,'p_sub_expression','completion_context.py',607),
  ('sub_expression -> BANG_LPAREN commands RPAREN','sub_expression',3,'p_sub_expression','completion_context.py',608),
  ('sub_expression -> ATDOLLAR_LPAREN commands RPAREN','sub_expression',3,'p_sub_expression','completion_context.py',609),
  ('sub_expression -> DOLLAR_LBRACKET commands RBRACKET','sub_expression',3,'p_sub_expression','completion_context.py',610),
  ('sub_expression -> BANG_LBRACKET commands RBRACKET','sub_expression',3,'p_sub_expression','completion_context.py',611),
  ('sub_expression -> AT_LPAREN commands RPAREN','sub_expression',3,'p_sub_expression','completion_context.py',612),
  ('sub_expression -> DOLLAR_LPAREN commands','sub_expression',2,'p_sub_expression','completion_context.py',613),
  ('sub_expression -> BANG_LPAREN commands','sub_expression',2,'p_sub_expression','completion_context.py',614),
  ('sub_expression -> ATDOLLAR_LPAREN commands','sub_expression',2,'p_sub_expression','completion_context.py',615),
  ('sub_expression -> DOLLAR_LBRACKET commands','sub_expression',2,'p_sub_expression','completion_context.py',616),
  ('sub_expression -> BANG_LBRACKET commands','sub_expression',2,'p_sub_expression','completion_context.py',617),
  ('sub_expression -> AT_LPAREN commands','sub_expression',2,'p_sub_expression','completion_context.py',618),
  ('arg -> sub_expression','arg',1,'p_sub_expression_arg','completion_context.py',687),
  ('arg -> DOLLAR_LPAREN','arg',1,'p_any_token_arg','completion_context.py',691),
  ('arg -> DOLLAR_LBRACKET','arg',1,'p_any_token_arg','completion_context.py',692),
  ('arg -> BANG_LPAREN','arg',1,'p_any_token_arg','completion_context.py',693),
  ('arg -> BANG_LBRACKET','arg',1,'p_any_token_arg','completion_context.py',694),
  ('arg -> ATDOLLAR_LPAREN','arg',1,'p_any_token_arg','completion_context.py',695),
  ('arg -> AT_LPAREN','arg',1,'p_any_token_arg','completion_context.py',696),
  ('arg -> STRING','arg',1,'p_any_token_arg','completion_context.py',697),
  ('arg -> ANY','arg',1,'p_any_token_arg','completion_context.py',698),
  ('args -> arg','args',1,'p_args_first','completion_context.py',709),
  ('args -> args arg','args',2,'p_args_many','completion_context.py',714),
]