# $MawkId: reg4.awk,v 1.2 2009/07/12 20:39:16 tom Exp $
{
	if ($0 ~/^[-+()0-9.,$%/'"]*$/)
        {
		print ("Found 1:",$0)
	}
	if ($0 ~/^[]-+()0-9.,$%/'"]*$/)
        {
		print ("Found 2:",$0)
	}
	if ($0 ~/^[^]-+()0-9.,$%/'"]*$/)
        {
		print ("Found 3:",$0)
	}
}
