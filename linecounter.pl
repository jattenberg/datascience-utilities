#!/usr/bin/perl


@files = @ARGV;

if(@files == 0) {
    print STDERR "must enter some file names!\nUsage: linecounter [filenames]\n";
    exit 1;
}

while(1) {
    foreach $file (@files) {
        print `wc -l $file`;
    }
    sleep(60);
}