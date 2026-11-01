# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_352`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_352/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 49 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 116 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [22–36], lower_priority='Action_ZoneBlock' annotated_start=25, effective_Action_ZoneBlock_start=37.
> - Action 'Action_None' range [22-317] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-91] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [52-77] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [79-82] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-162] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-89] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-317] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-282] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-270] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-74] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-149] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-185] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-214] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-302] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-98] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-307] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-49] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-86] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-233] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-123] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-156] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-192] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-241] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [22-34] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-258] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-65] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-102] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [104-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-197] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-284] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-110] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-83] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [80-230] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-191] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [194-202] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-278] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-168] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-199] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-289] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-282] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-185] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-272] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-230] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-230] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-275] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-240] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-299] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-314] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-314] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-320] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-241] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-282] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-238] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-285] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-278] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '48' has 1 frames without a visible bounding box.
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
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.