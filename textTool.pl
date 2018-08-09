use strict;
use warnings;
#command line arguments but for some reason they didn't work?
# my $inputFile = $ARGV[0];
# my $outputFile = $ARGV[1];
my $inputFile = "app_review.txt";
my $outputFile = "output.txt";
my @lines;

open(INPUT, '<', $inputFile) or die "Can't open or find input file";
open(OUTPUT, '>', $outputFile) or die "Can't open an output file";

while(my $line = <INPUT>) {
  @lines = split(/;\n/,$line,-1);
  chomp(@lines);
  tr/,/./ for @lines;
  print OUTPUT join(",\n", @lines);
}

close INPUT;
close OUTPUT;
