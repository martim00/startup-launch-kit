var path = require('path');

var ExtractTextPlugin = require('extract-text-webpack-plugin');
var ManifestRevisionPlugin = require('manifest-revision-webpack-plugin');

var rootAssetPath = './assets';

module.exports = {
    entry: {
        app_py: [
            rootAssetPath + '/python/test.py'
        ],
        app_js: [
            rootAssetPath + '/scripts/entry.js'
        ],
        app_css: [
            rootAssetPath + '/styles/main.css'
        ]
    },
    output: {
        path: './static/build/public',
        publicPath: 'http://localhost:2992/assets/',
        filename: '[name].js',
        chunkFilename: '[id].js'
    },
    resolve: {
        extensions: ['', '.js', '.css', 'py']
    },
    resolveLoader: {
        alias: {
        'python-loader': path.join(__dirname, './loader/python-loader'),
        },
        modules: ['node_modules', path.resolve(__dirname, 'loader')]
    },
    module: {
        loaders: [
            {
                test: /\.js$/i, loader: 'script-loader',
                exclude: /node_modules/
            },
            {
                test: /\.css$/i,
                /*loader: ExtractTextPlugin.extract('style-loader', 'css-loader')*/
                loaders: ['style-loader', 'css-loader']
            },
            {
                test: /\.(jpe?g|png|gif|svg([\?]?.*))$/i,
                loaders: [
                    'file?context=' + rootAssetPath + '&name=[path][name].[hash].[ext]',
                    'image?bypassOnDebug&optimizationLevel=7&interlaced=false'
                ]
            },
            {
                test: /\.py$/,
                loader: 'python-loader'
//                loader: require.resolve('./loader/python-loader'),
            }
        ]
    }
//    plugins: [
//        new ExtractTextPlugin('[name].[chunkhash].css'),
//        new ManifestRevisionPlugin(path.join('static', 'build', 'manifest.json'), {
//            rootAssetPath: rootAssetPath,
//            ignorePaths: ['/styles', '/scripts']
//        })
//    ]
};