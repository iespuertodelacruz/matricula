var gulp = require("gulp"),
    rev = require("gulp-rev"),
    sass = require("gulp-sass"),
    del = require("del");

var assets_base_dir = "./common/static/",
    dist_base_dir = "./common/static/dist/",
    tmp_path = "./.tmp";

var assets_paths = {
    "styles": {
        "source": assets_base_dir + "css/",
        "target": dist_base_dir + "css/"
    },
    "scripts": {
        "source": assets_base_dir + "js/",
        "target": dist_base_dir + "js/"
    },
    "images": {
        "source": assets_base_dir + "img/",
        "target": dist_base_dir + "img/"
    },
    "vendor": {
        "source": "./node_modules/",
        "target": dist_base_dir + "vendor/"
    }
};

gulp.task("clean-styles", function() {
    return del(assets_paths["styles"]["target"] + "**/*.css");
});

gulp.task("clean-scripts", function() {
    return del(assets_paths["scripts"]["target"] + "**/*.js");
});

gulp.task("clean-images", function() {
    return del(assets_paths["images"]["target"] + "**/*");
});

gulp.task("clean-vendor", function() {
    return del(assets_paths["vendor"]["target"] + "**/*");
});

gulp.task("build-styles", function() {
    return gulp.src(assets_paths["styles"]["source"] + "**/*.scss")
        .pipe(sass())
        .pipe(gulp.dest(tmp_path))
        .pipe(rev())
        .pipe(gulp.dest(assets_paths["styles"]["target"]))
        .pipe(rev.manifest())
        .pipe(gulp.dest(assets_paths["styles"]["target"]));
});

gulp.task("build-scripts", function() {
    return gulp.src(assets_paths["scripts"]["source"] + "**/*.js")
        .pipe(rev())
        .pipe(gulp.dest(assets_paths["scripts"]["target"]))
        .pipe(rev.manifest())
        .pipe(gulp.dest(assets_paths["scripts"]["target"]));
});

gulp.task("build-images", function() {
    return gulp.src(assets_paths["images"]["source"] + "**/*")
        .pipe(rev())
        .pipe(gulp.dest(assets_paths["images"]["target"]))
        .pipe(rev.manifest())
        .pipe(gulp.dest(assets_paths["images"]["target"]));
});

gulp.task("build-vendor", function() {
    return gulp.src(assets_paths["vendor"]["source"] + "**/*.*")
        .pipe(gulp.dest(assets_paths["vendor"]["target"]));
});

gulp.task("watch", function() {
    gulp.watch(
        assets_paths["styles"]["source"] + "**/*.scss",
        gulp.series("clean-styles", "build-styles")
    );
    gulp.watch(
        assets_paths["scripts"]["source"] + "**/*.js",
        gulp.series("clean-scripts", "build-scripts")
    );
    gulp.watch(
        assets_paths["images"]["source"] + "**/*",
        gulp.series("clean-images", "build-images")
    );
});

gulp.task("build", gulp.series(
    gulp.parallel("clean-styles", "clean-scripts", "clean-images"),
    gulp.parallel("build-styles", "build-scripts", "build-images")
));

gulp.task("update-vendor", gulp.series(
    "clean-vendor", "build-vendor"
));
