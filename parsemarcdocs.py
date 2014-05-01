testdata = """<!DOCTYPE html
  PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html40/loose.dtd">
<html>
   <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
   
      <title>MARC 21 Format for Bibliographic Data: 010: Library of Congress Control Number 
         					 (Network Development and MARC Standards Office, Library of
         					Congress)
      </title>
      <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
      <meta name="description" content="This field contains the Library of Congress Control Number (Network Development and MARC Standards Office, Library of Congress)">
      <meta name="keywords" content="marc, marc21, marc standards">
      <meta name="author" content="Library of Congress Network Development and MARC Standards Office">
      <link href="http://www.loc.gov/marc/marc-generic.css" rel="stylesheet" type="text/css"><style type="text/css">
					body {margin-left: 2em; margin-right: 2em;} 
					h1 {font-family:Arial, Helvetica, sans-serif;}
					h3 {text-align:left;}
					h4 {margin-top:.5em; margin-bottom:.5em;}
					p {text-align:justify; margin-left:2em; margin-right:2em;}
					.formatname {font-weight:bold; font-family:Arial, Helvetica, sans-serif; margin-left:.5em}
					.datename {font-weight:bold; text-align:right; font-family:Arial, Helvetica, sans-serif; margin-top:-1.2em;}
					.font_small {font-size:9pt;}
					.fieldtoc {margin-left:2em;}
					.box {font-family:ZapfDingbats;}
					.description {text-align:justify; margin-left:2em;}
					.description2  {text-align:justify; margin-top:1em; margin-bottom:1em;}
					.description3 {text-align:justify; margin-top:1em; margin-bottom:1em; margin-left:2em;}
					.indicator {text-align:left; margin-top:1em; margin-bottom:1em;}
					.indicatorvalue {margin-left:2em; margin-top:1em; margin-bottom:1em;}
					.subfield {text-align:left; margin-top:1em; margin-bottom:1em; margin-left:2em;}
					.characterposition {text-align:left; margin-top:1em; margin-bottom:1em; margin-left:2em;}
					.charactervalue {margin-left:2em; margin-top:1em; margin-bottom:1em;}
					.characterpositionhistory {text-align:left; margin-top:.5em; margin-bottom:.5em; margin-left:2em;}
					.charactervaluehistory {margin-left:2em; margin-top:.1em; margin-bottom:.1em;}
					.example {margin-left:4em;}
					.changed {color: #FF0000;}
					.captiontext {font-style:italic;}
					.displaytext {font-style:italic; margin-left:6em; margin-bottom:.5em; margin-top:.5em;}
					.displaycontent {margin-left:4em;}
					.table {margin-left:2em; margin-top:1em; margin-bottom:1em;}
					.head-nav {font-family:Arial, Helvetica, sans-serif; font-size:9pt;}
					.summary {margin-left:2em;}
					.summarytable {margin-left:4em;}
				</style><script type="text/javascript" src="http://cdn.loc.gov/js/global/foresee/foresee-trigger.js"></script></head>
   <body>
      <div class="head-nav"><a href="http://www.loc.gov/">Library of Congress</a> &gt;&gt;  <a href="http://www.loc.gov/marc/">MARC</a> &gt;&gt; <a href="http://www.loc.gov/marc/bibliographic/">Bibliographic</a> 
         					&gt;&gt; <a href="http://www.loc.gov/marc/bibliographic/bd01x09x.html">01X-09X</a> &gt;&gt;  <strong>010</strong></div>
      <hr><a name="skip_menu"></a><h1>010 - Library of Congress Control Number (NR)</h1>
      <hr>
      <div class="formatname">MARC 21 Bibliographic - Full</div>
      <div class="datename">October 2005</div>
      <hr>
      <table width="100%">
         <tr vAlign="top">
            <td width="45%"><strong>First Indicator</strong><br><em>Undefined</em><br># - Undefined <br><br></td>
            <td width="45%"><strong>Second Indicator</strong><br><em>Undefined</em><br># - Undefined <br><br></td>
         </tr>
      </table>
      <hr>
      <table width="100%">
         <tr vAlign="top">
            <td valign="top" width="50%" align="left"></td>
            <td valign="top" width="50%" align="left"></td>
         </tr>
         <tr vAlign="top">
            <td colspan="2"><strong>Subfield Codes</strong><br></td>
         </tr>
         <tr vAlign="top">
            <td colspan="1">$a - LC control number (NR) <br>$b - NUCMC control number (R) <br></td>
            <td colspan="1">$z - Canceled/invalid LC control number (R) <br>$8 - Field link and sequence number (R) <br></td>
         </tr>
   </table>
      <hr>
      <h3>FIELD DEFINITION AND SCOPE</h3>
      <p>Unique number assigned to a MARC record by the Library of Congress. Valid MARC prefixes
                     for LC control numbers are published in <em>MARC 21 Format for Bibliographic
                     Data</em>.
      </p>
      <p>The control number for MARC records distributed by LC is an LC control number (LCCN).
         The LC control number is carried in field 001 (Control Number) in records distributed by
                     LC's Cataloging Distribution Service and in field 010$a. An organization using LC
                     records may remove the LC control number from field 001 and use field 001 for its own
                     system control number.
      </p>
      <p>An LC record may contain field 010 with a canceled or invalid control number of a
                     previously-distributed record. A record may be canceled because it is a duplicate record
                     for the same item. The structure of the canceled/invalid control number is the same as
                     that used by LC in field 001.      </p>
      <hr>
      <h3>GUIDELINES FOR APPLYING CONTENT DESIGNATORS</h3>
      <h4><span class="box">&#9632;</span> INDICATORS
      </h4>
      <ul>
         <li class="nobullet">Both indicator positions are undefined; each contains a blank (#).</li>
      </ul>
     
      <h4><span class="box">&#9632;</span> SUBFIELD CODES
      </h4>
      <div class="subfield"><strong>$a - LC control number</strong> <div class="description">Valid LC control number (see explanation of structure of this number given
                           below).
         </div>
         <div class="example">
            <table width="100%">
               <tr>
                  <td valign="top" width="5%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="15%" align="left"></td>
               </tr>
               <tr>
                  <td vAlign="top" colspan="1" align="left"><strong>010</strong></td>
                  <td vAlign="top" colspan="9" align="left"><strong>##</strong><strong>$a</strong>###85153773#
                  </td>
               </tr>
               <tr>
                  <td vAlign="top" colspan="1" align="left"><strong>010</strong></td>
                  <td vAlign="top" colspan="9" align="left"><strong>##</strong><strong>$a</strong>nuc76039265#
                  </td>
               </tr>
               <tr>
                  <td vAlign="top" colspan="1" align="left"><strong>010</strong></td>
                  <td vAlign="top" colspan="9" align="left"><strong>##</strong><strong>$a</strong>##2001627090
                  </td>
               </tr>
               <tr>
                  <td vAlign="top" colspan="1" align="left"><strong>010</strong></td>
                  <td vAlign="top" colspan="9" align="left"><strong>##</strong><strong>$a</strong>##2001336783
                  </td>
               </tr>
            </table>
         </div>
      </div>
      <div class="subfield"><strong>$b - NUCMC control number</strong> <div class="description">Valid entry number for the item being described as found in <em>National Union
                                    Catalog of Manuscript Collections</em> (NUCMC). The number begins with the
                              prefix <em>ms</em>.
         </div>
         <div class="example">
            <table width="100%">
               <tr>
                  <td valign="top" width="5%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="15%" align="left"></td>
               </tr>
               <tr>
                  <td vAlign="top" colspan="1" align="left"><strong>010</strong></td>
                  <td vAlign="top" colspan="9" align="left"><strong>##</strong><strong>$a</strong>###89798632#<strong>$b</strong>ms#89001579#
                  </td>
               </tr>
            </table>
         </div>
      </div>
      <div class="subfield"><strong>$z - Canceled/invalid LC control number</strong> <div class="description">Canceled or invalid LC control number, including invalid NUCMC numbers.</div>
         <div class="example">
            <table width="100%">
               <tr>
                  <td valign="top" width="5%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="15%" align="left"></td>
               </tr>
               <tr>
                  <td vAlign="top" colspan="1" align="left"><strong>010</strong></td>
                  <td vAlign="top" colspan="9" align="left"><strong>##</strong><strong>$a</strong>###76647633#<strong>$z</strong>sc#76000587#
                  </td>
               </tr>
               <tr>
                  <td vAlign="top" colspan="1" align="left"><strong>010</strong></td>
                  <td vAlign="top" colspan="9" align="left"><strong>##</strong><strong>$a</strong>###81691938#<strong>$z</strong>###82692384#
                  </td>
               </tr>
            </table>
         </div>
      </div>
      <div class="subfield"><strong>$8 - Field link and sequence number</strong> 
        <div class="description">See description of this subfield in Appendix A: <em><a href="http://www.loc.gov/marc/bibliographic/ecbdcntf.html">Control
                                       Subfields</a></em>.
        </div>
   </div>
      <hr>
      <h3>INPUT CONVENTIONS</h3>
      <div class="description2"><strong>Classes of LCCNs</strong> - LCCNs may be valid, canceled, or invalid (structurally or application) for the record.
                     The following conventions are followed to select the appropriate subfield for an
                  LCCN.
      </div>
      <div class="description2"><strong>Valid LCCN:</strong> - A valid LCCN for a record is the one that appears in the 001 when the record is
                     distributed by LC. It has correct length and structure.
      </div>
      <div class="description2"><strong>Canceled LCCN:</strong> - A record, hence its LCCN, may be canceled for a variety of reasons, very often because
                     it is a duplicate record for the same manifestation of a resource. An LCCN is considered
                     to be canceled when LC designates it as such.
      </div>
      <div class="description2"><strong>Structurally invalid LCCN:</strong> - An LCCN is considered structurally invalid when its length or structure is incorrect
                     according to the practices of the Library of Congress.
      </div>
      <div class="description2"><strong>Application invalid LCCN:</strong> - An LCCN is invalid in application when it appears on the item being cataloged but it is
                     not the LCCN of the record for the item, e.g. the LCCN assigned to the record for one
                     edition is also printed in another, different edition which has its own record and
                  LCCN.
      </div>
      <div class="description2"><strong>Punctuation</strong> - Field 010 does not end in a mark of punctuation. A slash is used to separate revision
                     information from the control number and any suffix. Multiple suffixes are also separated
                     by a slash.
      </div>
      <div class="description2"><strong>Capitalization</strong> - Prefixes are always input as lowercase alphabetic characters. Suffixes and alphabetic
                     identifiers added to the end of the LC control number are input as uppercase alphabetic
                     characters.
      </div>
	  <hr>
        <h3>STRUCTURE OF THE LC CONTROL NUMBER</h3>
		<div class="description">
         <p>The LC control numbering system has had the same basic structure since its initial use
                        to control Library of Congress bibliographic information in card form beginning in 1898
                        (LCCN structure A). On January 1, 2001, a structural change occurred (LCCN structure B).
                        The basic control number has been fixed in length at 12 characters and will remain that
                        length, although under LCCN structure A suffixes were occasionally used and under LCCN
                        structure B the location of element parts is slightly altered to accommodate a four
                        digit year. Under both structures, the prefix, year, and serial number are the basic
                        elements required to make an LCCN unique.
         </p>
         <p><strong> LCCN Structure A (1898-2000)</strong></p>
         <div class="table">
            <table>
               <tr>
                  <td width="236" align="left" valign="top"><em>Name of Element</em></td>
                  <td width="181" align="left" valign="top"><em>Number of characters</em></td>
                  <td width="183" align="left" valign="top"><em>Character position in field</em></td>
               </tr>
               <tr>
                  <td valign="top" align="left">Alphabetic prefix</td>
                  <td valign="top" align="left">3</td>
                  <td valign="top" align="left">00-02</td>
               </tr>
               <tr>
                  <td valign="top" align="left">Year</td>
                  <td valign="top" align="left">2</td>
                  <td valign="top" align="left">03-04</td>
               </tr>
               <tr>
                  <td valign="top" align="left">Serial number</td>
                  <td valign="top" align="left">6</td>
                  <td valign="top" align="left">05-10</td>
               </tr>
               <tr>
                  <td valign="top" align="left">Supplement number</td>
                  <td valign="top" align="left">1</td>
                  <td valign="top" align="left">11</td>
               </tr>
               <tr>
                  <td valign="top" align="left">Suffix and/or Revision Date</td>
                  <td valign="top" align="left">variable</td>
                  <td valign="top" align="left">12-n</td>
               </tr>
            </table>
         </div>
         <p><strong> LCCN Structure B (2001- )</strong></p>
         <div class="table">
            <table>
               <tr>
                  <td width="242" align="left" valign="top"><em>Name of Element</em></td>
                  <td width="180" align="left" valign="top"><em>Number of characters</em></td>
                  <td width="178" align="left" valign="top"><em>Character position in field</em></td>
               </tr>
               <tr>
                  <td valign="top" align="left">Alphabetic prefix</td>
                  <td valign="top" align="left">2</td>
                  <td valign="top" align="left">00-01</td>
               </tr>
               <tr>
                  <td valign="top" align="left">Year</td>
                  <td valign="top" align="left">4</td>
                  <td valign="top" align="left">02-05</td>
               </tr>
               <tr>
                  <td valign="top" align="left">Serial number</td>
                  <td valign="top" align="left">6</td>
                  <td valign="top" align="left">06-11</td>
               </tr>
            </table>
         </div>
         <p><strong>Alphabetic prefix</strong></p>
         <p>Prefixes are carried in a MARC record as lowercase alphabetic characters and serve to
                        differentiate between different series of LC control numbers. Prefixes are left
                        justified and unused positions contain blanks. If no prefix is present, the prefix
                        portion contains blanks.
         </p>
         <div class="example">
            <table width="100%">
               <tr>
                  <td valign="top" width="5%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="15%" align="left"></td>
               </tr>
               <tr>
                  <td vAlign="top" colspan="1" align="left"><strong>010</strong></td>
                  <td vAlign="top" colspan="9" align="left"><strong>##</strong><strong>$a</strong>###68004897#<br><em>[LCCN structure A; number on printed card: 68-4897]</em></td>
               </tr>
               <tr>
                  <td vAlign="top" colspan="1" align="left"><strong>010</strong></td>
                  <td vAlign="top" colspan="9" align="left"><strong>##</strong><strong>$a</strong>##2001045944<br><em>[LCCN structure B; number in print form: 2001-45944]</em></td>
               </tr>
            </table>
         </div>
         <p>Prior to the existence of MARC records, prefixes of various lengths were used on printed
                        cards with combinations of uppercase or lowercase letters and numbers. For MARC records,
                        equivalents have been defined by the Library of Congress for some of these early
                        prefixes, including those that were longer than two or three characters. All other
                        prefixes are input as found but in lowercase. The first column in the list below gives
                        prefixes found on printed cards not printed from machine-readable records and shows how
                        they are to be input into a MARC version of the record. The list also includes some MARC
                        prefixes not found only on MARC records. Only prefixes which have a MARC form noted
                        below should be recorded in machine-readable records. (The alphabetic prefix for the
                        Library of Congress control number is an authoritative-agency data element, maintained
                        by the Library of Congress.)
         </p>
         <p>Since the prefixes were used in records before 2001, they are found in the LCCN
                        Structure A <em>only</em>.
         </p>
      </div>
	  <strong>LCCN Prefix Table</strong><p>Note: In the first column, an asterisked (*) item indicates the form in which the prefix
                  appears on the card.
   </p>
   <div class="table">
            <table>
               <tr>
                  <td width="115" align="left" valign="top"><em>Prefix on card</em></td>
                  <td width="100" align="left" valign="top"><em>MARC Prefix</em></td>
                  <td width="476" align="left" valign="top"><em>Explanation of usage</em></td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>A</strong></td>
                  <td valign="top" align="left">a</td>
                  <td valign="top" align="left">Cataloging provided to LC by an American library, 1909-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>AC</strong></td>
                  <td valign="top" align="left">ac</td>
                  <td valign="top" align="left">Cataloging for foreign materials provided to LC by cooperating libraries under
                                       the auspices of the ALA Committee on Cooperative Cataloging, 1932-1942
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>AC</strong></td>
                  <td valign="top" align="left">ac</td>
                  <td valign="top" align="left">Annotated cards for juvenile books, 1966-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>AF</strong></td>
                  <td valign="top" align="left">af</td>
                  <td valign="top" align="left">Cataloging for foreign acquisitions provided to LC by other American
                                       libraries, 1946-1950
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>AFLM</strong></td>
                  <td valign="top" align="left">afl</td>
                  <td valign="top" align="left">No explanation available</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>Agr</strong></td>
                  <td valign="top" align="left">agr</td>
                  <td valign="top" align="left">U.S. Department of Agriculture cataloging, 1902-</td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">bi</td>
                  <td valign="top" align="left">Handbook of Latin American Studies record</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>BR</strong></td>
                  <td valign="top" align="left">br</td>
                  <td valign="top" align="left">Library of Congress, Division for the Blind, braille book</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>BS</strong></td>
                  <td valign="top" align="left">bs</td>
                  <td valign="top" align="left">U.S. Bureau of Standards cataloging, 1913-1938</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>C</strong></td>
                  <td valign="top" align="left">c</td>
                  <td valign="top" align="left">U.S. Interstate Commerce Commission cataloging, 1915-1916</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>C</strong></td>
                  <td valign="top" align="left">c</td>
                  <td valign="top" align="left">Library of Congress, Chinese entries, 1949-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>C-245 or 245*</strong></td>
                  <td valign="top" align="left">c</td>
                  <td valign="top" align="left">LC card numbers for June-August 1898; year prefix &#8220;98" added when input into
                                       MARC
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>CA</strong></td>
                  <td valign="top" align="left">ca</td>
                  <td valign="top" align="left">LC temporary entries for books in the general classified collections,
                                       1905-1937
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>CA Dupl</strong></td>
                  <td valign="top" align="left">cad</td>
                  <td valign="top" align="left">LC temporary entries for books in the general classified collections,
                                       1905-1937
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>CD</strong></td>
                  <td valign="top" align="left">cd</td>
                  <td valign="top" align="left">LC analytical entries for sets and series prepared by the Card Division,
                                       1916-1940
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>CD</strong></td>
                  <td valign="top" align="left">cd</td>
                  <td valign="top" align="left">Cataloging prepared for LC card sales</td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">clc</td>
                  <td valign="top" align="left">Collection level cataloging; PREMARC record</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>CS</strong></td>
                  <td valign="top" align="left">cs</td>
                  <td valign="top" align="left">Cataloging prepared by the LC Cooperative Cataloging and Classification
                                       Service, 1934-1939
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>CX</strong></td>
                  <td valign="top" align="left">cx</td>
                  <td valign="top" align="left">Cross reference cards used in LC catalogs for Chinese entries, 1958-</td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">cy</td>
                  <td valign="top" align="left">Federal Cylinder Project, Oct. 1980</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>1-D-245 or D-245</strong></td>
                  <td valign="top" align="left">d</td>
                  <td valign="top" align="left">LC card numbers for May-December 1901; year prefix &#8220;01" added when input into
                                       MARC
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>DO</strong></td>
                  <td valign="top" align="left">do</td>
                  <td valign="top" align="left">U.S. Superintendent of Docs. cataloging, 1913-1916</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>E</strong></td>
                  <td valign="top" align="left">e</td>
                  <td valign="top" align="left">U.S. Office of Education cataloging, 1908-1958</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>ES</strong></td>
                  <td valign="top" align="left">es</td>
                  <td valign="top" align="left">U.S. Engineers School cataloging, 1913-1935</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>F</strong></td>
                  <td valign="top" align="left">f</td>
                  <td valign="top" align="left">U.S. Bureau of Fisheries cataloging, 1910-1940</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>1-F-245 or F-245</strong></td>
                  <td valign="top" align="left">f</td>
                  <td valign="top" align="left">LC card numbers for May-December 1901; year prefix &#8220;01" added when input into
                                       MARC
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>Fi</strong></td>
                  <td valign="top" align="left">fi</td>
                  <td valign="top" align="left">Films cataloged by LC, 1951-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>FiA</strong></td>
                  <td valign="top" align="left">fia</td>
                  <td valign="top" align="left">Cataloging provided by film producers, 1951-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>FiE</strong></td>
                  <td valign="top" align="left">fie</td>
                  <td valign="top" align="left">Cataloging provided by the Visual Education Service of the Office of
                                       Education, and other government agencies, 1951-
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>1-G-245 or G-245*</strong></td>
                  <td valign="top" align="left">g</td>
                  <td valign="top" align="left">LC card numbers for May-December 1901; year prefix &#8220;01" added when input into
                                       MARC
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>GM</strong></td>
                  <td valign="top" align="left">gm</td>
                  <td valign="top" align="left">Maps cataloged by LC, 1968-1972</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>GS</strong></td>
                  <td valign="top" align="left">gs</td>
                  <td valign="top" align="left">U.S. Geological Survey cataloging, 1904-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>H</strong></td>
                  <td valign="top" align="left">h</td>
                  <td valign="top" align="left">U.S. National Institute of Health cataloging, 1914-1921</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>HA</strong></td>
                  <td valign="top" align="left">ha</td>
                  <td valign="top" align="left">U.S. Housing Authority cataloging, 1940-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>HE</strong></td>
                  <td valign="top" align="left">he</td>
                  <td valign="top" align="left">Hebrew entries cataloged by LC, 1964-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>HEW</strong></td>
                  <td valign="top" align="left">hew</td>
                  <td valign="top" align="left">U.S. Dept. of Health, Ed., and Welfare cataloging, 1958-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>HEX</strong></td>
                  <td valign="top" align="left">hex</td>
                  <td valign="top" align="left">Cross reference cards used for Hebrew entries, 1964-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>1-I-245 or It-245*</strong></td>
                  <td valign="top" align="left">it</td>
                  <td valign="top" align="left">LC card numbers for May-December 1901; year prefix &#8220;01" added when input into
                                       MARC
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>Int</strong></td>
                  <td valign="top" align="left">int</td>
                  <td valign="top" align="left">U.S. Department of the Interior cataloging, 1959</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>J</strong></td>
                  <td valign="top" align="left">j</td>
                  <td valign="top" align="left">LC cataloging for Japanese materials 1949-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>JA</strong></td>
                  <td valign="top" align="left">ja</td>
                  <td valign="top" align="left">Cataloging for Japanese materials provided to LC by other American libraries,
                                       1951
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>JX</strong></td>
                  <td valign="top" align="left">jx</td>
                  <td valign="top" align="left">Cross reference cards used for Japanese entries, 1958-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>K</strong></td>
                  <td valign="top" align="left">k</td>
                  <td valign="top" align="left">Korean entries cataloged by LC, 1951-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>KX</strong></td>
                  <td valign="top" align="left">kx</td>
                  <td valign="top" align="left">Cross reference cards used for Korean entries, 1958-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>L</strong></td>
                  <td valign="top" align="left">l</td>
                  <td valign="top" align="left">U.S. Dept. of Labor cataloging, 1911-</td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">llh</td>
                  <td valign="top" align="left">Index to Hispanic Legislation cataloging</td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">ltf</td>
                  <td valign="top" align="left">Less-than-full cataloging; PREMARC record</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>M</strong></td>
                  <td valign="top" align="left">m</td>
                  <td valign="top" align="left">Sheet music cataloged by LC, 1953-1962</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>MA</strong></td>
                  <td valign="top" align="left">ma</td>
                  <td valign="top" align="left">Sheet music for which copy was supplied by another American library,
                                    1953-1961
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>Map</strong></td>
                  <td valign="top" align="left">map</td>
                  <td valign="top" align="left">Atlases in the Maps Division of LC, 1901-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>1-Map-50 or Map-50</strong></td>
                  <td valign="top" align="left">map</td>
                  <td valign="top" align="left">LC card numbers for maps for period May-December 1901; year prefix &#8220;01" added
                                       when input into MARC
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>Med</strong></td>
                  <td valign="top" align="left">med</td>
                  <td valign="top" align="left">U.S. Armed Forces Medical Library cataloging, 1946-1948</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>Mic</strong></td>
                  <td valign="top" align="left">mic</td>
                  <td valign="top" align="left">Microfilms cataloged by LC, 1949-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>MicA</strong></td>
                  <td valign="top" align="left">mid</td>
                  <td valign="top" align="left">Microfilms for which cataloging was provided by another American library,
                                       1946-
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>Micp</strong></td>
                  <td valign="top" align="left">mie</td>
                  <td valign="top" align="left">Microcards and microprints cataloged by LC, 1953-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>MicpA</strong></td>
                  <td valign="top" align="left">mif</td>
                  <td valign="top" align="left">Microcards and microprints for which cataloging was provided by another
                                       American library, 1953-
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">mm</td>
                  <td valign="top" align="left">Library of Congress Manuscripts Division</td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">mp</td>
                  <td valign="top" align="left">Early films cataloged by LC, 1970s</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>MPA</strong></td>
                  <td valign="top" align="left">mpa</td>
                  <td valign="top" align="left">Pan American Union cataloging for sheet music, 1956-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>MS</strong></td>
                  <td valign="top" align="left">ms</td>
                  <td valign="top" align="left">Manuscripts cataloged by LC, 1959-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>1-Music-245 or Music-245*</strong></td>
                  <td valign="top" align="left">mus</td>
                  <td valign="top" align="left">LC card numbers for music for May-December 1901; year prefix &#8220;01" added when
                                       input into MARC
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">ncn</td>
                  <td valign="top" align="left">Nitrate Film Service cataloging</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>NE</strong></td>
                  <td valign="top" align="left">ne</td>
                  <td valign="top" align="left">Materials published in the Near East or in the languages of those countries,
                                       1961-
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>NEX</strong></td>
                  <td valign="top" align="left">nex</td>
                  <td valign="top" align="left">Cross reference cards used for books published in the Near East or in the
                                       languages of those countries, 1961-
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>NO</strong></td>
                  <td valign="top" align="left">no</td>
                  <td valign="top" align="left">U.S. Naval Observatory cataloging, 1930-1940</td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">ntc</td>
                  <td valign="top" align="left">National Translation Center cataloging</td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">nuc</td>
                  <td valign="top" align="left">Records printed in the<em>National Union Catalog</em>for which no LC card
                                       number is available
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">or</td>
                  <td valign="top" align="left">Order Division cataloging</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>PA</strong></td>
                  <td valign="top" align="left">pa</td>
                  <td valign="top" align="left">Pan American Union cataloging, 1930-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>Pho</strong></td>
                  <td valign="top" align="left">pho</td>
                  <td valign="top" align="left">Cataloging provided by other libraries for photographic reproductions of
                                       books, 1927-
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>PhoM</strong></td>
                  <td valign="top" align="left">php</td>
                  <td valign="top" align="left">Cataloging provided by Card Division for photographic facsimiles issued by the
                                       Modern Language Association of America, 1927-1938
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>PhomA</strong></td>
                  <td valign="top" align="left">phq</td>
                  <td valign="top" align="left">Cataloging provided by other libraries for Modern Language Association of
                                       America photographic facsimiles
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>PO</strong></td>
                  <td valign="top" align="left">po</td>
                  <td valign="top" align="left">U.S. Patent Office cataloging, 1917-1953</td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">pp</td>
                  <td valign="top" align="left">Prints and Photographs videodisc system, March 1984</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>R</strong></td>
                  <td valign="top" align="left">r</td>
                  <td valign="top" align="left">Phonograph records cataloged by LC, 1953-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>RA</strong></td>
                  <td valign="top" align="left">ra</td>
                  <td valign="top" align="left">Cataloging provided by other American libraries for phonographs, 1955-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>1-Rc-245 or Rc-245*</strong></td>
                  <td valign="top" align="left">rc</td>
                  <td valign="top" align="left">LC card numbers for May-December 1901. Year prefix &#8220;01" added when input into
                                       MARC
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">re</td>
                  <td valign="top" align="left">Cataloging for commercial ethnic sound recordings produced in the U.S.
                                       project, 1981
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">ru</td>
                  <td valign="top" align="left">Cataloging from the Russian Book Chamber, 1988-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>S</strong></td>
                  <td valign="top" align="left">s</td>
                  <td valign="top" align="left">Smithsonian Institution cataloging, 1913-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>SA</strong></td>
                  <td valign="top" align="left">sa</td>
                  <td valign="top" align="left">Cataloging for materials published in Southeast Asia or in the languages of
                                       those countries, 1961-
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>SAX</strong></td>
                  <td valign="top" align="left">sax</td>
                  <td valign="top" align="left">Cross reference cards used for materials published in Southeast Asia or in the
                                       languages of those countries, 1961-
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">sc</td>
                  <td valign="top" align="left">Serials, CONSER item not in LC</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>SD</strong></td>
                  <td valign="top" align="left">sd</td>
                  <td valign="top" align="left">U.S. Dept. of State cataloging, 1914-</td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">sf</td>
                  <td valign="top" align="left">Serials form card or Minimal Level Cataloging or classed separately
                                       monographic series
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>SG</strong></td>
                  <td valign="top" align="left">sg</td>
                  <td valign="top" align="left">Surgeon General&#8217;s Library, U.S. Army cataloging, 1916-</td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">sn</td>
                  <td valign="top" align="left">Serials, CONSER; item may or may not be in LC</td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">su</td>
                  <td valign="top" align="left">Split manuscripts records</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>SS</strong></td>
                  <td valign="top" align="left">ss</td>
                  <td valign="top" align="left">Social Security Administration cataloging, 1944-1958</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>TB</strong></td>
                  <td valign="top" align="left">tb</td>
                  <td valign="top" align="left">Talking Books program cataloging</td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">tmp</td>
                  <td valign="top" align="left">Temporary cataloging from PREMARC</td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">um</td>
                  <td valign="top" align="left">Union map; an outside map record input by the Geography and Map Division for
                                       NUC use but residing in the G&amp;M database
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left">&nbsp;</td>
                  <td valign="top" align="left">unk</td>
                  <td valign="top" align="left">Card for which no LC card number was available; PREMARC</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>W</strong></td>
                  <td valign="top" align="left">w</td>
                  <td valign="top" align="left">District of Columbia Public Library cataloging, 1905-1942</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>War</strong></td>
                  <td valign="top" align="left">war</td>
                  <td valign="top" align="left">U.S. Army, War College cataloging, 1907-1932</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>X</strong></td>
                  <td valign="top" align="left">x</td>
                  <td valign="top" align="left">Cross reference cards used in LC catalogs, January 1941-</td>
               </tr>
               <tr>
                  <td valign="top" align="left"><strong>1-Z-245 or Z-245*</strong></td>
                  <td valign="top" align="left">z</td>
                  <td valign="top" align="left">LC card numbers for May-December 1901; year prefix &#8220;01" added when input into
                                       MARC
                  </td>
               </tr>
            </table>
         </div>
      <div class="description">
         <p><strong>Year</strong></p>
         <p>For control numbers assigned under LCCN structure A, the year portion consists of two
                        digits normally representing the year the record was created. For control numbers
                        assigned under LCCN structure B beginning with the year 2001, the year portion consists
                        of four digits.
         </p>
         <p>In most numbers, the year portion reflects the year in which the LC control number was
                        assigned to the record for the bibliographic item. During the 1969-1972 period, a
                           <em>7-series</em> year number was assigned. In these numbers the initial digit of
                           <em>7</em> was followed by a modulus-ll check digit. The year in which the card
                        number was assigned can be approximated from the year portion of the Date entered on
                        file (008/00-05). With the re-institution of the year series number in 1972, provisions
                        were made to skip those individual card numbers which could have been assigned
                        previously as a 7-series number. <em>Note:</em> 7-series numbers were not used for
                        non-book map material. The prefix <em>gm</em> was used from 1968 through 1972.
         </p>
         <p>For LC control numbers with two-digit years, the century may be determined according to
                        the following table:
         </p>
         <div class="table">
            <table width="644">
               <tr>
                  <td valign="top" align="left"><em>2-digit year</em></td>
                  <td valign="top" align="left"><em>Sequential number</em></td>
                  <td valign="top" align="left"><em>Century</em></td>
                  <td valign="top" align="left"><em>Sequential number</em></td>
                  <td valign="top" align="left"><em>Century</em></td>
               </tr>
               <tr>
                  <td valign="top" align="left">98</td>
                  <td valign="top" align="left">Less than 3000</td>
                  <td valign="top" align="left">18</td>
                  <td valign="top" align="left">3000 or greater</td>
                  <td valign="top" align="left">19</td>
               </tr>
               <tr>
                  <td valign="top" align="left">99</td>
                  <td valign="top" align="left">Less than 6000</td>
                  <td valign="top" align="left">18</td>
                  <td valign="top" align="left">6000 or greater</td>
                  <td valign="top" align="left">19</td>
               </tr>
               <tr>
                  <td valign="top" align="left">00</td>
                  <td valign="top" align="left">Less than 8000</td>
                  <td valign="top" align="left">19</td>
                  <td valign="top" align="left">8000 or greater</td>
                  <td valign="top" align="left">20</td>
               </tr>
           </table>
         </div>
         <p><strong>Serial number</strong></p>
         <p>Serial number portion consists of one to six digits. Serial numbers of less than six
                        digits are right justified and unused positions contain zeros. The hyphen which
                        separates the year and the serial number on LC printed products is not carried in the
                        MARC record. For example, the number 85-2 is carried as 85000002 in a record.
         </p>
         <p><strong>Supplement number (LCCN structure A only)</strong></p>
         <p>This character position was originally defined to carry a supplement number for
                        dashed-on supplement entries in bibliographic records. Use of the supplement number was
                        not implemented, therefore this position contains a blank. Supplements and similar
                        materials are now cataloged separately by LC and are carried as separate records with
                        their own LC control number. In some older records, information about supplements and
                        similar materials is given in a 500 note field.
         </p>
         <p><strong>Suffix/Alphabetic Identifier (LCCN structure A only)</strong></p>
         <p>Older LC control numbers sometimes include suffixes or alphabetic identifiers carried as
                        variable length data following the Supplement number. A single slash (/) introduces the
                        suffix/alphabetic identifier. Multiple occurrences of either suffixes or alphabetic
                        identifiers are separated one from the other by a slash. Suffixes and alphabetic
                        identifiers do not affect the uniqueness of the control number.
         </p>
         <p>All suffixes and alphabetic identifiers, except the revision date, appear in the MARC
                        record as uppercase alphabetic characters. On printed card copy, suffixes appear after
                        the LC control number separated by a slash. Suffixes have not been assigned since 1969
                        and they will be deleted from Library of Congress files in 1999. Alphabetic identifiers
                        appear on printed card copy as uppercase alphabetic characters beneath the LC card
                        number in the lower right hand corner of the card. Alphabetic identifiers were first
                        assigned in 1969 and were used as distribution information for card copy by LC.
                        Alphabetic identifiers will be deleted from the Library of Congress files in 1999.
         </p>
         <div class="example">
            <table width="100%">
               <tr>
                  <td valign="top" width="5%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="15%" align="left"></td>
               </tr>
               <tr>
                  <td vAlign="top" colspan="1" align="left"><strong>010</strong></td>
                  <td vAlign="top" colspan="9" align="left"><strong>##</strong><strong>$a</strong>###79139101#/AC/MN<br><em>[Printed number is 79-139101 with AC MN printed below the number.]</em></td>
               </tr>
               <tr>
                  <td vAlign="top" colspan="1" align="left"><strong>010</strong></td>
                  <td vAlign="top" colspan="9" align="left"><strong>##</strong><strong>$a</strong>###65077628#/MN<br><em>[Printed number is 65-77628 with MN printed below the number.]</em></td>
               </tr>
            </table>
         </div>
         <div class="table">
            <table>
               <tr>
                  <td width="194" align="left" valign="top"><i>Suffix/alphabetic identifiers</i></td>
                  <td width="469" align="left" valign="top"><i>&nbsp;</i></td>
               </tr>
               <tr>
                  <td valign="top" align="left">AC</td>
                  <td valign="top" align="left">used on records included in the "Annotated Card" program</td>
               </tr>
               <tr>
                  <td valign="top" align="left">AM</td>
                  <td valign="top" align="left">used for works in Amharic</td>
               </tr>
               <tr>
                  <td valign="top" align="left">ACN</td>
                  <td valign="top" align="left">used for works in Chinese</td>
               </tr>
               <tr>
                  <td valign="top" align="left">AJ</td>
                  <td valign="top" align="left">used for works in Japanese</td>
               </tr>
               <tr>
                  <td valign="top" align="left">AK</td>
                  <td valign="top" align="left">used for works in Korean</td>
               </tr>
               <tr>
                  <td valign="top" align="left">F</td>
                  <td valign="top" align="left">used for records created by the Audiovisual Section, Special Materials
                                             Cataloging Division for motion pictures, filmstrips, sets of slides and
                                             transparencies, video recordings, etc.
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left">HE</td>
                  <td valign="top" align="left">used for works published in the Hebrew alphabet, regardless of
                                          language
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left">M</td>
                  <td valign="top" align="left">used for works classed in M</td>
               </tr>
               <tr>
                  <td valign="top" align="left">MAP</td>
                  <td valign="top" align="left">used for atlases</td>
               </tr>
               <tr>
                  <td valign="top" align="left">MN</td>
                  <td valign="top" align="left">used for works classed in ML and MT</td>
               </tr>
               <tr>
                  <td valign="top" align="left">MP</td>
                  <td valign="top" align="left">used for records created by the Motion Picture, Broadcasting and
                                             Recorded Sound Division
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left">NE</td>
                  <td valign="top" align="left">used for works in Armenian, Arabic, Georgian, Ottoman Turkish, Persian,
                                             Pashto, and Turkish, as well as any non-Slavic language of Central Asia
                                             written in the Cyrillic alphabet
                  </td>
               </tr>
               <tr>
                  <td valign="top" align="left">PP</td>
                  <td valign="top" align="left">used for records created by the Prints and Photographs Division</td>
               </tr>
               <tr>
                  <td valign="top" align="left">R</td>
                  <td valign="top" align="left">used for all sound recordings</td>
               </tr>
            </table>
         </div>
         <p><strong>Revision Date </strong><strong>(LCCN structure A only)</strong></p>
         <p>Revision dates associated with LC control numbers specify the latest date that the
                        bibliographic data in a record underwent a change. Revision data do not affect the
                        uniqueness of the control number. To account for the number of times significant changes
                        have been made to a record beyond the first such change, a number was added as the last
                        character of the revision date. The date a record was originally created is the Date
                        entered on file (field 008/00-05).
         </p>
         <p>A revision date such as &#8220;<em>r73</em>" means that the record was changed in 1973. The
                        revision date &#8220;<em>r743</em>" means that significant changes have been made to the
                        record three times, the last being made in 1974.
         </p>
         <div class="example">
            <table width="100%">
               <tr>
                  <td valign="top" width="5%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="10%" align="left"></td>
                  <td valign="top" width="15%" align="left"></td>
               </tr>
               <tr>
                  <td vAlign="top" colspan="1" align="left"><strong>010</strong></td>
                  <td vAlign="top" colspan="9" align="left"><strong>##</strong><strong>$a</strong>###75425165#//r75<br><em>[Number 75-425165 revised in 1975.]</em></td>
               </tr>
               <tr>
                  <td vAlign="top" colspan="1" align="left"><strong>010</strong></td>
                  <td vAlign="top" colspan="9" align="left"><strong>##</strong><strong>$a</strong>###73002284#//r752<br><em>[Number 73-2284 with (r75)rev 2 printed revision information.]</em></td>
               </tr>
               <tr>
                  <td vAlign="top" colspan="1" align="left"><strong>010</strong></td>
                  <td vAlign="top" colspan="9" align="left"><strong>##</strong><strong>$a</strong>###58062665#/L/r58<br><em>[Printed number is 58-62665 rev*. (The * was represented on the printed product
                                          by a double dagger and indicated limited cataloging; it was carried in the MARC
                                          record as an L. When the LC control number was printed from the MARC record, the L
                                          printed as Lim beneath the control number.)]</em></td>
               </tr>
            </table>
         </div>
         <p>Revision date was used as an indication of the degree of importance of a change made to
                        a record. A significant change to a record at the Library of Congress was defined as one
                        important enough to warrant, among other things, redistribution of cards to LC's own
                        catalogs. A significant change included changes to content designation, to an access
                        point (fields 020, $a or $z, 028, $a, 050, 051, 082, 1XX, 240, 245$a, 4XX (excluding
                        490), 6XX, 7XX, 8XX), a change to the extent of an item (300$a), a change to the
                        publication date (260$c), a change to the record control number (field 001), or a change
                        to Leader/18 (Descriptive cataloging form).
         </p>
         <p>Revision information was separated from a suffix or an alphabetic identifier by one
                        slash (/). If no suffixes or alphabetic identifiers are present, revision information
                        was separated from the Supplement number by two slashes (//). The inclusion of revision
                        data was discontinued in 1999 and will be deleted from all records in the Library of
                        Congress files.
         </p>
      </div>
      <hr>
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
         <tr valign="bottom">
            <td>
               <div class="head-nav"><a href="http://www.loc.gov/">Library of
                     								Congress</a> &gt;&gt; <a href="http://www.loc.gov/marc/">MARC</a> &gt;&gt; <a href="http://www.loc.gov/marc/bibliographic/">Bibliographic</a>
                  								&gt;&gt; <a href="http://www.loc.gov/marc/bibliographic/bd01x09x.html">01X-09X</a> &gt;&gt; <strong>010</strong></div> (02/16/2008) 
            </td>
            <td align="right"><a href="mailto:ndmso@loc.gov">Contact Us</a></td>
         </tr>
      </table>
   <script type='text/javascript' src='http://cdn.loc.gov/js/global/metrics/sc/v25.2/2.0/s_code.js'></script></body>
</html>"""

tag = ""
current = 0
while testdata[current:current + 4] != '<h1>':
    current = current + 1
while testdata[current:current + 5] != '</h1>':
    tag = tag + testdata[current]
    current = current + 1
print(tag)
