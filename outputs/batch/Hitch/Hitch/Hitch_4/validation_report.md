# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_4`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_4/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 116 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 8: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_RunHitchRoute' for track '2' has invalid range: start=65, end=50. Clamping end to start.
> - Segment 'Action_BallCarry' for track '2' has invalid range: start=149, end=50. Clamping end to start.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [27–41], lower_priority='Action_PassBlock' annotated_start=37, effective_Action_PassBlock_start=42.
> - Segment 'Action_ThrowPass' for track '20' has invalid range: start=111, end=104. Clamping end to start.
> - Action 'Action_None' range [27-225] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-329] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-255] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-268] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-281] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-291] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-301] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [303-313] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-50] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-272] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-119] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-182] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-225] for track '6' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-304] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-156] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-263] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [27-208] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-74] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-250] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [252-266] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [269-270] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [272-273] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [278-300] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [308-322] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-237] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [241-264] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [267-271] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [277-285] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [289-298] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [301-329] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-80] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [91-105] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [108-109] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [111-239] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [242-329] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-225] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-262] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-310] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [312-326] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-94] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-91] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-99] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-329] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-225] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-250] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-259] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-326] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-200] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-203] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-250] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-306] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-213] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-227] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-329] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-221] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-329] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-307] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-315] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-320] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-327] for track '34' has 2 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.