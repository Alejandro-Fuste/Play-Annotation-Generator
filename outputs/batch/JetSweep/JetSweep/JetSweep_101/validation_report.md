# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_101`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_101/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Overlapping action conflict at frame 83 for track '0': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
> - Action 'Action_LeadBlock' range [83-132] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-115] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-259] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-138] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-254] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-277] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-94] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-171] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-214] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-122] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-169] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [174-233] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-144] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-131] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-88] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-90] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '12' starts at frame 137, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [137-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [79-82] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-136] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [78-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-282] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-141] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-136] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-171] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-195] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-177] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-227] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-263] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-299] for track '26' has 1 frames without a visible bounding box.
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