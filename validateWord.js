function validateWord(s) {
  var freq = {}
  s.toLowerCase().split('').forEach(function(s) {
    freq[s] ? freq[s]++ : freq[s] = 1
  })

  return new Set(Object.values(freq)).size == 1
}

console.log(validateWord('abs'))