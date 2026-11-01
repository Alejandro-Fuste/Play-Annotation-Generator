# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_186`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_186/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 372: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [433–444], lower_priority='Action_ZoneBlock' annotated_start=436, effective_Action_ZoneBlock_start=445.
> - Action 'Action_None' range [433-486] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-533] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-551] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [555-556] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-455] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-569] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [477-539] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-454] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-547] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [551-555] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-530] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-553] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [556-561] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [567-568] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-547] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-494] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '17' starts at frame 445, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [445-445] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [458-467] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [436-501] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-75] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-106] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-119] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-539] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-559] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [561-565] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-432] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [433-559] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [565-569] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-494] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-532] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-557] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-16] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-83] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-450] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-460] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-561] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [501-505] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-567] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [529-531] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-540] for track '28' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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