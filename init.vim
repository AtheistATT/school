:set mouse 
:set number
:set relativenumber
:set smarttab
:set tabstop=4
:set shiftwidth=4
:set softtabstop=4
:set autoindent
set clipboard=unnamedplus
set nocompatible
filetype plugin indent on
syntax on
set hidden

call plug#begin()
Plug 'https://github.com/vim-airline/vim-airline'
Plug 'https://github.com/preservim/nerdtree'
Plug 'https://github.com/ryanoasis/vim-devicons'
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'folke/tokyonight.nvim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'voldikss/vim-floaterm'
Plug 'psf/black', { 'branch': 'stable' }
Plug 'nvim-lua/plenary.nvim'
Plug 'mfussenegger/nvim-lint'
Plug 'vim-test/vim-test'
Plug 'jmcantrell/vim-virtualenv'
Plug 'tpope/vim-pydoc'
Plug 'airblade/vim-gitgutter'
Plug 'tpope/vim-commentary'
Plug 'tpope/vim-fugitive'
inoremap <silent> <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <silent> <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<C-d>"
inoremap <silent> <expr> <CR> pumvisible() ? coc#_select_confirm() : "\<CR>"
call plug#end()



function! RunCode()
  " Сохраняем текущий файл
  :w

  " Получаем расширение файла в нижнем регистре
  let file_extension = tolower(expand('%:e'))

  " Запускаем код в зависимости от расширения
  if file_extension == 'py'
    " Для Python
    :FloatermNew uv run %
    ":FloatermNew uv run %
  elseif file_extension == 'c'
    " Для C: компилируем и запускаем
    :FloatermNew gcc % -o %:r && ./%:r
  elseif file_extension == 'md'
    " Для Markdown: конвертируем в PDF и открываем в Okular
    :silent !okular % &
  elseif file_extension == 'js'
	  :FloatermNew node %
	  "Для JavaScript
  else
    echo "Неподдерживаемый тип файла"
  endif
endfunction

nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
nnoremap <F5> :w<CR>:call RunCode()<CR>
nnoremap <F1> :CocCommand document.toggleInlayHint<CR>
colorscheme tokyonight


lua << EOF
require'nvim-treesitter.configs'.setup {
  ensure_installed = "python", -- Убедитесь, что у вас установлен парсер для Python
  highlight = {
    enable = true,              -- Включить подсветку
    additional_vim_regex_highlighting = false,
  },
}

require('lint').linters_by_ft = {
  python = {'flake8'}
}

vim.api.nvim_create_autocmd({ "BufWritePost" }, {
  callback = function()
    require("lint").try_lint()
  end,
})
EOF
