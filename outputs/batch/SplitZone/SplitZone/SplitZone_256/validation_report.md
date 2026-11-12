# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_256`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_256/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 99 frames exceeds threshold 90 frames [start=135, end=233].
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [132–143], lower_priority='Action_ZoneBlock' annotated_start=135, effective_Action_ZoneBlock_start=144.
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 99 frames exceeds threshold 90 frames [start=135, end=233].
> - Action 'Action_None' range [160-176] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-105] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-287] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-85] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-178] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-207] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [160-298] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-213] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [220-232] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-240] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-256] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-227] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-191] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-286] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-151] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [172-181] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [202-204] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [207-221] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [133-151] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [174-233] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-285] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-159] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-196] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [206-207] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-185] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-218] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-196] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [132-141] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-147] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-149] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-261] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-238] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-268] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-277] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-271] for track '25' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.