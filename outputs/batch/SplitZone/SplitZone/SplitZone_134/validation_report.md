# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_134`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_134/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 49 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 134 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 270: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [19–30], lower_priority='Action_ZoneBlock' annotated_start=22, effective_Action_ZoneBlock_start=31.
> - Action 'Action_None' range [19-229] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-75] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-152] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-160] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-184] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-131] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [43-47] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [53-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [68-70] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [73-76] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-108] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-118] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-135] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-39] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-38] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-59] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-84] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-32] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-155] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-10] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-56] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-70] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-166] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-290] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-299] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-12] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-61] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [84-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-127] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-61] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-76] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-158] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [20-27] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [60-81] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-46] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-190] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [52-53] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [60-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-40] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-48] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-58] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-58] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-74] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-159] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-63] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-151] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-348] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-364] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-384] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-396] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-405] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-430] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-442] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-183] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-211] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-170] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-243] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-251] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-319] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-151] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-142] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-348] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-384] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [386-388] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-393] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-397] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-263] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-300] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-451] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [455-457] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-285] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-422] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-416] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-338] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-344] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-355] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-358] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-346] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-372] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [424-425] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-434] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-445] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-458] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [460-478] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [449-450] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [463-469] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-474] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [472-473] for track '48' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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