from flask import jsonify
def fibo(params):
  i = 0
  j = 1
  sequence = []
  current_operation = 0
  index = 0
  while True:
    # We appends now, since f(0) = 0 = i_initial , f(1) = 1 =j_initial
    sequence.append(i)
    # prepare next opération
    current_operation = i + j
    i = j
    j = current_operation
    # Stop condition
    if i > params:
      return sequence
    else:
      index += 1

  return sequence


@app.route("/fibonacci/<int:param_fi>/")
def get_fibo(param_fi):
    return jsonify(fibo(param_fi))