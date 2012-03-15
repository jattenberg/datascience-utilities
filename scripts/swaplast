#!/usr/bin/perl

while(<>)
{
	chomp;
	@p = split /\t/;
	$tmp = $p[-1];
	$p[-1] = $p[0];
	$p[0] = $tmp;

	print join("\t",@p),"\n";
}
