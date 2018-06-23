var gulp = require("gulp"),
    rev = require("gulp-rev"),
    clean = require("gulp-clean"),
    sass = require("gulp-sass");

var dist_css_path = "./common/static/dist/css/",
    dist_js_path = "./common/static/dist/js/",
    dist_vendor_path = "./common/static/dist/vendor/",
    css_path = "./common/static/css/",
    js_path = "./common/static/js/",
    vendor_path = "./node_modules/",
    tmp_path = "./.tmp";

gulp.task("clean-styles", function() {
    return gulp.src(dist_css_path + "**/*.css", {read: false})
        .pipe(clean());
});

gulp.task("clean-scripts", function() {
    return gulp.src(dist_js_path + "**/*.js", {read: false})
        .pipe(clean());
});

gulp.task("clean-vendor", function() {
    return gulp.src(dist_vendor_path, {read: false})
        .pipe(clean());
});

gulp.task("styles", function() {
    return gulp.src(css_path + "**/*.scss")
        .pipe(sass())
        .pipe(gulp.dest(tmp_path))
        .pipe(rev())
        .pipe(gulp.dest(dist_css_path))
        .pipe(rev.manifest())
        .pipe(gulp.dest(dist_css_path));
});

gulp.task("scripts", function() {
    return gulp.src(js_path + "**/*.js")
        .pipe(rev())
        .pipe(gulp.dest(dist_js_path))
        .pipe(rev.manifest())
        .pipe(gulp.dest(dist_js_path));
});

gulp.task("vendor", function() {
    return gulp.src(vendor_path + "**/*.*")
        .pipe(gulp.dest(dist_vendor_path));
});

gulp.task("watch", function() {
    gulp.watch(css_path + "**/*.scss", gulp.series("clean-styles", "styles"));
    gulp.watch(js_path + "**/*.js", gulp.series("clean-scripts", "scripts"));
});

gulp.task("build", gulp.series(
    gulp.parallel("clean-styles", "clean-scripts"),
    gulp.parallel("styles", "scripts")
));

gulp.task("update-vendor", gulp.series(
    "clean-vendor", "vendor"
));
