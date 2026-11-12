# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_236`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_236/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (RT) duration 108 frames exceeds threshold 90 frames [start=115, end=222].
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 104 frames exceeds threshold 90 frames [start=115, end=218].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 108 frames exceeds threshold 90 frames [start=115, end=222].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [112–125], lower_priority='Action_ZoneBlock' annotated_start=115, effective_Action_ZoneBlock_start=126.
> - Action 'Action_None' range [112-169] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [164-222] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '1' starts at frame 223, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [223-223] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-259] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-184] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-218] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-141] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-129] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-153] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-256] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-196] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [160-222] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-275] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-249] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-215] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-26] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-156] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [154-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [165-211] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-237] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-263] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-229] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-186] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-299] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-252] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-242] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-245] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-247] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-240] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-244] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [239-277] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-274] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-285] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [258-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-287] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.