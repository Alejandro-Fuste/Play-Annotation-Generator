# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_25`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 139 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [3–16], lower_priority='Action_PassBlock' annotated_start=7, effective_Action_PassBlock_start=17.
> - Action 'Action_None' range [3-289] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [81-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-128] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-201] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-275] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-53] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [57-72] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [74-99] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [101-105] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [108-164] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-135] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-168] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-191] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [193-208] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-218] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-192] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-228] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-236] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-282] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-79] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-51] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-60] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-39] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-96] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-299] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-35] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-73] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-83] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [86-87] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-131] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-238] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [3-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-74] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-265] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-100] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-299] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-98] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [112-191] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [195-238] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [240-257] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [260-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-22] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-39] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-70] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-73] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-83] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-98] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-62] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-70] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-85] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-147] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-165] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-171] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-229] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-123] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-135] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-251] for track '28' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [253-267] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-204] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-233] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-293] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-195] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-228] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-234] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-299] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-238] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-248] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-255] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-278] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-286] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-248] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-282] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-265] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-287] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [276-290] for track '39' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.