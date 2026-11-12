# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_88`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_88/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 120 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 178: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 178: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (LG) duration 95 frames exceeds threshold 90 frames [start=91, end=185].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 95 frames exceeds threshold 90 frames [start=91, end=185].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [88–103], lower_priority='Action_ZoneBlock' annotated_start=91, effective_Action_ZoneBlock_start=104.
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (LT) duration 95 frames exceeds threshold 90 frames [start=91, end=185].
> - Action 'Action_PreSnap' range [4-87] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-124] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-190] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-137] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-149] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-171] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-228] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-247] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-256] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [88-98] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-145] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [123-145] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [170-174] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-197] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-226] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-29] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-32] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-154] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-182] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-199] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-224] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-234] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-15] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-114] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-266] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-25] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-87] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [88-103] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-138] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-240] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-252] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-12] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [96-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [138-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [164-166] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-36] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-69] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-160] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [183-197] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-215] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-21] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-40] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-59] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [163-165] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-126] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-160] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-213] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-163] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-179] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-138] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-154] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-204] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-213] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-237] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-248] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '28' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.