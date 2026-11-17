# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_275`
- **Input XML**: `outputs/batch/Power/Power/Power_275/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 550: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 550: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '4' (DE1) duration 101 frames exceeds threshold 90 frames [start=181, end=281].
> - Validation warning: Action 'Action_PullBlock' for track '10' (RT) duration 101 frames exceeds threshold 90 frames [start=181, end=281].
> - Validation warning: Action 'Action_DownBlock' for track '15' (LT) duration 101 frames exceeds threshold 90 frames [start=181, end=281].
> - Validation warning: Action 'Action_DownBlock' for track '19' (LG) duration 101 frames exceeds threshold 90 frames [start=181, end=281].
> - Action 'Action_PreSnap' range [16-267] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-389] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-255] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-268] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-380] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [181-275] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-284] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-258] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-264] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-202] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-336] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-378] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-280] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-389] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-375] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-389] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-389] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-367] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-262] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-266] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-374] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-264] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-270] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-371] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-205] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [181-258] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [260-281] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-371] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-203] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-227] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-313] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-88] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-126] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-192] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-219] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-224] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-183] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-194] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-39] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-209] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-212] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-229] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-74] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-113] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-180] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-188] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-196] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-230] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-238] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-243] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-246] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-259] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-316] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-321] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-330] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-339] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-342] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-359] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-379] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-226] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-299] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-301] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-313] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-327] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-352] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-370] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-354] for track '35' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.