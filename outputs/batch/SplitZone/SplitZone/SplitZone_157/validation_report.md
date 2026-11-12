# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_157`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_157/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 316: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 124 frames exceeds threshold 90 frames [start=80, end=203].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (RT) duration 124 frames exceeds threshold 90 frames [start=80, end=203].
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [77–88], lower_priority='Action_ZoneBlock' annotated_start=80, effective_Action_ZoneBlock_start=89.
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 124 frames exceeds threshold 90 frames [start=80, end=203].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 124 frames exceeds threshold 90 frames [start=80, end=203].
> - Action 'Action_None' range [77-248] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-141] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [77-134] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-266] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [85-153] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [157-158] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [161-168] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [178-197] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-139] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-154] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-219] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-317] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-108] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-356] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-281] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-287] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-359] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [98-115] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [121-145] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [77-183] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-330] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-151] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-344] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-112] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-359] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-359] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-276] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-359] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-358] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [334-340] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '33' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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