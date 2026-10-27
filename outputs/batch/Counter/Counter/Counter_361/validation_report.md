# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_361`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_361/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 40 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '20' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_PullLeadBlock' for track '2' has invalid range: start=47, end=32. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '8' has invalid range: start=40, end=32. Clamping end to start.
> - Segment 'Action_Handoff' for track '8' has invalid range: start=66, end=32. Clamping end to start.
> - Segment 'Action_BallCarry' for track '12' has invalid range: start=88, end=9. Clamping end to start.
> - Segment 'Action_PullBlock' for track '13' has invalid range: start=47, end=32. Clamping end to start.
> - Segment 'Action_BallSnap' for track '17' has invalid range: start=96, end=54. Clamping end to start.
> - Action 'Action_PreSnap' range [0-32] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-7] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-19] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-33] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-4] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-33] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-32] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-120] for track '31' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.