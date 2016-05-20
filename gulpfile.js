var path =  {
  source: 'app/static/',
  target: 'app/static/',
};

var gulp = require('gulp'),
    sass = require('gulp-ruby-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    cleancss = require('gulp-clean-css'),
    jshint = require('gulp-jshint'),
    uglify = require('gulp-uglify'),
    imagemin = require('gulp-imagemin'),
    rename = require('gulp-rename'),
    concat = require('gulp-concat'),
    notify = require('gulp-notify'),
    cache = require('gulp-cache'),
    livereload = require('gulp-livereload'),
    del = require('del');
    sourcemaps = require('gulp-sourcemaps');
    rev = require('gulp-rev');
    revreplace = require('gulp-rev-replace');
    debug = require('gulp-debug');
    runSequence = require('run-sequence');

gulp.task('default', function() {
  //do something
  runSequence('clean', 'clean-styles', ['styles']);
});

gulp.task('clean', function() {
  return del(['rev-manifest-*.json']);
});

gulp.task('clean-styles', function() {
  return del(path.target + 'css/dist');
});

//handle styles
gulp.task('styles', function() {
  return gulp.src(path.source + 'css/**/*.css', { style: 'expanded' })
             .pipe(sourcemaps.init())
             .pipe(rename({suffix: '.min'}))
             .pipe(cleancss())
             .pipe(rev())
             .pipe(sourcemaps.write('.'))
             .pipe(gulp.dest(path.target + 'css/dist/'))
             .pipe(rev.manifest('rev-manifest-css.json',[{cwd: ''}]))
             .pipe(gulp.dest(''))
             .pipe(notify({ message: 'Styles task complete' }));
});


