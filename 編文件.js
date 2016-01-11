var ghpages = require('gh-pages');
var path = require('path');

ghpages.publish(
  path.join(__dirname, '文件/_build/html'),
  { dotfiles: true },
  function(){}
)
