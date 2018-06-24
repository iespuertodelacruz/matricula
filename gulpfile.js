var gulp = require("gulp"),
    rev = require("gulp-rev"),
    sass = require("gulp-sass"),
    concat = require("gulp-concat"),
    del = require("del");

var base_assets_path = "./common/static/",
    base_dist_path = "./common/static/dist/",
    tmp_path = "./.tmp";

var assets_paths = {
    "styles": {
        "source": base_assets_path + "css/",
        "target": base_dist_path + "css/"
    },
    "scripts": {
        "source": base_assets_path + "js/",
        "target": base_dist_path + "js/"
    },
    "images": {
        "source": base_assets_path + "img/",
        "target": base_dist_path + "img/"
    },
    "fonts": {
        "source": base_assets_path + "fonts/",
        "target": base_dist_path + "fonts/"
    },
    "files": {
        "source": base_assets_path + "files/",
        "target": base_dist_path + "files/"
    },
    "vendor": {
        "source": "./node_modules/",
        "target": base_dist_path + "vendor/"
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

gulp.task("clean-fonts", function() {
    return del(assets_paths["fonts"]["target"] + "**/*");
});

gulp.task("clean-files", function() {
    return del(assets_paths["files"]["target"] + "**/*");
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

gulp.task("build-fonts", function() {
    return gulp.src(assets_paths["fonts"]["source"] + "**/*")
        .pipe(rev())
        .pipe(gulp.dest(assets_paths["fonts"]["target"]))
        .pipe(rev.manifest())
        .pipe(gulp.dest(assets_paths["fonts"]["target"]));
});

gulp.task("build-files", function() {
    return gulp.src(assets_paths["files"]["source"] + "**/*")
        .pipe(rev())
        .pipe(gulp.dest(assets_paths["files"]["target"]))
        .pipe(rev.manifest())
        .pipe(gulp.dest(assets_paths["files"]["target"]));
});

gulp.task("build-vendor", function() {
    pth = assets_paths["vendor"]["source"]

    files = [
        pth + "bootstrap/dist/css/bootstrap.min.css",
        pth + "jquery-ui-dist/jquery-ui.min.css",
        pth + "font-awesome/css/font-awesome.min.css"
    ]

    gulp.src(files)
        .pipe(concat("vendor.css"))
        .pipe(gulp.dest(tmp_path))
        .pipe(rev())
        .pipe(gulp.dest(assets_paths["vendor"]["target"] + "css"))
        .pipe(rev.manifest())
        .pipe(gulp.dest(assets_paths["vendor"]["target"] + "css"));

    files = [
        pth + "jquery/dist/jquery.min.js",
        pth + "jquery-ui-dist/jquery-ui.min.js",
        pth + "jquery-ui/ui/i18n/datepicker-es.js"
    ]

    gulp.src(files)
        .pipe(concat("vendor.js"))
        .pipe(gulp.dest(tmp_path))
        .pipe(rev())
        .pipe(gulp.dest(assets_paths["vendor"]["target"] + "js"))
        .pipe(rev.manifest())
        .pipe(gulp.dest(assets_paths["vendor"]["target"] + "js"));

    files = [
        pth + "font-awesome/fonts/fontawesome-webfont.ttf",
        pth + "font-awesome/fonts/fontawesome-webfont.woff",
        pth + "font-awesome/fonts/fontawesome-webfont.woff2"
    ]

    return gulp.src(files)
        .pipe(gulp.dest(assets_paths["vendor"]["target"] + "fonts"));

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
    gulp.watch(
        assets_paths["fonts"]["source"] + "**/*",
        gulp.series("clean-fonts", "build-fonts")
    );
});

gulp.task("dist",
    gulp.series(
        gulp.parallel(
            "clean-styles",
            "clean-scripts",
            "clean-images",
            "clean-fonts",
            "clean-files",
            "clean-vendor"
        ),
        gulp.parallel(
            "build-styles",
            "build-scripts",
            "build-images",
            "build-fonts",
            "build-files",
            "build-vendor"
        )
    )
);
