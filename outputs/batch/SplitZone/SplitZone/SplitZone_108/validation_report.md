# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_108`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_108/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 117 frames exceeds threshold 90 frames [start=81, end=197].
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (RG) duration 117 frames exceeds threshold 90 frames [start=81, end=197].
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 117 frames exceeds threshold 90 frames [start=81, end=197].
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [77–87], lower_priority='Action_ZoneBlock' annotated_start=81, effective_Action_ZoneBlock_start=88.
> - Action 'Action_None' range [77-248] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-172] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-159] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-170] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-147] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-222] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [104-243] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-220] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-197] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-218] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-183] for track '13' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [198-261] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-147] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-215] for track '17' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-246] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-240] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-259] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '22' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.