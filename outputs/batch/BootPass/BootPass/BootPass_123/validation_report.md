# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_123`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_123/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_RunFlatRoute' for track '3' has invalid range: start=130, end=122. Clamping end to start.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [22–47], lower_priority='Action_RunBlock' annotated_start=40, effective_Action_RunBlock_start=48.
> - Action 'Action_None' range [22-329] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [22-179] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-76] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-83] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-87] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-266] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-52] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-277] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-170] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-207] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-270] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-271] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [40-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-123] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-145] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-186] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-278] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [48-261] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-203] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-268] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-300] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-190] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-215] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-225] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-236] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [40-42] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [53-201] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [206-224] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [230-242] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [250-251] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [40-170] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [40-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [73-75] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [186-188] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-92] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-188] for track '22' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [193-201] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-207] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-224] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-244] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [74-81] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-107] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-239] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-148] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-161] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-195] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-250] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-200] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-236] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-253] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-242] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-195] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-274] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-212] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-244] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-236] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-247] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-260] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-315] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [261-329] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-280] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-296] for track '41' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.