#!/usr/bin/perl

while(<>)
{
	chomp;
	$line = $_;
	if($line ne $last)
	{
		if($last)
		{
			print "$last\t$count\n"
		}
		$last = $line; 
		$count = 1;
	}
	else
	{
		$count++;
	}
}
print "$last\t$count\n";