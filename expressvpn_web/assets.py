# coding=utf-8
from webassets import Bundle

__author__ = 'Valentin Grouès'

common_css = Bundle(
    'vendors/node_modules/bootstrap/dist/css/bootstrap.css',
    'vendors/node_modules/bootstrap-material-design/dist/css/ripples.css',
    Bundle(
        'css/layout.less',
        filters='less',
        output='public/css/vpn.css'
    ),
    filters='cssmin', output='public/css/common.min.css')

common_js = Bundle(
    'vendors/node_modules/jquery/dist/jquery.js',
    'vendors/node_modules/bootstrap/dist/js/bootstrap.js',
    'vendors/node_modules/bootstrap-material-design/dist/js/ripples.js',
    'vendors/node_modules/bootstrap-material-design/dist/js/material.js',
    'js/main.js'
    ,
    output='public/js/common.min.js')
