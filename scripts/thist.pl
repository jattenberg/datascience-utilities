#!/usr/bin/perl
my $tot = 0;
@all = ();
while(<>)
{
	chomp; 
	my @p = split /\t/;
	$tot += $p[-1];
	push(@all, \@p);
}
$rtot = 0;
for($i = 0; $i < @all; $i++)
{
	@p = @{$all[$i]};
	$rtot += $p[-1]/$tot;
	push(@p,$p[-1]/$tot);
	push(@p,$rtot);
	print join("\t",@p),"\n";
}
