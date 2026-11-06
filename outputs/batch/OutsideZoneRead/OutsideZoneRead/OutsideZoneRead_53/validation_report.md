# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_53`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 125 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-329] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-178] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-183] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-205] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-285] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-305] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-329] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-132] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-143] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-304] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-311] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-157] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-187] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-240] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-245] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-301] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-316] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-323] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-138] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-325] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-244] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-310] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-69] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [85-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-195] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-220] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-258] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-68] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 119, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [119-123] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-137] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-151] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-329] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-27] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-35] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-70] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-112] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-100] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-132] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-116] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-261] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-311] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-96] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-105] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-182] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-98] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-123] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-144] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-222] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-234] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-119] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-329] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-302] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-323] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-167] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-183] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-212] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-216] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-242] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-253] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-186] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-248] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-299] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-304] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-299] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-302] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-252] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-301] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-312] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-242] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-245] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-267] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-274] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-287] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-292] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-297] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-301] for track '36' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.