# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_248`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_248/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 109 frames exceeds threshold 90 frames [start=122, end=230].
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (RG) duration 109 frames exceeds threshold 90 frames [start=122, end=230].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (LG) duration 109 frames exceeds threshold 90 frames [start=122, end=230].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [119–131], lower_priority='Action_ZoneBlock' annotated_start=122, effective_Action_ZoneBlock_start=132.
> - Action 'Action_BlockSecondLevel' range [153-179] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [183-212] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-248] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-295] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-147] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-169] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [172-176] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [178-191] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-277] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-280] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-146] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [149-230] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-276] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-171] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-187] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-296] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-169] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-283] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-178] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [185-189] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [191-192] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-267] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-27] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-80] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-88] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-105] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [147-151] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [127-160] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [162-230] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-139] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-158] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-205] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-222] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-270] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [119-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-164] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-318] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-142] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-186] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-13] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-76] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-89] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-112] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [121-123] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-192] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-11] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-193] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-217] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-317] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-230] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-329] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-292] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-287] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-313] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-252] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-310] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-306] for track '27' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.