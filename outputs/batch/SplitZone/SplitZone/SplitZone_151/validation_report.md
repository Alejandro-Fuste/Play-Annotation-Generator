# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_151`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_151/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 111 frames exceeds threshold 90 frames [start=49, end=159].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 111 frames exceeds threshold 90 frames [start=49, end=159].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [46–56], lower_priority='Action_ZoneBlock' annotated_start=49, effective_Action_ZoneBlock_start=57.
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 111 frames exceeds threshold 90 frames [start=49, end=159].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 111 frames exceeds threshold 90 frames [start=49, end=159].
> - Action 'Action_None' range [46-107] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-176] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-146] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [152-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '1' starts at frame 160, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [160-318] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [46-128] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-323] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-114] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-288] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-308] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [70-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [52-101] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-125] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-251] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-359] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [57-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-359] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-129] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-134] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-148] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-263] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-359] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-263] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-296] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-261] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-138] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-352] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-108] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [119-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-156] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-263] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [265-346] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-152] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-307] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-314] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-359] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-340] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '34' has 1 frames without a visible bounding box.
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