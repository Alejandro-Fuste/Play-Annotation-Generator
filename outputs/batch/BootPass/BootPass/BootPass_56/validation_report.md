# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_56`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_56/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 92: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_SecureCatch' for track '0' has invalid range: start=234, end=210. Clamping end to start.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [33–49], lower_priority='Action_RunBlock' annotated_start=41, effective_Action_RunBlock_start=50.
> - Action 'Action_PreSnap' range [0-86] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-93] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-102] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-98] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [33-151] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-67] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-126] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-95] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-116] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [41-84] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [97-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [114-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [41-96] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [98-100] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-169] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-109] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [50-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [41-53] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [113-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-109] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-78] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-55] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-65] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-209] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '29' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.