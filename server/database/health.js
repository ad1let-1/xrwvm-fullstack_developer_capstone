/* jshint node: true */
function health() {
  return { service: 'Best Cars', status: 'ok' };
}

module.exports = { health: health };
