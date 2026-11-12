# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_140`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_140/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (RG) duration 102 frames exceeds threshold 90 frames [start=71, end=172].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 92 frames exceeds threshold 90 frames [start=71, end=162].
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (RT) duration 102 frames exceeds threshold 90 frames [start=71, end=172].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 102 frames exceeds threshold 90 frames [start=71, end=172].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [68–80], lower_priority='Action_ZoneBlock' annotated_start=71, effective_Action_ZoneBlock_start=81.
> - Action 'Action_None' range [68-358] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [112-131] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [133-148] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-208] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-266] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-156] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-219] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-274] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [77-164] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-198] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-244] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-259] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-164] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-143] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-359] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-166] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-276] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-347] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-79] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-231] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-242] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-164] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-151] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-193] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-213] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-359] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-216] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-306] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-244] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-357] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.