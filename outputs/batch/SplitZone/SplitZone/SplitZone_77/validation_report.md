# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_77`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_77/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 113 frames exceeds threshold 90 frames [start=190, end=302].
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (C) duration 113 frames exceeds threshold 90 frames [start=190, end=302].
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [187–204], lower_priority='Action_ZoneBlock' annotated_start=190, effective_Action_ZoneBlock_start=205.
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (RG) duration 113 frames exceeds threshold 90 frames [start=190, end=302].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 113 frames exceeds threshold 90 frames [start=190, end=302].
> - Action 'Action_None' range [187-256] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [258-262] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-314] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-321] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-315] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [190-302] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-318] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-290] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-306] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-314] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-350] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [190-211] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [219-225] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [205-259] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [262-302] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-312] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [190-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-314] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-359] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-258] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-359] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [187-314] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [190-302] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [303-314] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-279] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-318] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-359] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-314] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-359] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-314] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-322] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-313] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.